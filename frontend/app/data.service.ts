import { Injectable } from '@angular/core';
import { ConfigService } from '@geonature/services/config.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Organism } from './models/organism';
import { Observable } from 'rxjs';


@Injectable()
export class OrganismStoreService {
    private module_prefix:string = "gn_mapping_geonature" 
    public constructor(private config_service: ConfigService, private http: HttpClient) {
        
    }

    getOrganism(id_organism: number) : Observable<Organism> {
        return this.http.get<Organism>(`${this.config_service.API_ENDPOINT}/${this.module_prefix}/organisms/${id_organism}`);
    }

    updateOrganism(organism: Organism) : Observable<Organism> {
        return this.http.put<any>(`${this.config_service.API_ENDPOINT}/${this.module_prefix}/organisms/${organism.id_organism}`, organism);
    }
    deleteOrganism(id_organism: number) : Observable<Organism> {
        return this.http.delete<any>(`${this.config_service.API_ENDPOINT}/${this.module_prefix}/organisms/${id_organism}`);
    }

    createOrganism(organism: Organism) : Observable<Organism> {
        return this.http.post<any>(`${this.config_service.API_ENDPOINT}/${this.module_prefix}/organisms`, organism);
    }
    getOrganisms() : Observable<Organism[]> {
        return this.http.get<Organism[]>(`${this.config_service.API_ENDPOINT}/${this.module_prefix}/organisms`);
    }
}