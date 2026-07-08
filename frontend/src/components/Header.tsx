export const Header = () => {
  return (
    <div className="text-center mb-8">
      <h1 className="text-5xl font-extrabold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-4">
        TripPilot AI
      </h1>
      <p className="text-xl text-gray-600 mb-2">Multi-Agent Travel Planner</p>
      <div className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-full shadow-lg">
        <span className="text-sm font-semibold uppercase tracking-wider">Developer:</span>
        <span className="text-lg font-bold">Milon Das</span>
      </div>
    </div>
  );
};
