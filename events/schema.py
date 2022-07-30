import decimal
import enum

from pydantic import BaseModel, Field


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class BaseEvent(BaseModel):
    coefficient: decimal.Decimal = Field(description="Event coefficient")
    deadline: int = Field(description="Event deadline")
    state: EventState = Field(description="Event state")


class Event(BaseEvent):
    event_id: int = Field(description="Event id")


class CreateEvent(BaseEvent):
    pass


class UpdateEvent(BaseModel):
    coefficient: decimal.Decimal | None = Field(description="Event coefficient", default=None)
    deadline: int | None = Field(description="Event coefficient", default=None)
    state: EventState | None = Field(description="Event state", default=None)


class EventList(BaseModel):
    total: int = Field(description="Count of all events")
    data: list[Event]
