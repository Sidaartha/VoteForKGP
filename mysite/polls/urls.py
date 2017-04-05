from django.conf.urls import url
from .import views

urlpatterns = [

	url(r'^$', views.index, name="index"),
	url(r'^feedback$',views.feedback, name="feedback"),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail, name="detail"),
	url(r'^(?P<question_id>[0-9]+)/results$',views.results, name="results"),
	url(r'^results$',views.results, name="result"),
	url(r'^(?P<question_id>[0-9]+)/vote$',views.vote, name="vote"),
]