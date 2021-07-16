from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Nazwa restauracji', blank=False)
    describtion = models.TextField(blank=False, verbose_name = 'Opis restauracji')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Data utworzenia')
    update_date = models.DateTimeField(auto_now=True, verbose_name = 'Data ostatniej zmiany')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name = 'Zdjęcie')
    is_published = models.BooleanField(default=True, verbose_name = 'Opublikowana')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Restaurację'
        verbose_name_plural = 'Restauracje'
        ordering = ['-pub_date']
