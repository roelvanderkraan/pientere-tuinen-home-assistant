from datetime import timedelta

DOMAIN = "pientere_tuinen"
API_URL = "https://services.goodcitysense.nl/mijn-pientere-tuin/measurements"
API_HEADER_NAME = "gcs-api-key"

DEFAULT_UPDATE_INTERVAL = timedelta(minutes=60)
