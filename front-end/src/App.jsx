import { useEffect, useState } from "react";
import { fetchPrices, fetchEvents, fetchChangePoints } from "./api";
import PriceChart from "./components/PriceChart";
import Filters from "./components/FilterS";
import MetricsPanel from "./components/MetricsPanel";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changepoints, setChangepoints] = useState([]);
  const [range, setRange] = useState({});

  useEffect(() => {
    fetchPrices().then(res => setPrices(res.data));
    fetchEvents().then(res => setEvents(res.data));
    fetchChangePoints().then(res => setChangepoints(res.data));
  }, []);

  const filtered = prices.filter(p => {
    if (!range.start || !range.end) return true;
    return p.Date >= range.start && p.Date <= range.end;
  });

  return (
    <div>
      <h1>Brent Oil Dashboard</h1>

      <Filters setRange={setRange} />
      <MetricsPanel data={filtered} />
      <PriceChart
        data={filtered}
        events={events}
        changepoints={changepoints}
      />
    </div>
  );
}

export default App;
