# Moose on the Loose

A personal website about my dog Moose, built with Flask to learn web development and authentication. 

## What This Is

A clean, modern website with a scrapbook aesthetic featuring:
- Home page with hero section and quick facts
- Adventures page showing places we've visited (sticky note style)
- Favorites page with colorful rotating cards
- Protected gallery with login (because not everyone needs to see 100 dog photos)

## Tech Stack

- **Flask** - Python web framework
- **Flask-Login** - User authentication and session management
- **Jinja2** - Template engine (comes with Flask)
- **HTML/CSS** - Frontend (no frameworks)
- **JavaScript** - Password show/hide toggle

## What I Learned About Flask

### Routing
Flask uses decorators to map URLs to functions. Super simple:
```python
@app.route('/')
def index():
    return render_template('index.html')
```
Each route is just a Python function that returns HTML.

### Templates (Jinja2)
Instead of writing the same header/footer on every page, you create a base template and extend it:
```html
<!-- base.html has the header/nav/footer -->
{% extends 'base.html' %}
{% block main_content %}
    <!-- Your page content here -->
{% endblock %}
```
Jinja2 also lets you use variables and logic in HTML:
```html
{% if current_user.is_authenticated %}
    <a href="/logout">Logout</a>
{% else %}
    <a href="/login">Login</a>
{% endif %}
```

### Static Files
CSS, images, and videos go in the `static/` folder. Use `url_for()` to reference them:
```html
<img src="{{ url_for('static', filename='photos/moose.jpg') }}">
```
This generates the correct path automatically.

### Forms and Request Data
When a form submits, Flask's `request` object has the data:
```python
username = request.form['username']
password = request.form['password']
```

### Flash Messages
One-time messages that show after redirects (like "Login successful!"):
```python
flash('Invalid username or password', 'error')
```
They appear once, then disappear on the next page load.

### Authentication with Flask-Login
This extension handles all the session cookie management:
- `@login_required` - Protects routes (redirects to login if not authenticated)
- `login_user(user)` - Creates a session when someone logs in
- `logout_user()` - Clears the session
- `current_user` - Access the logged-in user anywhere

It's way easier than building your own session management.

### Configuration
Never commit passwords or secret keys to git. I put them in `config.py` and added it to `.gitignore`:
```python
# config.py (not tracked in git)
```

## Project Structure
```
my_website/
├── app.py              # Main Flask app with routes
├── config.py           # Secrets 
├── templates/          # HTML files
│   ├── base.html       # Master template
│   ├── index.html      # Home page
│   ├── adventures.html
│   ├── favorites.html
│   ├── gallery.html    # Protected page
│   └── login.html
└── static/
    ├── css/
    │   └── style.css   # All styling
    ├── photos/         # Dog photos
    └── video/          # Dog video
```

## Running Locally

1. Install dependencies:
```bash
pip install flask flask-login
```

2. Create `config.py` with your secrets:
```python
SECRET_KEY = 'your-secret-key-here'
USERS = {
    'username': {'password': 'your-password'}
}
```

3. Run the app:
```bash
cd my_website
python app.py
```

4. Visit `http://localhost:5000`

## Design Choices

- **No CSS framework** - Wanted to practice vanilla CSS and understand flexbox/grid properly
- **Scrapbook aesthetic** - Used `transform: rotate()` on cards to make them look hand-placed
- **Protected gallery** - Practiced authentication without overcomplicating it

## What I'd Do Differently

- Use a proper database instead of hardcoded users (SQLite or PostgreSQL)
- Hash passwords with bcrypt instead of storing plain text
- Add form validation
- Make it responsive for mobile as well
- Deploy it somewhere (Heroku, AWS, or Render)

