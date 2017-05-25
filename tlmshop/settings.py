"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _
from cmsplugin_cascade.utils import format_lazy
from django.core.urlresolvers import reverse_lazy
from decimal import Decimal

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y&+f+)tw5sqkcy$@vwh8cy%y^9lwytqtn*y=lv7f9t39b(cufx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID = 1
APP_LABEL = 'tlmshop'

# Enable this to additionally show the debug toolbar
INTERNAL_IPS = ['localhost', '127.0.0.1', '192.168.1.69']

# Root directory for this django project
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))
# Directory where working files, such as media and databases are kept
WORK_DIR = os.environ.get('DJANGO_WORKDIR', os.path.abspath(os.path.join(PROJECT_ROOT, 'LegionMarket')))
if not os.path.exists(WORK_DIR):
    os.makedirs(WORK_DIR)

# Application definition
DJANGO_APPS_JET = (
    # todo: Fix bug in jet does not all for adding new page when clicked on from create page on start
    # 'jet_ole.dashboard',
    # 'jet_ole',
    'jet.dashboard',
    'jet',

)
DJANGO_APPS_ADMIN_INTERFACE = (
    # todo: Fix bug in jet does not all for adding new page when clicked on from create page on start
    'admin_interface',
    'flat_responsive',
    'colorfield',

)
DJANGO_APPS_MATERIAL = (
    # material apps
    'material',
    # 'material.frontend',
    'material.admin',

)
DJANGO_APPS = (
    # djangocms_admin_style needs to be before django.contrib.admin!
    # https://django-cms.readthedocs.org/en/develop/how_to/install.html#configuring-your-project-for-django-cms
    'djangocms_admin_style',
    'django.contrib.admin',

    # django defaults
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

)
DJANGO_CMS = (
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    # 'reversion',
    # requirements for django-filer
    'filer',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'mptt',
    # core addons
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_audio',

)
DJANGO_CMS_ADDONS = (
    # Cassaade
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.segmentation',

)

THIRD_PARTY_APPS = (
    'embed_video',
    'crispy_forms',
)
SHOP = (
    'django_select2',
    'cms_bootstrap3',
    'adminsortable2',
    'django_fsm',
    'fsm_admin',
    'djng',
    'compressor',
    'sass_processor',
    'django_filters',
    'post_office',
    'haystack',
    'shop',
    'shop_stripe',
)
SHOP_TOO = (
    'email_auth',
    'polymorphic',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

)
LOCAL_APPS = (
    'video_back',
    'videojs',
    # 'background',
    'tlmshop',
)
DEV_APP = (
    'django.contrib.flatpages',
    'django.contrib.redirects',
)

INSTALLED_APPS = DJANGO_APPS_ADMIN_INTERFACE + DJANGO_APPS + SHOP_TOO + \
                 DJANGO_CMS + DJANGO_CMS_ADDONS + THIRD_PARTY_APPS + \
                 LOCAL_APPS + SHOP
#######
# DJANGO_APPS_JET + \
# DJANGO_APPS_MATERIAL + \
# DJANGO_APPS_ADMIN_INTERFACE + \
##
MIDDLEWARE_CLASSES = (
    'djng.middleware.AngularUrlMiddleware',
    # its recommended to place this as high as possible to enable apphooks
    # to reload the page without loading unnecessary middlewaresfuschiaatinuma
    'cms.middleware.utils.ApphookReloadMiddleware',
    # django defaults
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shop.middleware.CustomerMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django CMS additions
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

)

ROOT_URLCONF = 'tlmshop.urls'

WSGI_APPLICATION = 'tlmshop.wsgi.application'


# Templates
# https://docs.djangoproject.com/en/1.8/ref/settings/#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # django CMS additions
                'cms.context_processors.cms_settings',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # additional context processors for local development
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                # django CMS additions
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
                # Shop
                'shop.context_processors.customer',
                'shop.context_processors.ng_model_options',
                'shop_stripe.context_processors.public_keys',

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                # django CMS additions
                'django.template.loaders.eggs.Loader',
            ],
            'debug': DEBUG,
        },
    },
]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# we use os.getenv to be able to override the default database settings for the docker setup

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WORK_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/New_York'

USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(WORK_DIR, 'static')
STATIC_URL = '/static/'
# print(STATIC_ROOT)
# we need to add additional configuration for filer etc.
MEDIA_ROOT = os.path.join(WORK_DIR, 'media')
MEDIA_URL = '/media/'

# Checking to see if directories are there
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

STATICFILES_FINDERS = [
    # 'tlmshop.finders.FileSystemFinder',  # or
    # 'tlmshop.finders.AppDirectoriesFinder',  # or
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
]
# we need to add additional configuration for filer etc.
NODE = os.path.join(PROJECT_ROOT, 'node_modules')
if not os.path.exists(NODE):
    os.makedirs(NODE)

STATICFILES_DIRS = [
    ('static', os.path.join(PROJECT_ROOT, 'static')),
    ('node_modules', os.path.join(PROJECT_ROOT, 'node_modules')),
    ('templates', os.path.join(PROJECT_ROOT, 'templates')),
]
# print(STATICFILES_DIRS)
NODE_MODULES_URL = STATIC_URL + 'node_modules/'
# print(STATICFILES_DIRS)

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_ROOT, 'node_modules'),
]
# print(SASS_PROCESSOR_INCLUDE_DIRS)
COERCE_DECIMAL_TO_STRING = True

FSM_ADMIN_FORCE_PERMIT = True

ROBOTS_META_TAGS = ('noindex', 'nofollow')
# django CMS settings
# http://docs.django-cms.org/en/latest/
# #########################################

# Static Templates Files


CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {

}

CMS_PAGE_WIZARD_CONTENT_PLACEHOLDER = 'content'


# django CMS internationalization
# http://docs.django-cms.org/en/latest/topics/i18n.html

# LANGUAGES = (
#     ('en', _('English')),
# )

# django CMS templates
# http://docs.django-cms.org/en/latest/how_to/templates.html

CMS_TEMPLATES = (
    ('content.html', 'Content'),
    ('t458_lavish/index.html', 'TLM-Lavish')
)

# CUSTOM

# Filer
THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# CKEditor
# DOCS: https://github.com/divio/djangocms-text-ckeditor
# CKEDITOR_SETTINGS = {
#     'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js',
#     'contentsCss': ['/static/css/base.css'],
# }

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texticon_wysiwig_config')),
}

CKEDITOR_SETTINGS_CAPTION = {
    'language': '{{ language }}',
    'skin': 'moono',
    'height': 70,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['Source']
    ],
}

CKEDITOR_SETTINGS_DESCRIPTION = {
    'language': '{{ language }}',
    'skin': 'moono',
    'height': 250,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
}
SELECT2_CSS = 'node_modules/select2/dist/css/select2.min.css'
SELECT2_JS = 'node_modules/select2/dist/js/select2.min.js'
# Embed Video
APPEND_SLASH = True

###################################################################################
#
# Shop Settings
#
###################################################################################

SHOP_APP_LABEL = 'tlmshop'
AUTH_USER_MODEL = 'email_auth.User'
SHOP_TYPE = 'smartcard'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
MIGRATION_MODULES = {
    'tlmshop': 'tlmshop.migrations.{}'.format(SHOP_TYPE)
}


############################################
# settings for sending mail

EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@example.com'
EMAIL_HOST_PASSWORD = 'smtp-secret-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'My Shop <no-reply@example.com>'
EMAIL_REPLY_TO = 'info@example.com'
EMAIL_BACKEND = 'post_office.EmailBackend'


############################################
# settings for third party Django apps

SERIALIZATION_MODULES = {'json': str('shop.money.serializers')}

############################################
# settings for django-restframework and plugins

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'shop.rest.money.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # can be disabled for production environments
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #   'rest_framework.authentication.TokenAuthentication',
    # ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}


############################################
# settings for storing session data

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_SAVE_EVERY_REQUEST = True

###########################################################
# Files

SHOP_TYPE = 'smartcard'
#  'commodity', 'i18n_commodity', 'smartcard', 'i18n_smartcard', 'i18n_polymorphic', 'polymorphic'



##############################################################
#
#

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'post_office': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

SILENCED_SYSTEM_CHECKS = ['auth.W004']

FIXTURE_DIRS = [os.path.join(WORK_DIR, SHOP_TYPE, 'fixtures')]

############################################
# settings for django-cms and its plugins

CMS_CACHE_DURATIONS = {
    'content': 600,
    'menus': 3600,
    'permissions': 86400,
}

cascade_workarea_glossary = {
    'breakpoints': ['xs', 'sm', 'md', 'lg'],
    'container_max_widths': {'xs': 750, 'sm': 750, 'md': 970, 'lg': 1170},
    'fluid': True,
    'media_queries': {
        'xs': ['(max-width: 768px)'],
        'sm': ['(min-width: 768px)', '(max-width: 992px)'],
        'md': ['(min-width: 992px)', '(max-width: 1200px)'],
        'lg': ['(min-width: 1200px)'],
    },
}


CMSPLUGIN_CASCADE_PLUGINS = [
    'cmsplugin_cascade.segmentation',
    'cmsplugin_cascade.generic',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.link',
    'shop.cascade',
    'cmsplugin_cascade.bootstrap3',
]

CMSPLUGIN_CASCADE = {
    'link_plugin_classes': [
        'shop.cascade.plugin_base.CatalogLinkPluginBase',
        'cmsplugin_cascade.link.plugin_base.LinkElementMixin',
        'shop.cascade.plugin_base.CatalogLinkForm',
    ],
    'alien_plugins': ['TextPlugin', 'TextLinkPlugin', 'AcceptConditionPlugin'],
    'bootstrap3': {
        'template_basedir': 'angular-ui',
    },
    'plugins_with_extra_render_templates': {
        'CustomSnippetPlugin': [
            ('shop/catalog/product-heading.html', _("Product Heading")),
            ('tlmshop/catalog/manufacturer-filter.html', _("Manufacturer Filter")),
        ],
    },
    'plugins_with_sharables': {
        'BootstrapImagePlugin': ['image_shapes', 'image_width_responsive', 'image_width_fixed',
                                 'image_height', 'resize_options'],
        'BootstrapPicturePlugin': ['image_shapes', 'responsive_heights', 'image_size', 'resize_options'],
    },
    'bookmark_prefix': '/',
    'segmentation_mixins': [
        ('shop.cascade.segmentation.EmulateCustomerModelMixin', 'shop.cascade.segmentation.EmulateCustomerAdminMixin'),
    ],
    'allow_plugin_hiding': True,
}


#############################################
# settings for full index text search (Haystack)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'tlmshop-{}-en'.format(SHOP_TYPE),
    },
}
if USE_I18N:
    HAYSTACK_CONNECTIONS['de'] = {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'tlmshop-{}-de'.format(SHOP_TYPE),
    }

HAYSTACK_ROUTERS = [
    'shop.search.routers.LanguageRouter',
]

#####################################################################################3

############################################
# settings for django-shop and its plugins

SHOP_VALUE_ADDED_TAX = Decimal(19)
SHOP_DEFAULT_CURRENCY = 'USD'
SHOP_PRODUCT_SUMMARY_SERIALIZER = 'tlmshop.serializers.ProductSummarySerializer'
if SHOP_TYPE in ['i18n_polymorphic', 'polymorphic']:
    SHOP_CART_MODIFIERS = ['tlmshop.polymorphic_modifiers.tlmshopCartModifier']
else:
    SHOP_CART_MODIFIERS = ['shop.modifiers.defaults.DefaultCartModifier']
SHOP_CART_MODIFIERS.extend([
    'shop.modifiers.taxes.CartExcludedTaxModifier',
    'tlmshop.modifiers.PostalShippingModifier',
    'tlmshop.modifiers.CustomerPickupModifier',
    'shop.modifiers.defaults.PayInAdvanceModifier',
])

if 'shop_stripe' in INSTALLED_APPS:
    SHOP_CART_MODIFIERS.append('tlmshop.modifiers.StripePaymentModifier')

SHOP_EDITCART_NG_MODEL_OPTIONS = "{updateOn: 'default blur', debounce: {'default': 2500, 'blur': 0}}"

SHOP_ORDER_WORKFLOWS = [
    'shop.payment.defaults.PayInAdvanceWorkflowMixin',
    'shop.payment.defaults.CancelOrderWorkflowMixin',
    'shop_stripe.payment.OrderWorkflowMixin',
]
if SHOP_TYPE in ['i18n_polymorphic', 'polymorphic']:
    SHOP_ORDER_WORKFLOWS.append('shop.shipping.delivery.PartialDeliveryWorkflowMixin')
else:
    SHOP_ORDER_WORKFLOWS.append('shop.shipping.defaults.CommissionGoodsWorkflowMixin')

SHOP_STRIPE = {
    'PUBKEY': 'pk_test_HlEp5oZyPonE21svenqowhXp',
    'APIKEY': 'sk_test_xUdHLeFasmOUDvmke4DHGRDP',
    'PURCHASE_DESCRIPTION': _("Thanks for purchasing at tlmshop"),
}

try:
    from .private_settings import *  # NOQA
except ImportError:
    pass

