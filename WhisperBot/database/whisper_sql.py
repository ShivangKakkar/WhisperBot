from sqlalchemy import Column, String
from WhisperBot.database import BASE, SESSION


class Whispers(BASE):
    __tablename__ = "whispers"
    __table_args__ = {'extend_existing': True}
    specific = Column(String, primary_key=True)  # inline_message_id
    message = Column(String)

    def __init__(self, specific, message):
        self.specific = specific
        self.message = message

    def __repr__(self):
        return "<Whispers {} ({})>".format(self.message, self.specific)


Whispers.__table__.create(checkfirst=True)


def num_whispers():
    try:
        return SESSION.query(Whispers).count()
    finally:
        SESSION.close()
