from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


pic_default = 'https://t7-live-ahsd8.nyc3.cdn.digitaloceanspaces.com/animalhumanesociety.org/files/styles/animal_450x330/flypub/default_images/shy_8.jpg?itok=TjgwRwVM'


class Pet(db.Model):
    """Pet model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20), nullable=False)

    species = db.Column(db.String(30), nullable=False)

    photo_url = db.Column(db.Text, default=pic_default)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
