from logs.models import Entry
from utils import db


def log(kind, text, data):
    return db.create(Entry, kind=kind, text=text, data=data)