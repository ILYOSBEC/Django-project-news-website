from .models import News


def latest_news(request):
    latest_news = News.published_manager.all().order_by('-published_time')[:1]

    context = {
        'latest_news':latest_news
    }

    return context