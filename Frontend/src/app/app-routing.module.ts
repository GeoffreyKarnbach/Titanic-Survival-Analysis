import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DecisionTreeComponent, StartPageComponent } from './components';

const routes: Routes = [
  { path: 'decision-tree', component: DecisionTreeComponent },
  { path: '**', component: StartPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
