import hashlib
import random
import string
import hmac

def hash_str1(s):
    return hashlib.md5(s).hexdigest()

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'username_secret'
def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

# -----------------
# User Instructions
# 
# Implement the function make_secure_val, which takes a string and returns a 
# string of the format: 
# s|HASH

def make_secure_val1(s):
    return s + '|' + hash_str(s)

def make_secure_val(s):
    return "%s|%s" % (s,hash_str(s))

def check_secure_val(h):
	val = h.split('|')[0]
	if h==make_secure_val(val):
		return val

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
	if not salt:
		salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s|%s' % (h, salt)

def valid_pw(name, pw, h):
	salt = h.split('|')[1]
	return h == make_pw_hash(name, pw, salt)