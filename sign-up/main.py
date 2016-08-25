import webapp2
import random
import re
import cgi
header_block = """
<!DOCTYPE html>
<html>
  <head>
    <title>The One and The Only</title>
    <style type='text/css'>
     body {
     background-color:#ccc;
     }
     input {
     margin-left:5px;
     }
     .label {
     display: inline-block;
     width: 140px;
     text-align:left;
     }
     #button {
     background-color:red;
     color:#fff;
     border:none;
     text-align: center;
     text-decoration: none;
     width:100px;
     height:40px;
     margin-left:150px;

     }
     #button:hover {
     background-color:green;

     }
     #error{
       color:red;
       font-size:20px;
       margin:10px;
     }

    </style>
  </head>

<body>
 """
myForm = """
  <form method="post" action="/">
  <label class="label">Name : </label>
  <input type="text" name="username" value="%(name)s"  placeholder="Enter Name"/> </br>
  <label class="label">Password : </label>
  <input type="password" name="password" placeholder="Enter Password" /> </br>
  <label class="label">Re-Enter Password : </label>
  <input type="password" name="verify" placeholder="Re-Enter Password"/> </br>
  <label class="label">Email : </label>
  <input type="text" name="email" value="%(email)s" placeholder="Enter Email(Optional)"/></br>
  <input id="button" type="submit" value="Join!" />
  </form>
  <div id="error">%(error)s</div>
"""

footer_block = """
</body>
</html>

 """
usernamecor = re.compile("^[a-zA-Z0-9_-]{3,20}$")
passwordcor = re.compile("^.{3,20}$")
emailcor = re.compile("^[\S]+@[\S]+.[\S]+$")

class MainHandler(webapp2.RequestHandler):
    def write_form(self,error="",name="",email=""):
        self.response.write(myForm %{"error":error,
                                     "name":name,
                                     "email":email})
    def valid_username(self,username):
        return usernamecor.match(username)
    def valid_password(self,password):
        return passwordcor.match(password)
    def valid_email(self,email):
        return emailcor.match(email)

    def header(self,message=""):
        self.response.write(message)

    def get(self):
        self.header("<h1> Application to join My PowerRanger Team!</h1>")
        page = header_block + footer_block
        self.response.write(page)
        self.write_form()

    def post(self):
        getUserName = self.request.get("username")
        getUserPassword = self.request.get("password")
        getUserRPassword = self.request.get("verify")
        getUserEmail = self.request.get("email")
        egetUserName = cgi.escape(getUserName)
        egetUserPassword= cgi.escape(getUserPassword)
        egetUserRPassword = cgi.escape(getUserRPassword)
        egetUserEmail = cgi.escape(getUserEmail)

        ranger = ["Black","Blue","Green","Pink","Red","White","Yellow"]
        powerranger = random.choice(ranger)

        page = header_block + footer_block
        self.response.write(page)

        if (egetUserName==""):
            self.header("<h1> Application to join My PowerRanger Team!</h1>")
            self.write_form("How am I suppose to contact you without a name?! Please enter a name!",egetUserName,egetUserEmail)
        elif not (self.valid_username(egetUserName)):
            self.write_form("Please erase any spaces in your username",egetUserName,egetUserEmail)
        elif (egetUserPassword==""):
            self.header("<h1> Application to join My PowerRanger Team!</h1>")
            self.write_form("Please enter a password",egetUserName,egetUserEmail)
        elif not (egetUserPassword==egetUserRPassword):
            self.header("<h1> Application to join My PowerRanger Team!</h1>")
            self.write_form("Your passwords do not match!",egetUserName,egetUserEmail)
        elif not (self.valid_email(egetUserEmail)):
            self.write_form("Please enter a valid email, so we can email you ofcourse!",egetUserName,egetUserEmail)
        else:
            self.header("<h1>Initiation</h1>")
            page = header_block + footer_block
            self.response.write(page)
            welcome = "Welcome "+ egetUserName + ", I bestow upon you the title <b>"+ powerranger+ " Ranger! </b>"
            self.response.write(welcome)







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
