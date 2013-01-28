__author__ = 'ferdous'
import celery
from celery.task import PeriodicTask
from datetime import timedelta, datetime
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery.task
class AlbumTask(PeriodicTask):
    """
        A periodic task that import photos from facebook
    """
    run_every = timedelta(minutes=100)
    TODAY = datetime.now()
    name = "photomatic.tasks.AlbumTask"

    def run(self, **kwargs):
        logger.info("Running fb album periodic task.")
        return True


