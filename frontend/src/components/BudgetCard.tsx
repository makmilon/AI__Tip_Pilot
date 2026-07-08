import { BudgetResponse } from '../types/trip';

interface BudgetCardProps {
  budget: BudgetResponse;
}

export const BudgetCard = ({ budget }: BudgetCardProps) => {
  return (
    <div className="mb-8 p-6 bg-white border border-gray-200 rounded-lg shadow-sm">
      <h3 className="text-xl font-bold text-blue-600 mb-4">Budget</h3>
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="p-4 bg-gray-50 rounded-lg">
          <p className="text-sm text-gray-600">Flight</p>
          <p className="text-xl font-semibold">₹{budget.flight}</p>
        </div>
        <div className="p-4 bg-gray-50 rounded-lg">
          <p className="text-sm text-gray-600">Hotel</p>
          <p className="text-xl font-semibold">₹{budget.hotel}</p>
        </div>
        <div className="p-4 bg-gray-50 rounded-lg">
          <p className="text-sm text-gray-600">Food</p>
          <p className="text-xl font-semibold">₹{budget.food}</p>
        </div>
        <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
          <p className="text-sm text-blue-600">Total</p>
          <p className="text-xl font-bold text-blue-700">₹{budget.total}</p>
        </div>
      </div>
      <div
        className={`p-3 rounded-lg ${
          budget.within_budget ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'
        }`}
      >
        <p
          className={`font-semibold ${
            budget.within_budget ? 'text-green-700' : 'text-red-700'
          }`}
        >
          {budget.within_budget ? '✓ Within Budget' : '✗ Exceeds Budget'}
        </p>
      </div>
      {budget.confidence && budget.reason && (
        <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
          <p className="text-sm text-yellow-800">
            <span className="font-semibold">Confidence: {budget.confidence}</span> - {budget.reason}
          </p>
        </div>
      )}
    </div>
  );
};
