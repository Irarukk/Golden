from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from .models import OrdenCompra
from .models import Cliente, Compra


def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro",[])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo=item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        request.session["carro"] = []
    return redirect(to=carrito)


def carrito(request):
    return render(request, 'core/4.Carrito.html',{"carro":request.session.get("carro",[])})

def addtocar(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0]== codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([codigo,producto.nombre, producto.imagen, producto.precio,1,producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")

def dropitem(request,codigo):
    carro = request.session.get("carro",[])
    for item in carro:
        if item[0]== codigo:
            if item[4]>1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    
    request.session["carro"] = carro
    return redirect(to="carrito")

def limpiar(request):
    request.session.flush()
    return redirect(to="home")

def home(request):
    plantas = Producto.objects.all()
    return render(request, 'core/1.Index.html',{'plantas':plantas, "carro":request.session.get("carro",[])})

def login(request):
    return render(request, 'core/3.Ingresar.html')

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/2.Registrar.html',{'form': registro})

def estado_orden(request, orden_id):
    orden = OrdenCompra.objects.get(orden_id=orden_id)
    return render(request, 'estado_orden.html', {'orden': orden})

def actualizar_estado_orden(request, orden_id):
    orden = OrdenCompra.objects.get(orden_id=orden_id)
    
    # Procesar la solicitud para actualizar el estado
    nuevo_estado = request.POST.get('nuevo_estado')
    orden.estado = nuevo_estado
    orden.save()
    
    return redirect('estado_orden', orden_id=orden_id)

def perfil_cliente(request):
    cliente = Cliente.objects.get(user=request.user)
    compras = Compra.objects.filter(cliente=cliente)
    return render(request, 'perfil_cliente.html', {'cliente': cliente, 'compras': compras})