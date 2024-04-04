from celery.schedules import crontab
from celery.task import periodic_task
import logging
from fauna.config.celery import app
from fauna.apps.vendors.gbif import client

logger = logging.getLogger(__name__)


@periodic_task(run_every=(crontab(hour='*')), name="load_data_naturalist")
def prueba_task():
    gbif = client.Gbif()
    gbif.set_data()
