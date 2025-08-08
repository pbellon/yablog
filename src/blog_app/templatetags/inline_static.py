from django import template
from django.utils.html import format_html
from django.conf import settings

import os

register = template.Library()


@register.simple_tag
def icon(name):
    svg_path = os.path.join(
        settings.BASE_DIR, "blog_app", "static", "icons", f"{name}.svg"
    )
    try:
        with open(svg_path, "r") as svg_file:
            svg = svg_file.read()
            # Optionally add width/height or class here
            return format_html(f"<span class='icon-holder'>{svg}</span>")
    except FileNotFoundError:
        print(f"[ERROR] Could find {name} icon at {svg_path}")
        return ""


@register.simple_tag
def image(name):
    svg_path = os.path.join(
        settings.BASE_DIR, "blog_app", "static", "images", f"{name}.svg"
    )

    try:
        with open(svg_path, "r") as svg_file:
            svg = svg_file.read()
            # Optionally add width/height or class here
            return format_html(svg)
    except FileNotFoundError:
        print(f"[ERROR] Could find {name} icon at {svg_path}")
        return ""
