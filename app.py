from flask import Flask, Blueprint, render_template
from src.meme import meme_blueprint
from database.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@172.17.0.2:5432/memesearcher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

main_blueprint = Blueprint('', __name__, url_prefix='')

@main_blueprint.route('/', methods=("GET",))
def home():
    return render_template('main.html')

app.register_blueprint(main_blueprint)
app.register_blueprint(meme_blueprint)
