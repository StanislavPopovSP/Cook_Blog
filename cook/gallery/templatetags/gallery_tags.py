from django import template
from gallery.models import *

register = template.Library()

@register.inclusion_tag('gallery/tags/gallery_tag.html')
def get_last_photos_in_gallery():
    """Включающий тег, забираем шесть последних фотографий"""
    photos = Photo.objects.filter(is_published=True).order_by()[:8]
    return {'photos': photos}


