1. contact vanne application create garyou
```
python manage.py startapp contact
```
2. Contact vanne table/model create garoyou
```
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

```
- create_at chai create hune bela aafai create hunxa - auto_now_add=True garda aafai date database rakhnxa

3. admin ma add garyou
```
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
```
4. forms.py vanne file create garxau
```
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]
    
```
- yo vaneko hamro form bata k k data line - esma hamle name, meial subject ra message li ra xau

5. views.py of portfolio ma gayera - get_context_data vitra yo rakhxau - contact Form
```
        context["contact_form"] = ContactForm()

```
6. index.html ma gyera contact ko lagi form halxau
```
        {{contact_form}}

        {{contact_form.as_p}}
        -- yo vaneko paragraph ma dekhaune ho <p> yo tag vitra haldinxa harek input lai 

```
7. form vanne ni banauna praxa ra button ni halna parxa
```
<form method="POST" action="{% url 'contact' %}">
        {% csrf_token %}
        {{contact_us_form.as_p}}
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
```

csrf token birana vayena - csrf le hamro system security ko help garxa ra sachikai genuine user le chalako ho vanera taha hunxa

method = POST hunxa kina ki hami data input gardai xau

action = yo vaneko data input bata backend ma kata pathaune ho


8. contact ma views.py banaune
```
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

class ContactCreateView(CreateView):
    form_class = ContactForm
    model = Contact
    success_url = "/"

```
CreateView vanne code inherit garne - esle hami databae ma code save gardai xau hai vanxa
9. hamro urls.py yeha xa vanera django lai vanna parxa
```
from django.urls import path, include

    path('', include("contact.urls")),

    #aaba django lai taha hunxa ki contact ko urls.py ma pani code xa vanera - waiter ko kam garxa

```


##Flow2:
Blog list garne ra templates repeate garna naparos wala code
1. blog ma view.py open garera code lekhne
ListView ko
```
from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


class BlogListView(ListView):
    queryset = Blog.objects.all()
    #select * from blog

    template_name = "blog_list.html"
    #templates vanne folder ko kun file kholne

    model = Blog
    #kun table ko data


    #object_list - default name - key
```

2. urls.py ma pani code lekhne
```
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list")
]
```
3. blog_list.html vanne file banaune ra template bata code import garne
