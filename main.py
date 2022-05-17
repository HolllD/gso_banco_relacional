from flask import Flask, jsonify, request
import names

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root_path():
    return jsonify(msg=f"It's running! Your ip is: {request.remote_addr}", code=200)


@app.route("/pessoa/random")
def random_person():
    print("temp")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='43333')