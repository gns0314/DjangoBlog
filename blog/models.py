from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

# Create your models here.
# 카테고리 필드
category_select = (
    ('자유', '자유'),
    ('취미', '취미'),
    ('정보', '정보'),
) 


# 게시글
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices= category_select, default='자유')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    hit = models.PositiveBigIntegerField(default=0)
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d/', blank=True)

    @property
    def update_counter(self):
        self.hit = self. hit + 1
        self.save()

    def get_file_name(self):
        return self.file_upload.name.split('/')[-1]

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
# 댓글
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content