import cherrypy
import csv
import os, os.path
class Generator(object):
    @cherrypy.expose
    def log(self):
        return open('login.html')
    global b
    b=0
    global c 
    c=0
    @cherrypy.expose
    def login(self, email, password):
        f=open('userdata.csv','r')
        list1=f.readlines()
        for i in list1:
            if  i.find(email)!=-1:
                global b
                b=1
                if i.find(password)!=-1:
                    print("correct")
                    
                    return open('home.html')
                if i.find(password)==-1:
                    return open('incorrectpswd.html')
            return open('signup.html') 
    if b==0:
        @cherrypy.expose
        def signup(self, name, regno, email, password):
            f1=open('userdata.csv','a')
            if email.find("vitstudent.ac.in")==-1:
                return open('nonvit pswd.html')
            else:
                f1.write(email+", "+password)            
                global b
                b=1
                global c 
                c=1
                return open('login.html')
    if c==1:
        @cherrypy.expose
        def login(self, email, password):
            f=open('userdata.csv','r')
            list1=f.readlines()
            for i in list1:
                if  i.find(email)!=-1:
                    global b
                    b=1
                    if i.find(password)!=-1:
                        print("correct")
                        
                        return open('rating.html')
                    else:
                        return open('incorrectpswd.html')
    
    #@cherrypy.expose
    #def rating(self, rate):
    #    print("the printed thing is : \n")
    #    print(rate)

        
        
            
if __name__=="__main__":
    conf = {
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './public'
    }
    }
    cherrypy.quickstart(Generator(),'/', conf)

