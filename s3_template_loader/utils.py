__all__ = ['get_template_engine']

def get_template_engine():
  return {
      "BACKEND": "django.template.backends.django.DjangoTemplates",
      "NAME": "s3",
      "DIRS": [],
      "APP_DIRS": False,
      "OPTIONS": {
          "loaders": [
              (
                  "django.template.loaders.cached.Loader",
                  ["s3_template_loader.loaders.S3TemplateLoader"],
              )
          ],
          "context_processors": [
              "django.template.context_processors.debug",
              "django.template.context_processors.request",
              "django.contrib.auth.context_processors.auth",
              "django.contrib.messages.context_processors.messages",
          ],
      },
    }
