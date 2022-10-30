#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Tushar Mittal (chiragmittal.mittal@gmail.com)
Flask API to return random meme images
"""

import random
import grequests
import requests
from gevent import monkey
from bs4 import BeautifulSoup
from flask import Flask, Response
from PIL import Image
from io import BytesIO

monkey.patch_all()

app = Flask(__name__)

def exception_handler(request, exception):
    print("Request failed", exception)

def get_new_memes():
    """Scrapers the website and extracts image URLs

    Returns:
        imgs [list]: List of image URLs
    """

    urls = [
        f'https://www.memedroid.com/memes/tag/programming?page={random.randrange(3)}',
        'https://www.memedroid.com/memes/tag/programmers',
        f'https://www.memedroid.com/user/view/System32Comics?page={random.randrange(6)}'
    ]
    
    imgs = []
    rs = (grequests.get(u) for u in urls)
    for resp in grequests.imap(rs, exception_handler=exception_handler):
        soup = BeautifulSoup(resp.content, 'lxml')
        divs = soup.find_all('div', class_='item-aux-container')
        for div in divs:
            img = div.find('img')['src']
            if img.startswith('http') and img.endswith('jpeg'):
                imgs.append(img)
    return imgs


@app.after_request
def set_response_headers(response):
    """Sets Cache-Control header to no-cache so GitHub
    fetches new image everytime
    """
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/", methods=['GET'])
def return_meme():
    img_url = random.choice(get_new_memes())
    res = requests.get(img_url, stream=True)
    # Stream Response over
    return Response(res.iter_content(chunk_size=10*1024),
                    content_type=res.headers['Content-Type'])