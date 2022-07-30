from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from events.controller import EventController
from settings import INNER_TOKEN

auth = HTTPBearer(description="Внутренний токен авторизации")


def check_inner_token(authorization: HTTPAuthorizationCredentials = Depends(auth)):
    """Проверка статичного токена."""
    if authorization.credentials == INNER_TOKEN:
        return
    raise HTTPException(status_code=403, detail="Invalid inner auth token")


def get_event_controller():
    return EventController()
