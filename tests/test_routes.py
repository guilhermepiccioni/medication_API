from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Unit Tests

def test_create_medication_request():
    """
    Test creating a new medication request.

    Steps:
    1. Send a POST request to create a new medication request.
    2. Check if the response status code is 200.
    3. Check if the response message indicates success.

    Returns:
        None
    """
    data = {
        "patient_reference": "123456",
        "clinician_reference": "789012",
        "medication_reference": "ABC123",
        "reason_text": "Treatment for headache",
        "prescribed_date": "2024-02-12",
        "start_date": "2024-02-12",
        "frequency": "3 times/day",
        "status": "active"
    }
    response = client.post("/medication_requests/", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Medication request created successfully"


# API Tests

def test_get_medication_requests():
    """
    Test getting medication requests.

    Steps:
    1. Send a GET request to fetch all medication requests.
    2. Check if the response status code is 200.
    3. Check if the response contains a list of medication requests.

    Returns:
        None
    """
    response = client.get("/medication_requests/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_medication_request():
    """
    Test updating a medication request.

    Steps:
    1. Create a new medication request.
    2. Send a PATCH request to update the created medication request.
    3. Check if the response status code is 200.
    4. Check if the response message indicates success.

    Returns:
        None
    """
    # Create a new medication request
    data = {
        "patient_reference": "123456",
        "clinician_reference": "789012",
        "medication_reference": "ABC123",
        "reason_text": "Treatment for headache",
        "prescribed_date": "2024-02-12",
        "start_date": "2024-02-12",
        "frequency": "3 times/day",
        "status": "active"
    }
    create_response = client.post("/medication_requests/", json=data)
    assert create_response.status_code == 200
    medication_request_id = create_response.json()["inserted_id"]

    # Update the created medication request
    update_data = {
        "end_date": "2024-02-15",
        "status": "completed"
    }
    response = client.patch(f"/medication_requests/{medication_request_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Medication request updated successfully"


def test_get_single_medication_request():
    """
    Test getting a single medication request.

    Steps:
    1. Create a new medication request.
    2. Send a GET request to fetch the created medication request by ID.
    3. Check if the response status code is 200.
    4. Check if the response contains the expected medication request.

    Returns:
        None
    """
    # Create a new medication request
    data = {
        "patient_reference": "123456",
        "clinician_reference": "789012",
        "medication_reference": "ABC123",
        "reason_text": "Treatment for headache",
        "prescribed_date": "2024-02-12",
        "start_date": "2024-02-12",
        "frequency": "3 times/day",
        "status": "active"
    }
    create_response = client.post("/medication_requests/", json=data)
    assert create_response.status_code == 200
    medication_request_id = create_response.json()["inserted_id"]

    # Get the created medication request
    response = client.get(f"/medication_requests/{medication_request_id}")
    assert response.status_code == 200
    assert response.json()  # Ensure response is not empty
