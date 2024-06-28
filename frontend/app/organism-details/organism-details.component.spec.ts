import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganismDetailsComponent } from './organism-details.component';

describe('OrganismDetailsComponent', () => {
  let component: OrganismDetailsComponent;
  let fixture: ComponentFixture<OrganismDetailsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OrganismDetailsComponent]
    });
    fixture = TestBed.createComponent(OrganismDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
