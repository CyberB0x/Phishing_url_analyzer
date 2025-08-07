from django.shortcuts import render
from .utils import analyze_url

def home(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        result = analyze_url(url)
        context["result"] = result
        context["url"] = url
    return render(request, "analyzer/home.html", context)
