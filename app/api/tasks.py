from typing import List

from sanic import Blueprint
from sanic import json
from sanic import Request

from app.utils.common import is_valid_url
from app.db.repository import TaskRepository
from sqlalchemy.ext.asyncio import AsyncSession

tasks_bp = Blueprint("Task_blueprint", "tasks")


@tasks_bp.post("")
async def safe_urls(request: Request) -> json:
    request_body: dict = request.json
    urls = request_body.get("urls", [])
    if not isinstance(urls, list):
        return json(
            body={
                "message": "",
                "error": f"Unexpected type of 'urls' field. Got {type(urls)}"
            },
            status=400
        )

    filtered_urls = list(filter(is_valid_url, urls))

    factory = request.app.ctx.db_session_factory
    session: AsyncSession

    async with factory() as session:
        repo = TaskRepository(session)
        success, failed = await repo.create_task(filtered_urls)

        if not success and failed:
            await session.rollback()
        else:
            await session.commit()

    status = 200
    body = {
        "success": success,
        "failed": failed
    }
    return json(body,  status)

