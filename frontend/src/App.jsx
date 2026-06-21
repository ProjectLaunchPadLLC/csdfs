import PhaseSpace from "./components/PhaseSpace";
import Spectrum from "./components/Spectrum";
import useWS from "./hooks/useWS";

export default function App() {
  const data = useWS("ws://localhost:8000/ws");

  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr" }}>
      <PhaseSpace data={data} />
      <Spectrum data={data} />
    </div>
  );
}
