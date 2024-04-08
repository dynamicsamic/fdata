import nest_asyncio
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

nest_asyncio.apply()


def environment(**options):
    options.update(enable_async=True)
    env = Environment(**options)
    env.globals.update({"static": static, "url": reverse})
    return env
