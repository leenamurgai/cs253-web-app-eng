###########################################################################################

import webapp2
import re

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

#### UNIT2 ####
from unit2_rot13 import Rot13Handler
from unit2_signup import SignupHandler
from unit2_signup import WelcomeHandler
#### BLOG ####
from blog import BlogHandler
from blog import BlogJSONHandler
from blog import BlogFlushHandler
from blog_newpost import BlogNewPostHandler
from blog_entry import BlogEntryHandler
from blog_entry import BlogEntryJSONHandler
from blog_signup import BlogSignupHandler
from blog_signup import BlogWelcomeHandler
from blog_loginout import BlogLoginHandler
from blog_loginout import BlogLogoutHandler
#### WIKI ####
from wiki_signup import WikiSignupHandler
from wiki_loginout import WikiLoginHandler
from wiki_loginout import WikiLogoutHandler
from wiki_edit import WikiEditHandler
from wiki_edit import WikiHandler
from wiki_page import WikiPageHandler
from wiki_history import WikiHistoryHandler

###########################################################################################

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('CS253 - Web Application Engineering Homework<br><br><br>')
        self.response.out.write('Unit 2: Introduction to web applications<br><br>')
        self.response.out.write('<a href="unit2/rot13">ROT13</a><br>')
        self.response.out.write('<a href="unit2/signup">Signup</a><br><br><br>')
        self.response.out.write('Unit 3: Blog<br><br>')
        self.response.out.write('<a href="blog">blog</a><br>')
        self.response.out.write('<a href="blog/newpost">blog - add a new post</a><br><br><br>')
        self.response.out.write('Unit 4: Blog users<br><br>')
        self.response.out.write('<a href="blog/signup">blog - signup</a><br>')
        self.response.out.write('<a href="blog/login">blog - login</a><br>')
        self.response.out.write('<a href="blog/logout">blog - logout</a><br><br><br>')
        self.response.out.write('Unit 5: Letting other websites get data from your blog<br><br>')
        self.response.out.write('<a href="blog.json">blog - JSON</a><br><br><br>')
        self.response.out.write('Unit 6: Caching the data in your blog<br><br>')
        self.response.out.write('<a href="blog/flush">blog - flush cache</a><br><br><br>')
        self.response.out.write('Unit 7: WIKI<br><br>')
        self.response.out.write('<a href="wiki">wiki</a><br>')
        self.response.out.write('<a href="wiki/signup">wiki - signup</a><br>')
        self.response.out.write('<a href="wiki/login">wiki - login</a><br>')
        self.response.out.write('<a href="wiki/logout">wiki - logout</a><br><br><br>')

###########################################################################################

app = webapp2.WSGIApplication([('/', MainHandler),
                               #### UNIT2 ####
                               ('/unit2/rot13', Rot13Handler),
                               ('/unit2/signup', SignupHandler),
                               ('/unit2/welcome', WelcomeHandler),
                               #### WIKI ####
                               ('/wiki/signup', WikiSignupHandler),
                               ('/wiki/login', WikiLoginHandler),
                               ('/wiki/logout', WikiLogoutHandler),
                               ('/wiki/_edit' + PAGE_RE, WikiEditHandler),
                               ('/wiki/_history' + PAGE_RE, WikiHistoryHandler),
                               ('/wiki' + PAGE_RE, WikiPageHandler),
                               #### BLOG ####
                               ('/blog', BlogHandler),
                               ('/blog.json', BlogJSONHandler),
                               ('/blog/.json', BlogJSONHandler),
                               ('/blog/newpost', BlogNewPostHandler),
                               ('/blog/signup', BlogSignupHandler),
                               ('/blog/welcome', BlogWelcomeHandler),
                               ('/blog/login', BlogLoginHandler),
                               ('/blog/logout', BlogLogoutHandler),
                               ('/blog/flush', BlogFlushHandler),
                               ('/blog/(.*.).json', BlogEntryJSONHandler),
                               ('/blog/(.*)', BlogEntryHandler),
                               ], debug=True)

###########################################################################################