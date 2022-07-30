import time

from events.error import EventNotExists
from events.schema import Event, UpdateEvent, CreateEvent, EventState


class EventController:
    events: dict[int, Event] = {
        1: Event(
            event_id=1,
            coefficient=1.2,
            deadline=int(time.time()) + 600,
            state=EventState.NEW,
        ),
        2: Event(
            event_id=2,
            coefficient=1.15,
            deadline=int(time.time()) + 60,
            state=EventState.NEW,
        ),
        3: Event(
            event_id=3,
            coefficient=1.67,
            deadline=int(time.time()) + 90,
            state=EventState.NEW,
        ),
    }

    def get_all_events(self, is_actual: bool = False) -> list[Event]:
        if is_actual:
            return list(
                event for event in self.events.values() if time.time() < event.deadline
            )
        return list(self.events.values())

    def get_event_count(self, is_actual: bool = False) -> int:
        if is_actual:
            return len(
                list(
                    event
                    for event in self.events.values()
                    if time.time() < event.deadline
                )
            )
        return len(self.events)

    def get_event(self, event_id) -> Event:
        event = self.events.get(event_id)
        if not event:
            raise EventNotExists(event_id)
        return event

    def create_event(self, event_data: CreateEvent) -> Event:
        event_id = len(self.events) + 1
        new_event = Event(event_id=event_id, **event_data.dict())
        self.events[event_id] = new_event
        return new_event

    def update_event(self, event_id: int, event_data: UpdateEvent) -> Event:
        event = self.events.get(event_id)
        if not event:
            raise EventNotExists(event_id)
        for p_name, p_value in event_data.dict(exclude_unset=True).items():
            setattr(event, p_name, p_value)
        return event
