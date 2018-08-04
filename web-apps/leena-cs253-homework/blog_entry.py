###########################################################################################

import webapp2
import json
import time

from handler import Handler

from blog_models import BlogEntry
from blog_models import getBlogEntry
from blog_models import BlogEntryToDict

###########################################################################################

class BlogEntryHandler(Handler):
	def get(self, blog_post_id):
		(blog_entry, query_time) = getBlogEntry(blog_post_id)
		time_elapsed = int(round(time.time()-query_time))
		self.render("blog_front.html", blog_entries=[blog_entry], time_elapsed=time_elapsed)

###########################################################################################

class BlogEntryJSONHandler(webapp2.RequestHandler):
	def get(self, blog_post_id):
		self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
		blog_entry = BlogEntry.get_by_id(long(blog_post_id))
		self.response.out.write(json.dumps(BlogEntryToDict(blog_entry)))

###########################################################################################

