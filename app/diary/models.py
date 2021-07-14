from datetime import datetime
from pytz import timezone, utc

from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .database import Base


class Diary(Base):
    __tablename__ = 'diary'

    KST = timezone('Asia/Seoul')
    now = datetime.utcnow()

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        String,
        ForeignKey('diary_users.name')
    )
    date = Column(Date)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    image_type = Column(String, nullable=True)
    updated_at = Column(
        DateTime(timezone=True),
        default=utc.localize(now).astimezone(KST)
    )

    creator = relationship("User", back_populates="diaries")


class User(Base):
    __tablename__ = 'diary_users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String)
    password = Column(String)

    diaries = relationship("Diary", back_populates="creator")