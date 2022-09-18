
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Blogs_Category,Blogs_Post

# Create your views here.
def home(request):
    Img_data= Blogs_Post.objects.get_queryset().order_by('post_id')
    category=Blogs_Category.objects.all()
    page=Paginator(Img_data,9)
    print(page)
    page_number=request.GET.get('page')
    print(page_number)
    page=page.get_page(page_number)
    print(page)
    
    

            
    data={
        "page":page,
        "category":category,
        
        
    }
    
    return render(request,"home.html",data)

def post(request,post_id):
    post=Blogs_Post.objects.get(post_id=post_id)
    category=Blogs_Category.objects.all()
  
    

    data={
        "data": post,
        "category":category,
    }
    return render(request,"posts.html",data)

def category(request,url):
    cat=Blogs_Category.objects.get(url=url)
    print(cat)
    category=Blogs_Category.objects.all()
    posts= Blogs_Post.objects.filter(category=cat)   
    data={
        "cat":cat,
        "posts":posts,
        "category":category,
    }    



    return render(request,"category.html",data)


def about(request):

    category=Blogs_Category.objects.all()

    data={
        "category":category
    }



    return render(request,"about.html",data)    