import json
import pickle as pk

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
model=pk.load(open('Churn_final.pkl','rb'))
scalar=pk.load(open('scaler_churn.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    
    if (predict==1):
            return render_template( "home.html", prediction_text= "Customer is churn")

    else: 
            return render_template('home.html', prediction_text='Customer is not churn')


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
   