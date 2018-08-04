import cgi

html_replace = [('&','&amp;'), ('>','&gt;'), ('<','&lt;'), ('"','&quot;')]

def escape_html1(s):
	for (i, o) in html_replace:
		s = s.replace(i, o)
	return s

def escape_html2(s):
	for (i, o) in (('&','&amp;'),
				   ('>','&gt;'),
				   ('<','&lt;'),
				   ('"','&quot;')):
		s = s.replace(i, o)
	return s

def escape_html(s):
	return cgi.escape(s, quote=True)