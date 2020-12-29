from django.db.models import *
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .juego import Juego, Genero, Plataforma
from datetime import date #Utilizar para fecha
from django.utils import timezone

""" Entidades del jugador """


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=256)
    correo = models.EmailField(help_text="ejemplo: usuario@mail.com",)
    fec_nac = models.DateField(help_text="Use el formato:Mes/Dia/Año", default=date.today)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.correo)


class Jugador(models.Model):
    usuario = models.OneToOneField(Usuario,
                                   on_delete=models.CASCADE,
                                   primary_key=True,
                                   to_field="id_usuario",
                                   db_column="id_jugador",
                                   verbose_name="Identificador del jugador"
                                   )
    juegos = models.ManyToManyField(Juego,
                                    through='JuegosFavoritos',
                                    verbose_name="Juegos favoritos del usuario"
                                    )
    generos = models.ManyToManyField(Genero,
                                     through='GenerosFavoritos',
                                     through_fields=('jugador', 'genero')
                                     )
    plataformas = models.ManyToManyField(Plataforma,
                                         through='PlataformasFavoritas',
                                         through_fields=(
                                             'jugador', 'plataforma')
                                         )
    # null indica que pueden almacenarse datos NULL en la tabla
    # blank indica que en los formularios se permite que el campo este en
    # blanco
    nickname = models.CharField(
        unique=True,
        null=False,
        max_length=30,
        verbose_name="Nickname del usuario")

    def __str__(self):
        return self.nickname


class Opinion(models.Model):
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.SET_NULL,
                                # AL Borrar el creador se pone en nulo y no
                                # mueren comentarios
                                to_field='nickname',
                                related_name='opiniones',
                                db_column='jugador',
                                verbose_name='Creador de la opinion',
                                null=True  # Activar para conservar la opinion SET_NULL CAMBIAR SI NECESARIO
                                )  # PONER EN NULL si jugador muere
    juego = models.ForeignKey(Juego,
                              on_delete=models.CASCADE,
                              # AL Borrar el juego se borran los comentarios
                              # relacionados
                              related_name='opiniones',
                              db_column='juego',
                              verbose_name='Juego al que pertenece la opinion',
                              )
    comentario = models.TextField(blank=True)
    CHOICES = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),
               (6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10')]
    gusto = models.PositiveSmallIntegerField(default=1, blank=True,
                                        validators=[
                                            MinValueValidator(1), MaxValueValidator(10)],
                                        choices = CHOICES,
                                        verbose_name='Qué tanto te gustó el juego en general',
                                        )
    guion = models.PositiveSmallIntegerField(default=1, blank=True,
                                        validators=[
                                            MinValueValidator(1), MaxValueValidator(10)],
                                        choices = CHOICES,
                                        verbose_name='Calificación del guión del juego',
                                        )
    artes = models.PositiveSmallIntegerField(default=1, blank=True,
                                        validators=[
                                            MinValueValidator(1), MaxValueValidator(10)],
                                        choices = CHOICES,
                                        verbose_name='Calificación de la arte del juego',
                                        )
    jugabilidad = models.PositiveSmallIntegerField(default=1, blank=True,
                                        validators=[
                                            MinValueValidator(1), MaxValueValidator(10)],
                                        choices = CHOICES,
                                        verbose_name='Calificación de la jugabilidad del juego',
                                        )
    tecnico = models.PositiveSmallIntegerField(default=1, blank=True,
                                        validators=[
                                            MinValueValidator(1), MaxValueValidator(10)],
                                        choices = CHOICES,
                                        verbose_name='Calificación del aspecto técnico del juego',
                                        )
    def __str__(self):
        return '%s, %s' % (self.jugador.id, self.juego.titulo)


""" Entidades de relacion """


class JuegosFavoritos(models.Model):
    # id_jfavoritos = models.AutoField(primary_key = True)
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.CASCADE,
                                null=True,
                                to_field='nickname',
                                db_column='jugador',
                                related_name='juegos_favoritos',
                                verbose_name='Jugador al que le gusta el juego',
                                )
    juego = models.ForeignKey(Juego,
                              on_delete=models.CASCADE,
                              null=True,
                              db_column='juego',
                              related_name='jugadores',
                              verbose_name='Juego que le gusta al jugador',
                              )

    def __str__(self):
        return '%s, %s' % (self.jugador.id, self.juego.titulo)
    # Dejando este campo opcional como comentario por el momento
    """
  fecha_adicion = models.DateField(blank = TRUE,
  null = TRUE,
  verbose="En que fecha el usuario indico que le gustaba"
  )
  """


class GenerosFavoritos(models.Model):
    # id_gfavoritos = models.AutoField(primary_key = True)
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.CASCADE,
                                null=True,
                                to_field='nickname',
                                db_column='jugador',
                                related_name='generos_favoritos',
                                verbose_name='Jugador al que le gusta el genero',
                                )
    genero = models.ForeignKey(Genero,
                               on_delete=models.CASCADE,
                               null=True,
                               db_column='genero',
                               related_name='jugadores',
                               verbose_name='Genero que le gusta al jugador',
                               )


class PlataformasFavoritas(models.Model):
    # id_pfavoritos = models.AutoField(primary_key = True)
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.CASCADE,
                                null=True,
                                to_field='nickname',
                                db_column='jugador',
                                related_name='plataformas_favoritas',
                                verbose_name='Jugador que tiene la plataforma',
                                )
    plataforma = models.ForeignKey(Plataforma,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   db_column='plataforma',
                                   related_name='jugadores',
                                   verbose_name='Plataforma que tiene el jugador',
                                   )


class CDE(models.Model):
    jugador = models.OneToOneField(Jugador,
                                   on_delete=models.CASCADE,
                                   primary_key=True,
                                   db_column="jugador",
                                   verbose_name="Jugador a quien pertenecen las CDE")
    
    cde0 = models.CharField(max_length=256)
    cde1 = models.CharField(max_length=256)
    cde2 = models.CharField(max_length=256)
    cde3 = models.CharField(max_length=256)
    cde4 = models.CharField(max_length=256)
    cde5 = models.CharField(max_length=256)
    cde6 = models.CharField(max_length=256)
    cde7 = models.CharField(max_length=256)
    cde8 = models.CharField(max_length=256)
    cde9 = models.CharField(max_length=256)


class CPU(models.Model):
    jugador = models.OneToOneField(Jugador,
                               on_delete=models.CASCADE,
                               primary_key=True,
                               db_column="jugador",
                               verbose_name="Jugador a quien pertenecen las CPU")
    cpu0 = models.CharField(max_length=256)
    cpu1 = models.CharField(max_length=256)
    cpu2 = models.CharField(max_length=256)
    cpu3 = models.CharField(max_length=256)
    cpu4 = models.CharField(max_length=256)
    cpu5 = models.CharField(max_length=256)
    cpu6 = models.CharField(max_length=256)
    cpu7 = models.CharField(max_length=256)
    cpu8 = models.CharField(max_length=256)
    cpu9 = models.CharField(max_length=256)


class Vector_Caracteristicas(models.Model):
    jugador = models.ForeignKey(Jugador,
                                on_delete=models.SET_NULL,
                                related_name='vectores_caracteristicas',
                                db_column='jugador',
                                verbose_name='Jugador al que pertenece este vector de caracteristicas',
                                null=True 
                                )
    juego = models.ForeignKey(Juego,
                              on_delete=models.CASCADE,
                              to_field='id_juego',
                              related_name='caracteristicas',
                              db_column='juego',
                              verbose_name='Juego al que pertenece la opinion',
                              )
    cpus = models.CharField(max_length=100)
    cdes = models.CharField(max_length=100)
