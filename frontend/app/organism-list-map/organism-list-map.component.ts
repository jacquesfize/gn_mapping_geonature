import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { OrganismStoreService } from '../data.service';
import { Organism, OrganismFeatureCollection } from '../models/organism';

@Component({
  selector: 'pnx-organism-list-map',
  templateUrl: './organism-list-map.component.html',
  styleUrls: ['./organism-list-map.component.scss'],
})
export class OrganismListMapComponent {
  public organismes: OrganismFeatureCollection;
  public deleteIdOrganism: Organism;

  constructor(private _organismeStoreService: OrganismStoreService, private _ngbModal: NgbModal) {
    this._organismeStoreService.getOrganisms().subscribe((organismes) => {
      this.organismes = organismes;
    });
  }

  openDeleteModal(id_organism, deleteModal) {
    this.deleteIdOrganism = id_organism;
    this._ngbModal.open(deleteModal);
  }
}
