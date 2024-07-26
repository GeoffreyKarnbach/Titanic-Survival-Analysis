import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KNearestNeighborsComponent } from './k-nearest-neighbors.component';

describe('KNearestNeighborsComponent', () => {
  let component: KNearestNeighborsComponent;
  let fixture: ComponentFixture<KNearestNeighborsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [KNearestNeighborsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(KNearestNeighborsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
