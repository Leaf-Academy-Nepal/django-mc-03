HTML same rakhne
1. base.html banaune
2. common common syntax haru / html ko - tya lagera rakhen - header footer
3. {% block content %} {% endblock %} yo halne - jaha chai hami aarko page halxau
4. remove unnecessary data
5. link garne
```
{% url 'index' %} -> django le aafnu urls or waiters haru lai index vanne page liyera aau vanxa
```
6. {% extends 'base.html' %} garne yo vaneko base.html ko sabai content liyera aau vaneko ho
7. {% block content %} {% endblock %}  esma content lekhne - aafnu html css haru

Blog Detail
1. BlogDetail vanne class banaune - DetailView import garne
```
class BlogDetail(DetailView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = "blog_detail.html"

```
2. blog_detail.html vanne page liyera aaune ani conent copy ganre
3. blog_detail ma {{object}} vanne key use garera aafnu content dynamic baanaune
4. urls.py
```
harek blog ko lagi unique url huna parxa
tesko lagi hami ki id use garxau ki slug use garxau
yo instance ma hami id use gardai xau

path("blog/<int:pk>/", BlogDetail.as_view(), name="blog_detail")

<int:pk> -> esle k baujnax vanda - yo pk vaneko primary key unique huna le eslai hami use garxau ra yo integer type ko ho
```

DB ma - get blog where id = pk

5. page link?
```
{% url 'blog_detail' blog.pk %}

{% url 'django lai hamle dine name' primarykey ki ta slug %}
```