import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecisionTreeV2Component } from './decision-tree-v2.component';

describe('DecisionTreeV2Component', () => {
  let component: DecisionTreeV2Component;
  let fixture: ComponentFixture<DecisionTreeV2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DecisionTreeV2Component]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DecisionTreeV2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
