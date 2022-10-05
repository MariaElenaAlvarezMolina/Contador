from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "keep it secret"

@app.route('/')
def index():
    if 'count' and 'visitas' in session:
        session['count'] += 1
        session['visitas'] += 1
    else:
        session['count'] = 0
        session['visitas'] = 0

    return render_template('index.html')

@app.route('/addtwo')
def addtwomore():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/addnumber', methods=['POST'])
def count_num():
    number = int(request.form['cantidad'])
    session['count'] += (number-1)
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)