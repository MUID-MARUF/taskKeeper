from django.contrib.auth.models import User
from django.db import models
import uuid

#status_options = ['todo', 'in progress', 'completed', 'cancelled']
#priority = ['urgent', 'high', 'medium', 'low']

STATUS_CHOICES = (
    ('todo', 'Todo'),
    ('in progress', 'In Progress'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)

PRIORITY_CHOICES= (
    ('urgent', 'Urgent'),
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'tasks', null= True)
    task_id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False, serialize= False, verbose_name= 'ID')
    title = models.CharField(max_length= 50)
    description = models.CharField(max_length=255, blank= True)
    created = models.DateTimeField(auto_now_add= True)
    last_updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES, default = 'todo')
    priority = models.CharField(max_length= 20, choices = PRIORITY_CHOICES, default= 'medium')
    target_date = models.DateTimeField(null= True, blank= True)
    extra_notes = models.CharField(max_length= 512, blank= True)

