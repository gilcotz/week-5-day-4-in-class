from .models import User
from flask import Flask
from config import Config
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth
from flask_migrate import Migrate
from .models import db, login_manager, ma
from .helpers import JSONEncoder
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)


app.register_blueprint(site)
app.register_blueprint(auth)

app.register_blueprint(api)

db.init_app(app)

login_manager.init_app(app)
ma.init_app(app)


# specify what page to load for NON_AUTHED users
login_manager.login_view = 'auth.signin'
migrate = Migrate(app, db)

app.json_encoder = JSONEncoder

CORS(app)
