from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")
    exec(f"name = '{name}'")  # Уязвимость: exec
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
