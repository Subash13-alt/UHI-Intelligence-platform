import React, { useEffect, useState } from 'react';
import api from '../api';

function PredictionPanel({ city }) {
  const [prediction, setPrediction] = useState({});

  useEffect(() => {
    api.post(`/predict/${city}`).then(res => {
      setPrediction(res.data);
    });
  }, [city]);

  return (
    <div className="bg-white rounded shadow p-4">
      <h2 className="text-xl font-semibold mb-2">5-Year Heat Prediction</h2>
      <div>2030 Heat Score: {prediction.heat_score_2030}</div>
      <div>2035 Heat Score: {prediction.heat_score_2035}</div>
      <div>R² Score: {prediction.r2_score}</div>
      <div>Confidence: {prediction.confidence}</div>
    </div>
  );
}

export default PredictionPanel;
