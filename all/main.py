import tornado.ioloop
import tornado.web
import function
from login_form import login_form
class BaseHandler(tornado.web.RequestHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
	def get(self):
		if not self.current_user:
			self.redirect("/login")
		return
		name = tornado.escape.xhtml_escape(self.current_user)
		self.write("Hello, " + name)

class LoginHandler(BaseHandler):
	def get(self):
		self.write(function.render(login_form))
	def post(self):
		self.set_secure_cookie("user", self.get_argument("name"))
		self.redirect("/")

application = tornado.web.Application([
(r"/", MainHandler),
(r"/login", LoginHandler),
], cookie_secret="63925114")# This is the phone number of number 5304 room in Henan Experimental highschool
if __name__ == '__main__':
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
