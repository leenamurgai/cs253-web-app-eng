###########################################################################################

from handler import Handler

from wiki_models import WikiEntry
from wiki_models import getWikiEntry
from hashing import check_secure_val

from google.appengine.ext import db

###########################################################################################

class WikiHandler(Handler):
    def get(self):
        user_id = self.request.cookies.get('user_id')
        user_username = check_secure_val(user_id)
        self.response.out.write("Welcome, %s!" % user_username)

###########################################################################################

class WikiEditHandler(Handler):

	def write_form(self, error="", content="", username=""):
		self.render("wiki_edit.html", error=error, content=content, username=username)

	def get(self, page):
		wiki_entry = getWikiEntry(page)
		content = ""
		if wiki_entry:
			content = wiki_entry.content
		user_id = self.request.cookies.get('user_id')
		username = check_secure_val(user_id)
		if username:
			self.write_form(error="", content=content, username=username)
		else:
			if (wiki_entry):
				self.redirect("/wiki%s" % page)
			else:
				self.redirect("/wiki/")

	def post(self, page):
		content = self.request.get('content')
		#page = self.request.get('page')
		if content:
			wiki_entry = getWikiEntry(page)
			version = 1
			if wiki_entry:
				version = wiki_entry.version + 1
			wiki_entry = WikiEntry(page=page, content=content, version=version)
			wiki_entry.put()
			self.redirect("/wiki%s" % page)
		else:
			self.write_form("content please!", content)

###########################################################################################