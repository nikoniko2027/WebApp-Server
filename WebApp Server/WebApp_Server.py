AuthDT = [
    {
        "login": "nikoniko2027",
        "pass": "nikoniko2027"
    },
    {
        "login": "admin",
        "pass": "admin"
    }
]


from flask import Flask, request, send_file
from flask_restful import Api, Resource, reqparse

import os
import base64

app = Flask(__name__)
api = Api(app)

class Quote(Resource):

        ### Регистрация клиента
    @app.route('/Register', methods=['POST'])
    def Register():
        login = request.form['login']
        password = request.form['pass']
        token = request.form['token']
        return "REGISTER", 200



        ### Авторизация клиента
    @app.route('/Auth', methods=['POST'])
    def Auth():
        login = request.form['login']
        password = request.form['pass']
        token = request.form['token']
        return "AUTH", 200




        ### Загрузка фото на сервер
    @app.route('/UploadFile', methods=['POST'])
    def UploadFile():
        print(request.form)
        if 'file' not in request.files:
            return "No file part", 200
        else:
            file = request.files['file']
            if file.filename != '':
                file.save(os.path.join(os.getcwd() + "/Images/", file.filename))
            return "Good file", 200




        ### Возврат фото с сервера
    @app.route('/ReturnFile', methods=['GET'])
    def ReturnFile():
        print(request.args['ID']) # ID Фото для возврата
        file = os.getcwd() + "/Images/Niko.png"
        return send_file(file, mimetype='image/png'), 202




api.add_resource(Quote)
if __name__ == '__main__':
    app.run(debug=False)