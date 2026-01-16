from django.db import models

# Customer Table
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


# Lead Table
class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Converted', 'Converted'),
        ('Lost', 'Lost'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    follow_up_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.customer.name
