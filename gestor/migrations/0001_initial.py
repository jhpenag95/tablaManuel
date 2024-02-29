# Generated by Django 5.0 on 2024-02-27 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('asociados', models.TextField()),
                ('cluster', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_inicio_planeada', models.DateField(blank=True, null=True)),
                ('fecha_inicio_real', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion_planeada', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion_real', models.DateField(blank=True, null=True)),
                ('alcance', models.TextField()),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('suspendido', 'Suspendido'), ('cerrado', 'Cerrado')], max_length=50)),
                ('porcentaje_completado', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=50)),
                ('lider', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('antecedentes', models.TextField()),
                ('fase', models.CharField(max_length=100)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('spi', models.FloatField(default=0)),
                ('es', models.FloatField(default=0)),
                ('grupo', models.ManyToManyField(related_name='proyectos', to='gestor.grupo')),
                ('programas', models.ManyToManyField(related_name='proyectos', to='gestor.programa')),
            ],
        ),
        migrations.CreateModel(
            name='MatrizRiesgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('Causas', models.CharField(max_length=200)),
                ('Plan', models.CharField(max_length=200)),
                ('Descripcion_tiempo', models.CharField(max_length=200)),
                ('Descripcion_alcance', models.CharField(max_length=200)),
                ('Descripcion_costo', models.CharField(max_length=200)),
                ('probavilidad', models.CharField(choices=[('alto1', 'Alto'), ('alto2', 'Muy Alto'), ('bajo1', 'Bajo'), ('medio', 'Medio'), ('Bajo2', 'Muy Bajo')], max_length=20)),
                ('gravedad', models.CharField(choices=[('alto1', 'Alto'), ('alto2', 'Muy Alto'), ('bajo1', 'Bajo'), ('medio', 'Medio'), ('Bajo2', 'Muy Bajo')], max_length=20)),
                ('riesgo', models.CharField(choices=[('grave', 'Muy grave'), ('importante', 'Importante'), ('apreciable', 'Apreciable'), ('marginal', 'Marginal')], max_length=20)),
                ('materializo', models.CharField(max_length=200)),
                ('acciones_mitigacion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Hito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descriocion', models.TextField()),
                ('link', models.URLField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Costos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrato', models.CharField(max_length=100)),
                ('objeto', models.TextField()),
                ('tipo', models.CharField(max_length=100)),
                ('aliado', models.CharField(max_length=200)),
                ('contrato_aliado', models.CharField(max_length=100)),
                ('backlog', models.TextField()),
                ('one_time', models.TextField()),
                ('recurrente', models.TextField()),
                ('meses', models.CharField(max_length=100)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificando_problema', models.TextField()),
                ('causa', models.TextField()),
                ('solucion', models.TextField()),
                ('planes_mejora_aplicados', models.TextField()),
                ('resultados_planes_mejora', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('administrador', 'Administrador'), ('gerente', 'Gerente'), ('miembro', 'Miembro')], max_length=20)),
                ('equipos', models.ManyToManyField(related_name='miembros', to='gestor.equipo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('dependencias', models.ManyToManyField(blank=True, to='gestor.tarea')),
                ('hito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.hito')),
                ('asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.usuario'),
        ),
        migrations.AddField(
            model_name='hito',
            name='asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.usuario'),
        ),
    ]
