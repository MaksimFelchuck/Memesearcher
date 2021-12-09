import os
import random

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect, secure_filename

from .crud import create_meme, delete_meme_by_name, get_all_memes

_ALLOWED_FORMATS = [".svg", ".jpg", ".png"]

meme_blueprint = Blueprint('meme', __name__, url_prefix='/meme')


@meme_blueprint.route('/', methods=("GET", "POST"))
def meme():
    if request.method == "GET":
        return render_template('meme/create.html')

    file = request.files["file"]

    if not file.filename:
        return render_template('meme/create.html', message="No file!")

    if os.path.splitext(file.filename)[1] not in _ALLOWED_FORMATS:
        return render_template('meme/create.html',
                               message="File not in allowed format!")

    create_meme(file.filename)

    filename = secure_filename(file.filename)
    file.save(os.path.join("static/images", filename))

    return render_template('meme/create.html', message="Successfull created!")


@meme_blueprint.route('/all', methods=("GET", ))
def all_memes():
    return render_template('meme/all.html', memes=get_all_memes())


@meme_blueprint.route('/random', methods=("GET", ))
def random_memes():
    meme_list = get_all_memes()
    random_memes = random.sample(meme_list, 2)

    return render_template('meme/all.html', memes=random_memes)


@meme_blueprint.route('/delete', methods=("DELETE", "POST"))
def delete_meme(*args, **kwargs):
    meme_name = request.form["meme_name"]
    delete_meme_by_name(meme_name)
    return redirect(url_for("meme.all_memes"))
