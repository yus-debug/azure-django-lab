from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("""
    <html>
    <body>
    <h1>Hello from Azure!</h1>
    <p><strong>Pipeline is working!</strong></p>
    </body>
    </html>
    """)

urlpatterns = [
    path('', home),
]