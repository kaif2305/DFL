from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginasdonar, name = 'donate-login'),
    path('donar_register/', views.registerasdonar, name = 'donate-register'),
    path('donar_logout/', views.logoutdonar, name = 'donate-logout'),
    path('donar_home', views.home, name='donate-home'),
    path('donate/', views.donate, name='donate-donate'),
    path('deliver/', views.deliver, name='donate-deliver'),
    path('team/', views.team, name='donate-team'),
    path('contact/', views.contact, name='donate-contact'),
    
    #organisation
    path('org/', views.org_home, name='org-home'),
    path('resources/', views.resources, name='org-resources'),
    path('request/', views.Request, name='org-request'),
    path('teamorg/', views.team_org, name='org-team'),
    path('contact/', views.contact_org, name='org-contact'),
    path('org_register/', views.registerasorg, name = 'org-register'),
    path('org_login/', views.loginasorg, name = 'org-login'),
    path('org_logout/', views.logoutorg, name = 'org-logout'),
    
]

