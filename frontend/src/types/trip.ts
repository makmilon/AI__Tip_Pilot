export interface ItineraryDay {
  day: number;
  activities: string[];
}

export interface DestinationResponse {
  destination: string;
  reason: string;
  confidence?: number;
}

export interface ItineraryResponse {
  days: ItineraryDay[];
}

export interface BudgetResponse {
  flight: number;
  hotel: number;
  food: number;
  total: number;
  within_budget: boolean;
  confidence?: string;
  reason?: string;
}

export interface PlannerResponse {
  agents_used: string[];
  destination?: DestinationResponse;
  itinerary?: ItineraryResponse;
  budget?: BudgetResponse;
  warnings?: string[];
}

export interface HistoryItem {
  id: number;
  query: string;
  agents_used: string[];
  destination?: any;
  created_at: string;
}
