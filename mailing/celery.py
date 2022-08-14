import os
import dotenv
from celery import Celery

env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')
dotenv.load_dotenv(env_file)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing.settings')

app = Celery('notification_service')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
