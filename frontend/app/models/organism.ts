export interface Type {
    id_type: number;
    nom: string;
}

export interface Organism {
    id_organism: number;
    nom: string;
    description: string;
    type: Type;
    url: string;
    geometry: {
        type: string;
        coordinates: [number, number];
      };
}