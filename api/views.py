from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, TaskSerializer
from .models import Category, Task

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()