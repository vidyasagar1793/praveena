from flask import Flask , render_template , jsonify ,request
from chat import get_response
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict",methods=['POST','GET'])
def predict():
    data = request.form.get('data')
    response = get_response(data)
    return jsonify({'success':True, 'chat':response})

if __name__ == "__main__":
    app.run(debug=True)