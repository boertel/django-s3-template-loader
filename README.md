# django-s3-template-loader

## Install

with pipenv:
```bash
pipenv install "git+https://github.com/boertel/django-s3-template-loader/#egg=s3_template_loader"
```

## Configure

1. Add the app to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
  ...
  "s3_template_loader",
  ...
]
```

2. Add the template engine definition to `TEMPLATES`

```python
TEMPLATES = [
  { ... },
  s3_template_loader.get_template_engine()
 
]
```

3. Define `S3_TEMPLATE_LOADER_BUILD_DIRECTORY`

```python
S3_TEMPLATE_LOADER_BUILD_DIRECTORY = os.getenv("COMMIT", default="build")
```
