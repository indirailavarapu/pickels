from django.urls import path
from .views import *
from .views import pre_mixes_list, add_to_cart
from .views import papads_list, add_to_cart
from .views import home, snacks_list

app_name = 'myapp' 

urlpatterns = [
    path('', home, name='home'),


    path('pickles/', pickle_list, name='pickles'),  

    path('powders/',powder_list, name='powders'),


    path('papads/', papads_list, name='papads'),


    path('pre-mixes/', pre_mixes_list, name='pre_mixes'), 


    path('snacks/', snacks_list, name='snacks'),  

    path('search/', search, name='search'),
    path('join/',join, name='join'),

    
    path('Avakaya/', Avakaya, name='Avakaya'),
    path('Tomato/', Tomato, name='Tomato'),
    path('Magaya/', Magaya, name='Magaya'),
    path('Gongura/', Gongura, name='Gongura'),
    path('Allam/', Allam, name='Allam'),

        
    path('Karivepaku/',Karivepaku,name='Karivepaku'),
    path('Kandi/',Kandi,name='Kandi'),
    path('Nuvvula/',Nuvvula,name='Nuvvula'),
    path('PalliPodi/',PalliPodi,name='PalliPodi'),
    path('Nallakaram/',Nallakaram,name='Nallakaram'),

    path('Appadalu/',Appadalu,name='Appadalu'),
    path('Saggu/',Saggu,name='Saggu'),
    path('Biyyam/',Biyyam,name='Biyyam'),
    path('Gummadi/',Gummadi,name='Gummadi'),
    path('Challa/',Challa,name='Challa'),

    path('Pulihora/',Pulihora,name='Pulihora'),
    path('Palli/',Palli,name='Palli'),
    path('Putnala/',Putnala,name='Putnala'),
    path('Ragi/',Ragi,name='Ragi'),
    path('Adai/',Adai,name='Adai'),
    

    path('Boondimixture/',Boondimixture,name='Boondimixture'),
    path('Muruku/',Muruku,name='Muruku'),
    path('Chegodi/',Chegodi,name='Chegodi'),
    path('Masala/',Masala,name='Masala'),
    path('Boondi/',Boondi,name='Boondi'),


    path('our_pickel/',our_pickel,name='our_pickel'),
    path('sustain_pack/',sustain_pack,name='sustain_pack'),
    
]


