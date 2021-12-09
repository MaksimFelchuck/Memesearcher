from typing import List
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

def get_all_memes() -> List[Meme]:
    """Получает список всех мемов

    Returns:
        List[Meme]: список всех мемов
    """
    return db.session.query(Meme).all()

def delete_meme_by_name(meme_name: str):
    """Удаляет неадоевший мем

    Args:
        meme_name (str): имя мема
    """
    meme = db.session.query(Meme).filter_by(name=meme_name).one_or_none()
    db.session.delete(meme)
    db.session.commit()
