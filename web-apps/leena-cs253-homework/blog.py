###########################################################################################

import webapp2
import json
import time

from handler import Handler

from blog_models import BlogEntry
from blog_models import getBlogEntries
from blog_models import BlogEntryToDict

from google.appengine.api import memcache

###########################################################################################

class BlogHandler(Handler):

	def get(self):
		(blog_entries, query_time) = getBlogEntries()
		time_elapsed = int(round(time.time()-query_time))
		self.render("blog_front.html", blog_entries=blog_entries, time_elapsed=time_elapsed)

###########################################################################################

class BlogJSONHandler(webapp2.RequestHandler):

	def get(self):
		self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
		(blog_entries, query_time) = getBlogEntries()
		blog_entries_dict_list = []
		for blog_entry in blog_entries:
			blog_entries_dict_list.append(BlogEntryToDict(blog_entry))
		self.response.out.write(json.dumps(blog_entries_dict_list))

###########################################################################################

class BlogFlushHandler(Handler):

    def get(self):
    	memcache.flush_all()
        self.redirect("/blog")

###########################################################################################

