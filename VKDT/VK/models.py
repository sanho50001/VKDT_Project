from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def file_vk_directory_path(instance: 'VK', filename: str) -> str:
    """Фукнция директории превью пользователя
    возвращает айди профиля и имя файла

    """
    return 'VK/post_{pk}/file_post/{filename}'.format(
        pk=instance.pk,
        filename=filename
    )


class VK(models.Model):
    """Модель Вконтакте"""
    text = models.TextField(max_length=500, blank=True, verbose_name=_('text'))
    post_id = models.CharField(max_length=500, blank=True, unique=True,  verbose_name=_('post_id'))
    file_post = models.FileField(null=True, blank=True, upload_to=file_vk_directory_path, verbose_name=_('file post'))
    post_image_url = models.CharField(max_length=500, blank=True, verbose_name=_('post image url'))
    created = models.DateField(
        auto_now_add=True, verbose_name=_("data created")
    )
    slug = models.SlugField(
        max_length=100,
        null=False,
        blank=True,
        verbose_name="URL post",
    )

    class Meta:
        verbose_name = _('VK')
        verbose_name_plural = _('VK')

    def __str__(self):
        return str(self.post_id) + ' Post ' + str(self.created)

