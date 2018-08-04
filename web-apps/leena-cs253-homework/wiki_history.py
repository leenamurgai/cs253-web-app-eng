###########################################################################################

import webapp2
import json
import time

from handler import Handler

from wiki_models import WikiEntry
from wiki_models import getWikiEntries
from hashing import check_secure_val

###########################################################################################

class WikiHistoryHandler(Handler):
	def get(self, page):
		wiki_entries = getWikiEntries(page)
		user_id = self.request.cookies.get('user_id')
		username = check_secure_val(user_id)
		if len(wiki_entries)>0:
			self.render("wiki_history.html", wiki_entries=wiki_entries,
											 page=page,
											 username=username)
		else:
			self.redirect("/wiki/_edit%s" % page)

###########################################################################################