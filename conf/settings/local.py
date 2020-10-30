"""
Local settings
"""
# pylint: disable=wildcard-import, relative-beyond-top-level, undefined-variable, unused-wildcard-import
import os
from .base import *

ENV = 'local'
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'ax1_5(q67fmupoh_@nf^r$w^!g-+-1s72103ib^&#=-k0uh$i9')

# Wildcard for CORS config, remove it on Production settings
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']