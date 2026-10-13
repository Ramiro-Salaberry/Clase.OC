from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("index.html")


@app.route("/album")
def album():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("album.html")


@app.route("/cafeteria")
def cafeteria():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("cafeteria.html")


@app.route("/formulario")
def formulario():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("formulario.html")

@app.route("/receta")
def receta():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("receta.html")



@app.route("/footer")
def footer():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("footer.html")


@app.route("/videosNE")
def videosNE():
    # En lugar de escribir HTML aquí, le decimos a Flask:
    # "Busca index.html en la carpeta templates y devuélvelo"
    return render_template("videosNE.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)