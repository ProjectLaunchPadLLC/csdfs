import * as d3 from "d3";
import { useEffect, useRef } from "react";

export default function PhaseSpace({ data }) {
  const ref = useRef();

  useEffect(() => {
    if (!data) return;

    const svg = d3.select(ref.current);
    svg.selectAll("*").remove();

    svg
      .selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", d => d.state[0] * 50 + 200)
      .attr("cy", d => d.state[1] * 50 + 200)
      .attr("r", 5);
  }, [data]);

  return <svg ref={ref} width={400} height={400} />;
}
