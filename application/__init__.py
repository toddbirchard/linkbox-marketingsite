from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from .assets import compile_assets
        from . import routes
        app.register_blueprint(routes.landing_bp)
        compile_assets(app)

        return app
