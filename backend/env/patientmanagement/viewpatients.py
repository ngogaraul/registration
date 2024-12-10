from sanic import Sanic
from sanic.response import json
import aiomysql

app = Sanic("patientsAPI")

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",   # Replace with your database username
    "password": "@Ndikumana2608!",  # Replace with your database password
    "db": "receptionist_db",     # Replace with your database name
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


@app.route("/viewpatients")
async def view_patients(request):
    """
    Endpoint to retrieve all employees from the database.
    """
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        # Query to fetch all employees
        await cur.execute("SELECT * FROM patients")
        employees = await cur.fetchall()

        # Column names for formatting the response
        columns =[
        "patient_name", "patient_surname", "insurance", "patient_age",
        "patient_gender", "patient_blood_group", "patient_contacts",
        "next_of_keen_contacts", "address"
    ]
        # Format the result as a list of dictionaries
        result = [dict(zip(columns, row)) for row in employees]
    
    conn.close()
    return json(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
