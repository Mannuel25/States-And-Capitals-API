from .views import StatesViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('states', StatesViewSet, basename='states')

urlpatterns = router.urls