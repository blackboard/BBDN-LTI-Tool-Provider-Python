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