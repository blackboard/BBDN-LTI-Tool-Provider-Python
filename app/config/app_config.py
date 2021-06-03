from decouple import config

PORT = config('PORT', default='5000')
DOMAIN = config('DOMAIN', default='localhost')
SERVER_NAME = DOMAIN + ':' + PORT
FRONTEND_URL = config('FRONTEND_URL', default="http://localhost:3000")
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': config('CACHE_DEFAULT_TIMEOUT', default=300, cast=int),
    'CACHE_REDIS_HOST': config('REDIS_HOST', default='localhost'),
    'CACHE_REDIS_PORT': config('REDIS_PORT', default=6379, cast=int),
    'CACHE_REDIS_URL': config('REDIS_URL', default='redis://localhost:6379/5')
}

AWS_KEY_ID = config('AWS_KEY_ID', default='')
AWS_KEY_ID_SECRET = config('AWS_KEY_ID_SECRET', default='')