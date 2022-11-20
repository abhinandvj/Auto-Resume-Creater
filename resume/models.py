from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Resume(models.Model):
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
    designation = models.CharField(
        'Designation',blank=False,null=False,db_index=True,max_length=30, default='Employee Designation'
    )
    date = models.DateField(
        'Start Date',null=True,blank=True,db_index=True
    )
    dateend = models.CharField(
        'End Date',null=False,blank=True,db_index=True,max_length=25,default='Present'
    )
    ocity = models.CharField(
        "Office City",blank=False,null=False,db_index=True,max_length=20,default='Remote'
    )
    ostate = models.CharField(
        "Office State",blank=True,null=True,db_index=True,max_length=20
    )
   
    
    
    desca = models.CharField(
        'Job Description 1st point',blank=False,null=False,db_index=True,max_length=60,default='Discription point one goes here...'
    )
    descb = models.CharField(
        'Job Description 2nd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point two goes here...'
    )
    descc = models.CharField(
        'Job Description 3rd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point three goes here...'
    )
    descd = models.CharField(
        'Job Description 4th point',blank=True,null=True,db_index=True,max_length=60,default='Discription point four goes here...'
    )





    company2 = models.CharField(
        'Company',blank=False,null=False,db_index=True,max_length=15,default='Company name'
    )
    designation2 = models.CharField(
        'Designation',blank=False,null=False,db_index=True,max_length=30, default='Employee Designation'
    )
    date2 = models.DateField(
        'Start Date',null=True,blank=True,db_index=True
    )
    dateend2 = models.CharField(
        'End Date',null=False,blank=True,db_index=True,max_length=25,default='Present'
    )
    ocity2 = models.CharField(
        "Office City",blank=False,null=False,db_index=True,max_length=20,default='Remote'
    )
    ostate2 = models.CharField(
        "Office State",blank=True,null=True,db_index=True,max_length=20
    )
   
    
    
    desca2 = models.CharField(
        'Job Description 1st point',blank=False,null=False,db_index=True,max_length=60,default='Discription point one goes here...'
    )
    descb2 = models.CharField(
        'Job Description 2nd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point two goes here...'
    )
    descc2 = models.CharField(
        'Job Description 3rd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point three goes here...'
    )
    descd2 = models.CharField(
        'Job Description 4th point',blank=True,null=True,db_index=True,max_length=60,default='Discription point four goes here...'
    )




    
    company3 = models.CharField(
        'Company',blank=False,null=False,db_index=True,max_length=15,default='Company name'
    )
    designation3 = models.CharField(
        'Designation',blank=False,null=False,db_index=True,max_length=30, default='Employee Designation'
    )
    date3 = models.DateField(
        'Start Date',null=True,blank=True,db_index=True
    )
    dateend3 = models.CharField(
        'End Date',null=False,blank=True,db_index=True,max_length=25,default='Present'
    )
    ocity3 = models.CharField(
        "Office City",blank=False,null=False,db_index=True,max_length=20,default='Remote'
    )
    ostate3 = models.CharField(
        "Office State",blank=True,null=True,db_index=True,max_length=20
    )
   
    
    
    desca3 = models.CharField(
        'Job Description 1st point',blank=False,null=False,db_index=True,max_length=60,default='Discription point one goes here...'
    )
    descb3 = models.CharField(
        'Job Description 2nd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point two goes here...'
    )
    descc3 = models.CharField(
        'Job Description 3rd point',blank=False,null=False,db_index=True,max_length=60,default='Discription point three goes here...'
    )
    descd3 = models.CharField(
        'Job Description 4th point',blank=True,null=True,db_index=True,max_length=60,default='Discription point four goes here...'
    )




    

    def __str__(self):
        return self.name1