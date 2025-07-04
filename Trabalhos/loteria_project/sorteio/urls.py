from django.urls import path
from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
        path('styles/', TemplateView.as_view(template_name='Styles/styles.css'), name='styles'),

]
