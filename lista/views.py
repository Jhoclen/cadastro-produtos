


from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Produtos

def home(request):
    print(request.method)
    if request.method == 'GET':
        erro = request.GET.get('erro')
        texto = request.GET.get('texto')
        texto2 = request.GET.get('texto2')
        #print(request.GET.get('texto'))
        return render(
             request,
            'home.html', {
                'erro':erro, 
                'texto':texto, 
                'texto2':texto2
            }
        )
    elif request.method == 'POST':
        produto = request.POST.get('produto')
        preco = request.POST.get('preco')
        
        if len(produto) <= 0:
            return redirect('/produtos/save?erro=1&texto=Digite o nome do produto completo')
        elif len(preco) <= 0:
            return redirect('/produtos/save?erro=2&texto2=Digite um valor valido')    
        
        save = Produtos(
            produto = produto,
            preco = preco
        )
        save.save()
        return redirect('/produtos/lista')
        
def colunas(request):
    produtos = Produtos.objects.all()
    print(produtos)
    return render(request, 'lista.html',{'produtos':produtos})

def inicio(request):
    return redirect('/produtos/save')

def deletar(resquest, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    return redirect('/produtos/lista')
