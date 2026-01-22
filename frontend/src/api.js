const API_URL = "http://127.0.0.1:8000/api";

export async function getSchedules(serviceId) {
  const response = await fetch(
    `${API_URL}/services/${serviceId}/schedules/`
  );
  return response.json();
}
