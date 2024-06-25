import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable, of } from 'rxjs';

import { CommonService } from '@geonature_common/service/common.service';

import { Organism, OrganismFeature } from '../models/organism';
import { OrganismStoreService } from '../data.service';

@Injectable({ providedIn: 'root' })
export class OrganismResolver implements Resolve<OrganismFeature> {
  constructor(
    private service: OrganismStoreService,
    private commonService: CommonService,
    private router: Router
  ) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<OrganismFeature> {
    return this.service.getOrganism(+route.paramMap.get('id_organism')).catch((error) => {
      if (error.status == 404) {
        this.commonService.translateToaster('warning', 'Organisme introuvable');
      }
      // this.router.navigate(['/organisms']);
      return of(null);
    });
  }
}
