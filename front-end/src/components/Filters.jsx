export default function Filters({ setRange }) {
  return (
    <div>
      <label>Date Range:</label>
      <input type="date" onChange={(e) => setRange(r => ({...r, start: e.target.value}))} />
      <input type="date" onChange={(e) => setRange(r => ({...r, end: e.target.value}))} />
    </div>
  );
}
