from flask import Flask, render_template, jsonify
from database import engine, text

app = Flask(__name__)

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

@app.route("/")
def home():
    # return "Hello, World!"
    plans = get_plans()
    customers = get_customers()
    subscriptions = get_subscriptions(1)
    return render_template('home.html', plans=plans, customers=customers, subscriptions=subscriptions)

@app.route("/api/plans")
def list_plans():
    # return "Hello, World!"
    return jsonify(PLANS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)