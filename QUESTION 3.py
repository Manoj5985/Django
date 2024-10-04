import django
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler to update user's email
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler running...")
    instance.email = "updated_email@example.com"
    instance.save()  # This will happen within the same transaction

# Function to trigger the signal
def create_user_with_rollback():
    try:
        with transaction.atomic():  # Open a transaction block
            user = User.objects.create(username="test_user")
            print(f"User created with username: {user.username}")
            # Force an exception to trigger rollback
            raise Exception("Simulating an error to rollback transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == '__main__':
    django.setup()
    create_user_with_rollback()

    # Check if user and email update are in the DB after rollback
    user_exists = User.objects.filter(username="test_user").exists()
    print(f"User exists after rollback: {user_exists}")
