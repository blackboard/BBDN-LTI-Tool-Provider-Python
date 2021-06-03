from decouple import config

PORT = '5555'
DOMAIN = 'localhost'
SERVER_NAME = DOMAIN + ':' + PORT
FRONTEND_URL = "http://localhost:3000"
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_URL': 'redis://localhost:6379/5'
}

AWS_KEY_ID = config('AWS_KEY_ID', default='')
AWS_KEY_ID_SECRET = config('AWS_KEY_ID_SECRET', default='')
