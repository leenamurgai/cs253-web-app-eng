###########################################################################################

import logging
import time

from google.appengine.ext import db
from google.appengine.api import memcache

###########################################################################################

class BlogUser(db.Model):
    user_id = db.StringProperty(required=True)
    user_pw = db.StringProperty(required=True)
    user_em = db.StringProperty()

###########################################################################################

class BlogEntry(db.Model):
	subject = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

###########################################################################################

def BlogEntryToDict(self):
	return {'subject': self.subject,
			'content': self.content,
			'created': self.created.strftime("%d %b %Y %H:%M")}

def getBlogEntries(update=False):
	key = 'blog'
	value = memcache.get(key)
	if value is None or update:
		logging.error('Database queried')
		query_time = time.time()
		blog_entries = db.GqlQuery("SELECT * FROM BlogEntry ORDER BY created DESC ")
		blog_entries = list(blog_entries)
		value = (blog_entries, query_time)
		memcache.set(key,value)
	return value
		
def getBlogEntry(blog_post_id):
	key = 'blog_%s' % blog_post_id
	value = memcache.get(key)
	if value is None:
		logging.error('Database queried')
		query_time = time.time()
		blog_entry = BlogEntry.get_by_id(long(blog_post_id))
		value = (blog_entry, query_time)
		memcache.set(key,value)
	return value
		
###########################################################################################
