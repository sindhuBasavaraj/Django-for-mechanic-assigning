from django.db import models

class Issue(models.Model):
    issueID = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    problem = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('INQUEUE', 'In Queue'),
        ('ASSIGNED', 'Assigned'),
        ('DISPATCHED', 'Dispatched'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='INQUEUE')

    def __str__(self):
        return f"Issue {self.issueID}"
class Agents(models.Model):
    agentID = models.AutoField(primary_key=True)
    queue = models.IntegerField(default=0)

    def __str__(self):
        return f"Agent {self.agentID}"
class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Mechanic {self.mechanicID}"
