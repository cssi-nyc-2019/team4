# the import section
import webapp2
import jinja2
import os
from webapp2_extras import sessions
from models import User


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
jinja_current_directory = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


#user info storage 
def getCurrentUser(self):
  #will return None if user does not exist
  return self.session.get('user')

def login(self, id):
  self.session['user'] = id

def logout(self):
  self.session['user'] = None

def isLoggedIn(self):
  if self.session['user'] is not None:
    return True
  else:
    return False

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

class SignupHandler(BaseHandler):
  def get(self):  # for a get request
    signup_template = jinja_current_directory.get_template('pages/survey.html')
    username = self.request.get('name')
    email = self.request.get('psw')
    password = self.request.get('psw-repeat')

    user = User(username = username, email = email, password = password)
    user_id = user.put()
    login(self, username)
    variable_dict = {"username": username}
    self.response.write(signup_template.render(variable_dict))

'''
  def post(self):
    signup_template = jinja_current_directory.get_template('pages/survey.html')
    username = self.request.get('username')
    email = self.request.get('email')
    password = self.request.get('password')

    user = User(username = username, email = email, password = password)
    user_id = user.put()
    login(self, username)
    variable_dict = {"username": username}
    self.response.write(signup_template.render(variable_dict))
'''

class LogoutHandler(BaseHandler):
  def get(self):  # for a get request
    logout_template =jinja_current_directory.get_template('pages/logout.html')
    user = getCurrentUser(self)
    if user is not None:
      logout(self)
      self.response.write(logout_template.render())
    else:
      self.redirect('/')


# other functions should go above the handlers or in a separate file

# the handler section
class MainHandler(webapp2.RequestHandler):

  def get(self):# for a get request
    login_template = jinja_current_directory.get_template("pages/loginPage.html")
    self.response.write(login_template.render())

  def post(self):
    recommend_list= self.request.get('uname')
    rec_template=jinja_current_directory.get_template("pages/recommendedPage.html")
    self.response.write(rec_template.render(recommend_list))



class QuizHandler(webapp2.RequestHandler):
  def get(self):

    quiz_template=jinja_current_directory.get_template("pages/survey.html")
    self.response.write(quiz_template.render())

  
  def post(self):
    quiz_list= self.request.get('name')
    survey_template=jinja_current_directory.get_template("pages/survey.html")
    self.response.write(survey_template.render(quiz_list))

  def post(self):
    start_list= self.request.get('books')
    mend_template=jinja_current_directory.get_template("pages/recommendedPage.html")
    self.response.write(mend_template.render(start_list))



class RecommendedPage(webapp2.RequestHandler):
  def get(self):
    recommended_template = jinja_current_directory.get_template('pages/recommendedPage.html')
    self.response.write(recommended_template.render())


  def post(self):
    recommend_list= self.request.get('uname')
    rec_template=jinja_current_directory.get_template("pages/recommendedPage.html")
    self.response.write(rec_template.render(recommend_list))


class AboutUsHandler(webapp2.RequestHandler):
  def get(self):
    about_template = jinja_current_directory.get_template("pages/about_us.html")
    self.response.write(about_template.render())

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}

# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ("/new_page.php", SignupHandler),
  ("/about", AboutUsHandler),
  ("/action_page.php", RecommendedPage),
  ("/logout.html", LogoutHandler),
  ], debug=True, config=config)


