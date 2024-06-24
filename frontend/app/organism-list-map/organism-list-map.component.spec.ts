import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OrganismListMapComponent } from './organism-list-map.component';

describe('OrganismListMapComponent', () => {
  let component: OrganismListMapComponent;
  let fixture: ComponentFixture<OrganismListMapComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OrganismListMapComponent]
    });
    fixture = TestBed.createComponent(OrganismListMapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
