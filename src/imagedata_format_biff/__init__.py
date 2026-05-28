"""imagedata_format_biff"""

import logging
import mimetypes

logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
    from importlib.metadata import version
    __version__ = version('imagedata_format_biff')
except Exception:
    __version__ = None

__author__ = 'Erling Andersen, Haukeland University Hospital, Bergen, Norway'
__email__ = 'Erling.Andersen@Helse-Bergen.NO'

mimetypes.add_type('application/biff', '.biff')
mimetypes.add_type('application/biff', '.us')
mimetypes.add_type('application/biff', '.real')
