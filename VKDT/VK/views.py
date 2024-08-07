from django.shortcuts import render, redirect, get_object_or_404
from VK.tasks.post_tasks import upload_tasks
from VK.models import VK
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from VK.services import vkapi


class MainView(ListView):
    """Функция отображения Скидок"""
    model = VK

    template_name = "VK/index.jinja2"
    paginate_by = 6
    context_object_name = "vk"


def upload_task(request):
    upload_tasks.delay()
    # parser_main_page()

    return redirect("VK:main")


def create_model(request):
    vk_model_post = VK(text='',
                       post_id=vkapi.get_photo_id(),
                       file_post=vkapi.get_photo_name(),
                       post_image_url=f'')
    vk_model_post.save()

    return redirect("VK:main")
