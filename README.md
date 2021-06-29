# Universal LTI Tool - Backend

This LTI Tool should provide the capability to test all the LTI services provided by an LMS, allowing to review anc
control the items that are sent between components

## HOW TO

### Install

```
pip install -r pip-requirements
```

### Run

```
npm start
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