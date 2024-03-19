from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .models import KirrUrl
from .forms import SubmitUrlForm

# Create your views here.

def home_view_fbv(request, *args, **kwatgs):
     if request.method == "POST":
          print(request.POST)
     return render(request, "shortener/home.html", {})

class HomeView(View):
     def get(self, request, *args, **kwargs):
          the_form = SubmitUrlForm()
          context = {
               "title": "SUBMIT URL",
               "form": the_form
          }
          return render(request, "shortener/home.html", context)

     def post(self, request, *args, **kwargs):
          form = SubmitUrlForm(request.POST)
          context ={
               "title": "SUNMIT URL",
               "form" : form
          }
          template = "shortener/home.html"
            
          if form.is_valid():
               new_url = form.cleaned_data.get("url")
               obj, created = KirrUrl.objects.get_or_create(url=new_url)
               context = {
                    "object": obj,
                    "created" : created,
               }
               if created:
                    template = "shortener/success.html"
               else:
                    template = "shortener/already-exists.html"
        
          return render(request,template, context)

#def Kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
     #obj = get_object_or_404(KirrUrl, shortcode=shortcode)
    # return HttpResponseRedirect(obj.url) 

    #print(request.user)
    #print(request.user.is_authenticated())\
    #obj = KirrURL.objects.get(shortcode=shortcode)

    #obj_url = obj.url
    #try:
        #obj = KirrURL.objects.get(shortcode=shortcode)
    #except:
        #obj = KirrURL.objects.all().first()

    #obj_url = None
    #qs = KirrURL.objects.filter(shortcode_iexact=shortcode.upper())
    #if qs.exists() and qs.count() == 1:
        #objqs.first()
        #obj_url = obj.url
    
    #return HttpResponse("hello {sc}".format(sc=obj.url))




class URLRedirectView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        #print(args)
        #print(shortcode)
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
     
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
    
   #def post(self, request, *args, **kwargs):
   #        return HttpResponse()