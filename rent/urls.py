from django.urls import path
from django.views.generic.base import RedirectView
from rent import views


urlpatterns = [

    path('home/', views.index),
    path('getdumy/',views.dummy),

    path('about/', views.About),

    path('Single_view_mess/<int:pk>', views.Single_view_mess),

    path('propertyDetail/', views.PropertyDetail),

    path('allproperty/', views.AllProperty),

    path('allmess/', views.Allmess),

    path('load-dists/',views.Districts, name='ajax_load_dists'),

    path('load-city/',views.city, name='ajax_load_city'),

    path('load-location/',views.locations, name='ajax_load_locations'),

    path('mypost/', views.mypost),

    path('validationpage/', views.ValidationPage),

    path('Validate/<int:pk>', views.Validate),

    path('DeletePost/<int:pk>', views.DeletePost),

    path('deletePostvalidation/<int:pk>', views.deletePostValidation),

    path('apii/<int:id>/', views.JsonCBV.as_view()),

    path('Detail/<int:pk>', views.HouseDetail),

    path('RegisterMess/', views.RegisterMess),

    path('UploadHouseDetail/', views.UploadHouseDetail),



    path('', RedirectView.as_view(url='home/'))

]




