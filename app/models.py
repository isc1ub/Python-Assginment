from django.db import models
class Employee(models.Model):
    TAG = (
        ('MR', 'Loyiha Menejeri'),
        ('HR', 'HR Menejer'),
        ('BC', 'Backend dasturchi'),
        ('FR', 'Frontend dasturchi'),
        ('DR', 'DevOps Injiner'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=TAG)
    photo = models.ImageField(upload_to='photos/')
    about = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'