from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Registra um novo usuário."""
    if request.method != 'POST':
        # Exibe um formulário em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Entra com o usuário e redireciona para a página inicial.
            login(request, new_user)
            return redirect('learning_logs:index')

    # MOstra um formulário em branco ou inválido
    context ={'form' : form}
    return render(request, 'registration/register.html', context)
