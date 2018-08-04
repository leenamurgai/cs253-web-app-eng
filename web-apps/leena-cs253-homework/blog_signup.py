###########################################################################################

from handler import Handler
from blog_models import BlogUser

from unit2_valid_input import valid_username
from unit2_valid_input import valid_password
from unit2_valid_input import valid_email
from hashing import make_pw_hash
from hashing import make_secure_val
from hashing import check_secure_val

###########################################################################################

class BlogSignupHandler(Handler):

    def write_form(self, err_uname="", err_pwd="", err_ver="", err_email="",
                   username="", email=""):
        self.render("signup.html", err_uname = err_uname,
                                   err_pwd = err_pwd,
                                   err_ver = err_ver,
                                   err_email = err_email,
                                   username = username,
                                   email = email)

    def get(self):
        self.write_form()

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify   = self.request.get('verify')
        user_email    = self.request.get('email')

        username = valid_username(user_username)
        password = valid_password(user_password)
        if (user_verify!=user_password):
            verify = None
        else:
            verify = user_verify
        if (user_email):
            email = valid_email(user_email)
        else:
            email = 'not_supplied'

        err_uname_ = ""
        err_pwd_   = ""
        err_ver_   = ""
        err_email_ = ""
        
        if not (username):
            err_uname_ ="That's not a valid username." 
        if not (password):
            err_pwd_ = "That wasn't a valid password."
        if not (verify):
            err_ver_ = "Your passwords didn't match."
        if not (email):
            err_email_ = "That's not a valid email."

        if (username):
            username_query = db.GqlQuery("SELECT * FROM BlogUser WHERE user_id=:1", user_username)
            username_used = username_query.fetch(1)
            if (username_used):
                username_new = False
                err_uname_="That user already exits"
            else:
                username_new = True

        if not (username and password and verify and email and username_new):
            self.write_form(err_uname_, err_pwd_, err_ver_, err_email_,
                            user_username, user_email)
        else:
            this_user = BlogUser(user_id=user_username,
                                 user_pw=make_pw_hash(user_username,user_password),
                                 user_em=user_email)
            this_user.put()
            self.response.headers.add_header('Set-Cookie','user_id=%s; Path=/'
                                             % str(make_secure_val(user_username)))
            self.redirect("/blog/welcome")

###########################################################################################

class BlogWelcomeHandler(Handler):
    def get(self):
        user_id = self.request.cookies.get('user_id')
        user_username = check_secure_val(user_id)
        if (user_username):
            self.response.out.write("Welcome, %s!" % user_username)
        else:
            self.redirect("/blog/signup")

###########################################################################################