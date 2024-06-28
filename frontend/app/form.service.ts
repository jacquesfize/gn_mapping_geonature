import { Injectable } from '@angular/core';
import {
  UntypedFormBuilder,
  UntypedFormGroup,
  UntypedFormControl,
  Validators,
  AbstractControl,
  UntypedFormArray,
} from '@angular/forms';
import { NgbDateParserFormatter } from '@ng-bootstrap/ng-bootstrap';
import { FormService } from '@geonature_common/form/form.service';
import { DataFormService } from '@geonature_common/form/data-form.service';
import { ConfigService } from '@geonature/services/config.service';
import { OrganismStoreService } from './data.service';

@Injectable()
export class OcchabFormService {
  public organismForm: UntypedFormGroup;

  constructor(
    private _fb: UntypedFormBuilder,
    private _dateParser: NgbDateParserFormatter,
    private _gn_dataSerice: DataFormService,
    private _storeService: OrganismStoreService,
    private _formService: FormService,
    public config: ConfigService
  ) {
    this.organismForm = this.initOrganismForm();
  }

  initOrganismForm(): UntypedFormGroup {
    const organismForm = this._fb.group({
      id_organism: null,
      nom: [null, Validators.required],
      adresse: [null, Validators.required],
      description: [null, Validators.required],
      url: [null, Validators.required],
      type: [null, Validators.required],
    });

    return organismForm;
  }

  resetAllForm() {
    this.organismForm.reset();
  }
}
