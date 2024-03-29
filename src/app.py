from flask import Flask
from src.database import db
from src.blueprints.users import bp as users_bp
from src.blueprints.cities import bp as cities_bp
from src.blueprints.colors import bp as colors_bp
from src.blueprints.images import bp as images_bp
from src.blueprints.ads import bp as ads_bp
from src.blueprints.auth import bp as auth_bp


def create_app():
	app = Flask(__name__)
	app.register_blueprint(ads_bp)
	app.config.from_object('config.Config')
	app.register_blueprint(auth_bp, url_prefix='/auth')
	app.register_blueprint(users_bp, url_prefix='/users')
	app.register_blueprint(colors_bp, url_prefix='/colors')
	app.register_blueprint(cities_bp, url_prefix='/cities')
	app.register_blueprint(images_bp, url_prefix='/images')
	db.init_app(app)
	return app
