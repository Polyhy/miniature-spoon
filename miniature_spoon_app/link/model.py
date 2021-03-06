from datetime import datetime
from sqlalchemy import event, DDL
from sqlalchemy import Column, Integer, VARBINARY, DateTime

from miniature_spoon_app import Base


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    createAt = Column(DateTime)
    originalLink = Column(VARBINARY(255))
    shortLink = Column(VARBINARY(6))
    # click = Column(Integer)

    def __init__(self, link):
        try:
            assert isinstance(link, str)
        except AssertionError as e:
            raise e

        self.createAt = datetime.now()
        self.originalLink = link
        self.shortLink = ""
        # self.click = 0


event.listen(Link.__table__,
             "after_create",
             DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 2400000;"))
