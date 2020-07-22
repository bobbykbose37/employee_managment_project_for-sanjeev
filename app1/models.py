from django.db import models

# Create your models here.



class user(models.Model):
    name=models.CharField(max_length=100)
    complaint_id=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return (self.name)

class complaint(models.Model):
    name=models.CharField(max_length=100,blank=True)
    complaint_id = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    issue=models.CharField(max_length=100,null=True)
    issue_type=models.CharField(max_length=100,null=True)
    reported_by=models.CharField(max_length=100,null=True)
    handled_by=models.CharField(max_length=100,null=True)
    company_name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    department=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    remarks=models.CharField(max_length=100,null=True)

    def __str__(self):
        return (self.complaint_id)



