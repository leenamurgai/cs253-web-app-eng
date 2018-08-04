import webapp2

from unit2_valid_input import valid_username
from unit2_valid_input import valid_password
from unit2_valid_input import valid_email
from functions import escape_html

form_signup="""
<head>
    <title>Sign Up</title>
    <style type="text/css">
        .label {text-align: right}
        .error {color: red}
    </style>
</head>
<body>
    <h2>Signup</h2>
    <form method="post">
        <table>
            <tr>
                <td class="label">
                    Username
               </td>
                <td>
                    <input type="text" name="username" value="%(username)s">
                </td>
                <td class="error">
                    %(err_uname)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    Password
                </td>
                <td>
                    <input type="password" name="password" value="">
                </td>
                <td class="error">
                    %(err_pwd)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    Verify Password
                </td>
                <td>
                    <input type="password" name="verify" value="">
                </td>
                <td class="error">
                    %(err_ver)s
                </td>
            </tr>

            <tr>
                <td class="label">
                    Email (optional)
                </td>
                <td>
                    <input type="text" name="email" value="%(email)s">
                </td>
                <td class="error">
                    %(err_email)s
                </td>
            </tr>
        </table>

        <input type="submit">
    </form>
</body>
"""

class SignupHandler(webapp2.RequestHandler):

    def write_form(self, err_uname="", err_pwd="", err_ver="", err_email="",
                   username="", email=""):
        self.response.out.write(form_signup % {"err_uname": err_uname,
                                               "err_pwd": err_pwd,
                                               "err_ver": err_ver,
                                               "err_email": err_email,
                                               "username": escape_html(username),
                                               "email": escape_html(email)})

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

        if not (username and password and verify and email):
            self.write_form(err_uname_, err_pwd_, err_ver_, err_email_,
                            user_username, user_email)
        else:
            self.redirect("/unit2/welcome?username=%s" % user_username )

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        user_username = self.request.get('username')
        self.response.out.write("Welcome, %s!" % user_username)
