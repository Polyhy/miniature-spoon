from flask import render_template, redirect

from miniature_spoon_app import app
from miniature_spoon_app.link import controller as linkController


@app.route('/', methods=['GET'])
def show():
    return render_template('pages/index.html')


@app.route('/<token>', methods=['GET'])
def redirectShortURL(token):
    status, link = linkController.getOriginalUrl(token)
    if status == 200:
        url = link.originalLink
        if url[0:7] == "http://" or url[0:8] == "https://":
            return redirect(url, 302)
        else:
            return redirect("http://www." + url, 302)
    elif status ==  404:
        return render_template('404.html')