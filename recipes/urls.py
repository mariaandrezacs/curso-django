from django.urls import path
from recipes.views import home


# HTTP REQUEST <- HTTP RESPONSE

urlpatterns = [
    path('', home), #home 
    #path('sobre/', sobre), # /sobre/
    #path('contato/', contato), # /contato/'''

]