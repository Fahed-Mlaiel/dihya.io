# analytics_backend/app.py
from flask import Flask, request, jsonify
from .analytics import AnalyticsProcessor
from .security import require_auth

app = Flask(__name__)
analytics_processor = AnalyticsProcessor()

@app.route('/analytics/events', methods=['POST'])
@require_auth
def track_event():
    data = request.json
    analytics_processor.process_event(data)
    return jsonify({"status": "success"}), 200