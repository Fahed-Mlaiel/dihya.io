import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import create_app

app = create_app()

if __name__ == "__main__":
    import sys
    port = 5000
    if len(sys.argv) > 1 and sys.argv[1].startswith('--port='):
        port = int(sys.argv[1].split('=')[1])
    app.run(host="0.0.0.0", port=port)
