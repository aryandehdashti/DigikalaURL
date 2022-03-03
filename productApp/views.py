from rest_framework.decorators import api_view
from .models import Product
from django.http import HttpResponse

# Create your views here.

@api_view(['POST'])
def AddProduct(request):
    if request.method == 'POST':
        try:
            Product.GetProducts(str(request.data))
            return HttpResponse('success')
        except:
            return HttpResponse('''wrong URL ... just put your URL in <" "> .
                                and remember, this project only support main category pages
                                ''')


