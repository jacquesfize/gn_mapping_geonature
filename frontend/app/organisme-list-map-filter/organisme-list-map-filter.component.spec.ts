import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganismeListMapFilterComponent } from './organisme-list-map-filter.component';

describe('OrganismeListMapFilterComponent', () => {
  let component: OrganismeListMapFilterComponent;
  let fixture: ComponentFixture<OrganismeListMapFilterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OrganismeListMapFilterComponent]
    });
    fixture = TestBed.createComponent(OrganismeListMapFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
