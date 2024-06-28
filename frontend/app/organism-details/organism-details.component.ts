import { Component } from '@angular/core';
import { OrganismStoreService } from '../data.service';
import { ActivatedRoute } from '@angular/router';
import { Organism } from '../models/organism';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'pnx-organism-details',
  templateUrl: './organism-details.component.html',
  styleUrls: ['./organism-details.component.scss']
})
export class OrganismDetailsComponent {

  public organism: Organism;
  organism_info: any;

  constructor(private service: OrganismStoreService,private _route: ActivatedRoute,private _ngbModal: NgbModal) {
    this._route.data.subscribe(({ organism }) => {
      this.organism = organism;
      this.organism_info = organism.properties;
    });
  }

  openDeleteModal(modalDelete){
    this._ngbModal.open(modalDelete);
  }

  
}
