import os

from string import letters
import jinja2
import webapp2


from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Rot13(Handler):
	def get(self):
		self.render("rot13.html")

	def post(self):
		output = ""
		text = self.request.get("text")
		if text:
			output = text.encode('rot13')
		
		self.render("rot13.html", text = output)



app = webapp2.WSGIApplication([('/', Rot13)], debug = True)





