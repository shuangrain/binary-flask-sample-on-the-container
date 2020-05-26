from abc import ABC

from gunicorn.app.base import Application, Config

from src.app import app


class GUnicornFlaskApplication(Application, ABC):
    def __init__(self, flask_app):
        self.usage, self.callable, self.prog, self.app = None, None, None, flask_app

    def run(self, **options):
        self.cfg = Config()
        for key, value in options.items():
            self.cfg.set(key, value)
        return Application.run(self)

    load = lambda self: self.app


if __name__ == "__main__":
    wsgi_app = GUnicornFlaskApplication(app)
    wsgi_app.run(
        worker_class="gunicorn.workers.ggevent.GeventWorker",
        bind="0.0.0.0:8000"
    )
