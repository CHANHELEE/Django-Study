from . import views
from django.urls import path, re_path, register_converter

class YearConverter: #custom converter
    regex = r"20\d{2}"

    def to_python(self,value):
        return  int(value)
    def to_url(self,value):
        return  str(value)

register_converter(YearConverter,'year')

app_name='instagram' # uRL Reverse 에서 namespace 역할
urlpatterns = [
    path('', views.post_list),
    path('<int>:pk/',views.post_detail),
    path('archives/<int:year>/',views.archives_year),
    # re_path(r'archives/(?P<year>\d{4}+)/',views.archives_year()), # 위 코드와 숫자수만 제와하고 같음
    # path('archives/<year:year>/',views.archives_year),
]