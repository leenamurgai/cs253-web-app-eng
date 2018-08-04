###########################################################################################

from handler import Handler

from blog_models import BlogEntry
from blog_models import getBlogEntries

from google.appengine.ext import db

###########################################################################################

class BlogNewPostHandler(Handler):

	def write_form(self, error="", subject="", content=""):
		self.render("blog_newpost.html", error=error, subject=subject, content=content)

	def get(self):
		self.write_form()

	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')
		if subject and content:
			blog_post = BlogEntry(subject=subject, content=content)
			blog_post_key = blog_post.put()
			getBlogEntries(True)
			self.redirect("/blog/%s" % blog_post_key.id())
		else:
			self.write_form("subject and content please!", subject, content)

###########################################################################################