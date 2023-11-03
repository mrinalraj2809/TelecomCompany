from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()
db_connection_string = os.getenv("DB_CONNECTION_STRING")
engine = create_engine(
     db_connection_string,
     connect_args={
          "ssl": {
             "ssl_ca": "/etc/ssl/cert.pem"
     }
})
print(db_connection_string)
def load_new_service_request_to_db(data):
    now = datetime.now()
    print(now)
    # print(data['description'])

    with engine.connect() as conn:
        query = text(f"INSERT INTO servicerequests(customer_id, issue_description, issue_date, issue_status, assigned_technician) \
                     VALUES(1,'{data['description']}', '{now}', 'ACTIVE', 'BOT')")

        conn.execute(query)

        new_request_query = text("select request_id from servicerequests where customer_id=1;")

        result = conn.execute(new_request_query)
        request_number = []
        for row in result.all():
            request_number.append(row)
        return request_number

def get_customer_details_from_db(phone):
    with engine.connect() as conn:
        query = text(f"SELECT * from customers where phone={phone};")
        result = conn.execute(query)
        customers = []
        for customer in result.all():
            customers.append(customer)
        return customers