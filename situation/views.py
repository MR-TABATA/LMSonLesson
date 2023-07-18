from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from course.models import ElmsCourse
from chapter.models import ElmsChapter
from lesson.models import ElmsLesson, ElmsLessonUserShip
from core.utilities import getNotifications

class IndexView(LoginRequiredMixin, TemplateView):
	template_name = 'situation/index.html'


class LessonIndex(LoginRequiredMixin, ListView):
  def get(self, request, *args, **kwargs):
    context = {}
    context['courses'] = ElmsCourse.objects.filter(deleted__isnull=True)
    context['chapters'] = ElmsChapter.objects.filter(deleted__isnull=True)
    context['lessons'] = ElmsLesson.objects.filter(deleted__isnull=True)
    context['lesson_users'] = ElmsLessonUserShip.objects.filter(deleted__isnull=True, custom_user=self.request.user.pk)
    context['notifications'] = getNotifications()
    return render(request, 'situation/lesson_index.html', context)

