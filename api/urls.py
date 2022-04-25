from .views import StatesViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', StatesViewSet, base_name='states')

urlpatterns = router.urls