from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('resumeAuthor',views.resumeAuthor,name='resumeAuthor'),
    path('register',views.register,name='register'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    path('acadmic/<int:tokenRec>',views.acadmic,name='acadmic'),
    path('addAcadmic/<int:tokenRec>',views.addAcadmic,name='addAcadmic'),

    path('workExp/<int:tokenRec>',views.workExp,name='workExp'),
    path('addWorkExp/<int:tokenRec>',views.addWorkExp,name='addWorkExp'),

    path('additionalDetails/<int:tokenRec>',views.additionalDetails,name='additionalDetails'),
    path('addAdditionalDetails/<int:tokenRec>',views.addAdditionalDetails,name='addAdditionalDetails'),
    
    path('skills/<int:tokenRec>',views.skills,name='skills'),
    path('addSkills/<int:tokenRec>',views.addSkills,name='addSkills'),

    path('awards/<int:tokenRec>',views.awards,name='awards'),
    path('addAward/<int:tokenRec>',views.addAward,name='addAward'),

    path('showTemplates/<int:tokenRec>',views.showTemplates,name='showTemplates'),

    path('selectTemplate/<int:resumeId>/<int:tokenRec>',views.selectTemplate,name='selectTemplate'),

    

    path('error',views.error,name='error'),

   

]
