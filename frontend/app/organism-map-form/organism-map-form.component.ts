import { Component } from '@angular/core';
import { Organism } from '../models/organism';
import { OrganismStoreService } from '../data.service';
import { ActivatedRoute, Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ConfigService } from '@geonature/services/config.service';
import {
  UntypedFormBuilder,
  UntypedFormGroup,
  UntypedFormControl,
  Validators,
  AbstractControl,
  UntypedFormArray,
} from '@angular/forms';

@Component({
  selector: 'pnx-organism-map-form',
  templateUrl: './organism-map-form.component.html',
  styleUrls: ['./organism-map-form.component.scss'],
})
export class OrganismMapFormComponent {
  public MAP_SMALL_HEIGHT = '50vh !important;';
  public MAP_FULL_HEIGHT = '87vh';
  public mapHeight = this.MAP_FULL_HEIGHT;
  public markerCoordinates;
  public organismForm: UntypedFormGroup;
  public isEdit: boolean = false;
  private id_organism: Number;

  constructor(
    private dataService: OrganismStoreService,
    private _route: ActivatedRoute,
    private _ngbModal: NgbModal,
    private _fb: UntypedFormBuilder,
    public config: ConfigService,
    private _router: Router
  ) {
    this.initOrganismForm();
    this._route.data.subscribe(({ organism }) => {
      if (organism) {
        this.id_organism = organism.properties.id_organism;
        this.isEdit = true;
        this.organismForm.patchValue(organism.properties);
        this.markerCoordinates = organism.geometry.coordinates;
        this.patchGeoValue(organism.geometry);
      }
    });
  }

  submit() {
    if (this.isEdit) {
      this.dataService.updateOrganism(this.organismForm.value, this.id_organism).subscribe(() => {
        this._router.navigate(['/mapping_geonature']);
      });
    } else {
      this.dataService.createOrganism(this.organismForm.value).subscribe(() => {
        this._router.navigate(['/mapping_geonature']);
      });
    }
  }

  patchGeoValue(geom) {
    this.organismForm.patchValue({ geometry: geom.geometry });
  }

  initOrganismForm() {
    const organismForm = this._fb.group({
      id_organism: null,
      nom: [null, Validators.required],
      adresse: [null, Validators.required],
      description: [null, Validators.required],
      url: [null, Validators.required],
      geometry: [null, Validators.required],
      // type: [null, Validators.required],
      id_type: 1,
    });

    this.organismForm = organismForm;
  }

  resetAllForm() {
    this.organismForm.reset();
  }

  ngAfterViewInit() {
    // this.markerCoordinates = station.geometry.coordinates;
  }
}
