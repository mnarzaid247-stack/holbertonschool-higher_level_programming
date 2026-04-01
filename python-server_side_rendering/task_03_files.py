from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


def read_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv_products():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_data = read_json_products()
    elif source == 'csv':
        products_data = read_csv_products()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [product for product in products_data if product['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error='Product not found')
            return render_template('product_display.html', products=filtered_products)
        except ValueError:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)