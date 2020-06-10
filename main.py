import os
from flask import Flask
from src.score import calcular

app = Flask(__name__)


@app.route("/score/<nome>/<int:idade>")
def resumo_score(nome=None, idade=0):
    return calcular(nome, idade)

@app.route("/")
def home(nome=None, idade=0):
    return "Hello!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
