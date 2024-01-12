from django.db import models

# Create your models here.
class Authors(models.Model):
    author_id=models.IntegerField(primary_key=True)
    author_name=models.CharField(max_length=100,unique=True)
    author_age=models.IntegerField(default='Unknown')
    author_exp=models.IntegerField()
    def __str__(self):
        return str(self.author_id)
    
class Books(models.Model):
    book_id=models.IntegerField(primary_key=True)
    author_id=models.ForeignKey(Authors,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100,null=False)
    book_price=models.IntegerField(default=100)

    def __str__(self):
         return str(self.book_id)

class Students(models.Model):
    stu_name=models.CharField(max_length=100,unique=True)
    stu_rank=models.IntegerField()
    stu_class=models.CharField(max_length=100)
    book_id=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now=False,auto_now_add=False,default='2023-12-19')


    def __str__(self):
        return self.stu_name