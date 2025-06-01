"""
Script CI/CD : push automatique du dashboard global (Markdown) en WebSocket à chaque build ou événement critique.
- Utilisable dans GitHub Actions, pipelines CI/CD, ou manuellement.
"""
import socketio
import os
import time

DASHBOARD_MD_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../dashboard_global.md'))
WS_URL = os.environ.get('DASHBOARD_WS_URL', 'ws://localhost:8000/ws/dashboard')

sio = socketio.Client()

def push_dashboard():
    with open(DASHBOARD_MD_PATH, encoding='utf-8') as f:
        md = f.read()
    sio.connect(WS_URL, namespaces=['/ws/dashboard'])
    sio.emit('dashboard', md, namespace='/ws/dashboard')
    time.sleep(1)
    sio.disconnect()

if __name__ == '__main__':
    push_dashboard()
