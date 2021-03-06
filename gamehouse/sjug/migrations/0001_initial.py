# Generated by Django 3.1.4 on 2020-12-31 12:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('id_compania', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CompaniasAsociadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compania', models.ForeignKey(db_column='compania', on_delete=django.db.models.deletion.CASCADE, related_name='juegos_asociados', to='sjug.compania', verbose_name='Compañias que hicieron el juego')),
            ],
        ),
        migrations.CreateModel(
            name='Generacion',
            fields=[
                ('id_generacion', models.AutoField(primary_key=True, serialize=False)),
                ('generacion', models.CharField(max_length=20, unique=True, verbose_name='Numero de generacion')),
                ('bits', models.PositiveIntegerField(blank=True, default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2056)])),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='GenerosAsociados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(db_column='genero', on_delete=django.db.models.deletion.CASCADE, related_name='juegos_asociados', to='sjug.genero', verbose_name='Generos que conforman el juego')),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('anio', models.PositiveIntegerField(default=2020)),
                ('descripcion', models.TextField()),
                ('descripcion_limpia', models.TextField(blank=True, null=True)),
                ('companias', models.ManyToManyField(through='sjug.CompaniasAsociadas', to='sjug.Compania')),
                ('generos', models.ManyToManyField(through='sjug.GenerosAsociados', to='sjug.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id_plataforma', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Recomendacion',
            fields=[
                ('id_recomendacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30, verbose_name='El de esta version de recomendacion')),
                ('retroalimentacion', models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=256)),
                ('correo', models.EmailField(help_text='ejemplo: usuario@mail.com', max_length=254)),
                ('fec_nac', models.DateField(default=datetime.date.today, help_text='Use el formato:Mes/Dia/Año')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('usuario', models.OneToOneField(db_column='id_jugador', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.usuario', verbose_name='Identificador del jugador')),
                ('nickname', models.CharField(max_length=30, unique=True, verbose_name='Nickname del usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PlataformasAsociadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.ForeignKey(db_column='juego', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plataformas_asociadas', to='sjug.juego', verbose_name='Juegos que pertenecen a la plataforma')),
                ('plataforma', models.ForeignKey(db_column='plataforma', on_delete=django.db.models.deletion.CASCADE, related_name='juegos_asociados', to='sjug.plataforma', verbose_name='Plataforma a las que pertenece el juego')),
            ],
        ),
        migrations.CreateModel(
            name='ListGeneros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listgenero', models.CharField(max_length=100)),
                ('listplataforma', models.CharField(max_length=100)),
                ('juego', models.ForeignKey(db_column='juego', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generos_boolean', to='sjug.juego', verbose_name='generos en boolean')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id_lista', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='El nombre de la lista')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion detallada de la lista si existe')),
                ('juego', models.ManyToManyField(to='sjug.Juego', verbose_name='Juegos que conforman esta lista')),
                ('recomendacion', models.ForeignKey(db_column='id_recomendacion', on_delete=django.db.models.deletion.CASCADE, related_name='listas', to='sjug.recomendacion', verbose_name='Recomendacion a la que pertenece esta lista')),
            ],
        ),
        migrations.CreateModel(
            name='JuegosFavoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.ForeignKey(db_column='juego', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='sjug.juego', verbose_name='Juego que le gusta al jugador')),
                ('jugador', models.ForeignKey(db_column='jugador', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='juegos_favoritos', to='sjug.jugador', to_field='nickname', verbose_name='Jugador al que le gusta el juego')),
            ],
        ),
        migrations.AddField(
            model_name='juego',
            name='plataformas',
            field=models.ManyToManyField(through='sjug.PlataformasAsociadas', to='sjug.Plataforma'),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.URLField(max_length=511)),
                ('alt', models.CharField(max_length=100, verbose_name='Texto alternativo a la imagen')),
                ('juego', models.ForeignKey(db_column='juego', on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='sjug.juego', verbose_name='Imagenes que representan el juego')),
            ],
        ),
        migrations.CreateModel(
            name='GenerosFavoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(db_column='genero', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='sjug.genero', verbose_name='Genero que le gusta al jugador')),
                ('jugador', models.ForeignKey(db_column='jugador', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generos_favoritos', to='sjug.jugador', to_field='nickname', verbose_name='Jugador al que le gusta el genero')),
            ],
        ),
        migrations.AddField(
            model_name='generosasociados',
            name='juego',
            field=models.ForeignKey(db_column='juego', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='generos_asociados', to='sjug.juego', verbose_name='Juegos que pertenecen al genero'),
        ),
        migrations.AddField(
            model_name='companiasasociadas',
            name='juego',
            field=models.ForeignKey(db_column='juego', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companias_asociadas', to='sjug.juego', verbose_name='Juegos que pertenecen a la plataforma'),
        ),
        migrations.CreateModel(
            name='CDE',
            fields=[
                ('jugador', models.OneToOneField(db_column='jugador', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.jugador', verbose_name='Jugador a quien pertenecen las CDE')),
                ('cde0', models.CharField(max_length=255)),
                ('cde1', models.CharField(max_length=255)),
                ('cde2', models.CharField(max_length=255)),
                ('cde3', models.CharField(max_length=255)),
                ('cde4', models.CharField(max_length=255)),
                ('cde5', models.CharField(max_length=255)),
                ('cde6', models.CharField(max_length=255)),
                ('cde7', models.CharField(max_length=255)),
                ('cde8', models.CharField(max_length=255)),
                ('cde9', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('jugador', models.OneToOneField(db_column='jugador', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.jugador', verbose_name='Jugador a quien pertenecen las CPU')),
                ('cpu0', models.CharField(max_length=255)),
                ('cpu1', models.CharField(max_length=255)),
                ('cpu2', models.CharField(max_length=255)),
                ('cpu3', models.CharField(max_length=255)),
                ('cpu4', models.CharField(max_length=255)),
                ('cpu5', models.CharField(max_length=255)),
                ('cpu6', models.CharField(max_length=255)),
                ('cpu7', models.CharField(max_length=255)),
                ('cpu8', models.CharField(max_length=255)),
                ('cpu9', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vector_Caracteristicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpus', models.CharField(max_length=100)),
                ('cdes', models.CharField(max_length=100)),
                ('juego', models.ForeignKey(db_column='juego', on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='sjug.juego', verbose_name='Juego al que pertenece la opinion')),
                ('jugador', models.ForeignKey(db_column='jugador', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vectores_caracteristicas', to='sjug.jugador', verbose_name='Jugador al que pertenece este vector de caracteristicas')),
            ],
        ),
        migrations.AddField(
            model_name='recomendacion',
            name='jugador',
            field=models.ForeignKey(db_column='jugador', on_delete=django.db.models.deletion.CASCADE, related_name='recomendaciones', to='sjug.jugador', to_field='nickname', verbose_name='Jugador al que se le hace esta recomendacion'),
        ),
        migrations.CreateModel(
            name='PlataformasFavoritas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.ForeignKey(db_column='plataforma', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='sjug.plataforma', verbose_name='Plataforma que tiene el jugador')),
                ('jugador', models.ForeignKey(db_column='jugador', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plataformas_favoritas', to='sjug.jugador', to_field='nickname', verbose_name='Jugador que tiene la plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True)),
                ('gusto', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Qué tanto te gustó el juego en general')),
                ('guion', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación del guión del juego')),
                ('artes', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación de la arte del juego')),
                ('jugabilidad', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación de la jugabilidad del juego')),
                ('tecnico', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación del aspecto técnico del juego')),
                ('puntaje_total', models.PositiveSmallIntegerField(blank=True, default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(50)], verbose_name='Puntaje total del juego de acuerdo al usuario')),
                ('juego', models.ForeignKey(db_column='juego', on_delete=django.db.models.deletion.CASCADE, related_name='opiniones', to='sjug.juego', verbose_name='Juego al que pertenece la opinion')),
                ('jugador', models.ForeignKey(db_column='jugador', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opiniones', to='sjug.jugador', to_field='nickname', verbose_name='Creador de la opinion')),
            ],
        ),
        migrations.AddField(
            model_name='jugador',
            name='generos',
            field=models.ManyToManyField(through='sjug.GenerosFavoritos', to='sjug.Genero'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='juegos',
            field=models.ManyToManyField(through='sjug.JuegosFavoritos', to='sjug.Juego', verbose_name='Juegos favoritos del usuario'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='plataformas',
            field=models.ManyToManyField(through='sjug.PlataformasFavoritas', to='sjug.Plataforma'),
        ),
    ]
