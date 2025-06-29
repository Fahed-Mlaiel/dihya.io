# api/analytics_api.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import analytics_service  # Supposons que ce module contient la logique métier
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/analytics/events', methods=['POST'])
def track_event():
    """Endpoint to track analytics events."""
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        analytics_service.track_event(data)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analytics/metrics', methods=['GET'])
def get_metrics():
    """Endpoint to retrieve analytics metrics."""
    try:
        metrics = analytics_service.get_metrics()
        return jsonify(metrics), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)