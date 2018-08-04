import webapp2

from functions import escape_html

form_rot13="""
<h2>Enter some text to ROT13:</h2>
<form method="post">
  <textarea name="text"
            style="height: 100px; width: 400px;">%s</textarea>
  <br>
  <input type="submit">
</form>
"""

class Rot13Handler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form_rot13 % "")

    def post(self):
		in_text = self.request.get('text')
		out_text = escape_html(in_text.encode("rot13"))
		self.response.out.write(form_rot13 % out_text)