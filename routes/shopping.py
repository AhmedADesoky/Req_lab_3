from flask import Blueprint, request, jsonify
from middleware.mid_ware import auth_token

Shop_file = Blueprint("Shop", __name__)

Shop_Users = []
Shop_Carts = []

@Shop_file.before_request
def before_request():
    auth_token()

@Shop_file.route("/", methods=["GET"])
def get_users():
    return jsonify(Shop_Users)

@Shop_file.route("/", methods=["POST"])
def create_user():
    new_user = {
        "Id": len(Shop_Users) + 1,
        "User Name": request.json.get("user name")
    }
    Shop_Users.append(new_user)
    return jsonify(new_user), 201

@Shop_file.route("/<int:user_id>", methods=["POST"])
def create_cart(user_id):
    user = next((u for u in Shop_Users if u["Id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    new_cart = {
        "User Id": user["Id"],
        "Items": request.json.get("item name"),
        "Quantity": request.json.get("quantity")
    }
    Shop_Carts.append(new_cart)
    return jsonify(new_cart), 201

@Shop_file.route("/<int:user_id>", methods=["PUT"])
def update_cart(user_id):
    cart = next((c for c in Shop_Carts if c["User Id"] == user_id), None)
    if not cart:
        return jsonify({"error": "Cart not found"}), 404
    
    cart["Items"] = request.json.get("item name", cart["Items"])
    cart["Quantity"] = request.json.get("quantity", cart["Quantity"])
    
    return jsonify(cart) , 200

@Shop_file.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global Shop_Users
    user = next((u for u in Shop_Users if u["Id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    Shop_Users = [u for u in Shop_Users if u["Id"] != user_id]
    
    return jsonify({"message": f"User {user_id} deleted"}), 200
