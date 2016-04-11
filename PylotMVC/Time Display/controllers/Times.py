"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime

class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        date = strftime("%B %d, %Y")
        time = strftime("%H:%M %p")
        return self.load_view('index.html', date=date,time=time)

    def show(self):
        return self.load_view('welcome/show.html')