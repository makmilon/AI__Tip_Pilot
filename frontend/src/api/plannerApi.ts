import api from './api';
import { PlannerResponse, HistoryItem } from '../types/trip';

export const generatePlan = async (query: string): Promise<PlannerResponse> => {
  const response = await api.post<PlannerResponse>('/api/planner', { query });
  return response.data;
};

export const getHistory = async (): Promise<HistoryItem[]> => {
  const response = await api.get<HistoryItem[]>('/api/history');
  return response.data;
};

export const clearHistory = async (): Promise<void> => {
  await api.delete('/api/history');
};
