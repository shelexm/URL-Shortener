from sqlalchemy import String, BIGINT, Text, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database.base import Base
from datetime import datetime
class Link(Base):
    __tablename__ = 'links'
    id: Mapped[Integer] = mapped_column(BIGINT, primary_key=True)
    original_link: Mapped[String] = mapped_column(Text)
    short_link: Mapped[String] = mapped_column(String(128))
    owner_id: Mapped[Integer] = mapped_column(BIGINT, ForeignKey('users.id'))
    date_created: Mapped[datetime] = mapped_column(default=datetime.now())
    user: Mapped['User'] = relationship(back_populates='posts')

