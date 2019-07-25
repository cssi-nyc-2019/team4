# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
jinja_current_directory = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

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

# the app configuration section	
app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ("/new_page.php", QuizHandler),
  ("/action_page.php", RecommendedPage)
  #('/about', AboutUsHandler),
  ], debug=True)


