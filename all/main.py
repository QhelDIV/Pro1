import tornado.ioloop
import tornado.web
import function
import torndb
import _mysql
from login_form import login_form
class BaseHandler(tornado.web.RequestHandler):
	def get_current_username(self):
		return self.get_secure_cookie("username")

class MainHandler(BaseHandler):
	def get(self):
		self.current_username=self.get_current_username()
		if not self.current_username:
			self.redirect("/login")
			return
	#	name = tornado.escape.xhtml_escape(current_username)
		self.write("<p>Hello, " + self.current_username+"</p <br> <a href='/logout'>log out</a>")

class LoginHandler(BaseHandler):
	def get(self):
		self.write(function.render(login_form))
	def post(self):
		self.set_secure_cookie("username", self.get_argument("username"))
		self.redirect("/")

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("username")
		self.redirect("/login")

class RegisterHandler(BaseHandler):
	def get(self):
		self.write(function.render(register_form))
	def post(self):
		self.set_secure_cookie("username", self.get_argument("username"))
		self.redirect("/login")
		
class FileHandler(BaseHandler):
	def get(self,p1):
		try:
			with open(r'/home/qheldiv/Documents/Pro1/all/'+str(p1),'rb') as f:
				data=f.read()
				self.write(data)
			self.finish()
		except IOError:
			self.send_error(404)
			print "File not found!"

application = tornado.web.Application([
(r"/", MainHandler),
(r"/login", LoginHandler),
(r"/logout",LogoutHandler),
(r"/register",RegisterHandler),
(r"/(.*)",FileHandler),
], cookie_secret="63925114")
# This is the phone number of number 5304 room in Henan Experimental highschool
if __name__ == '__main__':
	db=_mysql.connect()
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
