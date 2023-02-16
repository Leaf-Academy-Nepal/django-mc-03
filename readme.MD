```
python manage.py migrate
```
yo suru mai garne kina ki aru le garkeko code hamro database ma halnu parxa - user table


1. python manage.py startapp garera app/section create garne - cv
```
python manage.py startapp cv
```
2. setting.py ma jane INSTALLED_APPS ma "cv" vanne app thapne - jun app banayo tei thapne
3. models.py ma hamro table ko properties lekhne
4. pip install pillow
5. Skill vanne table banaune - cv ko models.py vanne file ma
```
class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

```
6. admin.py ma Skill vanne add garne - esle garda hamro admin panel ma Skill vane add, delete, update garna milxa
7. createsupruser garne
```
python manage.py createsuperuser
```
8. access garne admin panel 
```
127.0.0.0:8000/admin
```
paxadi ko /admin halne
login garne

9. tya skill add garne
10. portfolio view.py ma gayera skill_list ko data pathaune
```
from cv.models import Skill

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["skill_list"] = Skill.objects.all()
        return context

```

esma hamle get_context_data vanne function overwrite gareko hou
tyo data ma hamle skill_list vanne euta key add garyou - ra tesma select * from skill vanne query ko data patahyou
11. index.html file ma gayera for loop lagauxau ra teko data access garaxau

```
{% for skill in skill_list  %}
{{skill.name}}
{% endfor %}
```