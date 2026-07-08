import { DestinationResponse } from '../types/trip';

interface DestinationCardProps {
  destination: DestinationResponse;
}

export const DestinationCard = ({ destination }: DestinationCardProps) => {
  return (
    <div className="mb-8 p-6 bg-white border border-gray-200 rounded-lg shadow-sm">
      <h3 className="text-xl font-bold text-blue-600 mb-2">Destination</h3>
      <p className="text-2xl font-semibold text-gray-800 mb-2">
        {destination.destination}
      </p>
      <p className="text-gray-600">{destination.reason}</p>
      {destination.confidence && (
        <p className="mt-2 text-sm text-gray-500">
          Confidence: {Math.round(destination.confidence * 100)}%
        </p>
      )}
    </div>
  );
};
