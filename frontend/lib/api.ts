// lib/api.ts

const API_URL = "http://localhost:8000/api/services/";

interface Service {
  id: number;
  name: string;
  category: string;
  location: string;
  created_at: string;
}

export const fetchServices = async (): Promise<Service[]> => {
  try {
    const res = await fetch("http://localhost:8000/api/services/");

    if (!res.ok) {
      throw new Error(`Erreur HTTP ${res.status}`);
    }

    const data = await res.json();
    return data;
  } catch (error) {
    console.error("Erreur lors de la récupération des services:", error);
    throw error;
  }
};
