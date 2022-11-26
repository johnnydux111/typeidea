from .base import *  #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
<<<<<<< HEAD
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
=======
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
>>>>>>> 53a92949223925654b03eac16d9fe897eaba6e66
    }
}