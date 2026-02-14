import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# Исправлено: корректное преобразование строки из .env в булево значение
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'django_filters',

    'apps.main',
    'apps.price',
    'apps.car',
    'apps.location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'), 
        'PORT': os.getenv('DB_PORT'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

JAZZMIN_SETTINGS = {
    "site_title": "Rent Car Admin",
 
    "site_header": "Аренда Автомобилей",
    
    "site_brand": "RentCar Dashboard",

    "welcome_sign": "Добро пожаловать в систему управления прокатом",

    "copyright": "Rent Car Ltd",

    "search_model": ["auth.User", "your_app.Car"], 
}

JAZZMIN_SETTINGS = {
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
    
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # Иконки для разделов (используйте Font Awesome 5)
    "icons": {
        # Раздел CAR
        "car.CarWashOption": "fas fa-shower",
        "car.BookCar": "fas fa-calendar-check",
        "car.UserModel": "fas fa-user-tag",
        "car.ImgCar": "fas fa-images",
        "car.Car": "fas fa-car",

        # Раздел LOCATION
        "location.BaseLocation": "fas fa-map-marked-alt",
        "location.ImgLocation": "fas fa-camera-retro",
        "location.Location": "fas fa-star",
        "location.Characteristic": "fas fa-list-ul",

        # Раздел MAIN
        "main.Banner": "fas fa-ad",
        "main.Comment": "fas fa-comments",

        # Раздел PRICE
        "price.ExtraService": "fas fa-plus-circle",
        "price.Season": "fas fa-cloud-sun",
        "price.PricingPlan": "fas fa-money-check-alt",
        
        # Системные
        "auth.User": "fas fa-users",
        "auth.Group": "fas fa-user-shield",
    },
}

JAZZMIN_UI_TWEAKS = {    
    "theme": "flatly", 
    "dark_mode_theme": "darkly",
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10,
}