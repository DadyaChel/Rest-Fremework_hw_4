from django.contrib import admin
from django.urls import path, include
from mb_shop import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('firma', views.FirmaViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', views.create_product),
    path('product/<int:pk>/', views.detail_product),

    path('firma/', views.create_firma),
    path('firma/<int:pk>/', views.detail_firma),

    path('category/', views.create_category),
    path('category/<int:pk>/', views.detail_category),

    path('product/v-1/', views.ProductCreateListView.as_view()),
    path('product/v-1/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('firma/v-1/', views.FirmaCreateListView.as_view()),
    path('firma/v-1/<int:pk>/', views.FirmaRetrieveUpdateDestroyAPIView.as_view()),
    path('category/v-1/', views.CategoryCreateListView.as_view()),
    path('category/v-1/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('v-1/', include(router.urls))
]
