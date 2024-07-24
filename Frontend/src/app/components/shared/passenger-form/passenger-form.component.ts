import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PredictionRequestDto } from '../../../dtos/prediction-request-dto'

@Component({
  selector: 'app-passenger-form',
  templateUrl: './passenger-form.component.html',
  styleUrl: './passenger-form.component.scss'
})
export class PassengerFormComponent {

  @Input() requestDto: PredictionRequestDto = {
    pclass: 1,
    name: "Doe, Mr. John",
    sex: "male",
    age: 30,
    sibsp: 0,
    parch: 0,
    ticket: "123456",
    fare: 100,
    cabin: "A123",
    embarked: "S",
    model: "*"
  };

  @Output() submitRequest = new EventEmitter<PredictionRequestDto>();

  decisionTreeVersions: string[] = ['decision_tree_v1', 'decision_tree_v2', 'decision_tree_v3', 'decision_tree_v4', 'decision_tree_v5', 'decision_tree_v6', 'decision_tree_v7', '*'];

  onSubmit(event: Event) {
    event.preventDefault();
    this.submitRequest.emit(this.requestDto); // Emit the data you want to send
  }
}
