

# from django.urls import path, include
# from . import views
# urlpatterns = [
#     # path("", views.home, name="home" ),
#     path("products/", views.get_products, name="products" ),
#     path("products/<int:pk>/", views.view_product, name="product" ),
    
    
    
# ]


from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet),
custom_patterns = [
        path('trending_products/', ProductViewSet.as_view({'get': 'get_trending_products'}), name='get_trending_products'),
        path('patch_view/<int:pk>', ProductViewSet.as_view({'patch': 'view_update'}), name='view_update'),

    # path('my-models/<int:pk>/custom-action3/', MyModelViewSet.as_view({'put': 'custom_action3'}), name='custom-action3'
    
]


urlpatterns = [
    # Your other URL patterns
    path('', include(router.urls)),
    path('', include(custom_patterns)),
]
