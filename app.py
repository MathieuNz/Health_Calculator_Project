import sys
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from health_utils import calculate_bmi, calculate_bmr


app = Flask(__name__, static_folder='static')
CORS(app)  

@app.route("/")
def serve_doc():
    """Sert la page d'index HTML"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/api")
def api_documentation():
    """Return API documentation in JSON format"""
    return jsonify({
        "name": "Health Calculator API",
        "version": "1.0.0",
        "description": "API for calculating health metrics like BMI and BMR",
        "endpoints": {
            "/": {
                "method": "GET",
                "description": "Web interface for the calculator"
            },
            "/api": {
                "method": "GET",
                "description": "API documentation"
            },
            "/bmi": {
                "method": "POST",
                "description": "Calculate Body Mass Index (BMI)",
                "parameters": {
                    "height": {
                        "type": "number",
                        "description": "Height in meters",
                        "required": True
                    },
                    "weight": {
                        "type": "number",
                        "description": "Weight in kilograms",
                        "required": True
                    }
                },
                "example_request": {
                    "height": 1.75,
                    "weight": 70
                },
                "example_response": {
                    "operation": "bmi",
                    "result": 22.86
                }
            },
            "/bmr": {
                "method": "POST",
                "description": "Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation",
                "parameters": {
                    "height": {
                        "type": "number",
                        "description": "Height in centimeters",
                        "required": True
                    },
                    "weight": {
                        "type": "number",
                        "description": "Weight in kilograms",
                        "required": True
                    },
                    "age": {
                        "type": "number",
                        "description": "Age in years",
                        "required": True
                    },
                    "gender": {
                        "type": "string",
                        "description": "Gender ('male' or 'female')",
                        "required": True
                    }
                },
                "example_request": {
                    "height": 175,
                    "weight": 70,
                    "age": 25,
                    "gender": "male"
                },
                "example_response": {
                    "operation": "bmr",
                    "result": 1724.05
                }
            }
        },
        "errors": {
            "400": "Bad Request - Missing or invalid parameters",
            "500": "Internal Server Error"
        }
    })

@app.route("/bmi", methods=["POST"])
def bmi():
    """Calculate BMI based on height and weight"""
    data = request.get_json()
    try:
       
        height = float(data["height"])
        weight = float(data["weight"])
        
      
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Height and weight must be positive values"}), 400
            
        result = calculate_bmi(height, weight)
        return jsonify({
            "operation": "bmi",
            "result": round(result, 2),
            "interpretation": get_bmi_interpretation(result)
        })
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({
            "error": "Invalid or missing parameters. Please provide height (in meters) and weight (in kg)",
            "details": str(e)
        }), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route("/bmr", methods=["POST"])
def bmr():
    """Calculate BMR based on height, weight, age, and gender"""
    data = request.get_json()
    try:
        
        height = float(data["height"])
        weight = float(data["weight"])
        age = float(data["age"])
        gender = str(data["gender"]).lower()
        
        
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({"error": "Height, weight, and age must be positive values"}), 400
        if gender not in ["male", "female"]:
            return jsonify({"error": "Gender must be 'male' or 'female'"}), 400
            
        result = calculate_bmr(height, weight, age, gender)
        return jsonify({
            "operation": "bmr",
            "result": round(result, 2)
        })
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({
            "error": "Invalid or missing parameters",
            "details": str(e)
        }), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

def get_bmi_interpretation(bmi):
    """Return BMI category based on the calculated value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000, debug=True)