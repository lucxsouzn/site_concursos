from flask import Flask
import os

site = Flask(__name__)

@site.route('/')
def home():
    return "Bem-vindo ao site de estudos para concursos militares!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # fallback para 10000
    site.run(host='0.0.0.0', port=port)



