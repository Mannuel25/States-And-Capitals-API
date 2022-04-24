from django.urls import path
from .views import StateViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('users', UserViewSet, base_name='users')
router.register('', StateViewSet, base_name='states')

urlpatterns = router.urls
