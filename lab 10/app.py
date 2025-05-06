from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rules-based response logic
def get_response(user_input):
    user_input = user_input.lower()

    if "hours" in user_input or "open" in user_input:
        return "We are open Monday to Saturday, 9 AM to 6 PM."
    elif "services" in user_input:
        return "We offer general checkups, pediatrics, cardiology, and lab tests."
    elif "appointment" in user_input:
        return "You can book an appointment by calling us or through our website."
    elif "doctors" in user_input or "available" in user_input:
        return "Our doctors are available from 10 AM to 5 PM, Monday to Friday."
    elif "contact" in user_input:
        return "You can call us at (123) 456-7890 or email info@medcenter.com."
    else:
        return "I'm sorry, I didn't understand that. Please ask about hours, services, doctors, or appointments."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
