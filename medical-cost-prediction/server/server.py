from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_region')
def get_region():
    response = jsonify({
        'region':util.get_region()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_medical_charge',methods=['POST'])
def predict_medical_charge():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bmi = int(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = request.form['region']

    response = jsonify({
        'estimated_price':util.get_estimatied_price(region,age,sex,bmi,children,smoker)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    """在服务器上运行app"""
    print('Starting Python Flask Sever For Medical Cost Prediction')
    util.load_save_artifacts()
    app.run()

