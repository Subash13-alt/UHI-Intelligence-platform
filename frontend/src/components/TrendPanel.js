import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import api from '../api';

function TrendPanel({ city }) {
  const [trendData, setTrendData] = useState({ years: [], temps: [] });

  useEffect(() => {
    api.get(`/temperature/trend/${city}`).then(res => {
      setTrendData(res.data);
    });
  }, [city]);

  const data = {
    labels: trendData.years,
    datasets: [
      {
        label: 'Avg Temperature',
        data: trendData.temps,
        borderColor: '#16a34a',
        backgroundColor: 'rgba(22,163,74,0.2)',
      },
    ],
  };

  return (
    <div className="bg-white rounded shadow p-4">
      <h2 className="text-xl font-semibold mb-2">Temperature Trend (10 Years)</h2>
      <Line data={data} />
      <div className="mt-2">% Increase: {trendData.percent_increase}</div>
    </div>
  );
}

export default TrendPanel;
