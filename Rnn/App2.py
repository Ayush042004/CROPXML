from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

disease_data = {
    "American Bollworm on Cotton": {
        "chemicals": ["Cypermethrin", "Chlorantraniliprole"],
        "preventive_measures": [
            "Crop rotation", 
            "Resistant varieties", 
            "Use of pheromone traps (5-10 per hectare)",
            "Deep plowing during summer to expose hibernating larvae"
        ],
        "herbal_remedies": ["Neem oil", "Garlic extract", "Tulsi leaf extract (10%) as repellent"], 
        "yield_risk": ["high"],
        "additional": [
            {"Identification": "Look for circular holes in bolls and presence of green caterpillars"}, 
            {"Economic Threshold": "5-10% damaged bolls or 1 larva per plant"},
            {"Best Treatment Time": "Early morning or late evening"}
        ]
    },
    "Army worm": {
        "chemicals": {
            "Emamectin benzoate": ["Proclaim 5% SG", "Promec 1.9% EC", "Emstar 5% SG"],
            "Spinetoram": ["Delegate 25% WG", "Radiant 12% SC"]
        },
        "preventive_measures": [
            "Monitor fields regularly for egg masses and young larvae",
            "Maintain field sanitation and weed control"
        ],
        "herbal_remedies": [
            "Neem oil spray (2-3% concentration)",
            "Castor leaf extract (10%)"
        ],
        "yield_risk": ["High"],
        "additional": [
            {"Identification": "Irregular holes in leaves"}
        ]
    },
    "Common Rust": {
        "chemicals": ["Propiconazole", "Tebuconazole", "Chlorothalonil"],
        "preventive_measures": [
            "Use of rust-resistant wheat varieties",
            "Early sowing to escape peak infection period",
            "Crop rotation with non-host plants",
            "Proper spacing to improve air circulation and reduce humidity",
            "Removal of volunteer wheat plants and infected debris"
        ],
        "herbal_remedies": ["Neem oil spray", "Cow urine-based bio-fungicides", "Garlic extract spray"],
        "yield_risk": ["moderate to high"],
        "additional": [
            {"Identification": "Look for orange, yellow, or brown powdery pustules on leaves and stems"},
            {"Economic Threshold": "5-10% infected leaf area or presence of multiple pustules per plant"},
            {"Best Treatment Time": "Apply fungicides at early signs of infection, preferably before heading stage"}
        ]
    }
}


@app.route('/get_disease_info', methods=['POST'])
def get_disease_info():
    data = request.json
    disease_name = data.get('disease_name')
    
    if not disease_name:
        return jsonify({"error": "Disease name is required"}), 400

    disease_info = disease_data.get(disease_name)
    if disease_info:
        return jsonify(disease_info)
    else:
        return jsonify({"error": "Disease not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port , debug=True)