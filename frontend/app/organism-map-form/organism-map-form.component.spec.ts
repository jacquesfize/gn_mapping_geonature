import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganismMapFormComponent } from './organism-map-form.component';

describe('OrganismMapFormComponent', () => {
  let component: OrganismMapFormComponent;
  let fixture: ComponentFixture<OrganismMapFormComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OrganismMapFormComponent]
    });
    fixture = TestBed.createComponent(OrganismMapFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
