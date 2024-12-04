import React from 'react';

const EmployeeList = ({ employees, onUpdateEmployee, onDeleteEmployee }) => {
  return (
    <div>
      <h2>Employee List</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Surname</th>
            <th>Gender</th>
            <th>Age</th>
            <th>Contacts</th>
            <th>Address</th>
            <th>Specialization</th>
            <th>Degree</th>
            <th>Email</th>
           
          </tr>
        </thead>
        <tbody>
          {employees.map((emp) => (
            <tr key={emp.employee_id}>
              <td>{emp.employee_name}</td>
              <td>{emp.employee_surname}</td>
              <td>{emp.employee_gender}</td>
              <td>{emp.employee_age}</td>
              <td>{emp.employee_contacts}</td>
              <td>{emp.employee_address}</td>
              <td>{emp.employee_specialization}</td>
              <td>{emp.employee_degree}</td>
              <td>{emp.employee_email}</td>
              <td>
                <button onClick={() => onUpdateEmployee(emp.employee_id)}>Update</button>
                <button onClick={() => onDeleteEmployee(emp.employee_id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeList;
