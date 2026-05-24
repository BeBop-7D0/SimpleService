from sanic import Request
from sanic import json
from sanic import Blueprint

health_bp = Blueprint("health_check_blueprint", url_prefix="/health")

@health_bp.get("")
async def get_health_state(request: Request):
    return json(
        body={
            "message": "OK"
        },
        status=200
    )