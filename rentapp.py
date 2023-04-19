
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

pickle_in = open('modelmodel2.pkl', 'rb')
clf = pickle.load(pickle_in)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

def make_prediction(bhk, Bathroom, Size, City):
    city_enc = -1
    if City == 'Mumbai':
        city_enc = 5
    elif City == 'Chennai':
        city_enc = 1
    elif City == 'Bangalore':
        city_enc = 0
    elif City == 'Hyderabad':
        city_enc = 3
    elif City == 'Delhi':
        city_enc = 2
    elif City == 'Kolkata':
        city_enc = 4

    prediction = clf.predict([[bhk, Bathroom, Size, city_enc]])[0]
    return prediction

@app.route('/predict',methods=['POST'])
def predict():
    bhk = request.form['bhk']
    Bathroom = request.form['Bathroom']
    Size = request.form['Size']
    City = request.form['City']

    prediction = make_prediction(bhk, Bathroom, Size, City)

    #print(prediction)

    #return render_template('home.html', prediction_text='The price is most likely: {}'.format(prediction))
    return render_template('home.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
