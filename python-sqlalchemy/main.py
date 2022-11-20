from models import Customer
from database import db_session

if __name__ == '__main__':
    criar_customer = Customer("testes", "insert", "testes@test.com")
    db_session.add(criar_customer)
    db_session.commit()

    customers = Customer.query.all()
    customer_by_name = Customer.query.filter_by(first_name='testes').first()
    for c in customers:
        print(c.to_json())
    print(customer_by_name.to_json())

