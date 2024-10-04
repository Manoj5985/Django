import threading
import django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now

# Signal handler
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()} for user: {instance.username} at {now()}")

# Function to trigger the signal
def create_user():
    print(f"Main code running in thread: {threading.get_ident()} at {now()}")
    user = User.objects.create(username="test_user")

if __name__ == '__main__':
    django.setup()  # Set up Django before running the signal
    create_user()
