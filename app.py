from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Vag.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/program')
def program():
    return render_template('programa.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)