from django.contrib import admin
from VK.models import VK
from django import forms


class VKAdminForm(forms.ModelForm):
    """Форма для модели VK"""
    class Meta:
        model = VK
        fields = "__all__"


@admin.register(VK)
class VKAdmin(admin.ModelAdmin):
    """Админ панель модель VK"""

    list_display = [
        "post_id"
    ]
    form = VKAdminForm
