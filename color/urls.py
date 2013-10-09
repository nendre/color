from django.conf.urls import url, patterns

urlpatterns = patterns("color.views",
    url(r'^$', "start", name="start"),
    url(r'^moo/?$', "moo", name="moo"),
    url(r'^home/?$', "home", name="home"),
    url(r'^result/?$', "result", name="result"),
)
