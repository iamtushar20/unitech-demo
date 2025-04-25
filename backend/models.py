from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import request


# Initialize the SQLAlchemy object
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Added name field
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.name} ({self.email})>"  # Updated to include name

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# You can also define your other models here (like Amplifier)

class Amplifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=True)
    rated_power_stereo = db.Column(db.String(100), nullable=True)
    rated_power_bridge = db.Column(db.String(100), nullable=True)
    output_4ohm_stereo = db.Column(db.String(100), nullable=True)
    output_8ohm_stereo = db.Column(db.String(100), nullable=True)
    output_4ohm_bridge = db.Column(db.String(100), nullable=True)
    output_8ohm_bridge = db.Column(db.String(100), nullable=True)
    output_circuitry = db.Column(db.String(50), nullable=True)  # e.g., Class AB, Slim Class-H
    damping_factor = db.Column(db.String(50), nullable=True)
    slew_rate = db.Column(db.String(50), nullable=True)
    fuse = db.Column(db.String(50), nullable=True)
    power_supply = db.Column(db.String(100), nullable=True)
    technical = db.Column(db.String(100), nullable=True)
    frequency_response = db.Column(db.String(100), nullable=True)
    thd = db.Column(db.String(50), nullable=True)
    imd = db.Column(db.String(50), nullable=True)
    sn_ratio = db.Column(db.String(50), nullable=True)
    input_sensitivity_db = db.Column(db.String(50), nullable=True)
    input_sensitivity_v = db.Column(db.String(50), nullable=True)
    input_connectors = db.Column(db.String(100), nullable=True)
    input_impedance = db.Column(db.String(50), nullable=True)
    crosstalk = db.Column(db.String(50), nullable=True)
    input_cmr = db.Column(db.String(50), nullable=True)
    indicators = db.Column(db.String(200), nullable=True)
    smart_protections = db.Column(db.String(200), nullable=True)
    cooling = db.Column(db.String(100), nullable=True)
    filter_type = db.Column(db.String(100), nullable=True)
    bandwidth = db.Column(db.String(100), nullable=True)
    power_consumption = db.Column(db.String(50), nullable=True)
    stereo_mode = db.Column(db.String(10), nullable=True)
    product_dimensions = db.Column(db.String(100), nullable=True)
    packaging_dimensions = db.Column(db.String(100), nullable=True)
    weight = db.Column(db.String(50), nullable=True)
    product_gross_weight = db.Column(db.String(50), nullable=True)
    extra_1 = db.Column(db.String(1000), nullable=True)
    extra_2 = db.Column(db.String(1000), nullable=True)
    image_filename = db.Column(db.String(200), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Amplifier {self.model_name or 'Unnamed'}>"

    def to_dict(self):
        base_url = request.host_url.rstrip('/')
        return {
            "id": self.id,
            "model_name": self.model_name,
            "rated_power_stereo": self.rated_power_stereo,
            "rated_power_bridge": self.rated_power_bridge,
            "output_4ohm_stereo": self.output_4ohm_stereo,
            "output_8ohm_stereo": self.output_8ohm_stereo,
            "output_4ohm_bridge": self.output_4ohm_bridge,
            "output_8ohm_bridge": self.output_8ohm_bridge,
            "output_circuitry": self.output_circuitry,
            "damping_factor": self.damping_factor,
            "slew_rate": self.slew_rate,
            "fuse": self.fuse,
            "power_supply": self.power_supply,
            "technical": self.technical,
            "frequency_response": self.frequency_response,
            "thd": self.thd,
            "imd": self.imd,
            "sn_ratio": self.sn_ratio,
            "input_sensitivity_db": self.input_sensitivity_db,
            "input_sensitivity_v": self.input_sensitivity_v,
            "input_connectors": self.input_connectors,
            "input_impedance": self.input_impedance,
            "crosstalk": self.crosstalk,
            "input_cmr": self.input_cmr,
            "indicators": self.indicators,
            "smart_protections": self.smart_protections,
            "cooling": self.cooling,
            "filter_type": self.filter_type,
            "bandwidth": self.bandwidth,
            "power_consumption": self.power_consumption,
            "stereo_mode": self.stereo_mode,
            "product_dimensions": self.product_dimensions,
            "packaging_dimensions": self.packaging_dimensions,
            "weight": self.weight,
            "product_gross_weight": self.product_gross_weight,
            "extra_1": self.extra_1,
            "extra_2": self.extra_2,
            "image_url": f"{base_url}/static/uploads/{self.image_filename}" if self.image_filename else None,
            "date_added": self.date_added.strftime("%Y-%m-%d %H:%M:%S")
        }
class Speaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(100), nullable=True)
    magnet_size = db.Column(db.String(50), nullable=True)  # e.g., "190×25"
    power_rating = db.Column(db.String(50), nullable=True)  # e.g., "500W"
    voice_coil_diameter = db.Column(db.String(50), nullable=True)  # e.g., "3.2 inch"
    voice_coil_type = db.Column(db.String(50), nullable=True)  # e.g., "in/out"
    image_filename = db.Column(db.String(200), nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Speaker {self.model_name or 'Unnamed'}>"

    def to_dict(self):
        base_url = request.host_url.rstrip('/')
        return {
            "id": self.id,
            "model_name": self.model_name,
            "magnet_size": self.magnet_size,
            "power_rating": self.power_rating,
            "voice_coil_diameter": self.voice_coil_diameter,
            "voice_coil_type": self.voice_coil_type,
            "image_url": f"{base_url}/static/uploads/{self.image_filename}" if self.image_filename else None,
            "date_added": self.date_added.strftime("%Y-%m-%d %H:%M:%S")
        }