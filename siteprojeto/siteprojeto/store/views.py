from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import Produto, Tamanho, Compra, productImage, Cliente, ItemsCompra, Morada_envio
from django.contrib.auth import authenticate, login, logout


def index(request):
    produtos_homepage = Produto.objects.order_by('-nome')[0:3]

    return render(request, 'store/index.html', {'produtos_homepage': produtos_homepage})

def login_page(request):
    return render(request, 'store/login.html')

def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('store:index'))
    else:
        error = 'O username e/ou a password incorreto(s)'
        return render(request, 'store/login.html', {'error': error})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('store:index'))

def products_view(request, ):
    products_list = Produto.objects.order_by('nome')[:]
    if request.method == 'POST':
        if request.POST['ordem'] == 'alfabetica':
            products_list = Produto.objects.order_by('nome')[:]
        if request.POST['ordem'] == 'preco':
            products_list = Produto.objects.order_by('preco')[:]
    context = {
        'products_list': products_list
    }
    return render(request, 'store/produtos.html', context)


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password_confirm']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                error = 'Este utilizador já existe.'
                return render(request, 'store/register.html', {'error': error})
            else:
                if User.objects.filter(email=email).exists():
                   error = 'Este email ja existe.'
                   return render(request, 'store/register.html', {'error': error})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                    cliente = Cliente(user=user)
                    cliente.save()
                    user.save()
                    print('user created :)')
                    return HttpResponseRedirect(reverse('store:index'))
        else:
            error = 'As passwords não coincidem'
            return render(request, 'store/register.html', {'error': error})
    else:
        return render(request, 'store/register.html')



def shop_cart(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        compra, created = Compra.objects.get_or_create(customer=cliente)
        items = compra.itemscompra_set.all()
    else:
        items = []
        compra = {'obter_total_items': 0, 'obter_total_compra': 0}
    return render(request, 'store/shop_cart.html', {'items': items, 'compra': compra})


def checkout(request):

    if request.user.is_authenticated:
        cliente = request.user.cliente
        compra, created = Compra.objects.get_or_create(customer=cliente, complete=False)
        items = compra.itemscompra_set.all()
    else:
        items = []
        compra = {'obter_total_items': 0, 'obter_total_compra': 0}

    return render(request, 'store/checkout.html', {'items': items, 'compra': compra})

def product_view(request, product_id):
    produto = get_object_or_404(Produto, pk=product_id)

    if request.user.is_authenticated:
        context = {
            'product_id': product_id,
            'produto': produto
        }
        return render(request, 'store/product_view.html', context)

    return render(request, 'store/product_view.html', {'product_id': product_id, 'produto': produto, 'erro': 'Não é possível adicionar produtos ao carrinho sem sessão iniciada.'})

def add_to_cart(request, product_id):


    if request.user.is_authenticated:
        cliente = request.user.cliente
        product = get_object_or_404(Produto, pk=product_id)
        array_compra = Compra.objects.filter(complete=False, customer=cliente)
        quant = request.POST['Quantidade']
        print(quant)
        repeticao = False
        if len(array_compra) ==0:
            cmp = Compra(customer=cliente)
            cmp.save()
            array_compra = [cmp,]

        if len(array_compra) > 0:
            compra = array_compra[0]
            for item in compra.itemscompra_set.all():
                print(item.produto == product)
                if (item.produto == product):
                    item.quantidade += int(quant)
                    item.save()
                    print('Add mais quantidade')
                    repeticao = True
                    break
                #else:
            if repeticao == False:
                add = ItemsCompra(produto=product, compra=compra, quantidade=quant)
                add.save()

        return HttpResponseRedirect(reverse('store:index'))


    return HttpResponseRedirect(reverse('store:product_view', args=(product_id,)))

def delete_from_cart(request, item_id):
    print(item_id)
    item = get_object_or_404(ItemsCompra, pk=item_id)
    print(item)
    item.delete()
    return HttpResponseRedirect(reverse('store:shop_cart'))

def payment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cidade = request.POST['city']
            concelho = request.POST['concelho']
            customer = request.user.cliente
            morada = request.POST['address']
            codigo_postal = request.POST['zipcode']
            compra = get_object_or_404(Compra, customer=customer, complete=False)
            print(compra)
            # compra.complete = True,  |SOON|
            rep = False

            for x in Morada_envio.objects.all():
                if x.morada == morada and x.codigo_postal == codigo_postal and x.customer == customer:
                    rep = True


            if rep == False:
                morada_cliente = Morada_envio(customer=customer, compra=compra, morada=morada, codigo_postal=codigo_postal, cidade=cidade, concelho=concelho)
                morada_cliente.save()
            return render(request, 'store/coming_soon.html')


    return HttpResponseRedirect(reverse('store:checkout'))

