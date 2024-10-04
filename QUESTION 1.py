import time
import django
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.timezone import now

# Signal handler that introduces a delay
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username} at {now()}")
    time.sleep(5)  # Simulate a long task
    print("Signal handler finished execution.")

# Code to trigger the signal
def create_user():
    print(f"Start creating user at {now()}")
    user = User.objects.create(username="test_user")
    print(f"User creation finished at {now()}")

if __name__ == '__main__':
    django.setup()  # Set up Django before running the signal
    create_user()
