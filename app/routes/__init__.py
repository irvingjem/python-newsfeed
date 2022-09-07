from .home import bp as home

from .dashboard import bp as dashboard

from app.routes import home, dashboard

app.register_blueprint(home)
app.register_blueprint(dashboard)