from flask import request, jsonify
from utils.db import appointments
from services.triage_service import classify_patient
import uuid

def create_appointment():
    data = request.json

    if not data.get("patient_name") or not data.get("symptoms"):
        return jsonify({"message": "Missing required fields"}), 400

    priority = classify_patient(data.get("symptoms"))

    appointment = {
        "id": str(uuid.uuid4()),
        "patient_name": data.get("patient_name"),
        "symptoms": data.get("symptoms"),
        "date": data.get("date"),
        "priority": priority,
        "status": "PENDING"
    }

    appointments.append(appointment)

    return jsonify({
        "message": "Appointment created successfully",
        "appointment": appointment
    })


def get_appointments():
    # Sort: EMERGENCY first
    sorted_data = sorted(
        appointments,
        key=lambda x: 0 if x["priority"] == "EMERGENCY" else 1
    )

    return jsonify(sorted_data)