from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views  

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    # Static HTML Template Routes
    path('', views.index, name='index'), # 👈 This handles http://127.0.0.1:8000/restaurant/
    path('about/', views.about, name='about'),

    path('api-token-auth/', obtain_auth_token),
    path('booking/', include(router.urls)),
    
    # 👈 Add these two lines for your Menu paths
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]