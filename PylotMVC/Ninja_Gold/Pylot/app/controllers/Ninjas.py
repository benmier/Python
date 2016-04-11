from system.core.controller import *
from random import randint
from time import strftime

class Ninjas(Controller):
    def __init__(self, action):
        super(Ninjas, self).__init__(action)

    def index(self):
        try:
            session['gold']
        except:
            session['gold'] = 0
            session['activity'] = []
        return self.load_view('index.html', gold=session['gold'], activity=session['activity'])

    def process_monkey(self):
        if request.form['building']=='farm':
            reward = randint(10,20)
            session['gold']+=reward
            session['activity'].insert(0,"Earned {} golds from the farm! ({})".format(reward,strftime("%H:%M:%S %p - %B %d, %Y")))
        elif request.form['building']=='cave':
            reward = randint(5,10)
            session['gold']+=reward
            session['activity'].insert(0,"Earned {} golds from the cave! ({})".format(reward,strftime("%H:%M:%S %p - %B %d, %Y")))
        elif request.form['building']=='house':
            reward = randint(2,5)
            session['gold']+=reward
            session['activity'].insert(0,"Earned {} golds from the house! ({})".format(reward,strftime("%H:%M:%S %p - %B %d, %Y")))
        elif request.form['building']=='casino':
            reward = randint(-50,50)
            session['gold']+=reward
            if reward>0:
                gainLoss = "Earned"
            else:
                gainLoss = "Lost"
            session['activity'].insert(0,"{} {} golds from the casino! ({})".format(gainLoss,abs(reward),strftime("%H:%M:%S %p - %B %d, %Y")))
        return redirect('/')

