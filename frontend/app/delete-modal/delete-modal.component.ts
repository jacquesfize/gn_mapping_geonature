import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CommonService } from '@geonature_common/service/common.service';
import { Router } from '@angular/router';
import { OrganismStoreService } from '../data.service';

@Component({
  selector: 'pnx-mapping-geonature-delete',
  templateUrl: './delete-modal.component.html',
})
export class ModalDeleteOrganism implements OnInit {
  @Input() idOrganism: number;
  @Input() c: any;
  @Output() onDelete = new EventEmitter();
  constructor(
    private _commonService: CommonService,
    private _organismDataService: OrganismStoreService,
    private _router: Router
  ) {}

  ngOnInit() {}

  deleteStation() {
    this.onDelete.emit();
    this._organismDataService.deleteOrganism(this.idOrganism).subscribe(
      (d) => {
        this._commonService.regularToaster('success', 'Organisme supprimé avec succès');

        this._router.navigate(['/mapping_geonature']);
      },
      () => {
        this.c();
      }
    );
  }
}
