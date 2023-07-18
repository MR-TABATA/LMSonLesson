from django.shortcuts import render
from django.views.generic import ListView
from course.models import ElmsCourse
from .models import ElmsChapter
from lesson.models import ElmsLesson, ElmsLessonUserShip
from django.contrib.auth.mixins import LoginRequiredMixin
from core.utilities import getNotifications

class Index(LoginRequiredMixin, ListView):
  def get(self, request, *args, **kwargs):
    context = {}
    #context['chapters'] = ElmsChapter.objects.filter(deleted__isnull=True)
    """
    elms_lesson_user_shipにログイン者のデータがなかったら
    lessonを、elms_lesson_user_shipにインポート
    """
    is_lesson = ElmsLessonUserShip.objects.filter(deleted__isnull=True, custom_user=self.request.user.pk).first()
    if not is_lesson:
      lessons = ElmsLesson.objects.filter(deleted__isnull=True)
      lesson_obj = []
      for lesson in lessons:
        lesson_obj.append(ElmsLessonUserShip(custom_user_id=self.request.user.pk, lesson_id=lesson.id))
      ElmsLessonUserShip.objects.bulk_create(lesson_obj)


    context['courses'] = ElmsCourse.objects.filter(deleted__isnull=True)
    context['chapters'] = ElmsChapter.objects.filter(deleted__isnull=True)
    context['lessons'] = ElmsLesson.objects.filter(deleted__isnull=True)
    context['notifications'] = getNotifications()
    return render(request, 'chapter/index.html', context)



