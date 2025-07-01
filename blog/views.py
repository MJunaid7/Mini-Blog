from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post , Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# @login_required(login_url="/login/")
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    
    
    
    if request.GET.get('search'):
        posts = posts.filter(title__icontains = request.GET.get('search'))
        
    
    return render(request, 'home.html', {'posts': posts})

    




@login_required(login_url="/login/")
def post_detail(request, id):
    
    post = get_object_or_404(Post, id=id)  
    
    comments = post.comments.all().order_by('-created_at') 
    
    

    
    
    if request.method == 'POST' and request.user.is_authenticated:
        body = request.POST['comment']
        Comment.objects.create(post=post, user=request.user, body=body)
        return redirect('/post_detail/', id = id)
    
    return render(request, 'post_detail.html', {'post': post , 'comments': comments})
    
   



@login_required(login_url="/login/")
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # created_at  = request.POST['created_at']
        Post.objects.create(title=title, content=content, user =request.user)
        
        return redirect('/home/')
    
    
    queryset = Post.objects.all()
    context = {'post_create' : queryset}
    return render(request, 'post_form.html', context)




def register(request):
    
    if request.method == "POST":
        
        data = request.POST
        
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
             )
        
    
    
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created Sucessfully.")
    
    
        return redirect('/register/')
    
    return render(request, 'register.html') 



def login_page(request):
    if request.method == "POST":
        
        data = request.POST
        
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalide username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Invalide password")
            return redirect('/login/')
        
        else:
            login(request, user) 
            return redirect('/home/')
            
        
        
    return render(request, 'login.html') 



def logout_page(request):
    logout(request)

    
    return render(request, 'login.html') 




def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')