"""
FILE TO HELP STYLE THE ADMIN CSS TO OUR LIKING
"""
from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """To add the static css to the the admin"""
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static("css/custom.css")
        # "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    )


@hooks.register("insert_global_admin_js", order=100)
def global_admin_js():
    """Add /static/css/custom.js to the admin."""
    return format_html(
        '<script src="{}"></script>',
        static("/js/custom.js")
    )
