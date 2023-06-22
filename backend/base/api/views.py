
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from base.models import Product
from rest_framework import viewsets

# @api_view(["GET"])
# def get_products(request):
#     products=Product.objects.all()
#     serializer=ProductSerializer(products, many=True)
#     return Response(serializer.data)

# @api_view(["GET"])
# def view_product(request,pk):
#     product=Product.objects.get(_id=pk)
#     serializer=ProductSerializer(product, many=False)
    
#     return Response(serializer.data)

from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def get_trending_products(self, request):
        trending_products = Product.objects.order_by('-views')[:5]
        serializer = self.get_serializer(trending_products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['patch'])
    def view_update(self,request,pk=None):
        instance=self.get_object()
        # views=instance.views+1
        # instance.views=views
        instance.views+=1
        serializer=self.get_serializer(instance,data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

