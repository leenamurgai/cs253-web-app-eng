###########################################################################################

from handler import Handler

from wiki_models import WikiUser

from hashing import valid_pw
from hashing import make_secure_val

from google.appengine.ext import db

###########################################################################################

class WikiLoginHandler(Handler):

    def write_form(self, error=""):
        self.render("login.html", error = error)

    def get(self):
        self.write_form()

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')

        username_query = db.GqlQuery("SELECT * FROM WikiUser WHERE user_id=:1", user_username)
        this_user = username_query.fetch(1)
        if (this_user and valid_pw(user_username, user_password, this_user[0].user_pw)):
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/'
                                             % str(make_secure_val(user_username)))
            self.redirect("/wiki/")
        else:
            self.write_form("Invalid login")

###########################################################################################

class WikiLogoutHandler(Handler):

    def get(self):
        self.response.headers.add_header('Set-Cookie','user_id=; Path=/')
        self.redirect("/wiki/")

###########################################################################################