from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, User  # Ensure User model is imported
from controllers import main_routes
import os

app = Flask(__name__)

# Secret key for session or CSRF (if needed later)
app.secret_key = 'your-secret-key'  # replace with a strong secret key in production

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Image upload folder
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize extensions
db.init_app(app)
CORS(app)  # Allow cross-origin requests for frontend

# Register blueprint routes
app.register_blueprint(main_routes)

# Function to create a default admin user if it doesn't exist
from models import db, User  # Import your models
from werkzeug.security import generate_password_hash

# Function to create a default admin user if it doesn't exist
def create_default_admin():
    admin_email = "admin@admin.com"
    admin_password = "adminpassword"  # This is the plain-text password
    
    # Check if the admin user already exists
    admin_user = User.query.filter_by(email=admin_email).first()

    if not admin_user:
        name = 'admin'
        new_admin = User(name=name ,email=admin_email, is_admin=True)
        new_admin.set_password(admin_password)  # Hash the password before storing it
        db.session.add(new_admin)
        db.session.commit()
        print("Default admin created")


# Create database tables on first run and create default admin if needed
with app.app_context():
    db.create_all()  # Creates database tables
    create_default_admin()  # Creates the default admin if it doesn't exist

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
