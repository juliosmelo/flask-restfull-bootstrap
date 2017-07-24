import os
from src import app

if __name__ == '__main__':
    port = os.getenv('PORT', '5000')
    host = os.getenv('HOST', '0.0.0.0')
    app.run(host=host, port=int(port))
