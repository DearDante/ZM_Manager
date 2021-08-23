from flask import Flask, render_template, session, request, redirect, url_for
import pickle
import os

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #with open('db/managers.pickle')
        session['usertname'] = request.form['userid']
    return render_template('login.html')

@app.route('/register')
def regis():
    if request.method == 'POST':
        if not os.path.exists('db/managers.pickle'):
            data = {request.form['userid']: request.form['passwd']}
            pickle.dump(data, 'db/managers.pickle')
        else:
            data = pickle.load('db/managers.pickle')
            data[request.form['userid']] = request.form['passwd']
            pickle.dump(data, 'db/managers.pickle')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/main/<username>') #结尾没有斜杠，在访问时地址结尾也不能有斜杠；结尾有斜杠，访问时结尾可以没有斜杠
def func(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.debug = True
    app.run()