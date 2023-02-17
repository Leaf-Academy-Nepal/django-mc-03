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
8. django lai media file kata rakhne taha huna parxa - settings.py ma vanne
```
MEDIA_URL = 'media/' 
- url ma k halne
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
- folder ko name k rakhne
```
9. aaba waiter lai ni taha huna parxa yo media/ vanne magda kata bata lyaune vanera
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

yo vaneko mathi ko media url ho ra kun folder ma store vako xa vaneko ho
```

10. index.html
```
{% for blog in blog_list %}

{{blog.title}} estaii esti garera property get garne
{% endfor %}

```

11. blog image check garna parxa xa ki xaina vanera
```
{% if blog.image %}
<img src="{{blog.image.url}}">
{% else %}

{% endif %}
```
12. condition check in django templates
```
{% if experience.is_currently_working_here %} 
    Current 
{%else%}
    {{experience.end_date}}
{% endif %}
```