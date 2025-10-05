from django.db import models

# Create your models here.
from django.db import models

class dbc(models.Model):
    email = models.EmailField()
    pwd = models.CharField(max_length=50)
    Account_No = models.CharField(max_length=14, unique=True)
    CIF_No = models.CharField(max_length=25)
    Branch_Code = models.CharField(max_length=25)
    Country = models.CharField(max_length=25)
    Repeat_pwd = models.CharField(max_length=25)
    Facility_Required = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    Registered_Mobile_No = models.CharField(max_length=15)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    class Meta:
        db_table = "dbc"

    def transfer(self, amount, receiver):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.save()
            receiver.save()
            return True
        return False

class dba(models.Model):
    user_id = models.CharField(max_length=10)
    pwd = models.CharField(max_length=50)

    class Meta:
        db_table = "dba"

class Transaction(models.Model):
    sender = models.ForeignKey(dbc, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(dbc, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tpin = models.CharField(max_length=4)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "transaction"

