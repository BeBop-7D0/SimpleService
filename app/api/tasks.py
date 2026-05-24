from typing import List

from sanic import Blueprint
from sanic import json
from sanic import Request

from app.utils.common import is_valid_url

tasks_bp = Blueprint("Task_blueprint", "tasks")


@tasks_bp.post("")
async def safe_tasks(request: Request) -> json:
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

    success_count, failed_list = await process_urls(urls)

    status = 200
    body = {
        "success_count": success_count,
        "failed_to_process": failed_list
    }
    return json(body,  status)



async def process_urls(urls: List[str]) -> (int, List[str]):
    success_count = 0
    failed_list = []

    for url in urls:
        if is_valid_url(url):
            # TODO: сохранить в бд
            success_count += 1
            pass
        else:
            failed_list.append(url)

    return success_count, failed_list