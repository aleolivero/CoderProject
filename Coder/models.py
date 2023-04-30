from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.

class Players(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='players')
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    date_birth = models.DateField(blank=True,null=True, verbose_name="Birth",)
    phone = models.CharField(max_length=100, verbose_name="Phone")
    adress = models.CharField(max_length=100, verbose_name="Adress")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    country = models.CharField(max_length=100, verbose_name="Country")

    def __str__(self,):
        if not self.first_name and not self.last_name:
            
            _str = str(self.user.username)

        else:
            
            _str = str(self.first_name) + ' ' + str(self.last_name)

        return _str
    
class Questions(models.Model):
    
    STATUS_CHOICES = (
    ('open', 'Open'),
    ('pending', 'Pending'),
    ('closed', 'Closed'),
    )


    title = models.CharField(max_length=1000, verbose_name="Title")
    category = models.CharField(max_length=1000, verbose_name="Category")
    question = models.CharField(max_length=1000, verbose_name="Question")
    date = models.DateField(verbose_name="Date")
    correct_answer = models.CharField(max_length=1000, verbose_name="Correct Answer")
    author = models.ForeignKey(Players,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Player")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    points = models.FloatField(verbose_name="Points", default=3)    

    def statusFormat(self):
        if str(self.status) == 'open':

            return format_html('<span style="color:green"> <b>{} </b></span>', str(self.status).upper())

        elif str(self.status) == 'pending':
            return format_html('<span style="color:orange"> <b>{} </b></span>', str(self.status).upper())

        elif str(self.status) == 'closed':
            return format_html('<span style="color:red"> <b>{} </b></span>', str(self.status).upper())
        
    def __str__(self,):
        return str(self.question)


class Answers(models.Model):

    answer = models.CharField(max_length=1000, verbose_name="Answer")
    player = models.ForeignKey(Players,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Player")
    question = models.ForeignKey(Questions,blank=False,null=True,on_delete=models.CASCADE, verbose_name="Question")

    def __str__(self,):
        return str(self.answer)
    
class PlayerScore(models.Model):
    winner_answer = models.ForeignKey(Answers,blank=False,null=True,on_delete=models.CASCADE, verbose_name="winner_answer")
