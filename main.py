from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    #uvedba piskotka, da preverimo, če že obstaja kkako skrivno število, če ne obstaja, si ga moramo izmislit
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        new_secret = random.randint(1,20)
        response.set_cookie("secret_number", str(new_secret))

    return response

#spodaj kontroler, ki bo sprocesiral uporabnikov vnos

@app.route("/answer", methods=["POST"])
def answer():
    #pridobitev vnosa spodaj
    guess = int(request.form.get("guess"))
    #definiramo spremenljivko za skrito število
    secret_number = int(request.cookies.get("secret_number"))
    #v int spremenimo, ker nizov ne mores primerjat med sabo, potem ko bomo predlagali višje, nižje

    if guess == secret_number:
        message = "Correct!"
        response = make_response(render_template("answer.html", message=message))
        new_secret = random.randint(1, 20)
        response.set_cookie("secret_number",str(new_secret))
        return response
    
    elif guess > secret_number:
        message ="Your guess is incorrect...try smaller!"
        return render_template("answer.html", message=message)
    
    elif guess < secret_number:
        message ="Your guess is incorrect..try bigger"
        return render_template("answer.html", message=message)
    
if __name__ == "__main__":
    app.run(use_reloader=True)