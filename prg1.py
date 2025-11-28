from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        department  = request.form["department"]
        return f"Registered: {name} ({email}), Phone: {phone}"

    return '''
    <form method="post">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        Phone: <input type="text" name="phone"><br>
        Department : <input type="text" name="dept"><br>
        <input type="submit" value="Register">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

