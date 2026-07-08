import { useMutation, useQuery, useQueryClient } from 'react-query';
import { generatePlan, getHistory, clearHistory } from '../api/plannerApi';

export const usePlanner = () => {
  const queryClient = useQueryClient();

  const planMutation = useMutation(generatePlan, {
    onSuccess: () => {
      queryClient.invalidateQueries('history');
    },
  });

  const clearHistoryMutation = useMutation(clearHistory, {
    onSuccess: () => {
      queryClient.invalidateQueries('history');
    },
  });

  const historyQuery = useQuery('history', getHistory, {
    retry: 1,
  });

  return {
    generatePlan: planMutation.mutate,
    isGenerating: planMutation.isLoading,
    planData: planMutation.data,
    planError: planMutation.error,
    history: historyQuery.data,
    isHistoryLoading: historyQuery.isLoading,
    historyError: historyQuery.error,
    clearHistory: clearHistoryMutation.mutate,
    isClearingHistory: clearHistoryMutation.isLoading,
  };
};
