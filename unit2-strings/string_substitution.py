given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
	return given_string % s

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1,s2):
	return given_string % (s1,s2)

given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
	return given_string3 % {'name': name, 'nickname': nickname}