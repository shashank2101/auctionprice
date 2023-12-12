

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

c1=100
h1=20000
a1=40000
ipl=1322433
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    category = data.get('category', 'General')
    result = perform_prediction(category)

    return jsonify({'result': result})

def perform_prediction(category):
    if category == 'Cars':
        return f"{c1} -predicted car price"
    elif category == 'Houses':
        return f'{h1} -Predicted outcome for Houses'
    elif category == 'Arts':
        return f'{a1} -Predicted outcome for Arts'
    elif category == 'IPL Players':
        return f'{ipl} -Predicted outcome for IPL Players'
    else:
        return 'General prediction outcome'
def model():

    print("build your model in a different python file and import the predict fucntion in this file and simple use the predict(input_data) and return that value like above")

if __name__ == '__main__':
    app.run(debug=True)
