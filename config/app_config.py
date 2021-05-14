PORT = '5555'
DOMAIN = 'localhost'
SERVER_NAME = DOMAIN + ':' + PORT
FRONTEND_URL = "http://localhost:3001"
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_URL': 'redis://localhost:6379/5'
}
