from sanic import Sanic
from app.api.health import health_bp
from app.api.tasks import tasks_bp

from app.db.engine import async_session_factory

app = Sanic("AggregatorService")
app.blueprint([health_bp, tasks_bp])

@app.before_server_start
async def setup_db(app, ):
    app.ctx.db_session_factory = async_session_factory


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        single_process=True
    )