import { useEffect, useState } from "react";
import { getSchedules } from "../api";

function ScheduleList({ serviceId }) {
  const [schedules, setSchedules] = useState([]);

  useEffect(() => {
    getSchedules(serviceId).then(setSchedules);
  }, [serviceId]);

  return (
    <ul>
      {schedules.map(s => (
        <li key={s.id}>
          {s.date} {s.start_time}
        </li>
      ))}
    </ul>
  );
}

export default ScheduleList;
