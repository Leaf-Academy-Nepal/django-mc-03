from django.views.generic import TemplateView


# yeha hamle django le diyeko kunai pani html file open garna lai or server garna lai TemplateView use gareko ho
# IndexPageView -> yo function or class  call garne bitikai - index.html file open gar 

class IndexPageView(TemplateView):
    template_name = "index.html"
