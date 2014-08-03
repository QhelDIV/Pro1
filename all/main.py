import sys
import time
import torndb
import function
import tornado.web
import mysql_config
import tornado.ioloop
from login_form import login_form
from register_form import register_form
class BaseHandler(tornado.web.RequestHandler):
    def get_current_username(self):
        return self.get_secure_cookie("username")

class MainHandler(BaseHandler):
    def get(self):
        self.current_username=self.get_current_username()
        if not self.current_username:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_username)
        self.write("<p>Hello, " + self.current_username+"</p <br> <a href='/logout'>log out</a>")

class LoginHandler(BaseHandler):
    def get(self):
        self.write(function.render(login_form))
    def post(self):
        request_name=self.get_argument('username')
        query_result=db.query("SELECT * FROM Users WHERE BINARY Username='"+str(request_name)+"'")
        print query_result
        if len(query_result)==0 or query_result[0]['Password']!=self.get_argument('password') :
            print "username or password invalid"
            self.write(function.render("<p><a href='/login'>Invalid Username or password~.~click to go back to login page~.~</a></p>"))
            self.finish()
            return
        print "OOOKKK"
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
        Error_Massege='NONE'
        request_name=self.get_argument('username')
        query_result=db.query("SELECT * FROM Users WHERE BINARY Username='"+str(request_name)+"'")
        print "registering: "+str(query_result)
        print len(query_result)
        if len(query_result)!=0 or not self.get_argument('username'):
            Error_Massege='That username is unacceptable @_@'
            print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        elif self.get_argument('password')!=self.get_argument('confirm'):
            Error_Massege='Passwords do not match'
        elif len(self.get_argument('password'))==0:
            Error_Massege="That password is unacceptable :)"
        if Error_Massege!='NONE':
            print "encounter error when registing:"+Error_Massege
            self.write(function.render("<p><a href='/register'>"+Error_Massege+" click to return to register page@_@"+"</a></p>"))
            self.finish()
            return
        print "no error when registering"
        Getarg=self.get_argument
        print "INSERT INTO Users (Username,Password,Gender,ID) VALUES ('{0}','{1}','{2}',{3})".format(Getarg('username'),Getarg('password'),'male',0)
        db.execute("INSERT INTO Users VALUES ('{0}','{1}','{2}',{3})".format(Getarg('username'),Getarg('password'),'male',0))
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/login")
        
class FileHandler(BaseHandler):
    def get(self,p1):
        try:
            with open(sys.path[0]+"/"+str(p1),'rb') as f:
                data=f.read()
                self.write(data)
            self.finish()
        except IOError:
            self.send_error(404)
            print "File not found!!!!!!!!!!"

application = tornado.web.Application([
(r"/", MainHandler),
(r"/login", LoginHandler),
(r"/logout",LogoutHandler),
(r"/register",RegisterHandler),
(r"/(.*)",FileHandler),
], cookie_secret="63925114")# This is the phone number of number 5304 room in Henan Experimental highschool
if __name__ == '__main__':
    application.listen(8888)
    db = torndb.Connection(host=mysql_config.host+":"+str(mysql_config.port),
                            database=mysql_config.database,
                            user=mysql_config.user,
                            password=mysql_config.password,
                            )
    tornado.ioloop.IOLoop.instance().start()

