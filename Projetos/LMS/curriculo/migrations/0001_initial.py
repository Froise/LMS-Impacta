# Generated by Django 2.0.5 on 2018-05-15 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.AutoField(db_column='idCurso', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('iddisciplina', models.AutoField(db_column='idDisciplina', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('statusdisc', models.CharField(blank=True, db_column='statusDisc', max_length=20, null=True)),
                ('planodeensino', models.CharField(blank=True, db_column='planoDeEnsino', max_length=1000, null=True)),
                ('cargahoraria', models.IntegerField(blank=True, db_column='cargaHoraria', null=True)),
                ('competencias', models.CharField(blank=True, max_length=1000, null=True)),
                ('habilidades', models.CharField(blank=True, max_length=1000, null=True)),
                ('ementa', models.CharField(blank=True, max_length=1000, null=True)),
                ('conteudoprogramatico', models.CharField(blank=True, db_column='conteudoProgramatico', max_length=1000, null=True)),
                ('bibliografiabasica', models.CharField(blank=True, db_column='bibliografiaBasica', max_length=1000, null=True)),
                ('bibliografiacomplementar', models.CharField(blank=True, db_column='bibliografiaComplementar', max_length=1000, null=True)),
                ('percentualpratico', models.IntegerField(blank=True, db_column='percentualPratico', null=True)),
                ('percentualteorico', models.IntegerField(blank=True, db_column='percentualTeorico', null=True)),
                ('idcoordenador', models.ForeignKey(db_column='idCoordenador', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Coordenador')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplinaofertada',
            fields=[
                ('iddisciplinaofertada', models.AutoField(db_column='idDisciplinaOfertada', primary_key=True, serialize=False)),
                ('dtiniciomatricula', models.DateField(blank=True, db_column='dtInicioMatricula', null=True)),
                ('dtfimmatricula', models.DateField(blank=True, db_column='dtFimMatricula', null=True)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('turma', models.CharField(blank=True, max_length=6, null=True)),
                ('metodologia', models.CharField(blank=True, max_length=1000, null=True)),
                ('recursos', models.CharField(blank=True, max_length=1000, null=True)),
                ('criterioavaliacao', models.CharField(blank=True, db_column='criterioAvaliacao', max_length=1000, null=True)),
                ('planodeaulas', models.CharField(blank=True, db_column='planoDeAulas', max_length=1000, null=True)),
                ('idcoordenador', models.ForeignKey(db_column='idCoordenador', on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Coordenador')),
                ('idcurso', models.ForeignKey(db_column='idCurso', on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Curso')),
                ('iddisciplina', models.ForeignKey(db_column='IdDisciplina', on_delete=django.db.models.deletion.DO_NOTHING, to='curriculo.Disciplina')),
                ('idprofessor', models.ForeignKey(blank=True, db_column='idProfessor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contas.Professor')),
            ],
        ),
    ]