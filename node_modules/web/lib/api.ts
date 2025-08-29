const API_URL = process.env.API_URL || 'http://localhost:8000';

export type CreateItinerary = {
  title: string;
  traveler_type: 'solo' | 'couple' | 'family' | 'business';
  days: number;
  places: any[];
};

export async function listItineraries({ limit = 20, offset = 0 } = {}) {
  const res = await fetch(`${API_URL}/v1/itineraries?limit=${limit}&offset=${offset}`);
  if (!res.ok) throw new Error('Failed to fetch itineraries');
  return res.json();
}

export async function createItinerary(payload: CreateItinerary) {
  const res = await fetch(`${API_URL}/v1/itineraries`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error('Failed to create itinerary');
  return res.json();
}

export async function getItinerary(id: string) {
  const res = await fetch(`${API_URL}/v1/itineraries/${id}`);
  if (!res.ok) throw new Error('Itinerary not found');
  return res.json();
}

export async function updateItinerary(id: string, patch: Partial<CreateItinerary>) {
  const res = await fetch(`${API_URL}/v1/itineraries/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(patch),
  });
  if (!res.ok) throw new Error('Failed to update itinerary');
  return res.json();
}

export async function deleteItinerary(id: string) {
  const res = await fetch(`${API_URL}/v1/itineraries/${id}`, {
    method: 'DELETE',
  });
  if (!res.ok) throw new Error('Failed to delete itinerary');
  return true;
}
