from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Connection, Area

# Create your views here.
def login(request):
    return render(request, 'registration/login.html', {})

@login_required
def index(request):
    return render(request, 'social/index.html', {})

### COMPILAR ESSAS 3 JUNTAS NUMA SÓ ############################

@login_required
def profile(request, pk):
    profile_user = get_object_or_404(User, pk=pk)
    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/profile.html', {'profile_user': profile_user, 'connections': connections,
        'num': num})

@login_required
#Redireciona para a aba do perfil correspondente ao link clicado
def tabs(request, pk, tab):
    profile_user = get_object_or_404(User, pk=pk)
    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/profile.html', {'profile_user': profile_user,
        'tab': tab, 'connections': connections, 'num': num})  

@login_required
def connect(request, pk, tutor, area):
    profile_user = get_object_or_404(User, pk=pk)
    area = Area.objects.get(id=area)
    tutor = User.objects.get(id=tutor)

    #adiciona uma nova conexão no banco
    new_con = Connection(area_interesse=area, tutor=tutor, educando=profile_user)
    new_con.save()

    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()

    return render(request, 'social/profile.html', {'profile_user': profile_user,
        'area': area, 'connections': connections, 'num': num})    
### COMPILAR ESSAS 3 JUNTAS NUMA SÓ (END) #######################


@login_required
def math_list(request):
    users = User.objects.filter(groups__name='Matemática')
    return render(request, 'social/matematica.html', {'users': users})

@login_required
def info_list(request):
    users = User.objects.filter(groups__name='Informática')
    return render(request, 'social/informatica.html', {'users': users})

@login_required
def connect_details(request, pk, con_user, conexao):
    profile_user = get_object_or_404(User, pk=pk)
    con_user = User.objects.get(id=con_user)
    conexao = Connection.objects.get(id=conexao)
    #area = Connection.objects.get(id=conexao.area_interesse)
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/connect-details.html', {'profile_user': profile_user, 'num': num, 
        'con_user': con_user, 'conexao': conexao})

@login_required
#ACEITA a conexao e redireciona para 'Minhas Conexoes'
def connect_accept(request, pk, conexao, tab):
    profile_user = get_object_or_404(User, pk=pk)

    #atualiza status da conexão no banco
    conexao = Connection.objects.get(id=conexao)
    conexao.status = 'Ativa'
    conexao.save()

    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/profile.html', {'profile_user': profile_user,
        'tab': tab, 'connections': connections, 'num': num}) 

@login_required
#RECUSA a conexao e redireciona para 'Minhas Conexoes'
def connect_delete(request, pk, conexao, tab):
    profile_user = get_object_or_404(User, pk=pk)

    #deleta a conexão no banco
    conexao = Connection.objects.get(id=conexao)
    conexao.delete()

    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/profile.html', {'profile_user': profile_user,
        'tab': tab, 'connections': connections, 'num': num}) 

@login_required
#FINALIZA a conexao e redireciona para 'Minhas Conexoes'
def connect_end(request, pk, conexao, tab):
    profile_user = get_object_or_404(User, pk=pk)

    #atualiza status da conexão no banco
    conexao = Connection.objects.get(id=conexao)
    conexao.status = 'Inativa'
    conexao.save()

    connections = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk))
    num = Connection.objects.filter(Q(tutor=pk) | Q(educando=pk), status='Ativa').count()
    return render(request, 'social/profile.html', {'profile_user': profile_user,
        'tab': tab, 'connections': connections, 'num': num}) 