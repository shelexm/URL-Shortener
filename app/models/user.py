from datetime import datetime
from sqlalchemy import String, Boolean, Enum, Integer, BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base
from app.models.enums import role
class User(Base):
    __tablename__ = 'users'
    id: Mapped[Integer] = mapped_column(BIGINT, primary_key=True)
    username: Mapped[String] = mapped_column(String(32), unique=True)
    email: Mapped[String] = mapped_column(String(128), unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role: Mapped[role] = mapped_column(Enum(role, name="user_role_enum") , default=role.user)
    date_created: Mapped[datetime] = mapped_column(default=datetime.now())
    links: Mapped[list['Link']] = relationship(back_populates='user')