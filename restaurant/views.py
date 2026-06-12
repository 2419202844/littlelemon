from django.shortcuts import render
from rest_framework import viewsets, generics # 👈 Added generics
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Menu # 👈 Added Menu here
from .serializers import BookingSerializer
from rest_framework import serializers # 👈 Added for a quick Menu serializer inline

# --- Menu Serializer ---
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# --- Menu Views ---
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# --- Booking ViewSet ---
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    # --- HTML Template Views ---
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})