from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import FileResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from  django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.utils.text import slugify

news = News.objects.all()




def index(request):
    irc= ProIrc.objects.first()
    if irc==None:
        return redirect('irc_info')
    else:
        return render(request, 'irc_news/about_irc.html', {'title':'Про ІРЦ', 'irc':irc} )


class UpdateProIRC(UpdateView):
    model = ProIrc
    form_class = ProIrcForm
    template_name = 'irc_news/add_pro_irc.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'].required = False
        form.fields['link'].required = False
        form.fields['contact'].required = False
        form.fields['title'].required = False
        form.fields['content'].required = False
        form.fields['photo'].required = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редагувати Інформацію'
        context['button'] = 'Зберегти'
        return context


class AddProIRC(CreateView):
    model = ProIrc
    form_class = ProIrcForm
    template_name = 'irc_news/add_pro_irc.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['email'].required = False
        form.fields['link'].required = False
        form.fields['contact'].required = False
        form.fields['title'].required = False
        form.fields['content'].required = False
        form.fields['photo'].required = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додати Інформацію'
        context['button'] = 'Додати Інформацію'
        return context

def one_page(request, post_slug):
    post = News.objects.get(slug=post_slug)
    photos = Pictures.objects.filter(news_id=post.pk)
    comentari_db=Comentari.objects.filter(news_id=post.pk)
    user = Users.objects.get(id=post.author_id)

    if not photos:
        photos='null'
    form_coment = ComentForm()
    if request.method == "POST":
        id_f = post.pk
        name_f = request.POST['name']
        content_f = request.POST['content']
        coment = Comentari()
        coment.name=name_f
        coment.content=content_f
        coment.news_id=id_f
        coment.save()
    return render(request, 'irc_news/about.html', {'title':post.title,
                                                   'post':post, 'albom':photos, 'form_coment':form_coment, 'comentari_db':comentari_db, 'user_u':user, }, )

def delete_coment(request, id):
    news_id = Comentari.objects.get(pk=id)
    page_slug= News.objects.get(pk=news_id.news_id).slug
    Comentari.objects.get(pk=id).delete()
    return redirect('/one_page/%s/' %page_slug)


def categorie(request, parametr):
    if parametr==1:
        news = News.objects.filter(categorie_id=1)
        title='Всі новини'

    elif parametr==2:
        news = News.objects.filter(categorie_id=2)
        title='Школа'

    elif parametr==3:
        news = News.objects.filter(categorie_id=3)
        title='Дитячий садок'
    elif parametr==4:
        news = News.objects.filter(categorie_id=4)
        title='Батькам'
    return render(request, 'irc_news/index.html', {'news':news, 'title':title})

def users_login_all(request):
    all_users = Users.objects.all()
    return render(request, 'irc_news/users.html', {'title':'Користувач', 'all_users':all_users} )

def users(request, id):
    try:
        user_one = Users.objects.get(user_id=id)
        stati = News.objects.filter(author_id=user_one.id)
        return render(request, 'irc_news/user_page.html', {'title':user_one.first_name+' '+user_one.last_name, 'user_one':user_one, 'stati':stati} )
    except:
        return HttpResponse('Такогої сторінки не істує')


class UpdateUser(UpdateView):
    model = Users
    form_class = RegistrationFormFull
    template_name = 'irc_news/registration_full.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id_pk = self.kwargs.get('id')
        id = Users.objects.get(id=id_pk).user_id
        return reverse('user_page', kwargs={'id': id})



    # def get_success_url(self):
    #     return '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].required = False
        form.fields['last_name'].required = False
        form.fields['pobatkovi'].required = False
        form.fields['birth_day'].required = False
        form.fields['posada'].required = False
        form.fields['photo'].required = False
        form.fields['info'].required = False
        form.fields['user'].required = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редагувати користувача'
        context['button'] = 'Редагувати'
        return context


class AddNews(CreateView):
    model = News
    form_class = addPostForm
    success_url = reverse_lazy('add_news_page_albom')
    template_name = 'irc_news/add_news.html'



    def get_success_url(self):
        return reverse('add_news_page_albom', args=(self.object.id,))

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['file'].required = False
        form.fields['link'].required = False
        return form

    def get_initial(self):
        initial = super().get_initial()
        id_user = self.request.user
        id_user=User.objects.get(username=id_user).pk
        full_user=Users.objects.get(user_id=id_user).pk
        initial['author'] = full_user
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додати новину'
        context['button'] = 'Додати новину'
        context['url'] = 'add_news_page'
        return context

class AddNewsAlbom(CreateView):
    model = Pictures
    form_class = PicturesForm
    template_name = 'irc_news/add_albom.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        id = self.kwargs.get('id')
        slug=News.objects.get(pk=id).slug
        return reverse('one_page', kwargs={'post_slug': slug})


    def form_valid(self, form):
        news = News.objects.get(id=self.kwargs['id'])
        for file in self.request.FILES.getlist('pictures'):
            picture = Pictures(news=news, pictures=file)
            picture.save()
        return redirect(self.get_success_url())



    def get_initial(self):
        initial = super().get_initial()
        initial['news'] =  self.kwargs.get('id')
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Додати фотографії'
        context['button'] = 'Додати фотографії'
        return context


class UpdateNews(UpdateView):
    model = News
    form_class = addPostForm
    template_name = 'irc_news/add_news.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return '/update_albom/' + str(self.object.id) + '/'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['file'].required = False
        form.fields['link'].required = False
        form.fields['slug'].required = False
        form.fields['title'].required = False
        form.fields['content'].required = False
        form.fields['photo'].required = False
        form.fields['categorie'].required = False
        form.fields['is_published'].required = False
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редагувати новину'
        context['button'] = 'Редагувати новину'
        context['url'] = 'update_news_page'
        return context


def update_albom(request, id):
    albom = Pictures.objects.filter(news_id=id)
    return render(request, 'irc_news/photos_update.html', {'title':'Редагувати новину', 'albom':albom, 'id':id})



def delete_albom_one(request, id):
    a = Pictures.objects.get(pk=id)
    id_albom = a.news_id
    a.delete()
    return redirect('/update_albom/%d/' % id_albom)


def delete_news(request, id):
    delete = News.objects.filter(pk=id)
    delete.delete()
    return redirect('irc_page')



def dowload(request, post_id):
    obj = News.objects.get(id=post_id)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


class LoginUser (LoginView):
    form_class = LoginUserForm
    template_name = 'irc_news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Увійти'
        context['button'] = 'Увійти'
        return context


    def get_success_url(self):
        user_id = self.request.user.id
        if user_id==1:
            return reverse_lazy('irc_page')
        else:
            id = Users.objects.get(user_id=user_id).user_id
            return reverse_lazy('user_page', kwargs={'id': id})


def logout_user(request):
    logout(request)
    return redirect('irc_page')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],

            )
            return redirect('next_registration', id=user.id)
    else:
        form = RegistrationForm()
    return render(request, 'irc_news/registration.html', {'form': form})

class RegisterFull(CreateView):
    model = Users
    form_class = RegistrationFormFull
    template_name = 'irc_news/registration_full.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('irc_page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['posada'].required = False
        form.fields['info'].required = False
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.kwargs['id']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Повна реєстрація'
        context['button'] = 'Зберегти'
        return context

def user_delete(request, id):
    user_d1= Users.objects.get(user_id=id)
    user_d1.delete()
    user_d2 = User.objects.get(pk=id)
    user_d2.delete()
    return redirect('irc_page')


