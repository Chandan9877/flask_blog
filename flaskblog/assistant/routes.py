from flask import request, jsonify, render_template , Blueprint

from flaskblog.assistant.bot import ask_ai   

bot = Blueprint('bot', __name__)
@bot.route("/ask_bot")
def ask_bot():
    return render_template("ask_bot.html")

@bot.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    reply = ask_ai(user_message)  
    return jsonify({"reply": reply})