from database.db import db

class Meme(db.Model):
    """Базовая моделька мема
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"
