"""
This module is for running a central server. To use it, run kalite with
--settings=kalite.project.settings.central_server or set then environment
variable DJANGO_SETTINGS_MODULE to 'kalite.project.settings.central_server'.
"""
from .base import *  # @UnusedWildImport

# Used to have two very different use cases in the same codebase :)
CENTRAL_SERVER = True


# DO NOT EDIT THIS FILE; it is generated from an Ansible template, and changes should be made via Ansible
# -------------------------------

# overwrite the above defaults with the actual values
from local_settings_secrets import *

# these are defaults, in case one of these isn't defined in local_settings_secrets.py
SECRET_KEY = "not so secret, this one"
POSTMARK_API_KEY = "Q?"
DATABASE_PASSWORD = ""
# TEMP: until we fix securesync counters, just send models down as one huge batch
SYNCING_MAX_RECORDS_PER_REQUEST = 100000
POSTMARK_SENDER = "kalite@learningequality.org"
POSTMARK_TEST_MODE = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "{{ ka_lite_central_db_name }}",
        "USER": "{{ ka_lite_central_db_user }}",
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": "{{ db_server_host }}",
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.file"
CENTRAL_WIKI_URL = "https://learningequality.org/ka-lite/user-guides/"
KA_CROWDIN_PROJECT_ID = "khanacademy"
CROWDIN_PROJECT_ID = "ka-lite"