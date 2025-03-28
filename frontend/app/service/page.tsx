"use client";

import { useServices } from "@/lib/queries";

export default function ServicesPage() {
  const { data: services, isLoading, error } = useServices();

  if (isLoading) return <p>Chargement...</p>;
  if (error) return <p>Erreur de chargement des services.</p>;

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
