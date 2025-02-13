from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/lokasi')
def lokasi():
    return render_template('lokasi.html')

@app.route('/erd')
def erd():
    return render_template('erd.html')

if __name__ == '__main__':
    app.run(debug=True)
