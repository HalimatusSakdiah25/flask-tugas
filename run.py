from flask  import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/input')
def input_data():
    return render_template('input_data.html')

@app.route('/list')
def list_data():
    return render_template('list_data.html')
    
app.run()