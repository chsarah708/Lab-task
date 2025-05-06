from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Optional if you're testing frontend separately

@app.route("/")
def index():
    return render_template("chat.html")  # Renders your HTML file

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form.get("msg")

    # 🔄 Replace this logic with a medical AI model or API call
    if "fever" in user_msg.lower():
        response = "It might be a sign of an infection. Please consult a doctor if it persists."
    elif "headache" in user_msg.lower():
        response = "Drink plenty of water and rest. If the headache is severe or recurring, seek medical advice."
    else:
        response = "I'm a simple medical assistant. Could you tell me more about your symptoms?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

