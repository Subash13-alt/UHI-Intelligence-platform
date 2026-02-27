import React, { useState, useEffect } from 'react';
import CityDashboard from './CityDashboard';
import Auth from './Auth';

function Dashboard() {
  const [city, setCity] = useState('Chennai');
  const [isAdmin, setIsAdmin] = useState(false);

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-3xl font-bold text-green-800">Urban Heat Island Intelligence Platform</h1>
        <Auth setIsAdmin={setIsAdmin} />
      </div>
      <CityDashboard city={city} isAdmin={isAdmin} setCity={setCity} />
    </div>
  );
}

export default Dashboard;
