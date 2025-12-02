from django.urls import path
from .views import CategoryViewSet 

urlpatterns = [
    path('categorys/', CategoryViewSet.as_view(
        {
            'get' : 'list', 
            'post' : 'create',
        }
        )),

    path('categorys/<int:pk>/', CategoryViewSet.as_view(
        {
            'get' : 'retrieve', 
            'post': 'update', 
            'delete' : 'destroy',
        }

            )),

    
]
# from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet, basename='category')

# urlpatterns = router.urls