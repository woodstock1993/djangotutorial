import pytest
from model_bakery import baker
from users.models import User

pytest = pytest.mark.unit

# create and don't save
baker.prepare(User)