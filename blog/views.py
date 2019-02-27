from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator #paginator 쓸것
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    #모든 블로그 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세개를 한 페이지로 자르기 Paginator(객체, N개씩)
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page') #request된 (get방식으로 온 url에서) page라는 key값을 가진 딕셔너리를 page에 담겠다
    #request된 페이지를 얻어온 뒤 return 해준다 ( paginator 의 메소드 함수에서 get_page(페이지번호)를 사용)
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()
    return redirect('/detail/' + str(blog.id))

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> 메소드로 기능 구분 POST방식
    #2. 빈페이지를 띄워주는 기능 -> GET방식으로
    if request.method == 'POST':
        #입력된 내용을 처리하는 기능
        form = BlogPost(request.POST)
        if form.is_valid(): #잘 입력이 됐는지 확인하는 함수 == True
            #블로그 객체를 갖고오되 아직은 저장하지 않음
            post = form.save(commit=False)
            post.pub_date = timezone.now() #form에서 받지 않은 변수 넣어줌
            post.save() #post저장
            return redirect('home')
    else:
        #빈페이지를 띄워주는 기능
        form = BlogPost() #비어있는 form 객체
        return render(request, 'new.html', {'form':form})