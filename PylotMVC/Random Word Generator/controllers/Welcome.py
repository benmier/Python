from system.core.controller import *
import random, string

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

    def index(self):
    	try:
    		session['attempt']
    	except:
    		session['attempt'] = 0

        return self.load_view('index.html', attempt=session['attempt'])

    def generate(self):
        session['attempt'] += 1
        session['randomWord'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
        return redirect('/')
