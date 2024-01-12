from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_all(request):
    QLAO=Authors.objects.all()
    QLBO=Books.objects.all()
    QLSO=Students.objects.all()
    d={'authors':QLAO,'books':QLBO,'students':QLSO}
    return render(request,'Display_all.html',d)

def author(request):
    QLAO=Authors.objects.all()
    QLAO=Authors.objects.order_by('author_name')
    QLAO=Authors.objects.order_by('-author_name')
    QLAO=Authors.objects.order_by(Length('author_name'))    
    QLAO=Authors.objects.order_by(Length('author_name').desc())    
    QLAO=Authors.objects.all()
    QLAO=Authors.objects.filter(author_id__in=(1,))
    QLAO=Authors.objects.all()
    QLAO=Authors.objects.filter(Q(author_name__startswith='r') & Q(author_age__gt=50)) 
    QLAO=Authors.objects.all()   
    QLAO=Authors.objects.filter(Q(author_name__startswith='r') | Q(author_name__startswith='j') & Q(author_age__lt=100))
    d={'authors':QLAO,}
    return render(request,'author.html',d)

def book(request):
    QLBO=Books.objects.all()
    QLBO=Books.objects.filter(book_price=100).order_by('book_name')
    QLBO=Books.objects.filter(book_price__gt=100)
    QLBO=Books.objects.filter(book_price__lt=500)
    QLBO=Books.objects.filter(book_price__gte=100)
    QLBO=Books.objects.filter(book_price__lte=500)
    QLBO=Books.objects.filter(book_name__startswith='a')
    QLBO=Books.objects.filter(book_name__endswith='a')
    QLBO=Books.objects.filter(book_name__contains='s')
    QLBO=Books.objects.all()

    d={'books':QLBO}
    return render(request,'book.html',d)

def student(request):
    QLSO=Students.objects.all()
    QLSO=Students.objects.filter(date__year=2023)
    QLSO=Students.objects.filter(date__month=11)
    QLSO=Students.objects.filter(date__day=19)
    QLSO=Students.objects.filter(date__day__lt=20)
    QLSO=Students.objects.filter(date__day__gt=19)
    QLSO=Students.objects.filter(date__day__lte=19)
    QLSO=Students.objects.filter(date__day__gte=19)
    QLSO=Students.objects.all()

    d={'students':QLSO}
    return render(request,'student.html',d)

def insert_author(request):
    i=int(input('Enter author_id:'))
    n=input('Enter author_name:')
    a=int(input('Enter author_age:'))
    e=int(input('Enter author_exp:'))
    ao=Authors.objects.get_or_create(author_id=i,author_name=n,author_age=a,author_exp=e)[0]
    ao.save()
    return HttpResponse('An author data is created')

def insert_book(request):
    i=int(input('Enter book_id:'))
    ai=input('Enter author_id:')
    n=input('Enter book_name:')
    p=int(input('Enter book_price:'))
    ao=Authors.objects.get(author_id=ai)
    ao.save()
    bo=Books.objects.get_or_create(book_id=i,author_id=ao,book_name=n,book_price=p)[0]
    bo.save()
    return HttpResponse('A book data is created')

def insert_student(request):
    n=input('Enter stu_name:')
    r=input('Enter stu_rank:') 
    c=input('Enter stu_class:')
    p=int(input('Enter pk value:'))
    bo=Books.objects.get(pk=p)
    bo.save()
    so=Students.objects.get_or_create(stu_name=n,stu_rank=r,stu_class=c,book_id=bo)[0]
    so.save()
    return HttpResponse('A student data is created')

def update_student(request):
    
    #Students.objects.filter(stu_name='Sarangya').update(stu_rank=2)
    Students.objects.update_or_create(stu_name='Yurekha',defaults={'stu_rank':3,'stu_class':'Intermediate'})


    QLSO=Students.objects.all()
    d={'students':QLSO}
    return render(request,'display_all.html',d)



