from django.urls import path
from .views import IndexView, LessonIndex

app_name = 'situation'

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('lesson/', LessonIndex.as_view(), name='lesson_index'),

]