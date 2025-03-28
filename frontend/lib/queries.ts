import { useQuery } from "@tanstack/react-query";
import { api } from "./api";

export const useServices = () => {
  return useQuery({
    queryKey: ["services"],
    queryFn: async () => {
      const { data } = await api.get("/services/");
      return data;
    },
  });
};
