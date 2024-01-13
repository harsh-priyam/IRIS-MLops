from flask import Flask, render_template, request
import os
import numpy as np
from IRIS_MLops.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Completed"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            sepal_length = float(request.form['sepal_length'])
            sepal_width = float(request.form['sepal_width'])
            petal_length = float(request.form['petal_length'])
            petal_width = float(request.form['petal_width'])

            data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
