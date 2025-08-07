
from django import template
from django.utils.html import format_html
from django.templatetags.static import static
from django.conf import settings

import os

register = template.Library()

@register.simple_tag
def icon(name, **kwargs):
    url = static(f"icons/{name}.svg")
    width = kwargs.get('width', 14)
    height = kwargs.get("height", 14)
    svg_path = os.path.join(settings.BASE_DIR, 'blog_app', 'static', 'icons', f'{name}.svg')
    try:
        with open(svg_path, 'r') as svg_file:
            svg = svg_file.read()
            # Optionally add width/height or class here
            return format_html(f"<span class='icon-holder'>{svg}</span>")
    except FileNotFoundError:
        return ''
    
    # return format_html(f"""
    #     <img 
    #         width='{width}'
    #         height='{height}'
    #         class='logo'
    #         src='{url}'
    #         alt='{name} icon' />
    # """)