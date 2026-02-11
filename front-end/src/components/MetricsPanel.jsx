export default function MetricsPanel({ data }) {
  const avg = data.reduce((a, b) => a + b.Price, 0) / data.length;

  return (
    <div>
      <h3>Average Price</h3>
      <p>${avg.toFixed(2)}</p>
    </div>
  );
}
