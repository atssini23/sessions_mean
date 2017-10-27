from flask import Flask, redirect, render_template,request, session
app = Flask(__name__)

app.secret_key = "shhhhh"

def sumSessionsCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sumSessionsCounter()
    return render_template('index.html')

@app.route('/plus2buttom', methods=['POST'])
def returnindex():
    print request.form
    session['counter'] +=2
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def rest():
    print request.form
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
