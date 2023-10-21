from flask import Flask, render_template, jsonify

app = Flask(__name__)

PLANS = [
    {
        'plan_id': 1,
        'plan_name': "Rs 2479, Full Talk Time,365 days",
        'download_speed': '300 MBPS',
        'upload_speed': '300 MBPS',
        'price': 'Rs 2479.00',
        'validity': '365 days'
    },
    {
        'plan_id': 2,
        'plan_name': "Rs 1479, Full Talk Time,65 days",
        'download_speed': '200 MBPS',
        'upload_speed': '200 MBPS',
        'price': 'Rs 1479.00',
        'validity': '65 days'
    },
    {
        'plan_id': 3,
        'plan_name': "Rs 479, Full Talk Time,6 days",
        'download_speed': '100 MBPS',
        'upload_speed': '100 MBPS',
        'price': 'Rs 479.00',
        'validity': '6 days'
    },
    {
        'plan_id': 4,
        'plan_name': "Rs 79, Full Talk Time,5 days",
        'download_speed': '30 MBPS',
        'upload_speed': '30 MBPS',
        'price': 'Rs 79.00',
        'validity': '5 days'
    },
    {
        'plan_id': 5,
        'plan_name': "Rs 9, Full Talk Time,3 days",
        'download_speed': '3 MBPS',
        'upload_speed': '3 MBPS',
        'price': 'Rs 9.00',
        'validity': '3 days'
    }

]
@app.route("/")
def hello():
    # return "Hello, World!"
    return render_template('home.html', plans=PLANS)

@app.route("/api/plans")
def list_plans():
    # return "Hello, World!"
    return jsonify(PLANS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)