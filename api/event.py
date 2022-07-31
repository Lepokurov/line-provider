from fastapi import APIRouter, Depends, Query, Body, Path

from bet_maker_client import get_line_provider_client, BetMakerClient
from dependencies import check_inner_token, get_event_controller
from events.controller import EventController
from events.schema import EventList, Event, CreateEvent, UpdateEvent

event_router = APIRouter(
    prefix="/api/events", tags=["event"], dependencies=[Depends(check_inner_token)]
)


@event_router.get("", response_model=EventList)
async def get_events(
    is_actual=Query(default=True, description="Return events before the deadline"),
    controller: EventController = Depends(get_event_controller),
):
    events = controller.get_all_events(is_actual=is_actual)
    total = controller.get_event_count(is_actual=is_actual)
    return EventList(data=events, total=total)


@event_router.post("", response_model=Event)
async def add_event(
    event_data: CreateEvent = Body(...),
    controller: EventController = Depends(get_event_controller),
):
    event = controller.create_event(event_data)
    return event


@event_router.get("/{event_id}", response_model=Event)
async def get_event(
    event_id: int = Path(...),
    controller: EventController = Depends(get_event_controller),
):
    event = controller.get_event(event_id)
    return event


@event_router.patch("/{event_id}", response_model=Event)
async def update_event(
    event_data: UpdateEvent = Body(...),
    event_id: int = Path(...),
    controller: EventController = Depends(get_event_controller),
    bet_maker_client: BetMakerClient = Depends(get_line_provider_client)
):
    event = controller.update_event(event_id, event_data)
    if event_data.state:
        await bet_maker_client.update_event_status(event_id=event_id, state=event_data.state)
    return event
