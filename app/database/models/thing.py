import datetime

from sqlalchemy.dialects.postgresql import TIMESTAMP

from .. import db


class Thing(db.Model):
    __tablename__ = 'thing'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow)
    updated_at = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)
