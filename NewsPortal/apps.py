from django.apps import AppConfig
import redis


class NewsportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewsPortal'

red = redis.Redis(
    host='redis-12042.c253.us-central1-1.gce.cloud.redislabs.com',
    port='12042',
    password='wr17ygbcp0rptcTwFqUD10LnFPc5yyv5',

)