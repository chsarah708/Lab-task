from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    vehicle_data = None
    error = None
    if request.method == "POST":
        vin = request.form.get("vin")
        if vin:
            url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
            response = requests.get(url)
            if response.status_code == 200:
                results = response.json().get("Results", [])
                vehicle_data = {item["Variable"]: item["Value"] for item in results if item["Value"]}
            else:
                error = "API request failed."
        else:
            error = "Please enter a VIN."
    return render_template("index.html", vehicle_data=vehicle_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
