from django.views import generic
from login.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
def signup(request):
    username = "not logged in"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password')
            
            return render(request, 'login/loggedin.html', {'username': username})
    else:
        form = SignUpForm()

    return render(request, 'login/signup.html', {'form': form})


def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'login/loggedin.html', {"username" : username})


class DetailView(generic.DetailView):
    #model = Question
    #import pdb; pdb.set_trace()
    #template_name = 'polls/detail.html'
    pass

class ResultsView(generic.DetailView):
    #model = Question
    #template_name = 'polls/results.html'
    pass