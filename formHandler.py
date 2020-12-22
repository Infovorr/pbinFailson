from app.tables import Posts, Users
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, RadioField, StringField, SubmitField, validators

class AdminLoginPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide a username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric")])
   password = StringField("Password", [validators.DataRequired("Must provide a password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"), 
      validators.EqualTo("confirm", message="Passwords must be the same")])
   submit = SubmitField("Submit")
   
class DeleteAPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide your username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), validators.Regexp("[a-zA-Z0-9]", 
      "Must be alphanumeric")])
   userEmail = StringField("Email", [validators.DataRequired("Must provide your email address"), 
      validators.Email("Must be a valid email address"), validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be a valid email address")])
   password = PasswordField("Password", [validators.DataRequired("Must provide your password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"), 
      validators.EqualTo("confirm", message="Passwords must be the same")])
   confirm = PasswordField("Confirm Password")
   submit = SubmitField("Submit")
   
class DeleteUPage(FlaskForm):
   confirm = RadioField("Delete user?", choices=[("1","Yes"),("0","No")])
   submit = SubmitField("Submit")
   
class DeletePPage(FlaskForm):
   confirm = RadioField("Enable or disable", choices=[("1","Enable"),("0","Disable")])
   submit = SubmitField("Submit")
   
class EditAPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide a username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), validators.Regexp("[a-zA-Z0-9]", 
      "Must be alphanumeric")])
   userEmail = StringField("Email", [validators.DataRequired("Must provide an email address"), 
      validators.Email("Must be a valid email address"), validators.Length(min=6, max=36, "Must be 6 to 36 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be a valid email address")])
   password = PasswordField("Password", [validators.DataRequired("Must provide a password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"))
   admin = RadioField("Is admin", choices=[("1","Yes"),("0","No")])
   submit = SubmitField("Submit")
   
class EditPPage(FlaskForm):
   title = StringField("Title")
   private = BooleanField("Private")
   permissions = StringField("Permissions", 
      [validators.Regexp("[a-zA-Z0-9,]", "Must be alphanumeric usernames separated by commas")])
   content = StringField("Post")
   expiration = StringField("Expiration Date", 
      [validators.Regexp("[0123][0-9]/[01][0-9]/2[0-9][0-9][0-9]", "Must be a date in the format DD/MM/YYYY")])
   submit = SubmitField("Submit")
   
class EditUPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide a username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), validators.Regexp("[a-zA-Z0-9]", 
      "Must be alphanumeric")])
   userEmail = StringField("Email", [validators.DataRequired("Must provide an email address"), 
      validators.Email("Must be a valid email address"), validators.Length(min=6, max=36, "Must be 6 to 36 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be a valid email address")])
   password = PasswordField("Password", [validators.DataRequired("Must provide a password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"))
   submit = SubmitField("Submit")
   
class EndisPage(FlaskForm):
   confirm = RadioField("Confirm post deletion", choices=[("1","Yes"),("0","No")])
   submit = SubmitField("Submit")

class LoginPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide a username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric")])
   password = StringField("Password", [validators.DataRequired("Must provide a password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"), 
      validators.EqualTo("confirm", message="Passwords must be the same")])
   submit = SubmitField("Submit")
   
   #def validate_username(self, username):
   #   users = Users.query.filter_by(username=username.data).count()
   #   if users == 0:
   #      raiseValidationError("Invalid username or password.")
   
class PostPage(FlaskForm):
   title = StringField("Title")
   private = BooleanField("Private")
   permissions = StringField("Permissions", 
      [validators.Regexp("[a-zA-Z0-9,]", "Must be alphanumeric usernames separated by commas")])
   content = StringField("Post")
   expiration = StringField("Expiration Date", 
      [validators.Regexp("[0123][0-9]/[01][0-9]/2[0-9][0-9][0-9]", "Must be a date in the format DD/MM/YYYY")])
   submit = SubmitField("Submit")

class RegistrationPage(FlaskForm):
   username = StringField("Username", [validators.DataRequired("Must provide a username"), 
      validators.Length(min = 6, max = 26, "Must be 6 to 26 characters long"), validators.Regexp("[a-zA-Z0-9]", 
      "Must be alphanumeric")])
   userEmail = StringField("Email", [validators.DataRequired("Must provide an email address"), 
      validators.Email("Must be a valid email address"), validators.Length(min=6, max=36, "Must be 6 to 36 characters long"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be a valid email address")])
   password = PasswordField("Password", [validators.DataRequired("Must provide a password"), 
      validators.Regexp("[a-zA-Z0-9]", "Must be alphanumeric"), 
      validators.Length(min = 6, max = 36, "Must be 6 to 36 characters long"), 
      validators.EqualTo("confirm", message="Passwords must be the same")])
   confirm = PasswordField("Confirm Password")
   submit = SubmitField("Submit")
   
   def validate_userEmail(self, userEmail):
      users = Users.query.filter_by(userEmail=userEmail.data).count()
      if users != 0:
         raiseValidationError("Email already in use.")
      
   def validate_username(self, username):
      users = Users.query.filter_by(username=username.data).count()
      if users != 0:
         raiseValidationError("Username already in use.")
