import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings') # setting up my environment variable

import django #la 7atta e7ki ma3 el database.
django.setup()
# ayya script beddi e3emlou bdi e3mel setting lal django


from app_two.models import CustomUser

from faker import Faker

fake = Faker()

def populate_user(number_of_users):
    for i in range (number_of_users):
        fake_name = fake.name()
        #fake_email = fake.email()
        user = CustomUser.objects.get_or_create(
            first_name = fake_name.split()[0],
            last_name = fake_name.split()[1],
            email = fake_name.split()[0] + "." + fake_name.split()[1] + "@gmail.com"
        )[0]
    user.save()

if __name__ == "__main__":
    populate_user(100)