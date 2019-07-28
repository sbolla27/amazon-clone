# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from amazon_clone import app

if __name__ == '__main__':
    app.debug = True
    app.run()
