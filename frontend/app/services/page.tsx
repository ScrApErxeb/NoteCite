"use client";

import { useEffect, useState } from "react";

export default function ServicesPage() {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await fetch("http://localhost:8000/api/services/");
        if (!response.ok) {
          throw new Error("Erreur lors de la récupération des services");
        }
        const data = await response.json();
        setServices(data);
        setLoading(false);
      } catch (error: any) {
        setError(error.message);
        setLoading(false);
      }
    };

    fetchServices();
  }, []);

  if (loading) return <p>Chargement...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Liste des Services</h1>
      <ul>
        {services.map((service: any) => (
          <li key={service.id}>
            <strong>{service.name}</strong> - {service.category}
          </li>
        ))}
      </ul>
    </div>
  );
}
