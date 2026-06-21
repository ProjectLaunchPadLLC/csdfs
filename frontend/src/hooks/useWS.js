import { useEffect, useState } from "react";

export default function useWS(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(url);

    ws.onmessage = (e) => {
      setData(JSON.parse(e.data));
    };

    return () => ws.close();
  }, [url]);

  return data;
}
