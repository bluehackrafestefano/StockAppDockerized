from .base import *

ENV_NAME = config("ENV_NAME")

if ENV_NAME == 'DEV':
    from .dev import *
elif ENV_NAME == 'PROD':
    from .prod import *
