from app.interface import db
from app.domain.models import Person

def is_real_person(email):
    person = db.session.query(Person).filter(Person.email == email).first()
    if person:
        return person.id

