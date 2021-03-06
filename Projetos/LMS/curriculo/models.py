from django.db import models
from contas.models import Coordenador, Professor

class Curso(models.Model):
    idcurso = models.AutoField(db_column='idCurso', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30)
    
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    iddisciplina = models.AutoField(db_column='idDisciplina', primary_key=True)  
    nome = models.CharField(unique=True, max_length=30, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    statusdisc = models.CharField(db_column='statusDisc', max_length=20, blank=True, null=True)  
    planodeensino = models.CharField(db_column='planoDeEnsino', max_length=1000, blank=True, null=True)  
    cargahoraria = models.IntegerField(db_column='cargaHoraria', blank=True, null=True)  
    competencias = models.CharField(max_length=1000, blank=True, null=True)
    habilidades = models.CharField(max_length=1000, blank=True, null=True)
    ementa = models.CharField(max_length=1000, blank=True, null=True)
    conteudoprogramatico = models.CharField(db_column='conteudoProgramatico', max_length=1000, blank=True, null=True)  
    bibliografiabasica = models.CharField(db_column='bibliografiaBasica', max_length=1000, blank=True, null=True)  
    bibliografiacomplementar = models.CharField(db_column='bibliografiaComplementar', max_length=1000, blank=True, null=True)  
    percentualpratico = models.IntegerField(db_column='percentualPratico', blank=True, null=True)  
    percentualteorico = models.IntegerField(db_column='percentualTeorico', blank=True, null=True)  
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')  

    def __str__(self):
        return self.nome


class Disciplinaofertada(models.Model):
    iddisciplinaofertada = models.AutoField(db_column='idDisciplinaOfertada', primary_key=True)  
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador')  
    dtiniciomatricula = models.DateField(db_column='dtInicioMatricula', blank=True, null=True)  
    dtfimmatricula = models.DateField(db_column='dtFimMatricula', blank=True, null=True)  
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='idCurso')  
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.CharField(max_length=6, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor', blank=True, null=True)  
    metodologia = models.CharField(max_length=1000, blank=True, null=True)
    recursos = models.CharField(max_length=1000, blank=True, null=True)
    criterioavaliacao = models.CharField(db_column='criterioAvaliacao', max_length=1000, blank=True, null=True)  
    planodeaulas = models.CharField(db_column='planoDeAulas', max_length=1000, blank=True, null=True)
    
    def __str__(self):
        pass
