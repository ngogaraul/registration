# Import necessary libraries
from sanic import Sanic
from sanic.response import json, text
from sanic_ext import Extend
from hashlib import sha256
import aiomysql

# Initialize Sanic app
app = Sanic("EmployeeRegistrationApp")
Extend(app)

# Configure database connection
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "@Ndikumana2608!",
    "db": "employees",
}

# Route to handle employee registration
@app.post("/register")
async def register_employee(request):
    # Extract form data
    data = request.json
    required_fields = [
        "employee_name", "employee_surname", "employee_gender", "employee_age",
        "employee_contacts", "employee_address", "employee_specialization",
        "employee_degree", "employee_email", "employee_password"
    ]

    # Validate request payload
    if not all(field in data for field in required_fields):
        return json({"error": "Missing required fields"}, status=400)

    # Hash the password
    hashed_password = sha256(data["employee_password"].encode()).hexdigest()

    # Insert employee data into the database
    try:
        pool = await aiomysql.create_pool(**DB_CONFIG)
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    """
                    INSERT INTO Employees (
                        employee_name, employee_surname, employee_gender, employee_age,
                        employee_contacts, employee_address, employee_specialization,
                        employee_degree, employee_email, employee_password
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        data["employee_name"],
                        data["employee_surname"],
                        data["employee_gender"],
                        data["employee_age"],
                        data["employee_contacts"],
                        data["employee_address"],
                        data["employee_specialization"],
                        data["employee_degree"],
                        data["employee_email"],
                        hashed_password,
                    )
                )
                await conn.commit()
        pool.close()
        await pool.wait_closed()

        return json({"message": "Employee registered successfully!"})

    except Exception as e:
        return json({"error": str(e)}, status=500)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
