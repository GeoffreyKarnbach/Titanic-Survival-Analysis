import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { PredictionRequestDto } from '../../../dtos';
import { SurvivalPredictionService } from '../../../services';

@Component({
  selector: 'app-decision-tree',
  templateUrl: './decision-tree.component.html',
  styleUrl: './decision-tree.component.scss'
})
export class DecisionTreeComponent {

  loading: boolean = false;
  survivalPrediction: boolean | null = null;

  requestDto: PredictionRequestDto = {
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
  }
  constructor(private survivalPredictionService: SurvivalPredictionService){}

  onSubmit(_: Event): void {
    this.requestDto.model = "decision_tree";

    console.log(this.requestDto);

    this.loading = true;
    this.survivalPredictionService.getSurvivalPrediction(this.requestDto).subscribe(
      (response) => {
        this.loading = false;
        if (response['Survived'] == 1) {
          this.survivalPrediction = true;
        } else {
          this.survivalPrediction = false;
        }
      },
      (error) => {
        this.loading = false;
        console.log(error);
      }
    );
  }
}
