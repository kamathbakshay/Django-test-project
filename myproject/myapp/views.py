from django.shortcuts import render
from  .forms import LoginForm

def hello(request):
   return render(request, "myapp/hello.html", {})

def loginpage(request):
    return render(request, "myapp/login.html")
    
def login(request):
   username = "not logged in"
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()

   return render(request, 'loggedin.html', {"username" : username})
