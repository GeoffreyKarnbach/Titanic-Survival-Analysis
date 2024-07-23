import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DecisionTreeComponent, DecisionTreeV2Component, StartPageComponent } from './components';

const routes: Routes = [
  { path: 'decision-tree-v1', component: DecisionTreeComponent },
  { path: 'decision-tree-v2', component: DecisionTreeV2Component },
  { path: '**', component: StartPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
