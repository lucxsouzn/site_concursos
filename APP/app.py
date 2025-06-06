from flask import Flask

site = Flask(__name__)

@site.route('/')
def home():
    return "Bem-vindo ao site de estudos para concursos militares!"

if __name__ == '__main__':
    site.run(debug=True)

    