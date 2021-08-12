from sqlalchemy import Column, Integer, JSON
from WhisperBot.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)
    target_user = Column(JSON)

    def __init__(self, user_id, target_user=None):
        self.user_id = user_id
        self.target_user = target_user

    def __repr__(self):
        return "<User {} ({})>".format(self.target_user, self.user_id)


Users.__table__.create(checkfirst=True)


def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()
