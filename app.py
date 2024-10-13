from flask import Flask , jsonify
from routes.shopping import Shop_file

app = Flask(__name__)


app.register_blueprint(Shop_file , url_prefix = "/Shop")
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Resource not found"}), 404

if __name__ == "__main__":
    app.run(port = 3000)