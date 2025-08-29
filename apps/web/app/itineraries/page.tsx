

"use client";

import React, { useState, useEffect } from 'react';
import { listItineraries, createItinerary } from '@/lib/api';

export default function ItinerariesPage() {
  const [itineraries, setItineraries] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    async function fetchData() {
      try {
        const data = await listItineraries({ limit: 20, offset: 0 });
        setItineraries(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Itineraries</h1>
      <CreateForm onCreated={() => window.location.reload()} />
      {process.env.NODE_ENV === "development" && (
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded mb-4"
          onClick={async () => {
            await fetch("/api/sample-data", { method: "POST" });
            window.location.reload();
          }}
        >
          Sample Data
        </button>
      )}
      {loading ? (
        <div>Loading...</div>
      ) : error ? (
        <div className="text-red-600">{error}</div>
      ) : (
        <table className="min-w-full border mt-6">
          <thead>
            <tr>
              <th className="border px-4 py-2">Title</th>
              <th className="border px-4 py-2">Traveler Type</th>
              <th className="border px-4 py-2">Days</th>
            </tr>
          </thead>
          <tbody>
            {itineraries.map((it: any) => (
              <tr key={it.id}>
                <td className="border px-4 py-2">{it.title}</td>
                <td className="border px-4 py-2">{it.traveler_type}</td>
                <td className="border px-4 py-2">{it.days}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}


function CreateForm({ onCreated }: { onCreated: () => void }) {
  const [title, setTitle] = useState('');
  const [travelerType, setTravelerType] = useState<'solo' | 'couple' | 'family' | 'business'>('solo');
  const [days, setDays] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  async function handleSubmit(e: any) {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      await createItinerary({ title, traveler_type: travelerType, days, places: [] });
      onCreated();
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="mb-4" onSubmit={handleSubmit}>
      <div className="flex gap-4 items-end">
        <div>
          <label className="block text-sm">Title</label>
          <input className="border px-2 py-1" value={title} onChange={e => setTitle(e.target.value)} required />
        </div>
        <div>
          <label className="block text-sm">Traveler Type</label>
          <select className="border px-2 py-1" value={travelerType} onChange={e => setTravelerType(e.target.value as any)}>
            <option value="solo">Solo</option>
            <option value="couple">Couple</option>
            <option value="family">Family</option>
            <option value="business">Business</option>
          </select>
        </div>
        <div>
          <label className="block text-sm">Days</label>
          <input className="border px-2 py-1" type="number" min={1} max={60} value={days} onChange={e => setDays(Number(e.target.value))} required />
        </div>
        <button className="bg-blue-600 text-white px-4 py-2 rounded" type="submit" disabled={loading}>Create</button>
      </div>
      {error && <div className="text-red-600 mt-2">{error}</div>}
    </form>
  );
}
