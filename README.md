# Random Memer Docker

Flask API to return random [programming](https://www.memedroid.com/memes/tag/programming) and [programmers](https://www.memedroid.com/memes/tag/programmers) meme images as well as [System32Comics](https://www.memedroid.com/user/view/System32Comics) scrapped from [Memedroid](https://www.memedroid.com/).

To use just send a GET request to https://random-memer.elp.quest/

You can also use this with `img` tag in your website and it will display a random meme everytime the website is loaded

```html
<img src='https://random-memer.elp.quest/' title="Meme" alt="Please refresh the page if the meme doesn't show up.">
```

### Usage Notes:

* The API is deployed on Heroku free dyno which provides certain number of free compute hours per month, so app might stop working at the end of the month. You can deploy your own instance of the app on Heroku for free and use that.
* The API is deployed on the free dyno provided by Heroku, which shuts-down if there is no request to it for some time, so sometimes it might take some time to load the image from the URL.

### Credits
This is a fork of [techytushar/random-memer](https://github.com/techytushar/random-memer)
Updated and easy to deploy on docker using the Dockerfile

