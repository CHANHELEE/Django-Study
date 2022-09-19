from django.db import models

# Create your models here.


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False , verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now 는 자동으로 디비에 저장된다.
    #register to admin

    # Java 의 toString 과 같은 기능
    def __str__(self):
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description ="메세지 글자수"

