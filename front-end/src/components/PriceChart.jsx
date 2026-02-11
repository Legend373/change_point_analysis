import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine
} from "recharts";

export default function PriceChart({ data, events, changepoints }) {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="Price" stroke="#2563eb" />

        {changepoints.map((cp, i) => (
          <ReferenceLine
            key={i}
            x={cp.date}
            stroke="red"
            label="Change Point"
          />
        ))}

        {events.map((e, i) => (
          <ReferenceLine
            key={i}
            x={e.Date}
            stroke="green"
            label={e.Event}
          />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
}
