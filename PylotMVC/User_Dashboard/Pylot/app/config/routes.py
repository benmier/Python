from system.core.router import routes

routes['default_controller'] = 'Users'
routes['/signin'] = 'Users#signin'
routes['/register'] = 'Users#register'
routes['POST']['/register_user'] = 'Users#register_user'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/post_message'] = 'Messages#post_message'
routes['POST']['/post_comment/<message_id>'] = 'Messages#post_comment'
routes['/logout'] = 'Users#logout'
routes['/travels/destination/<id>'] = 'Travels#destination'

# routes['/users/show/<id>'] = 'users#show'
# routes['/users/edit/<id>'] = 'users#edit'
# routes['/users/new'] = 'users#new'
# routes['POST']['/users/create'] = 'users#create'
# routes['POST']['/users/update/<id>'] = 'users#update'
# routes['POST']['/users/delete/<id>'] = 'users#destroy'











"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
