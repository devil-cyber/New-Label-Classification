from flask import Flask,request,jsonify
import sys
sys.path.insert(1,'../')
import predict
import time

app = Flask(__name__)

@app.route('/')
def home_route():
    return {'message':'This is an invalid route',
            'desc':'try route with /predict',
            'github':'devil-cyber'}

@app.route('/predict',methods=['GET','POST'])
def predict_route():
    try:
        if request.method == "GET":
            t1 = time.time()
            data = request.form['data']
            pred,label,prob = predict.predict([data])
            t2 = time.time()
            #print(pred,label)
            value = {'prediction_accuracy':prob,
                     'label':label,
                     'time_consume':str(t2-t1)+' sec ',
                     'status':200,
                     'author':'Manikant Kumar',
                     'github':'https://github.com/devil-cyber'
                     }
            return value
        else:
            return "invalid request"
    except Exception as e:
        print('error from the api as:',str(e))
        return str(e)



app.run(debug=True,host='0.0.0.0',port=8088)

