# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		self.response.write('Greetings')  # the response

class LoginPage(webapp2.RequestHandler):
	def get(self):
		login_template = the_jinja_env.get_template('pages/loginPage.html')
		self.response.write('LoginPage')

class RecommendedPage(webapp2.RequestHandler):
	def get(self):
		recommended_page = the_jinja_env.get_template('pages/recommendedPage.html')


# the app configuration section	
app = webapp2.WSGIApplication([
  ('/signin',SignupPage),
  ('/login', LoginPage),
  ('/', MainHandler),
  ('/recommend', RecommendedPage)
  ], debug=True)