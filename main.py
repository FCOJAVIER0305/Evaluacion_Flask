from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------------
# RUTA MENÚ PRINCIPAL
# -------------------------
@app.route("/")
def inicio():
    return render_template("index.html")


# -------------------------
# EJERCICIO 1: PINTURAS
# -------------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio = 9000
        total = cantidad * precio

        descuento = 0

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_final = total - (total * descuento)

        return render_template(
            "resultado.html",
            nombre=nombre,
            total=total,
            descuento=descuento * 100,
            total_final=total_final
        )

    return render_template("ejercicio1.html")


# -------------------------
# EJERCICIO 2: LOGIN
# -------------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "juan" and password == "admin":
            mensaje = "Bienvenido Administrador"
        elif usuario == "pepe" and password == "user":
            mensaje = "Bienvenido Usuario"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


# -------------------------
# EJECUCIÓN
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)