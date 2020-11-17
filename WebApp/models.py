from django.db import models

# Create your models here.

class Users(models.Model):
    EmpId=models.IntegerField()
    EmpName=models.CharField(max_length=100)
    EmpAge=models.IntegerField()
    EmpRank=models.IntegerField()

    def upload_photo(self,filename):
        path='WebApp/photo/{}'.format(filename)
        return path
    Photo=models.ImageField(blank=True,null=True,upload_to=upload_photo)

    def upload_file(self,filename):
        path = 'WebApp/file/{}'.format(filename)
        return path

    resume= models.FileField(blank=True, null=True, upload_to=upload_photo)





