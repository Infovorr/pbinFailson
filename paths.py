from flask import render_template, redirect
from flask_login import current_user, login_user, logout_user
from app import app
from app import database
from app.formHandler import *
from app.tables import *
import datetime
import re
import short_url

@app.route("/")
@app.route("/index")
def index():
   post = Posts.query.filter_by(private = 0).order_by(desc(id)).limit(10)
   return render_template("index.html", posts = posts)

@app.route("/adminLogin", methods=["GET", "POST"])
def adminLogin():
   if current_user.is_authenticated:
      return redirect("/index")
   adminLoginForm = AdminLoginPage()
   if adminLoginForm.validate_on_submit():
      user = Users.query.filter_by(username = adminLoginForm.username.data, admin = 1).first()
      if user is None or not user.verify(adminLoginForm.password.data):
         return redirect("/adminLogin")
      login_user(user, remember = adminLoginForm.remember_me.data)
   return render_template("adminLogin.html", title = "Admin Log In", adminLoginForm = adminLoginForm)

@app.route("/adminPortal", methods = ["GET", "POST"])
def adminPortal():
   
@app.route("/browse/posts/<dynamic>", methods = ["GET", "POST"])
def browseP(dynamic):
   
@app.route("/browse/users/<dynamic>", methods = ["GET", "POST"])
def browseU(dynamic):
   
@app.route("/create", methods = ["GET", "POST"])
def create():
   
@app.route("/deleteAccount", methods = ["GET", "POST"])
def deleteAccount():
   if not current_user.is_authenticated:
      return redirect("/login")
   deleteAForm = DeleteAPage()
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   if deleteAForm.validate_on_submit():
      if not user.verify(deleteAForm.password.data):
         return redirect("/management")
      logout_user()
      user = Users.query.filter(username = deleteAForm.username.data).first().delete()
      database.session.commit()
      return redirect("/index")
   return render_template("deleteAccount.html", title = "Delete Account", deleteAForm = deleteAForm)

@app.route("/deleteUser/<dynamic>", methods = ["GET", "POST"])
def deleteUser(dynamic):
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   if not current_user.is_authenticated:
      return redirect("/login")
   deleteUForm = DeleteUPage()
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   if deleteUForm.validate_on_submit():
      if user.admin != 1:
         return redirect("/index")
      delUser = Users.query.filter(id = dynamic).first().delete()
      database.session.commit()
      return redirect("/index")
   return render_template("deleteUser.html", title = "Delete User", deleteUForm = deleteUForm)

@app.route("/post/delete/<dynamic>", methods = ["GET", "POST"])
def deletePost(dynamic):
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   if not current_user.is_authenticated:
      return redirect("/login")
   deletePForm = DeletePPage()
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   if deletePForm.validate_on_submit():
      if int(deletePForm.confirm.data) == 0:
         return redirect("/index")
      if user.username != Posts.query.filter(id = sanitized).first().author:
         return redirect("/index")
      post = Posts.query.filter(id = sanitized).first().delete()
      database.session.commit()
      return redirect("/index")
   return render_template("deletePost.html", title = "Delete Post", deletePForm = deletePForm)

@app.route("/<dynamic>", methods = ["GET"])
def display(dynamic):
   tempFix = re.findall("[a-z0-9]", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = tempFix[0]
   post = Posts.query.filter_by(short = sanitized).first()
   if not current_user.is_authenticated and post.private == 1:
      return redirect("/index")
   if post.private == "1":
      user = Users.query.filter_by(id = int(current_user.get_id())).first()
      permissions = post.permissions.split(",")
      if user.name not in permissions and user.admin == 0:
         return redirect("/index")
   return render_template("display.html", title = post.title, author = post.author, id = post.id, 
      content = post.content, date = post.date)

@app.route("/post/edit/<dynamic>", methods = ["GET", "POST"])
def editP(dynamic):
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   if not current_user.is_authenticated:
      return redirect("/login")
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   post = Posts.query.filter(id = sanitized).first()
   editPForm = EditPPage(obj = post)
   if editPForm.validate_on_submit():
      if user.name != post.author:
         return redirect("/index")
      editPForm.populate_obj(post)
      database.session.commit()
      return redirect("/index")
   return render_template("editPost.html", title = "Edit Post", editPForm = editPForm)
   
@app.route("/endis/<dynamic>", methods = ["GET", "POST"])
def endis(dynamic):
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   if not current_user.is_authenticated:
      return redirect("/login")
   endisForm = EndisPage()
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   if user.admin != 1:
      return redirect("/index")
   if deletePForm.validate_on_submit():
      post = Posts.query.filter(id = sanitized).first()
      if int(endisForm.confirm.data) == 0:
         post.enabled = 0
         database.session.commit()
         return redirect("/index")
      post.enabled = 1
      database.session.commit()
      return redirect("/index")
   return render_template("endis.html", title = "Enable/Disable Post", endisForm = endisForm)
   
@app.route("/login", methods=["GET", "POST"])
def login():
   if current_user.is_authenticated:
      return redirect("/index")
   loginForm=LoginPage()
   if loginForm.validate_on_submit():
      user = Users.query.filter_by(username = loginForm.username.data, admin = 0).first()
      if user is None or not user.verify(loginForm.password.data):
         return redirect("/login")
      login_user(user, remember = loginForm.remember_me.data)
   return render_template("login.html", title= "Log In", loginForm = loginForm)

@app.route("/logout")
def logout():
   if not current_user.is_authenticated:
      return redirect("/login")
   logout_user()
   return redirect("/index")

@app.route("/management", methods = ["GET", "POST"])
def management():
   
@app.route("/post", methods = ["GET", "POST"])
def post():
   if not current_user.is_authenticated:
      return redirect("/login")
   user = Users.query.filter_by(id = int(current_user.get_id()))
   if user.admin == "1":
      return redirect("/index")
   postForm = postPage()
   if postForm.validate_on_submit():
      current_dt = datetime.datetime.now()
      dateCheck = current_dt.strftime("%d/%m/%Y").split("/")
      expirationCheck = postForm.expiration.data.split("/")
      if expirationCheck is not None:
         if expirationCheck[3] < dateCheck[3]:
            return redirect("/post")
         if expirationCheck[3] == dateCheck[3]:
            if expirationCheck[2] < dateCheck[2]:
               return redirect("/post")
            if expirationCheck[2] == dateCheck[2]:
               if expirationCheck[1] <= dateCheck[1]:
                  return redirect("/post")
         if expirationCheck[2] > "12":
            return redirect("/post")
         if expirationCheck[1] > "31":
            return redirect("/post")
         if expirationCheck[2] == "2" and expirationCheck[1] > "28":
            return redirect("/post")
         if expirationCheck[2] == "4" or "6" or "9" or "11" and expirationCheck[1] > "30":
            return redirect("/post")
      post = Posts()
      post.title = postForm.title.data or ""
      post.date = current_dt.strftime("%d/%m/%Y")
      post.author = user.username
      post.private = postForm.private.data
      post.permissions = postForm.permissions.data or ""
      post.short = short_url.encode_url(post.username + post.date + datetime.datetime.now().time())
      post.content = postForm.content.data or ""
      post.expiration = postForm.expiration.data or ""
      post.enabled = 1
      database.session.add(post)
      database.session.commit()
      return redirect("")
   return render_template("post.html", title = "New Post", postForm = postForm)
   
@app.route("/registration", methods=["GET", "POST"])
def register():
   if current_user.is_authenticated:
      return redirect("/index")
   regForm=RegistrationPage()
   if regForm.validate_on_submit():
      user = Users()
      user.username = regForm.username.data
      user.userEmail = regForm.userEmail.data
      user.hashPassw(regForm.password.data)
      user.reset = 0
      user.admin = 0
      database.session.add(user)
      database.session.commit()
      return redirect("/index")
   return render_template("registration.html", title="Register An Account", regForm=regForm)

@app.route("/reset", methods = ["GET", "POST"])
def reset():
   
@app.route("/search/posts/<dynamic>", methods = ["GET", "POST"])
def searchP(dynamic):
   
@app.route("/search/users/<dynamic>", methods = ["GET", "POST"])
def searchU(dynamic):

@app.route("/upload", methods = ["GET", "POST"])
def upload():

@app.route("/user/edit/<dynamic>", methods = ["GET", "POST"])
def editU(dynamic):
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   if not current_user.is_authenticated:
      return redirect("/login")
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   editUForm = EditUPage(obj = user)
   if editUForm.validate_on_submit():
      if user.id != sanitized and user.admin != "1":
         return redirect("/index")
      editUForm.populate_obj(user)
      database.session.commit()
      return redirect("/index")
   return render_template("editUser.html", title = "Edit User", editUForm = editUForm)

@app.route("/admin/edit/<dynamic>", methods = ["GET", "POST"])
def editA(dynamic):
   if not current_user.is_authenticated:
      return redirect("/login")
   user = Users.query.filter_by(id = int(current_user.get_id())).first()
   if user.admin != "1":
      return redirect("/login")
   tempFix = re.findall("\d+", dynamic)
   if len(tempFix) == 0:
      return redirect("/index")
   sanitized = ""
   for x in tempFix:
      sanitized += x
   sanitized = int(sanitized)
   editAForm = EditAPage(obj = user)
   if editAForm.validate_on_submit():
      if user.id != sanitized:
         return redirect("/index")
      editAForm.populate_obj(user)
      database.session.commit()
      return redirect("/index")
   return render_template("editAdmin.html", title = "Edit User", editAForm = editAForm)
   
@app.route("/user/delete/<dynamic>", methods = ["GET", "POST"])
def deleteUser(dynamic):
