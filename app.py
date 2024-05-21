#from crypt import methods
#from distutils.log import debug
from operator import index
import pandas as pd
import numpy as np
from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

model=pickle.load(open('linear_model.pkl','rb'))
columns=pickle.load(open('columns.pkl','rb'))

@app.route('/')
def prediction():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])

def predict():
    data=request.form
    vector=np.zeros(246)
    location=data['location']
    print(location)
    location_list=columns.get('columns')[4:].tolist()
    print(location_list)
    location_index=location_list.index(location)
    vector[location_index]==1
    vector[0]=data['clean_size']
    vector[1]=data['bath']
    vector[2]=data['balcony']
    vector[3]=data['total_sqft_clean1']

    input=[vector]

    prediction = model.predict(input)
    return ('Your house estimate price is Rs.{} lakhs'.format(prediction))
























if __name__== "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
