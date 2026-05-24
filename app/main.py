from sanic import Sanic
from app.api.health import health_bp
from app.api.tasks import tasks_bp

app = Sanic("AggregatorService")
app.blueprint([health_bp, tasks_bp])

for route in app.router.routes:
    methods = ",".join(sorted(route.methods))
    print(f"{methods[:10]} {route.path}")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        single_process=True
    )