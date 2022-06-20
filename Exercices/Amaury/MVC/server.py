import os
from app import app

port = int(os.environ.get('PORT', 8080))
app.run('0.0.0.0', port=port)