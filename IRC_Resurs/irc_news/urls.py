from django.urls import path
from .views import *

urlpatterns =  [
    path('', index, name='irc_page'),
    path('one_page/<slug:post_slug>/', one_page, name='one_page'),
    path('categorie/<int:parametr>/', categorie, name='categorie_page'),
    path('users/', users_login_all, name='users_page'),
    path('add_news/', AddNews.as_view(), name='add_news_page'),
    path('add_news_albom/<int:id>/', AddNewsAlbom.as_view() , name='add_news_page_albom'),
    path('dowload/<int:post_id>/', dowload, name='dowload_page'),
    path('update/<int:id>/', UpdateNews.as_view(), name='update_news_page'),
    path('update_albom/<int:id>/', update_albom),
    path('delete/<int:id>/', delete_news, name='delete_news_page'),
    path('delete_albom_one/<int:id>/', delete_albom_one, name='delete_albom_one'),
    path('delete_coment/<int:id>/', delete_coment, name='delete_coment'),
    path('add_pro_irc/<int:id>/', UpdateProIRC.as_view(), name='add_pro_irc_page'),
    path('my_page/', LoginUser.as_view(), name='my_page'),
    path('logout/', logout_user, name='logout'),
    path('registration/', register, name='registration'),
    path('registration_full/<int:id>/', RegisterFull.as_view(), name='next_registration'),
    path('user/<int:id>/', users, name='user_page'),
    path('user_update/<int:id>/', UpdateUser.as_view(), name='user_page_update'),
    path('user_delete/<int:id>/', user_delete, name='user_delete'),
    path('add_pro_irc_info/', AddProIRC.as_view(), name='irc_info'),

]


