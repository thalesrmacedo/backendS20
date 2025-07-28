from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['STRIPE_SECRET_KEY'] = os.getenv("STRIPE_SECRET_KEY")
    app.config['STRIPE_PUBLIC_KEY'] = os.getenv("STRIPE_PUBLIC_KEY")

    from .routes import main
    app.register_blueprint(main)

    return app
