import webapp2
import random


def getRandomFortune():
    fortunes = [
    	"I see much code",
	"Consider eating more",
	"you have tamed python ...",
    ]
    return random.choice(fortunes)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	header = "<h1>Fortune Cookie</h1>"

	fortune = "<strong>" + getRandomFortune() + "</strong>"
	fortune_sentence = "Your fortune is: " + fortune
	fortune_paragraph = "<p>" + fortune_sentence + "</p>"

	luckynumber = random.randint(1,100)
        number_sentence = 'Your luck number: ' + "<strong>" + str(luckynumber) + "</strong>"
	number_paragragh = "<p>" + number_sentence + "</p>"

	more_cookie = "<a href='.'><button>Another cookie please!</button></a>"
	content = header + fortune_paragraph + number_paragragh + more_cookie

        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for the login")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
