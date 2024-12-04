import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/register', // Adjust the base URL as needed
});

export const fetchEmployees = async () => {
  try {
    const response = await API.get('/employees');
    return response.data;
  } catch (error) {
    console.error('Error fetching employees:', error);
    throw error;
  }
};

export const addEmployee = async (formData) => {
  try {
    const response = await API.post('/employees', formData);
    return response.data;
  } catch (error) {
    console.error('Error adding employee:', error);
    throw error;
  }
};

export const updateEmployee = async (id, updatedData) => {
  try {
    const response = await API.put(`/employees/${id}`, updatedData);
    return response.data;
  } catch (error) {
    console.error('Error updating employee:', error);
    throw error;
  }
};

export const deleteEmployee = async (id) => {
  try {
    const response = await API.delete(`/employees/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting employee:', error);
    throw error;
  }
};
