1. naya app banaune - blog
```
python manage.py startapp blog
```
2. add blog in INSTALLED_APPS of settings.py
3. pip install pillow
4. create new table called Blogs
```
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog/images/")
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    author = models.CharField(max_length=255, null=True, blank=True)
    published_date = models.DateField()

```
5. makemigraitons
```
python manage.py makemigrations
python manage.py migrate
```
6.  add to admin.py of blogs
```
from .models import Blog

admin.site.register(Blog)
```
7. in portfolio views.py
```
from blog.models import Blog

def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #select * from skill
        data["skill_list"] = Skill.objects.all()
        data["blog_list"] = Blog.objects.all()
        return data
```