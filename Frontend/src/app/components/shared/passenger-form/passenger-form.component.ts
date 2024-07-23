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
    name: "Mr. John Doe",
    sex: "male",
    age: 30,
    sibsp: 0,
    parch: 0,
    ticket: "123456",
    fare: 100,
    cabin: "A123",
    embarked: "S",
    model: "decision_tree"
  };

  @Output() submitRequest = new EventEmitter<PredictionRequestDto>();

  onSubmit(event: Event) {
    event.preventDefault();
    this.submitRequest.emit(this.requestDto); // Emit the data you want to send
  }
}
