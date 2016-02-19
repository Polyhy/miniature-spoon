from miniature_spoon_app import db
from datetime import datetime


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createAt = db.Column(db.DateTime)
    originalLink = db.Column(db.String(255))
    shortLink = db.Column(db.String(6))

    def __init__(self, link, shortLink):
        try:
            assert isinstance(link, str)
            assert isinstance(shortLink, str)
        except AssertionError as e:
            raise e

        self.createAt = datetime.now()
        self.originalLink = link
        self.shortLink = shortLink
