import React, { useState } from 'react';
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

function MapPanel({ wards }) {
  const [layer, setLayer] = useState('temperature');

  const getColor = (score) => {
    if (score < 30) return '#3498db'; // Blue
    if (score < 60) return '#f1c40f'; // Yellow
    if (score < 80) return '#e67e22'; // Orange
    return '#e74c3c'; // Red
  };

  return (
    <div className="bg-white rounded shadow p-4">
      <h2 className="text-xl font-semibold mb-2">Heat Hotspot Map</h2>
      <div className="mb-2">
        <label>Layer:</label>
        <select value={layer} onChange={e => setLayer(e.target.value)} className="ml-2 p-1 border rounded">
          <option value="temperature">Temperature</option>
          <option value="vegetation">Vegetation</option>
          <option value="builtup">Built-up</option>
          <option value="population">Population</option>
        </select>
      </div>
      <MapContainer center={[13.0827, 80.2707]} zoom={11} style={{ height: '300px', width: '100%' }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {wards.map(ward => (
          <GeoJSON key={ward.id} data={ward.geometry} style={{ color: getColor(ward.heat_score), weight: 2, fillOpacity: 0.6 }} />
        ))}
      </MapContainer>
    </div>
  );
}

export default MapPanel;
