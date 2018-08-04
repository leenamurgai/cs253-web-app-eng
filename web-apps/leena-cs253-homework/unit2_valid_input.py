import re

username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_re = re.compile(r"^.{3,20}$")
email_re	= re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
	return username_re.match(username)

def valid_password(password):
	return password_re.match(password)

def valid_email(email):
	return email_re.match(email)