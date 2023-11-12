from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder, timezone, carrier

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        ph_number = request.form["ph_number"]
        phone = phonenumbers.parse(ph_number)

        carrier_name = carrier.name_for_number(phone, "en")
        result = f"The carrier for {ph_number} is: {carrier_name}"

    # shows first carrier
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
# A carrier, in the context of cellular technology is a company that provides mobile services.
