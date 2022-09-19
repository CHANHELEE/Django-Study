from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    tag_set = models.ManyToManyField('Tag',blank=True)
    is_public = models.BooleanField(default=False , verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now 는 자동으로 디비에 저장된다.
    #register to admin

    # Java 의 toString 과 같은 기능
    def __str__(self):
        return self.message

    class Meta: #inner class 로 기본정렬을 지정. 쿼리를 날릴때 마다 order_by 를 자동으로 날린다.
        ordering=['-id']


    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description ="메세지 글자수"

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, limit_choices_to={'is_public':True}) # post_id 로 컬럼이 생성 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)