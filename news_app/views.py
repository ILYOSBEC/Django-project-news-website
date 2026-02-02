from django.db.models.fields import return_None
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .forms import ContactForm
from .models import News, Category


# Create your views here.

# def news_list(request):
#     news_list = News.published_manager.all()
#     context = {
#         'news_list': news_list
#     }
#     return render(request, 'News/News_list.html', context)
#
#
#
# def news_detail(request,id):
#     news = get_object_or_404(News, id=id , status=News.Status.Published)
#     context = {
#         'news':news
#     }
#     return render(request, 'News/News_detail.html', context)


class news_list(ListView):
    model = News
    queryset = News.published_manager.all()
    template_name = 'News/News_list.html'
    context_object_name = 'news_list'


class news_detail(DetailView):
    model = News
    template_name = 'News/News_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



# class index_view(ListView):
#     model = News
#     queryset = News.published_manager.all()
#     categories = Category.objects.all()
#     template_name = 'News/News_list.html'


def HomePageView(request):
    news_list = News.published_manager.all().order_by('-published_time')[:10]
    local_news_list = News.published_manager.all().filter(category__name='Mahalliy').order_by('-published_time')[:3]
    sport_news_list = News.published_manager.all().filter(category__name='Sport').order_by('-published_time')[:3]
    abroad_news_list = News.published_manager.all().filter(category__name='Xorij').order_by('-published_time')[:3]
    technology_news_list = News.published_manager.all().filter(category__name='Texnalogiya').order_by('-published_time')[:3]

    categories = Category.objects.all()
    context = {'news_list': news_list,
               'local_news_list': local_news_list,
               'sport_news_list': sport_news_list,
               'abroad_news_list': abroad_news_list,
               'technology_news_list': technology_news_list,
               'categories': categories}


    return render(request, 'News/index.html', context)


# def ContactPageViews(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h1>Success!</h1>")
#
#     context = {'form': form}
#
#     return render(request, 'News/contact.html', context)


class ContactPageViews(TemplateView):
    template_name = 'News/contact.html'


    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}


        return render(request, 'News/contact.html', context)



    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>biz bilan bo'glanganingiz uchun rahmat !</\h2>")

        context = {'form': form}
        return render(request, 'News/contact.html', context)





#  categoriyalarning sahifalari


class LoacalNewsView(ListView):
    model = News
    template_name = 'News/Mahalliy.html'
    context_object_name = 'Mahalliy_yangiliklar'


    def get_queryset(self):
       news = self.model.published_manager.all().filter(category__name='Mahalliy')
       return news


class SportNewsView(ListView):
    model = News
    template_name = 'News/sport.html'
    context_object_name = 'Sport_yangiliklar'


    def get_queryset(self):
       news = self.model.published_manager.all().filter(category__name='Sport').order_by('-published_time')
       return news



class AboardNewsView(ListView):
    model = News
    template_name = 'News/xorij.html'
    context_object_name = 'Xorij_yangiliklar'


    def get_queryset(self):
       news = self.model.published_manager.all().filter(category__name='Xorij').order_by('-published_time')
       return news




class TechnologyNewsView(ListView):
    model = News
    template_name = 'News/texnalogiya.html'
    context_object_name = 'Texnalogiya_yangiliklar'


    def get_queryset(self):
       news = self.model.published_manager.all().filter(category__name='Texnalogiya').order_by('-published_time')
       return news

