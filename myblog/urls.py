from django.conf.urls import url,include,patterns
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
					   url(r'^$','myblog.views.index',name='home'),
					   url(r'^blog/','myblog.views.blog',name='blog'),
                       url(r'^post/(?P<id_post>\d+)/$','myblog.views.post',name='post'),
                       url(r'^calc/','myblog.views.calc',name='calc'),
                       url(r'^divisas/','myblog.views.divisas',name='divisas'),
                       url(r'^cron/','myblog.views.cron',name='cron'),
                       url(r'^form/','myblog.views.formulario',name='formulario'),
                       url(r'^gallery/','myblog.views.gallery',name='gallery'),
)
