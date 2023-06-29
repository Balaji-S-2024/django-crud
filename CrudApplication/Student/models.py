from django.db import models

# Create your models here.

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True, blank=False, null=False)
    stu_name = models.CharField(max_length=25, blank=False, null=False)
    stu_email = models.EmailField()
    stu_age = models.IntegerField()
    stu_gender = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.stu_name
