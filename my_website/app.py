from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_our_family')
def about_our_family():
    return render_template('about_our_family.html')

@app.route('/meet_our_dog')
def meet_our_dog():
    return render_template('meet_our_dog.html')

if __name__ == '__main__':
    app.run(debug=True)