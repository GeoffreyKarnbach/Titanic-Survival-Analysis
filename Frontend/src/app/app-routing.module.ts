import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DecisionTreeComponent, EnsembleMethodsComponent, KNearestNeighborsComponent, LogisticRegressionComponent, PredictionComponent, StartPageComponent, SupportVectorMachinesComponent } from './components';

const routes: Routes = [
  { path: 'decision-tree', component: DecisionTreeComponent },
  { path: 'support-vector-machines', component: SupportVectorMachinesComponent },
  { path: 'ensemble-methods', component: EnsembleMethodsComponent },
  { path: 'k-nearest-neighbors', component: KNearestNeighborsComponent },
  { path: 'logistic-regression', component: LogisticRegressionComponent },
  { path: 'prediction', component: PredictionComponent },
  { path: '', component: StartPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
