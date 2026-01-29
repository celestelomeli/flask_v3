# Import Flask framework and related functions
# Flask: main web framework
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

# Flask-Login: handles user authentication and session management
# LoginManager: manages login system
# UserMixin: provides default implementations for user authentication
# login_user: logs user in and creates session
# login_required: decorator to protect routes that need authentication
# logout_user: logs user out and clears session
# current_user: accesses currently logged-in user
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Import secrets from config file (not tracked in git for security)
from config import SECRET_KEY, USERS
import os  # Operating system interface

# Create Flask application instance
app = Flask(__name__)
app.secret_key = SECRET_KEY  # Used for session management and flash messages
app.secret_key = SECRET_KEY  # Used for session management and flash messages

# Initialize Flask-Login to handle user sessions
# Initialize Flask-Login to handle user sessions
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if user not authenticated
login_manager.login_view = 'login'  # Redirect to login page if user not authenticated

class User(UserMixin):
    """Simple user class for Flask-Login"""
    """Simple user class for Flask-Login"""
    def __init__(self, id):
        self.id = id

# Load user credentials from config file
users = USERS

@login_manager.user_loader
def load_user(user_id):
    """Required by Flask-Login to reload user from session"""
    """Required by Flask-Login to reload user from session"""
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login - accepts both GET (show form) and POST (process form)"""
    if request.method == 'POST':
        # Get username and password from submitted form
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists in our users dictionary
        user_data = users.get(username)
        # Verify both user exists and password matches
        if user_data and user_data['password'] == password:
            # Create user object and log them in
            user = User(username)
            login_user(user)  # Create session for user
            login_user(user)  # Create session for user
            flash('Logged in successfully!', 'success')
            return redirect('/gallery')  # Go to gallery after successful login
        else:
            # Show error message if credentials are invalid
            flash('Invalid username or password', 'error')
    # If GET request, just show the login form
    return render_template('login.html')

@app.route('/dashboard')
@login_required  # User must be logged in to access this route
def dashboard():
    """Dashboard route - redirects to gallery"""
    return redirect('/gallery')  # Redirect to gallery after login

@app.route('/logout')
@login_required  # User must be logged in to logout
@login_required  # User must be logged in to logout
def logout():
    """Handle user logout"""
    logout_user()  # Clear user session
    """Handle user logout"""
    logout_user()  # Clear user session
    flash('Logged out successfully!', 'success')
    return redirect('/')  # Return to home page

# PUBLIC ROUTES (no login required)

@app.route('/')
def index():
    """Home page - shows intro, stats, featured photo, and about section"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About Moose page - detailed personality and facts"""
    return render_template('about.html')

@app.route('/adventures')
def adventures():
    """Adventures page - shows places Moose has visited"""
    return render_template('adventures.html')

@app.route('/favorites')
def favorites():
    """Favorites page - shows Moose's favorite things"""
    return render_template('favorites.html')

# PROTECTED ROUTE (login required)

@app.route('/gallery')
@login_required  # This decorator protects the route - redirects to login if not authenticated
def gallery():
    """Photo gallery page - requires login to view"""
    return render_template('gallery.html')

# Run the Flask application
if __name__ == '__main__':
    # Disable template caching for development
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    # debug=True enables auto-reload when code changes and shows detailed error pages
    # Only use debug=True in development, never in production
    app.run(debug=True)