import { useState } from 'react';
import { Header } from '../components/Header';
import { ChatInput } from '../components/ChatInput';
import { AgentTimeline } from '../components/AgentTimeline';
import { DestinationCard } from '../components/DestinationCard';
import { ItineraryCard } from '../components/ItineraryCard';
import { BudgetCard } from '../components/BudgetCard';
import { usePlanner } from '../hooks/usePlanner';

export const Home = () => {
  const { generatePlan, isGenerating, planData, history, isHistoryLoading, historyError, clearHistory, isClearingHistory } = usePlanner();
  const [showResults, setShowResults] = useState(false);

  const handleSubmit = (query: string) => {
    setShowResults(false);
    generatePlan(query, {
      onSuccess: () => {
        setShowResults(true);
      },
    });
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        <Header />
        <ChatInput onSubmit={handleSubmit} isLoading={isGenerating} />

        {isGenerating && (
          <div className="text-center py-8">
            <p className="text-gray-600 text-lg">Generating your trip plan...</p>
          </div>
        )}

        {showResults && planData && (
          <>
            <AgentTimeline agentsUsed={planData.agents_used} />
            {planData.destination && <DestinationCard destination={planData.destination} />}
            {planData.itinerary && <ItineraryCard itinerary={planData.itinerary} />}
            {planData.budget && <BudgetCard budget={planData.budget} />}
          </>
        )}

        {!isHistoryLoading && !historyError && history && history.length > 0 && (
          <div className="mt-12 p-6 bg-white border border-gray-200 rounded-lg shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-xl font-bold text-blue-600">History</h3>
              <button
                onClick={() => clearHistory()}
                disabled={isClearingHistory}
                className="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 disabled:bg-gray-400 transition-colors"
              >
                {isClearingHistory ? 'Clearing...' : 'Clear History'}
              </button>
            </div>
            <div className="space-y-3">
              {history.map((item) => (
                <div
                  key={item.id}
                  className="p-4 bg-gray-50 rounded-lg border border-gray-200"
                >
                  <p className="text-gray-800 font-medium">{item.query}</p>
                  <p className="text-sm text-gray-500 mt-1">
                    Agents: {item.agents_used.join(', ')} •
                    {new Date(item.created_at).toLocaleString()}
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
