from app import database
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@userLogin.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Posts(database.Model):
   id = database.Column(database.Integer, primary_key = True)
   title = database.Column(database.String)
   date = database.Column(database.DateTime)
   author = database.Column(database.String)
   private = database.Column(database.Integer)
   permissions = database.Column(database.String)
   short = database.Column(database.String)
   content = database.Column(database.String)
   expiration = database.Column(database.DateTime)
   enabled = database.Column(database.Integer)
   
class Users(UserMixin, database.Model):
   id = database.Column(database.Integer, primary_key = True)
   user = database.Column(database.String)
   passHash = database.Column(database.String)
   email = database.Column(database.String)
   watch = database.Column(database.String)
   reset = database.Column(database.Integer)
   admin = database.Column(database.Integer)

   def hashPassw(self, passw):
      self.passHash = generate_password_hash(passw, 23)

   def verify(self, passw):
      return check_password_hash(self.passHash, passw)
