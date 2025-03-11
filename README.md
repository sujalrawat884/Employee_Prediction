# Employee Productivity Prediction

This project is a web application built with Flask that predicts employee productivity based on various input parameters. The prediction is made using a trained Random Forest model.

## Features
- Web-based interface to input employee details
- Predict employee productivity based on input factors
- Uses a trained machine learning model for accurate predictions
- Built with Flask for backend and HTML/CSS for frontend

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3
- Flask
- NumPy
- scikit-learn
- Pickle

### Steps to Run the Project
1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://127.0.0.1:5000/` in your web browser.

## API Endpoints
- `GET /` - Loads the home page with the input form.
- `POST /predict` - Accepts input parameters and returns predicted productivity.

## File Structure
```
📁 Project Folder
│-- app.py (Flask application)
│-- random_forest_model.pkl (Trained ML model)
│-- requirements.txt (Dependencies)
│-- templates/
│   │-- predict.html (Frontend UI)
│-- static/
│   │-- styles.css (CSS for styling)
│-- README.md (Project documentation)
```

## Example API Request (Using `requests` in Python)
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "team": 2,
    "month": 5,
    "quarter": 1,
    "department": 0,
    "day": 2,
    "targeted_productivity": 0.8,
    "smv": 10.5,
    "wip": 50.0,
    "over_time": 120,
    "incentive": 100,
    "idle_time": 5.0,
    "idle_men": 2,
    "no_of_style_change": 1,
    "no_of_workers": 30
}
response = requests.post(url, data=data)
print(response.text)
```

## Contributing
Feel free to contribute to this project by creating issues or submitting pull requests.

## License
This project is licensed under the MIT License.

---
**Made with ❤️ using Flask & Machine Learning** 🚀

