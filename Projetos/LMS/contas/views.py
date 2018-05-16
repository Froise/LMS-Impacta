from django.shortcuts import render

def listaAluno(request):
    context{
        "formAluno": Aluno.objects.all()
    }
    return render(request,"formNovoAluno.html",context)

def listaProfessor(request):
    context{
        "formAluno": Professor.objects.all()
    }
    return render(request,"formNovoProfessor.html",context)

def listaCoordenador(request):
    context{
        "formAluno": Coordenador.objects.all()
    }
    return render(request,"formNovoCoordenador.html",context)
