INNER_TOKEN = "123"

BET_MAKER_API_HOST_URL = "localhost"
BET_MAKER_API_TOKEN = "123"
SERVICE_NAME = "line-provider"

try:
    from settings_local import *  # NOQA
except ImportError:
    pass

