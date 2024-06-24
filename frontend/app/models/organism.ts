export interface Type {
    id_type: number;
    nom: string;
}

export interface Organism {
    id_organism: number;
    nom: string;
    description: string;
    adresse: string;
    type_: Type;
    url: string;
    geometry?: any;
    cruved: any;

}

export interface OrganismFeature{
    type: string;
    properties: Organism;
    geometry: {
        type: string;
        coordinates: [number, number];
      };
}

export interface OrganismFeatureCollection{
    type: 'FeatureCollection';
    features: OrganismFeature[];
}