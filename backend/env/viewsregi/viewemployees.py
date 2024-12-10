from sanic import Sanic
from sanic.response import json
import aiomysql

app = Sanic("EmployeeAPI")

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",   # Replace with your database username
    "password": "@Ndikumana2608!",  # Replace with your database password
    "db": "employees",     # Replace with your database name
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


@app.route("/viewemployees")
async def view_employees(request):
    """
    Endpoint to retrieve all employees from the database.
    """
    conn = await get_db_connection()
    async with conn.cursor() as cur:
        # Query to fetch all employees
        await cur.execute("SELECT * FROM Employees")
        employees = await cur.fetchall()

        # Column names for formatting the response
        columns = [
            "employee_id", "employee_name", "employee_surname", 
            "employee_gender", "employee_age", "employee_contacts",
            "employee_address", "employee_specialization", 
            "employee_degree", "employee_email", "employee_password"
        ]
        
        # Format the result as a list of dictionaries
        result = [dict(zip(columns, row)) for row in employees]
    
    conn.close()
    return json(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
