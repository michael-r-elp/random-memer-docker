# Random Memer Docker

Flask API to return random [programming](https://www.memedroid.com/memes/tag/programming) and [programmers](https://www.memedroid.com/memes/tag/programmers) meme images as well as [System32Comics](https://www.memedroid.com/user/view/System32Comics) scrapped from [Memedroid](https://www.memedroid.com/).

To use just send a GET request to https://random-memer.elp.quest/

You can also use this with `img` tag in your website and it will display a random meme everytime the website is loaded

```html
<img src='https://random-memer.elp.quest/' title="Meme" alt="Please refresh the page if the meme doesn't show up.">
```

### Usage Notes:

* The API is deployed on a Docker host which itself is installed on an Oracle Cloud Free Compute VM. You can deploy your own instance of the app as an Docker container.
* A premade docker image is not available for download, you'll have to build one yourself

### Credits
This is a fork of [techytushar/random-memer](https://github.com/techytushar/random-memer)
Updated and easy to deploy on docker using the Dockerfile

