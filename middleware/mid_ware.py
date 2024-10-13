from flask import request , jsonify

Token = '1222'

def auth_token():
    token = request.headers.get("Authorization")
    if not token or token != f"beaarer {Token}":
        return jsonify({"error":"Unauthorized"}) , 401