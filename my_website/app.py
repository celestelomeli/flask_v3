# Flask: web framework for building the application
# render_template: renders HTML templates
# request: handles incoming request data (forms, etc.)
# redirect: redirects user to different routes
# flash: displays one-time messages to user
from flask import Flask, render_template, request, redirect, flash

# Flask-Login: handles user authentication and session management
# LoginManager: manages login system
# UserMixin: provides default implementations for user authentication
# login_user: logs user in and creates session
# login_required: decorator to protect routes that need authentication
# logout_user: logs user out and clears session
# current_user: accesses currently logged-in user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from config import SECRET_KEY, USERS  # Import secrets from config file (not tracked in git)
import os  # Operating system interface (not currently used but available)

app = Flask(__name__)
app.secret_key = SECRET_KEY  # Used for session management and flash messages

# Initialize Flask-Login to handle user sessions
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if user not authenticated

class User(UserMixin):
    """Simple user class for Flask-Login"""
    def __init__(self, id):
        self.id = id

users = USERS  # Load user credentials from config

@login_manager.user_loader
def load_user(user_id):
    """Required by Flask-Login to reload user from session"""
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    if request.method == 'POST':
        # Use .get() to safely retrieve form data without KeyError
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Check if user exists and password matches
        user_data = users.get(username)
        if user_data and user_data['password'] == password:
            user = User(username)
            login_user(user)  # Create session for user
            flash('Logged in successfully!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/dashboard')
@login_required  # User must be logged in to access
def dashboard():
    """User dashboard page"""
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required  # User must be logged in to logout
def logout():
    """Handle user logout"""
    logout_user()  # Clear user session
    flash('Logged out successfully!', 'success')
    return redirect('/')

@app.route('/')
@login_required  # Protected route - requires login
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/about_our_family')
def about_our_family():
    """About our family page - public route"""
    return render_template('about_our_family.html')

@app.route('/meet_our_dog')
def meet_our_dog():
    """Meet our dog page - public route"""
    return render_template('meet_our_dog.html')

@app.route('/gallery')
def gallery():
    """Photo gallery page - public route"""
    return render_template('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)  # Run Flask development server