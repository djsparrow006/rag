from flask import Flask , request,Blueprint,jsonify
app = Flask(__name__)
from service.rag import answer as ans
chat_bp = Blueprint("chat",__name__)
@chat_bp.route("/chat",methods = ["POST","GET"])
def chat():
    data = request.get_json(silent=True)
    if not data or not isinstance(data,dict):
        return jsonify ({"responce": "Invalid  data "})
    question = data.get("question")
    if not isinstance(question,str) or not question.strip():
        return jsonify({"responce":"Invalid data"})
    answer = ans(question)
    print(answer)
    return jsonify({"sucess":True,"ans":answer}),200
app.register_blueprint(chat_bp)
if __name__ == "__main__":
    app.run(debug=True)
