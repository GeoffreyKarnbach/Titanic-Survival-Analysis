import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SupportVectorMachinesComponent } from './support-vector-machines.component';

describe('SupportVectorMachinesComponent', () => {
  let component: SupportVectorMachinesComponent;
  let fixture: ComponentFixture<SupportVectorMachinesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SupportVectorMachinesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SupportVectorMachinesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
