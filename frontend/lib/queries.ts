const fetchServices = async () => {
  try {
    const res = await fetch("/api/services/", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (!res.ok) {
      throw new Error(`Erreur HTTP ${res.status}`);
    }

    return await res.json();
  } catch (error) {
    console.error("Erreur de récupération des services :", error);
    throw error;
  }
};
