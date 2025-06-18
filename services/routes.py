from flask import Blueprint, request, jsonify
from service.models import Product

bp = Blueprint('products', __name__)

@bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.serialize()), 200

@bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.available = data.get('available', product.available)
    product.save()
    return jsonify(product.serialize()), 200

@bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.find_by_id(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    product.delete()
    return '', 204

@bp.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available is not None:
        avail_bool = available.lower() == 'true'
        products = Product.find_by_availability(avail_bool)
    else:
        products = Product.list_all()

    return jsonify([p.serialize() for p in products]), 200
