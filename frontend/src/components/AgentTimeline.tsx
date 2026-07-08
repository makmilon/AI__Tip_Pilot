interface AgentTimelineProps {
  agentsUsed: string[];
}

export const AgentTimeline = ({ agentsUsed }: AgentTimelineProps) => {
  return (
    <div className="mb-8">
      <h3 className="text-lg font-semibold mb-4">Agent Activity</h3>
      <div className="space-y-2">
        {agentsUsed.map((agent, index) => (
          <div
            key={index}
            className="flex items-center gap-3 p-3 bg-green-50 border border-green-200 rounded-lg"
          >
            <div className="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center text-white text-sm">
              ✓
            </div>
            <span className="text-green-700">{agent} Agent</span>
          </div>
        ))}
      </div>
    </div>
  );
};
