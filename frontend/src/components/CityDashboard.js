import React, { useState, useEffect } from 'react';
import api from '../api';
import MapPanel from './MapPanel';
import TrendPanel from './TrendPanel';
import PredictionPanel from './PredictionPanel';
import RecommendationsPanel from './RecommendationsPanel';

function CityDashboard({ city, isAdmin, setCity }) {
  const [metrics, setMetrics] = useState({});
  const [wards, setWards] = useState([]);

  useEffect(() => {
    // Fetch city metrics
    api.get(`/cities/${city}`).then(res => {
      setMetrics(res.data);
    });
    // Fetch ward data
    api.get(`/wards?city=${city}`).then(res => {
      setWards(res.data);
    });
  }, [city]);

  return (
    <div>
      <div className="flex flex-col md:flex-row gap-4 mb-4">
        <div className="flex-1 bg-white rounded shadow p-4">
          <h2 className="text-xl font-semibold mb-2">Top Metrics</h2>
          <div>Current Avg Temp: {metrics.avg_temperature}</div>
          <div>Heat Risk Score: {metrics.heat_risk_score}</div>
          <div>Trend % Increase: {metrics.trend_increase}</div>
        </div>
        <div className="flex-1 bg-white rounded shadow p-4">
          <label htmlFor="city-select" className="block mb-2">Select City</label>
          <select id="city-select" value={city} onChange={e => setCity(e.target.value)} className="w-full p-2 border rounded">
            <option value="Chennai">Chennai</option>
            {/* Add more cities as needed */}
          </select>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <MapPanel wards={wards} />
        <TrendPanel city={city} />
        <PredictionPanel city={city} />
        <RecommendationsPanel wards={wards} />
      </div>
    </div>
  );
}

export default CityDashboard;
