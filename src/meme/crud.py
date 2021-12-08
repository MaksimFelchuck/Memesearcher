from database.db import db

from database.models import Meme

def create_meme(name: str):
    """Создает мем

    Args:
        name (str): имя файла
    """
    meme = Meme(name=name)
    db.session.add(meme)
    db.session.commit()
