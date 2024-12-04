
import React, { useState, useEffect } from 'react';
import './App.css';
import EmployeeForm from './components/EmployeeForm';
import EmployeeList from './components/EmployeeList';
import { fetchEmployees, addEmployee, updateEmployee, deleteEmployee } from './services/api';

const App = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetchAllEmployees();
  }, []);

  const fetchAllEmployees = async () => {
    try {
      const data = await fetchEmployees();
      setEmployees(data);
    } catch (error) {
      console.error('Error fetching employees:', error);
    }
  };

  const handleAddEmployee = async (formData) => {
    try {
      await addEmployee(formData);
      fetchAllEmployees();
    } catch (error) {
      console.error('Error adding employee:', error);
    }
  };

  const handleUpdateEmployee = async (id, updatedData) => {
    try {
      await updateEmployee(id, updatedData);
      fetchAllEmployees();
    } catch (error) {
      console.error('Error updating employee:', error);
    }
  };

  const handleDeleteEmployee = async (id) => {
    try {
      await deleteEmployee(id);
      fetchAllEmployees();
    } catch (error) {
      console.error('Error deleting employee:', error);
    }
  };

  return (
    <div className="App">
      <h1>Employee Management</h1>
      <EmployeeForm onAddEmployee={handleAddEmployee} />
      <EmployeeList 
        employees={employees} 
        onUpdateEmployee={handleUpdateEmployee} 
        onDeleteEmployee={handleDeleteEmployee} 
      />
    </div>
  );
};

export default App;
