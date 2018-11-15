from django.urls import path
from edtechworx import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('home/', views.Home.as_view() , name='home'),
    path('courses_list/', views.Courses.as_view() , name='courses_list'),
    path('course_detail/', views.CoursesDetail.as_view() , name='course_detail'),
    path('blog/', views.Blog.as_view() , name='blog'),
    path('blog_detail/', views.BlogDetail.as_view() , name='blog_detail'),
    path('gallery/', views.Gallery.as_view() , name='gallery'),
    path('contact/', views.Contact.as_view() , name='contact'),
    path('about/', views.About.as_view() , name='about'),
    path('login/', views.Login.as_view() , name='login'),
    path('register/', views.Register.as_view() , name='register'),
    path('error/', views.Error.as_view() , name='error'),
]