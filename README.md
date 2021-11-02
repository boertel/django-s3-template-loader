# django-s3-template-loader

## Install

1. Add the app to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
  ...
  "s3_template_loader",
  ...
]
```

2. Add the template loader definitioin to `TEMPLATES`

```python
TEMPLATES = [
  { ... },
  s3_template_loader.TEMPLATE
 
]
```

3. Define `S3_TEMPLATE_LOADER_BUILD_DIRECTORY`

```python
S3_TEMPLATE_LOADER_BUILD_DIRECTORY = os.getenv("COMMIT", default="build")
```
