from flask import Flask, render_template, request, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


import os

app = Flask(__name__)
app.secret_key = 'Moose_Angel24'  

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id):
        self.id = id


users = {
    'celestelomeli': {'password': 'Mellifluous24!'}, 
    'ajramirez': {'password': 'moosebaby04'}
    }

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = users.get(username)
        if user_data and user_data['password'] == password:
            user = User(username)
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect('/')

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/about_our_family')
def about_our_family():
    return render_template('about_our_family.html')

@app.route('/meet_our_dog')
def meet_our_dog():
    return render_template('meet_our_dog.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
    #photo_path = 'static/photos/'
    #photos = [photo for photo in os.listdir(photo_path) if photo.endswith(('jpg', 'png', 'jpeg', 'gif'))]
    #return render_template('gallery.html', photos=photos)


if __name__ == '__main__':
    app.run(debug=True)