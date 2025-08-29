import { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method !== 'POST') {
    return res.status(405).end();
  }
  // Call backend seed endpoint
  await fetch(process.env.API_URL + '/v1/seed', { method: 'POST' });
  res.status(200).json({ status: 'seeded' });
}
