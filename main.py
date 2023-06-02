import cherrypy
import csv
class Generator(object):
    @cherrypy.expose
    def log(self):
        return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\index.html')
    global b
    b=0
    global c 
    c=0
    @cherrypy.expose
    def login(self, email, password):
        f=open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\userdata.csv','r')
        list1=f.readlines()
        for i in list1:
            if  i.find(email)!=-1:
                global b
                b=1
                if i.find(password)!=-1:
                    print("correct")
                    
                    return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\home.html')
                if i.find(password)==-1:
                    return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\incorrectpswd.html')
            return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\signup.html') 
    if b==0:
        @cherrypy.expose
        def signup(self, name, regno, email, password):
            f1=open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\userdata.csv','a')
            if email.find("vitstudent.ac.in")==-1:
                return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\nonvit pswd.html')
            else:
                f1.write(email+", "+password)            
                global b
                b=1
                global c 
                c=1
                return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\index.html')
    if c==1:
        @cherrypy.expose
        def login(self, email, password):
            f=open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\userdata.csv','r')
            list1=f.readlines()
            for i in list1:
                if  i.find(email)!=-1:
                    global b
                    b=1
                    if i.find(password)!=-1:
                        print("correct")
                        
                        return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\rating.html')
                    else:
                        return open('C:\\Users\\91702\\OneDrive\\Documents\\.vscode\\devsoc\\incorrectpswd.html')
    
    @cherrypy.expose
    def rating(self, rate):
        print("the printed thing is : \n")
        print(rate)

        
        
            
if __name__=="__main__":
    cherrypy.quickstart(Generator())

