from django.urls import path
from myapp.views import new_issue

urlpatterns = [
    path('', new_issue, name='home'),
    path('new-issue/', new_issue, name='new_issue'),
]
