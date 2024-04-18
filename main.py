
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    price = db.Column(db.Float)
    image = db.Column(db.String(120))

cart = []

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/add_to_cart')
def add_to_cart():
    product_id = request.args.get('product_id')
    product = Product.query.get_or_404(product_id)
    cart.append(product)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
