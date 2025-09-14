from sqlalchemy import (
    DateTime,
    func,
    Integer,
    BigInteger,
    String,
    UUID,
    ForeignKey,
    Enum as MySQL,
    Boolean,
    Date,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import uuid

from db.enums import CallSessionStatus, CallSessionDuration


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(128))
    number: Mapped[str] = mapped_column(String(40))

    calls_sessions: Mapped[list["CallsSession"]] = relationship(
        back_populates="creater", cascade="all, delete-orphan"
    )


class CallsSession(Base):
    __tablename__ = "calls_sessions"

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False, unique=True, primary_key=True)

    max_users_count: Mapped[int] = mapped_column(Integer, default=2)
    link: Mapped[str] = mapped_column(String)
    call_type: Mapped[CallSessionStatus] = mapped_column(MySQL(CallSessionStatus), default=CallSessionStatus.HISTROY)
    duration: Mapped[CallSessionDuration] = mapped_column(MySQL(CallSessionDuration), default=CallSessionDuration.DURATION_20)
    date: Mapped[Date] = mapped_column(Date)

    is_closed: Mapped[bool] = mapped_column(Boolean, default=False)
    creater_user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    creater: Mapped["User"] = relationship(back_populates="calls_sessions")
    