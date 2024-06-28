import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { GN2CommonModule } from '@geonature_common/GN2Common.module';
import { OrganismListMapComponent } from './organism-list-map/organism-list-map.component';
import { OrganismMapFormComponent } from './organism-map-form/organism-map-form.component';
import { OrganismDetailsComponent } from './organism-details/organism-details.component';
import { OrganismResolver } from './resolvers/organism.resolver';
import { OrganismStoreService } from './data.service';
import { ModalDeleteOrganism } from './delete-modal/delete-modal.component';

// my module routing
const routes: Routes = [
  { path: '', component: OrganismListMapComponent },
  { path: 'add', component: OrganismMapFormComponent },
  {
    path: 'edit/:id_organism',
    component: OrganismMapFormComponent,
    resolve: { organism: OrganismResolver },
  },
  { path: 'create', component: OrganismMapFormComponent },
  {
    path: 'info/:id_organism',
    component: OrganismDetailsComponent,
    resolve: { organism: OrganismResolver },
  },
];

@NgModule({
  declarations: [
    OrganismDetailsComponent,
    OrganismMapFormComponent,
    OrganismListMapComponent,
    ModalDeleteOrganism,
  ],
  imports: [GN2CommonModule, CommonModule, RouterModule.forChild(routes)],
  providers: [OrganismResolver, OrganismStoreService],
  bootstrap: [],
})
export class GeonatureModule {}
