import React, { useState } from 'react';

const EmployeeForm = ({ onAddEmployee }) => {
  const [formData, setFormData] = useState({
    employee_name: '',
    employee_surname: '',
    employee_gender: 'Male',
    employee_age: '',
    employee_contacts: '',
    employee_address: '',
    employee_specialization: '',
    employee_degree: 'bacholar',
    employee_email: '',
    employee_password: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAddEmployee(formData);
    setFormData({
      employee_name: '',
      employee_surname: '',
      employee_gender: 'Male',
      employee_age: '',
      employee_contacts: '',
      employee_address: '',
      employee_specialization: '',
      employee_degree: 'bacholar',
      employee_email: '',
      employee_password: '',
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add New Employee</h2>
      <input name="employee_name" placeholder="Name" value={formData.employee_name} onChange={handleInputChange} required />
      <input name="employee_surname" placeholder="Surname" value={formData.employee_surname} onChange={handleInputChange} required />
      <select name="employee_gender" value={formData.employee_gender} onChange={handleInputChange}>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
        <option value="other">Other</option>
      </select>
      <input name="employee_age" type="number" placeholder="Age" value={formData.employee_age} onChange={handleInputChange} required />
      <input name="employee_contacts" placeholder="Contacts" value={formData.employee_contacts} onChange={handleInputChange} />
      <textarea name="employee_address" placeholder="Address" value={formData.employee_address} onChange={handleInputChange} required />
      <input name="employee_specialization" placeholder="Specialization" value={formData.employee_specialization} onChange={handleInputChange} />
      <select name="employee_degree" value={formData.employee_degree} onChange={handleInputChange}>
        <option value="bacholar">Bachelor</option>
        <option value="masters">Masters</option>
        <option value="PHD">PhD</option>
        <option value="certificate">Certificate</option>
      </select>
      <input name="employee_email" type="email" placeholder="Email" value={formData.employee_email} onChange={handleInputChange} required />
      <input name="employee_password" type="password" placeholder="Password" value={formData.employee_password} onChange={handleInputChange} required />
      <button type="submit">Add Employee</button>
    </form>
  );
};

export default EmployeeForm;
