from flask import Flask
from flask_cors import CORS

from controllers.auth_controller import register, login
from controllers.appointment_controller import create_appointment, get_appointments
from controllers.user_controller import get_users

app = Flask(__name__)
CORS(app)

# AUTH ROUTES
app.add_url_rule('/api/auth/register', view_func=register, methods=['POST'])
app.add_url_rule('/api/auth/login', view_func=login, methods=['POST'])

# APPOINTMENT ROUTES
app.add_url_rule('/api/appointments', view_func=create_appointment, methods=['POST'])
app.add_url_rule('/api/appointments', view_func=get_appointments, methods=['GET'])

# USER ROUTES
app.add_url_rule('/api/users', view_func=get_users, methods=['GET'])

@app.route("/")
def home():
    return "Healthcare Backend Running 🚀"

if __name__ == "__main__":
    app.run(debug=True)