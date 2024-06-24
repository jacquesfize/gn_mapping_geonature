import { Injectable } from '@angular/core';
import { ConfigService } from '@geonature/services/config.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Organism, OrganismFeature, OrganismFeatureCollection } from './models/organism';
import { Observable } from 'rxjs';
import { ModuleConfig } from './module.config';


@Injectable()
export class OrganismStoreService {
    private module_prefix:string = ModuleConfig.MODULE_URL; 
    public constructor(private config_service: ConfigService, private http: HttpClient) {
        
    }

    getOrganism(id_organism: number) : Observable<OrganismFeature> {
        return this.http.get<OrganismFeature>(`${this.config_service.API_ENDPOINT}${this.module_prefix}/organisms/${id_organism}`);
    }

    updateOrganism(organism: Organism) : Observable<OrganismFeature> {
        return this.http.put<any>(`${this.config_service.API_ENDPOINT}${this.module_prefix}/organisms/${organism.id_organism}`, organism);
    }
    deleteOrganism(id_organism: number) : Observable<OrganismFeature> {
        return this.http.delete<any>(`${this.config_service.API_ENDPOINT}${this.module_prefix}/organisms/${id_organism}`);
    }

    createOrganism(organism: Organism) : Observable<OrganismFeature> {
        return this.http.post<any>(`${this.config_service.API_ENDPOINT}${this.module_prefix}/organisms`, organism);
    }
    getOrganisms() : Observable<OrganismFeatureCollection> {
        return this.http.get<OrganismFeatureCollection>(`${this.config_service.API_ENDPOINT}${this.module_prefix}/organisms`);
    }
}