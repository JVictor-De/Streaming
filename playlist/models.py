from django.db import models
from django.contrib.auth.models import User
from content_app.models import Content  # Assumindo que o modelo Content está no app 'content_app'

class Playlist(models.Model):
    title = models.CharField(max_length=255)  # Título da playlist
    description = models.TextField(blank=True, null=True)  # Descrição opcional da playlist
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')  # Proprietário da playlist
    contents = models.ManyToManyField(Content, related_name='playlists')  # Conteúdos incluídos na playlist
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data de última atualização

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.title