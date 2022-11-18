from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Portfolio(models.Model):
    class Meta(object):
        db_table = 'post'

    name1 = models.CharField(
        'First Name',blank=False,null='False',max_length=15,db_index=True,default='First Name: '
    )
    name2 = models.CharField(
        'Last Name',blank=False,null='False',max_length=15,db_index=True,default='Last Name: '
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True
    )
    code = models.IntegerField(
        'CountryCode: ',blank=False,null=False,db_index=True,default=91
    )
    phone = models.IntegerField(
        'Phone No: ',blank=False,null=False,db_index=True,default=0000000000
    )
    email = models.CharField(
        'Email:',blank=False,null=False,max_length=50,db_index=True,default='sample@gmail.com'

    )
    address1 = models.CharField(
        'Address Line 1', null=False,blank=False,db_index=True,max_length=30,default='House and street'

    )
    address2 = models.CharField(
        'city,state', null=False,blank=False,db_index=True,max_length=30,default='City and state'

    )
    address3 = models.IntegerField(
        'pin-code1', null=False,blank=False,db_index=True,default=00000

    )
    address4 = models.CharField(
        'Country', null=False,blank=False,db_index=True,max_length=20,default='Country'

    )




    company = models.CharField(
        'Company',blank=False,null=False,db_index=True,max_length=15,default='Company name'
    )
    work1 = models.CharField(
        'Designation',blank=False,null=False,db_index=True,max_length=30, default='Employee Designation'
    )
    desc = models.CharField(
        'Job Description',blank=False,null=False,db_index=True,max_length=60,default='Discription goes here...'
    )
    
    experience = models.IntegerField(
        'Work Experience',blank=False,null=False,db_index=True,default=0
    )

    def __str__(self):
        return self.name1