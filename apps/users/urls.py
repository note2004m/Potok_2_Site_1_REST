from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPI
from apps.products.views import ProductAPI

router = DefaultRouter()
router.register('users', UserAPI, 'api_user')
router.register('products', ProductAPI, 'api_product')

urlpatterns = router.urls