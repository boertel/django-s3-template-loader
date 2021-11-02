from . import views
from . import loaders
from .utils import get_template_settings


__all__ = ['views', 'loaders', '__version__', 'get_template_settings']

__version__ = '0.1.8'

VERSION = __version__
