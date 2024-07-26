import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnsembleMethodsComponent } from './ensemble-methods.component';

describe('EnsembleMethodsComponent', () => {
  let component: EnsembleMethodsComponent;
  let fixture: ComponentFixture<EnsembleMethodsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EnsembleMethodsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EnsembleMethodsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
