###########################################################################################

import logging
import time

from google.appengine.ext import db
from google.appengine.api import memcache

###########################################################################################

class WikiUser(db.Model):
    user_id = db.StringProperty(required=True)
    user_pw = db.StringProperty(required=True)
    user_em = db.StringProperty()

###########################################################################################

class WikiEntry(db.Model):
	page = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	version = db.IntegerProperty(required=True)

###########################################################################################

def WikiEntryToDict(self):
	return {'content': self.content,
			'created': self.created.strftime("%d %b %Y %H:%M")}

def getWikiEntry(page):
	wiki_entries = list(db.GqlQuery("SELECT * FROM WikiEntry WHERE page=:1 ORDER BY version DESC", page))
	if len(wiki_entries)>0:
		return wiki_entries[0]
	else:
		return None

def getWikiEntries(page):
	wiki_entries = list(db.GqlQuery("SELECT * FROM WikiEntry WHERE page=:1 ORDER BY version DESC", page))
	return wiki_entries
		
###########################################################################################
