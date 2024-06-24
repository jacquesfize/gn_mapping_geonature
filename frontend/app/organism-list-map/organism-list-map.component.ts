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
  public deletedOne: Organism;

  constructor(private _organismeStoreService: OrganismStoreService, private _ngbModal: NgbModal) {
    this._organismeStoreService.getOrganisms().subscribe((organismes) => {
      this.organismes = organismes;
      console.log(this.organismes);
    });
  }

  openDeleteModal(organism, deleteModal) {
    this.deletedOne = organism;
    this._ngbModal.open(deleteModal);
  }
}
