from flask import Flask,render_template,jsonify,request
import os
import pickle,json
import numpy as np


app = Flask(__name__)

def make_predict(sample):
   print(os.listdir('.'))
   print(os.getcwd())
   with open('iris_model.pkl', 'rb') as f:
       model = pickle.load(f)
       
   prediction = model.predict(sample)[0]
   
   labels={0:"setosa",1:"versicolor",2:"virginica"}

   return labels[prediction]
   
   
@app.route("/")
def hello():
   return render_template('home.html')

@app.route("/predict/",methods=['POST'])
def predict():

   data = request.json
   #d1 = json.loads(data)
   #print(d1)
   #print(data)
   t = data['test_data']
   #print(t)
   
   sample = np.array([t])
   pred = make_predict(sample)
   #print(pred)

   return jsonify({'response':pred})
   
   
   


if __name__ == "__main__":
   
   app.run(host='0.0.0.0', port="5000")
