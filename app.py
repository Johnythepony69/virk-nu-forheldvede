from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json, os, time

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Make session available to all templates
@app.context_processor
def inject_user():
    return dict(session=session)

DATA_FILE = "data.json"

# Indlæs eller opret datafil
if not os.path.exists(DATA_FILE):
    data = {
        "users": {
            "kofod": {"password": "alexLA", "role": "leader"},
            "kontrollor1": {"password": "check123", "role": "controller"},
            "kassearbejder1": {"password": "ab12XY", "role": "cashier"},
            "kassearbejder2": {"password": "cd34YZ", "role": "cashier"},
            "kassearbejder3": {"password": "ef56ZA", "role": "cashier"},
            "kassearbejder4": {"password": "gh78QB", "role": "cashier"},
            "kassearbejder5": {"password": "ij90KL", "role": "cashier"},
            "kassearbejder6": {"password": "mn12RS", "role": "cashier"}
        },
        "inventory": {
            "Cola": {"price": 15, "stock": 20, "sold": 0},
            "Chips": {"price": 10, "stock": 30, "sold": 0},
            "Sandwich": {"price": 25, "stock": 15, "sold": 0}
        },
        "sales": [],
        "profit": 0.0
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
else:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def login():
    # Clear any existing session on login page
    if request.method == "GET":
        session.clear()
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in data["users"] and data["users"][username]["password"] == password:
            session["user"] = username
            role = data["users"][username]["role"]
            if role == "leader":
                return redirect(url_for("leader_dashboard"))
            elif role == "controller":
                return redirect(url_for("controller_dashboard"))
            else:
                return redirect(url_for("cashier_dashboard"))
    return render_template("login.html")

@app.route("/cashier", methods=["GET", "POST"])
def cashier_dashboard():
    if "user" not in session: return redirect(url_for("login"))
    if data["users"][session["user"]]["role"] != "cashier": return redirect(url_for("login"))
    if request.method == "POST":
        item = request.form["item"]
        if data["inventory"][item]["stock"] > 0:
            data["inventory"][item]["stock"] -= 1
            data["inventory"][item]["sold"] += 1
            price = data["inventory"][item]["price"]
            sale = {"item": item, "price": price, "time": time.time(), "cashier": session["user"]}
            data["sales"].append(sale)
            data["profit"] += price
            save_data()
    return render_template("cashier.html", inventory=data["inventory"], sales=data["sales"][-5:])

@app.route("/undo", methods=["POST"])
def undo_sale():
    if "user" not in session: return redirect(url_for("login"))
    if data["users"][session["user"]]["role"] != "cashier": return redirect(url_for("login"))
    if not data["sales"]: return redirect(url_for("cashier_dashboard"))
    last_sale = data["sales"][-1]
    if last_sale["cashier"] == session["user"] and time.time() - last_sale["time"] <= 30:
        item = last_sale["item"]
        data["inventory"][item]["stock"] += 1
        data["inventory"][item]["sold"] -= 1
        data["profit"] -= last_sale["price"]
        data["sales"].pop()
        save_data()
    return redirect(url_for("cashier_dashboard"))

@app.route("/controller")
def controller_dashboard():
    if "user" not in session: return redirect(url_for("login"))
    if data["users"][session["user"]]["role"] != "controller": return redirect(url_for("login"))
    return render_template("controller.html", inventory=data["inventory"], sales=data["sales"])

@app.route("/leader", methods=["GET", "POST"])
def leader_dashboard():
    if "user" not in session: return redirect(url_for("login"))
    if data["users"][session["user"]]["role"] != "leader": return redirect(url_for("login"))
    return render_template("leader.html", inventory=data["inventory"], profit=data["profit"])

@app.route("/add_item", methods=["POST"])
def add_item():
    if "user" not in session or data["users"][session["user"]]["role"] != "leader":
        return redirect(url_for("login"))
    item = request.form["item"]
    price = float(request.form["price"])
    stock = int(request.form["stock"])
    data["inventory"][item] = {"price": price, "stock": stock, "sold": 0}
    save_data()
    return redirect(url_for("leader_dashboard"))

@app.route("/profit_data")
def profit_data():
    if "user" not in session or data["users"][session["user"]]["role"] != "leader":
        return redirect(url_for("login"))
    chart_data = [{"item": k, "sold": v["sold"], "revenue": v["sold"] * v["price"]} for k,v in data["inventory"].items()]
    return jsonify({"profit": data["profit"], "chart": chart_data})

@app.route("/manage_users")
def manage_users():
    if "user" not in session or data["users"][session["user"]]["role"] != "leader":
        return redirect(url_for("login"))
    return render_template("manage_users.html", users=data["users"])

@app.route("/update_password", methods=["POST"])
def update_password():
    if "user" not in session or data["users"][session["user"]]["role"] != "leader":
        return redirect(url_for("login"))
    
    username = request.form["username"]
    new_password = request.form["new_password"]
    
    if username in data["users"]:
        data["users"][username]["password"] = new_password
        save_data()
    
    return redirect(url_for("manage_users"))

if __name__ == "__main__":
    app.run(debug=True)
