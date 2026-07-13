from . import customers, pets, groomers, grooming_services, appointments
from . import payments, reviews, schedules, grooming_notes

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    pets.Base.metadata.create_all(engine)
    groomers.Base.metadata.create_all(engine)
    grooming_services.Base.metadata.create_all(engine)
    appointments.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)
    schedules.Base.metadata.create_all(engine)
    grooming_notes.Base.metadata.create_all(engine)
