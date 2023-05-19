import React, { useState } from 'react';

const AddCountry = () => {
  const [countryName, setCountryName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/add_country', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({name: countryName})
    });
    const data = await response.json();
    alert(data.status);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Country Name:
        <input type="text" value={countryName} onChange={(e) => setCountryName(e.target.value)} />
      </label>
      <input type="submit" value="Add Country" />
    </form>
  );
}

export default AddCountry;
