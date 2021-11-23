from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import url_for

class User:
    def __init__(self, id_num, username, password):
        self.id_num = id_num
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id_num = 2, username='admin', password='1234'))

app = Flask(__name__)
app.secret_key = 'secretsecretsecret'

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['user']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id_num
            return redirect(url_for('index'))

        return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('register'))

    return render_template("register.html")


    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)


