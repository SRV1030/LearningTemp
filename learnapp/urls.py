from django.conf.urls import url
from learnapp import views
app_name= "learnapp"
urlpatterns=[
 url(r'^details/$',views.details, name = 'details'),
]
