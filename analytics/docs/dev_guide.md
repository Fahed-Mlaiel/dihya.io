from flask import Flask, request, jsonify
from analytics_service import AnalyticsService

app = Flask(__name__)
analytics_service = AnalyticsService()

@app.route('/track', methods=['POST'])
def track_event():
    event_data = request.json
    analytics_service.track_event(event_data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')