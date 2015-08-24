# project/app/admin/admin.py
#!C:/Python27/python.exe
# We make use of flask Methodview
# it's a class that we can inherit from and define a get and post methods
# inside of it and the url dispatcher will automaticly link to relevant http method
from flask.views import MethodView

# the model to we want to administer
from .models import Blog

# our crud class that we will continiously expand on
# and later use for any given model that we define
class CRUDView(MethodView):
	# default template that we will use to display a list
    # of all items in a model
    list_template = 'admin/list_view.html'

    def __init__(self, model, endpoint, list_template=None):
        self.model = model
        self.endpoint = endpoint
        # so we can generate a url relevant to this
        # endpoint, for example if we utilize this CRUD object
        # to enpoint comments the path generated will be
        # /admin/comments/
        self.path = url_for('.%s' % self.endpoint)
        if list_template:
            self.list_template = list_template


    # all GET methods will link to this function
    def get():
        obj = self.model.query.all()
        return render_template(list_template, obj=obj, path=self.path)
	

# this turns the class to a function that flask can use for requests
# the argument it takes is the endpoint that you can call in url_for()
# since we are using a blueprint called admin the endpoint becomes
# in this case 'admin.blog' or simply '.blog'
# the '.' links to the current app(which is 'admin')
view = CRUDView.as_view('blog')

# now we just add the url rule
admin.add_url_rule('/blog/', view_func=view, methods=['GET', 'POST'])