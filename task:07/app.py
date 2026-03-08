from flask import Flask, render_template, request
import requests
import logging
from typing import Optional

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET", "POST"])
def home() -> str:
    """Home page for age prediction."""
    name: Optional[str] = None
    age: Optional[int] = None
    error: Optional[str] = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        
        if not name:
            error = "Please enter a name"
        else:
            try:
                url = f"https://api.agify.io/?name={name}"
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()
                
                age = data.get("age")
                if age is None:
                    error = "Could not predict age for this name"
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"API request failed: {e}")
                error = "Failed to connect to age prediction service"
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                error = "An unexpected error occurred"

    return render_template("index.html", name=name, age=age, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)