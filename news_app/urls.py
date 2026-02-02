from django.urls import path
from .views import HomePageView, news_detail, ContactPageViews, \
LoacalNewsView , SportNewsView , AboardNewsView , TechnologyNewsView

urlpatterns = [
    path('', HomePageView , name='Home_page' ),
    path('contact-us/', ContactPageViews.as_view() , name='contact_page'),


    path('Local-news/' , LoacalNewsView.as_view() , name='local_news_page' ),
    path('Sport-news/' , SportNewsView.as_view() , name='sport_news_page' ),
    path('Aboard-news/' , AboardNewsView.as_view() , name='aboard_news_page' ),
    path('Technology-news/' , TechnologyNewsView.as_view() , name='technology_news_page' ),

    path('<slug:slug>/', news_detail.as_view(), name='news_detail_page'),
]