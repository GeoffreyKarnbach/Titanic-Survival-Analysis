import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DecisionTreeComponent } from './components/pages/decision-tree/decision-tree.component';
import { StartPageComponent } from './components/pages/start-page/start-page.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { PassengerFormComponent } from './components/shared/passenger-form/passenger-form.component';
import { NavbarComponent } from './components/shared';

@NgModule({
  declarations: [
    AppComponent,
    DecisionTreeComponent,
    StartPageComponent,
    PassengerFormComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    CommonModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
