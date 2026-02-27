import React from 'react';

function RecommendationsPanel({ wards }) {
  return (
    <div className="bg-white rounded shadow p-4">
      <h2 className="text-xl font-semibold mb-2">Smart Recommendations</h2>
      <ul>
        {wards.map(ward => {
          let recs = [];
          if (ward.heat_score > 70 && ward.ndvi_score < 0.3) {
            recs.push('🌳 High Priority Green Intervention Zone');
          }
          if (ward.builtup_index > 0.6 && ward.avg_temperature > 33) {
            recs.push('🏠 Cool Roof Recommended');
          }
          return (
            <li key={ward.id} className="mb-2">
              <span className="font-semibold">Ward {ward.ward_name}:</span>
              {recs.length ? (
                <ul className="ml-4 list-disc">
                  {recs.map((r, i) => <li key={i}>{r}</li>)}
                </ul>
              ) : (
                <span className="ml-2 text-gray-500">No intervention needed</span>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default RecommendationsPanel;
