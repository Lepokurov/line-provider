from fastapi import Request, Response
from starlette.responses import JSONResponse


class BaseEventControllerException(Exception):
    pass


class EventNotExists(BaseEventControllerException):
    def __init__(self, event_id):
        self._event_id = event_id

    def message(self):
        return f"Event with id {self._event_id} doesn't exists"


async def controller_exceptions_handler(request: Request, exc: BaseEventControllerException):
    match exc:
        case EventNotExists() as err:
            return JSONResponse(status_code=404, content={"message": err.message()})
        case BaseEventControllerException() as err:
            return JSONResponse(status_code=500, content={"message": str(err)})
