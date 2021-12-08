import os

from database.db import db
from database.models import Meme
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from .crud import create_meme

_ALLOWED_FORMATS = [".svg", ".jpg", ".png"]

meme_blueprint = Blueprint('meme', __name__, url_prefix='/meme')


@meme_blueprint.route('/', methods=("GET", "POST"))
def meme():
    if request.method == "GET":
        db.session.query(Meme).all()
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
