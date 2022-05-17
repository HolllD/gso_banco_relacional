from flask import Flask, jsonify, request
import names
from faker import Faker
import mysql.connector

def insert_person(name, birthday):
    mydb = mysql.connector.connect(
        user='aluno',
        password='aluno123',
        database='gso'
    )

    mycursor = mydb.cursor()

    values = (name, birthday)

    mycursor.execute(
        'INSERT INTO Pessoa (nome, nascimento) VALUES (%s, %s)', values
    )

    mydb.commit()

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root_path():
    return jsonify(msg=f"It's running! Your ip is: {request.remote_addr}", code=200)


@app.route("/pessoa/random", methods=['POST'])
def random_person():
    name = names.get_full_name()
    birthday = Faker().date_between(
        start_date='-18y', end_date='+100y'
    )

    response = {
        'name': name,
        'nascimento': birthday
    }

    print(name, birthday)

    insert_person(name, birthday.strftime("%y-%m-%d"))

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='4333')