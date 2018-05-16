from django.db import models
from contas.models import Aluno,Coordenador,Professor
from curriculo.models import Disciplina,Disciplinaofertada, Curso



class Solicitacaomatricula(models.Model):
    idsolicitacaomatricula = models.AutoField(db_column='idSolicitacaoMatricula', primary_key=True)
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada')
    dtsolicitacao = models.DateField(db_column='dtSolicitacao')
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador', blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)


class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=1000)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=1000, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')



class Atividadevinculada(models.Model):
    idatividadevinculada = models.AutoField(db_column='idAtividadeVinculada', primary_key=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='idAtividade')  
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada') 
    rotulo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, blank=True, null=True)
    dtiniciorespostas = models.DateField(db_column='dtInicioRespostas', blank=True, null=True) 
    dtfimrespostas = models.DateField(db_column='dtFimRespostas', blank=True, null=True) 



class Entrega(models.Model):
    identrega = models.AutoField(db_column='idEntrega', primary_key=True)  
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')
    titulo = models.CharField(max_length=40, blank=True, null=True)
    resposta = models.CharField(max_length=1000, blank=True, null=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='idAtividadeVinculada') 
    dtentrega = models.DateField(db_column='dtEntrega') 
    status = models.CharField(max_length=20, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtavaliacao = models.DateField(db_column='dtAvaliacao') 
    obs = models.CharField(max_length=1000, blank=True, null=True)
