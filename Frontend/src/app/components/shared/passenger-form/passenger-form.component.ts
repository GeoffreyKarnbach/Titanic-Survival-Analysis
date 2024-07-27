import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { PredictionRequestDto } from '../../../dtos/prediction-request-dto'
import { HelperService } from '../../../services';
import { tick } from '@angular/core/testing';

@Component({
  selector: 'app-passenger-form',
  templateUrl: './passenger-form.component.html',
  styleUrl: './passenger-form.component.scss'
})
export class PassengerFormComponent implements OnInit {

  constructor(
    private helperService: HelperService
  ) {}

  ngOnInit(): void {
    this.helperService.getModels().subscribe(
      (response) => {
        this.modelVersions = response["models"];
        this.modelVersions.push("*");
      },
      (error) => {
        console.log(error);
      }
    );
  }

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

  modelVersions: string[] = ['*'];

  onSubmit(event: Event) {
    event.preventDefault();
    this.submitRequest.emit(this.requestDto);
  }
}
