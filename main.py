from flask import Flask, render_template, jsonify, request
from database import engine, text, load_new_service_request_to_db, get_customer_details_from_db

app = Flask(__name__)

####### DB CONNECTIONS ######
def load_data_from_db(query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        results = []
        for row in result.all():
            results.append(row._asdict())
            # result_dicts.append(dict(row._mapping))
        return results

def get_plans():
    return load_data_from_db("select * from plans")
def get_customers():
    return load_data_from_db("select * from customers")

def get_subscriptions(c_id):
    return load_data_from_db("select *\
                             from plans\
                             INNER JOIN subscriptions\
                             ON subscriptions.plan_id = plans.plan_id\
                             where subscriptions.customer_id=1;")
def get_service_request():
    return load_data_from_db("select * from servicerequests;")

####### DB CONNECTIONS ENDS######


####### Populate HOME PAGE STARTS######
@app.route("/", methods=['get'])
def home():
    plans = get_plans()
    customers = get_customers()
    subscriptions = get_subscriptions(1)
    service_requests = get_service_request()
    return render_template('home.html', plans=plans, customers=customers, subscriptions=subscriptions,service_requests=service_requests)
    # return render_template('home.html', plans=plans, customers=customers, subscriptions=subscriptions)

####### Populate HOME PAGE ENDS######

@app.route("/Pricing")
def list_plans():
    plans = get_plans()
    return render_template('planitems.html', plan=plans)
####### Populate PLANS ENDS STARTS######

# login #
@app.route("/login", methods=['post', 'get'])
def login():
    if request.method == 'post' or request.method == 'get':
        return jsonify(request.args)
    return render_template('login.html')

# sign up #
@app.route("/signup", methods=['post', 'get'])
def signup():
    if request.method == 'get':
        data = request.form
        return jsonify(data)
        load_new_customer_into_db(data)
        return render_template('login.html')
    return render_template('signup.html')

# raise service request #
@app.route("/new/request", methods=['post', 'get'])
def create_new_request():
    return render_template('raiseservicerequest.html')

#New Service Reqeuest Form Data#
@app.route("/new/request/raise", methods=['post', 'get'])
def add_service_request_to_db():
    # data = request.form
    # return jsonify(data)
    # print("DATA:",data)
    data = {}
    data['description'] = 'Internet Issue'
    request_number = load_new_service_request_to_db(data)
    # print(request_number)
    plans = get_plans()
    customers = get_customers()
    subscriptions = get_subscriptions(1)
    service_requests = get_service_request()
    return render_template('home.html', plans=plans, customers=customers, subscriptions=subscriptions,
                           service_requests=service_requests)

###### MAIN FUNCTION########
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)