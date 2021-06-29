# Universal LTI Tool - Backend

This LTI Tool should provide the capability to test all the LTI services provided by an LMS, allowing to review anc
control the items that are sent between components

## HOW TO

### Install

```
python -m venv <path to project>/BBDN-LTI-Tool-Provider-Python/venv

pip install -r pip-requirements.txt
```

### Setup
```
source venv/bin/activate

export PYTHONPATH='<path to project>/BBDN-LTI-Tool-Provider-Python/app'
```

### Run

```
python app.py
```

### Configuration

If you want to modify your configuration it's best to create a `.env` file. These are the possible values you can change:

```
PORT='5000'
DOMAIN='localhost'
FRONTEND_URL='http://localhost:3000'
CACHE_DEFAULT_TIMEOUT=300
REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_URL='redis://localhost:6379/5'
AWS_KEY_ID = 'whatever'
AWS_KEY_ID_SECRET = 'key'
```

### Docker

To build the docker image run the following command on the root folder

```
docker build . -f docker/Dockerfile -t ltitool-python 
```

### Key Generation

This project generates keys dynamically. If using Docker, this process happens at build time. If you are running locally without Docker, you will need to perform this step before you can run the application from the root level of the project:

```
python app/config/keys/build_config.py
```

This will generate private.key, public.key, and public.jwk.json.
