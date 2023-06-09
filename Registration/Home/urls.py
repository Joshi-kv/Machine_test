from django.urls import path
from . import views
app_name='Registration'
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('student/',views.student,name='student'),
    path('admin_view/',views.admin_view,name='admin_view'),
    path('staff/',views.staff,name='staff'),
    path('editor/',views.editor,name='editor'),
]
