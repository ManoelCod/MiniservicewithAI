from app.api import app
from app.storage import init_db

if __name__ == '__main__':
    init_db()
    app.run(debug=True)