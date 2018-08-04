###########################################################################################

import webapp2
import json
import time

from handler import Handler

from wiki_models import WikiEntry
from wiki_models import getWikiEntry
from hashing import check_secure_val

###########################################################################################

class WikiPageHandler(Handler):
	def get(self, page):
		wiki_entry = getWikiEntry(page)
		user_id = self.request.cookies.get('user_id')
		username = check_secure_val(user_id)
		if wiki_entry:
			content = wiki_entry.content
			self.render("wiki_page.html", content=content, page=page, username=username)
		else:
			self.redirect("/wiki/_edit%s" % page)

###########################################################################################