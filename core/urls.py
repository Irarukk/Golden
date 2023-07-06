from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', home,name="home"),
    path('logout', logout,name="logout"),
    path('login', LoginView.as_view(template_name = 'core/3.ingresar.html'), name="login"),
    path('registro', registro, name="registro"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('limpiar', limpiar),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('estado_orden/<orden_id>', estado_orden, name='estado_orden'),
    path('orden/<orden_id>/actualizar_estado/', actualizar_estado_orden, name='actualizar_estado_orden'),
    path('perfil', perfil_cliente, name='perfil_cliente'),
]
