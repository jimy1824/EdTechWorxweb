from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

class Home(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Courses(View):
    template_name = 'courses_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class CoursesDetail(View):
    template_name = 'course_details.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Blog(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BlogDetail(View):
    template_name = 'blog_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Gallery(View):
    template_name = 'gallery.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Contact(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
class About(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Login(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Register(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Error(View):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)