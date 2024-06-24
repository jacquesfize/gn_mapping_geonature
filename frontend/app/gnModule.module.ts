import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { GN2CommonModule } from '@geonature_common/GN2Common.module';
import { OrganismListMapComponent } from './organism-list-map/organism-list-map.component';
import { OrganismMapFormComponent } from './organism-map-form/organism-map-form.component';
import { OrganismDetailsComponent } from './organism-details/organism-details.component';

// my module routing
const routes: Routes = [
    { path: '', component: OrganismListMapComponent },
    { path: 'edit', component: OrganismMapFormComponent },
    { path: 'create', component: OrganismMapFormComponent},
    { path: 'info', component: OrganismDetailsComponent}
];

@NgModule({
    declarations: [
        OrganismDetailsComponent,OrganismMapFormComponent,OrganismListMapComponent
    ],
    imports: [
        GN2CommonModule,
        CommonModule,
        RouterModule.forChild(routes),
    ],
    providers: [],
    bootstrap: [],
})
export class GeonatureModule { }