from flask import Flask, jsonify, request
import names
from faker import Faker

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root_path():
    return jsonify(msg=f"It's running! Your ip is: {request.remote_addr}", code=200)


@app.route("/pessoa/random")
def random_person():
    name = names.get_full_name()
    birthday = Faker().date_between(
        start_date='-18y', end_date='+10y'
    )

    return {'name': name, 'birthday': birthday}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='43333')