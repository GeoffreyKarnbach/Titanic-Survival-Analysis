import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogisticRegressionComponent } from './logistic-regression.component';

describe('LogisticRegressionComponent', () => {
  let component: LogisticRegressionComponent;
  let fixture: ComponentFixture<LogisticRegressionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LogisticRegressionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LogisticRegressionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
