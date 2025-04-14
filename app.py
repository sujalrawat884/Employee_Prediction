from flask import Flask, render_template, request, url_for, redirect
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.route("/")
def main():
    return redirect('/home')
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Extract form data
            features = [
                int(request.form["team"]),
                int(request.form["month"]),
                int(request.form["quarter"]),
                int(request.form["department"]),
                int(request.form["day"]),
                float(request.form["targeted_productivity"]),
                float(request.form["smv"]),
                float(request.form["wip"]),
                int(request.form["over_time"]),
                int(request.form["incentive"]),
                float(request.form["idle_time"]),
                int(request.form["idle_men"]),
                int(request.form["no_of_style_change"]),
                int(request.form["no_of_workers"]),
            ]

            # Validate input length
            if len(features) != 14:
                return render_template("predict.html", prediction_text="Error: Incorrect number of inputs!")

            # Convert to NumPy array and reshape for model
            final_features = np.array(features).reshape(1, -1)

            # Make prediction
            prediction = model.predict(final_features)[0]

            return render_template("predict.html", prediction_text=f"Predicted Productivity: {round(prediction, 2)}")

        except Exception as e:
            return render_template("predict.html", prediction_text=f"Error: {str(e)}")
    else:
        # GET request - just show the form
        return render_template("predict.html")

@app.route("/submit/<float:prediction>")
def submit(prediction):
    return render_template("submit.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
