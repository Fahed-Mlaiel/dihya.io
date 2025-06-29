# analytics_service.py

from flask import Flask, request, jsonify
from analytics_manager import AnalyticsManager

app = Flask(__name__)
analytics_manager = AnalyticsManager()

@app.route('/track', methods=['POST'])
def track_event():
    event_data = request.json
    analytics_manager.track_event(event_data)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5000)