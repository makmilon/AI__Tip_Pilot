import { ItineraryResponse } from '../types/trip';

interface ItineraryCardProps {
  itinerary: ItineraryResponse;
}

export const ItineraryCard = ({ itinerary }: ItineraryCardProps) => {
  return (
    <div className="mb-8 p-6 bg-white border border-gray-200 rounded-lg shadow-sm">
      <h3 className="text-xl font-bold text-blue-600 mb-4">Itinerary</h3>
      <div className="space-y-4">
        {itinerary.days.map((day) => (
          <div key={day.day} className="p-4 bg-gray-50 rounded-lg">
            <h4 className="font-semibold text-gray-800 mb-2">Day {day.day}</h4>
            <ul className="list-disc list-inside text-gray-600 space-y-1">
              {day.activities.map((activity, index) => (
                <li key={index}>{activity}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};
