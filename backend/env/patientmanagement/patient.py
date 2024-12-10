from sanic import Sanic
from sanic.response import json
import aiomysql

app = Sanic("PatientManagementSystem")

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",  # Replace with your database username
    "password": "@Ndikumana2608!",  # Replace with your database password
    "db": "receptionist_db",  # Replace with your database name
}


async def get_db_connection():
    """
    Establishes a connection to the database.
    """
    return await aiomysql.connect(
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        db=DB_CONFIG["db"],
    )

#register patients
@app.post("/register")

async def register_patients(request):
    # Extract form data
    data = request.json
    required_fields = [
        "patient_name", "patient_surname", "insurance", "patient_age",
        "patient_gender", "patient_blood_group", "patient_contacts",
        "next_of_keen_contacts", "address"
    ]

    # Validate request payload
    if not all(field in data for field in required_fields):
        return json({"error": "Missing required fields"}, status=400)


    # Insert patient data into the database
    try:
        pool = await aiomysql.create_pool(**DB_CONFIG)
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    """
                    INSERT INTO patients (
                        patient_name, patient_surname, insurance, patient_age,
                        patient_gender, patient_blood_group, patient_contacts,
                        next_of_keen_contacts, address,
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        data["patient_name"],
                        data["patient_surname"],
                        data["insurance"],
                        data["patient_age"],
                        data["patient_gender"],
                        data["patient_blood_group"],
                        data["patient_contacts"],
                        data["next_of_keen_contacts"],
                        data["address"]
                    )
                )
                await conn.commit()
        pool.close()
        await pool.wait_closed()

        return json({"message": "patient registered successfully!"})

    except Exception as e:
        return json({"error": str(e)}, status=500)
    
 #updating patient data   
@app.route("/update/<patient_id:int>", methods=["PUT"])
async def update_patient(request, patient_id):
    """
    Endpoint to update patient details.
    """
    data = request.json

    try:
        conn = await get_db_connection()
        async with conn.cursor() as cur:
            # Check if the patient exists
            await cur.execute("SELECT * FROM Patients WHERE patient_id = %s", (patient_id,))
            patient = await cur.fetchone()
            if not patient:
                return json({"error": "Patient not found"}, status=404)

            # Update patient details
            update_fields = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE Patients SET {update_fields} WHERE patient_id = %s"
            await cur.execute(query, (*data.values(), patient_id))
            await conn.commit()
        conn.close()
        return json({"message": "Patient updated successfully"}, status=200)

    except Exception as e:
        return json({"error": str(e)}, status=500)


@app.route("/delete/<patient_id:int>", methods=["DELETE"])
async def delete_patient(request, patient_id):
    """
    Endpoint to delete a patient by ID.
    """
    try:
        conn = await get_db_connection()
        async with conn.cursor() as cur:
            # Check if the patient exists
            await cur.execute("SELECT * FROM Patients WHERE patient_id = %s", (patient_id,))
            patient = await cur.fetchone()
            if not patient:
                return json({"error": "Patient not found"}, status=404)

            # Delete the patient record
            await cur.execute("DELETE FROM Patients WHERE patient_id = %s", (patient_id,))
            await conn.commit()
        conn.close()
        return json({"message": "Patient deleted successfully"}, status=200)

    except Exception as e:
        return json({"error": str(e)}, status=500)

 
@app.route("/patients", methods=["GET"])
async def view_all_patients(request):
    try:
        # Connect to the database
        async with aiomysql.connect(**db_config) as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                # Query to fetch all patients
                query = "SELECT * FROM patients"
                await cur.execute(query)
                patients = await cur.fetchall()

        # Return the patients as a JSON response
        return response.json({"patients": patients})

    except Exception as e:
        # Handle any errors
        return response.json({"error": str(e)}, status=500)


@app.get("/test")
async def test_route(request):
    return json({"message": "Server is running!"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
