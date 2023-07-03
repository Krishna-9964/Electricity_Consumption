from flask import Flask, request, jsonify
import util
import report
import lazy_predict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_State_names',  methods=['GET'])
def get_State_names():
    response = jsonify({
        'States': util.get_State_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# @app.route('/predict_electricity',methods=['GET', 'POST'])
# def predict_electricity():
#     Month = int(request.form['Month'])
#     Day = int(request.form['Day'])
#     print(Month)
#     State = request.form['State']

#     response = jsonify({
#         "estimated_usage": util.get_estimated_usage(State,Month,Day)
#     })

#     response.headers.add('Access-Control-Allow-Origin','*')
#     return response


@app.route('/predict_electricity_lazy_predict', methods=['GET', 'POST'])
def predict_electricity_lazy_predict():
    Month = int(request.form['Month'])
    Day = int(request.form['Day'])
    # print(Month)
    State = request.form['State']
    # print(State)
    response = jsonify({
        "estimated_usage": lazy_predict.predict_usage(State, Day, Month)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_state_usage',  methods=['GET', 'POST'])
def get_state_usage():
    result = util.state_usage()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_monthwise_report',  methods=['GET', 'POST'])
def get_monthwise_report():
    State = request.form['State']
    Year = request.form['Year']
    result = report.get_monthwise_report(State, Year)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_month_usage_details',  methods=['GET', 'POST'])
def get_month_usage_details():
    State = request.form['State']
    Month = request.form['Month']
    Year = request.form['Year']
    print(Month)
    result = report.get_month_usage_details(State, Month, Year)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting python flask eletricity consumption..")
    util.load_saved_artifacts()
    app.run()
