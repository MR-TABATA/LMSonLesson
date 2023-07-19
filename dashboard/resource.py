from accounts.models import CustomUser
from chapter.models import ElmsChapter
from lesson.models import ElmsLesson, ElmsLessonUserShip
from notification.models import ElmsNotification
from course.models import ElmsCourse
from query.models import ElmsQuery

from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
from import_export.formats import base_formats
from import_export.widgets import Widget

from django.contrib.auth.hashers import make_password
import re
from django.utils.safestring import mark_safe
from django.utils import timezone


class ElmsCourseResource(ModelResource):
  class Meta:
    model = ElmsCourse
    fields = ('id', 'title', 'memo',)

class ElmsChapterResource(ModelResource):
  class Meta:
    model = ElmsChapter
    fields = ('id', 'chapter_title', 'memo', 'elms_chapter_course')

class ElmsLessonResource(ModelResource):
  class Meta:
    model = ElmsLesson
    fields = ('id', 'title', 'type', 'content', 'timelimit', 'memo', 'elms_lesson_chapter', 'image')

class ElmsNotificationResource(ModelResource):
  class Meta:
    model = ElmsNotification
    fields = ('id', 'title', 'content', 'elms_user', )

class ElmsQueryResource(ModelResource):
  class Meta:
    model = ElmsQuery
    fields = ('id', 'mail', 'content',)


class MyUserResource(ModelResource):
  def before_import_row(self, row, **kwargs):
    value = row['password']
    #空白、または20文字以上の場合、ハッシュ化する
    if len(row['password']) < 20 & len(row['password']) > 0:
      row['password'] = make_password(value)
  class Meta:
    model = CustomUser

"""
レッスンの理解度をCSV出力
"""
class ChoicesWidget(Widget):
  def __init__(self, choices, *args, **kwargs):
    self.choices = dict(choices)
    self.revert_choices = dict((v, k) for k, v in self.choices.items())

  def clean(self, value, row=None, *args, **kwargs):
    return self.revert_choices.get(value, value) if value else None

  def render(self, value, obj=None):
    return self.choices.get(value, '')

class ElmsLessonUserShipResource(ModelResource):
  ChapterName = Field(
    column_name='lesson title',
    attribute='lesson',
    widget=ForeignKeyWidget(model=ElmsLesson, field='title')
  )
  CustomUserLastName = Field(
    column_name='last_name',
    attribute='custom_user',
    widget=ForeignKeyWidget(model=CustomUser, field='last_name')
  )
  CustomUserFirstName = Field(
    column_name='first_name',
    attribute='custom_user',
    widget=ForeignKeyWidget(model=CustomUser, field='first_name')
  )
  Comprehension = Field(
    widget=ChoicesWidget(ElmsLessonUserShip.COMPREHENSION_TYPES),
    column_name='comprehension_type',
    attribute='comprehension',
  )
  class Meta:
    model = ElmsLessonUserShip
    fields = ('lesson title', 'lesson', 'last_name', 'first_name', 'comprehension', 'comprehension_type', 'modified')

  def export(self, queryset=None, *args, **kwargs):
    queryset = queryset.filter(comprehension__isnull=False)
    return super().export(queryset, *args, **kwargs)


