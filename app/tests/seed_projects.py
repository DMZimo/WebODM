# Creates 1000 test projects for the 'admin' user.
# Run with:
# docker cp app/tests/seed_projects.py webapp:/webodm/ && docker exec webapp bash -c "cd /webodm && /webodm/venv/bin/python seed_projects.py"

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webodm.settings")
django.setup()

from app.models import Project
from django.contrib.auth.models import User

user = User.objects.get(username="admin")
projects = [Project(owner=user, name="Test Project " + str(i)) for i in range(1, 1001)]
Project.objects.bulk_create(projects)
print("Done. 1000 test projects created.")
