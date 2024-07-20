from django.db import models





class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    mob = models.CharField(max_length=15)
    msg = models.TextField()

    def __str__(self):
        return f"{self.fname} {self.lname} {self.msg}"



