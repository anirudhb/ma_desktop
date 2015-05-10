from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/api", methods=["POST", "GET"])
def api():
    if request.method == "GET":
        return "This is not a Response"
    elif request.method == "POST":
        return Response(status=200)
        
app.run(port=8080, debug=True)
