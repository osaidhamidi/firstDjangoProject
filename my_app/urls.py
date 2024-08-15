from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('budige/', views.budgie_page, name='budgie_page'),
    path('canari/', views.canari_page, name='canari_page'),
    path('cardinalred/', views.cardinalred_page, name='cardinalred_page'),
    path('cocatoo/', views.cocatoo_page, name='cocatoo_page'),
    path('coctail/', views.coctail_page, name='coctail_page'),
    path('goldenparakeet/', views.goldenparakeet_page, name='goldenparakeet_page'),
    path('grayparrot/', views.grayparrot_page, name='grayparrot_page'),
    path('home/', views.home_page, name='home_page'),
    path('lov/', views.lov_page, name='lov_page'),
    path('macaw/', views.macaw_page, name='macaw_page'),
    path('ganna/', views.ganna_page, name='ganna_page'),
    path('siskin/', views.siskin_page, name='siskin_page'),
    path('turkman/', views.turkman_page, name='turkman_page'),
    path('yellowth/', views.yellowth_page, name='yellowth_page'),
    path('zebra/', views.zebra_page, name='zebra_page'),

]
