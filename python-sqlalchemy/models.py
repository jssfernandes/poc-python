import database as db
import json


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    first_name = db.Column(db.String(140))
    last_name = db.Column(db.String(140))
    email = db.Column(db.String(140))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_json(self):
        return json.dumps(
            dict(
                id=self.id,
                first_name=self.first_name,
                last_name=self.last_name,
                email=self.email
            )
        )

    @property
    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


# event.listen(db_session, 'after_flush', search.update_model_based_indexes)
db.init_db()
