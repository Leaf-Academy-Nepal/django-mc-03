1. unzip the file and view the html file
2. make templates folder
3. make static folder
4. go to settings.py
```
import os
DIRS': [os.path.join(BASE_DIR, 'templates')],
```
5. create views.py in portfolio
6. 
```
from django.views.generic import TemplateView

# here we are following the convention provided by Django
# IndexPageView vanne class call garyo vane index.html pathauxa

class IndexPageView(TemplateView):
    template_name = "index.html"
```

7. go to urls.py
8. 
```
from .views import IndexPageView

path('', IndexPageView.as_view(), name="homepage")
path('k hanne', 'kun function/class kholne', 'tesko name k vanne - django le chinne gari')

```
9. 127.0.0.0:8000 jada without css ko page load huna parxa
10. aaba css load garna lai settings.py ma jane
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
yo vaneko static file haru hami kata store garxau vanera vaneko ho
11. index.html ma jane ra {% load static %} suru ma halne - yo vaneko hamro static file chai yeha pauxa hai vaneko ho
12. change every static href and src into dynamic one
```
{% static 'file/ko/path.extension' %}

{% static 'css/style.css' %}
```

