from django.urls import path, re_path
from django.conf.urls import url
from .views import IndexView, DetailView  # , MySearchView
from voler.feeds import AllArticleRssFeed
import voler.views

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='index'),
    path('date/<int:year>/<int:month>', IndexView.as_view(template_name='index.html'), name='date'),
    path('tag/<str:tag>', IndexView.as_view(template_name='index.html'), name='tag'),
    path('author/<str:authorname>', voler.views.AuthorView, name='author'),
    # re_path(r'^link/$', LinkView, name='link'),     # 申请友情链接
    # re_path(r'^category/message/$', MessageView, name='message'),
    # re_path(r'^category/about/$', AboutView, name='about'),
    # re_path(r'^category/donate/$', DonateView, name='donate'),
    # re_path(r'^category/exchange/$', ExchangeView, name='exchange'),
    # re_path(r'^category/project/$', ProjectView, name='project'),
    # re_path(r'^category/question/$', QuestionView, name='question'),
    # 分类页面
    url(r'^category/(?P<bigslug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='content.html'), name='category'),
    # 归档页面
    re_path(r'^date/(?P<year>\d+)/(?P<month>\d+)/$', IndexView.as_view(template_name='archive.html'), name='date'),
    # 标签页面
    re_path(r'^tag/(?P<tag>.*?)/$', IndexView.as_view(template_name='content.html'), name='tag'),
    # 文章详情页面
    re_path(r'^article/(?P<slug>.*?)/$', DetailView.as_view(), name='article'),
    # # 全文搜索
    # re_path(r'^search/$', MySearchView.as_view(), name='search'),
    # 喜欢
    url(r'^love/$', voler.views.LoveView, name='love'),
    url(r'^feed/$', AllArticleRssFeed(), name='rss'),  # rss订阅
]
