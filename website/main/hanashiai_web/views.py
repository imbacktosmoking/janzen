from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from .models import Post
from .models import Comments
from .forms import PostForm,Comments 
from users.forms import RegistrationForm
from django.views.generic.base import View


# Create your views here.

#def homepage(request):
    #return render(request, 'homepage.html')

class Homepage(ListView):
    model = Post 
    template_name = 'homepage.html'

class Post_details(DetailView):
    model = Post
    template_name = 'post_details.html'

class Submit_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = "submit_post.html"
    #fields = '__all__'

class Post_comments(CreateView):
    model = Comments
    form_class = Comments
    template_name = "post_comments.html"


    def form_valid(self, form):
       form.instance.post_id = self.kwargs['pk']
       return super().form_valid(form)


  

class About(ListView):
    model = Post
    template_name = "about.html"
    fields = "__all__"



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
            return redirect('success_url')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email'],
                profile_pic=form.cleaned_data['profile_pic']
            )
            login(request, user)
            return redirect('homepage')
        return render(request, self.template_name, {'form': form})
