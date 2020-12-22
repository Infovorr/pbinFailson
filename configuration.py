import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "testkey"
basedir = os.path.abspath(os.path.dirname(__file__))

class Configs(object):
   SECRET_KEY = os.environ.get("SECRET_KEY") or "testkey"
   dbLocale = os.environ.get("DATABASE_URL")
   if dbLocale:
      SQLALCHEMY_DATABASE_URI = dbLocale
   else:
      SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "failbin.db")
