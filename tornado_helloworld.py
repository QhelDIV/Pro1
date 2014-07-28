import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self,para):
		self.write("""
		Hello, world
		<br>
		<form name="input1" action="/" method="post">
			Input your name:
			<input type="text" name="name">
			<input type="submit" value="Submit">
		</form>
		<h3>Or</h3>
		<form name="input2" action="http://www.cojs.tk" method="get">
			<input type="submit" value="Redirect to www.cojs.tk">
		</form>
	<p>And you just send """+string(para)+"as para's value~</p>"
		)
	def post(self):
		self.write("""You just send your name to the web server,and your name is """+self.get_argument("name"))
application = tornado.web.Application([
	(r"/.*", MainHandler),
])

if __name__ == '__main__':
	application.listen(8889)
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
