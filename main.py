from fastapi import FastAPI
from api import ping_router, event_router
from events.error import controller_exceptions_handler, BaseEventControllerException

app = FastAPI(
    title="line-provider",
    version="1.0.0",
    description="Сервис line-provide",
)

app.include_router(ping_router)
app.include_router(event_router)
app.add_exception_handler(BaseEventControllerException, controller_exceptions_handler)
