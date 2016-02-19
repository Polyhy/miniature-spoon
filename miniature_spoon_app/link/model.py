from miniature_spoon_app import db
from datetime import datetime
from sqlalchemy import event
from sqlalchemy import DDL


class Link(db.Model):
    id = db.Column(db.Integer,
                   db.Sequence('link_id_seq', start=2400000, increment=1),
                   primary_key=True)
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

event.listen(Link.__table__,
             "after_create",
             DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 2400000;"))
