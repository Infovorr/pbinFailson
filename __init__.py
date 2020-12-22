# Import required libraries
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app import app
from app import paths, tables

app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "testkey"
basedir = os.path.abspath(os.path.dirname(__file__))
dbLocale = os.environ.get("DATABASE_URL")
if dbLocale is not None:
   SQLALCHEMY_DATABASE_URI = dbLocale
else:
   SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "failbin.db")
csrf = CSRFProtect(app)
database = SQLAlchemy(app)
login = LoginManager(app)

# Application entry point / startup function
if __name__ == "__main__":
   app.run(host = "0.0.0.0")
