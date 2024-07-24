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
  survivalPredictionType : string | null = null;
  survivalPrediction: boolean | null | { [key: string]: number } = null;

  requestDto: PredictionRequestDto = {
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
  }
  constructor(private survivalPredictionService: SurvivalPredictionService){}

  onSubmit(_: Event): void {

    console.log(this.requestDto);

    this.loading = true;
    this.survivalPredictionService.getSurvivalPrediction(this.requestDto).subscribe(
      (response) => {
        console.log(response);
        this.loading = false;
        if (response['model'] == "*") {
          this.survivalPredictionType = "multiple_prediction";
          this.survivalPrediction = response['Survived'];
          console.log(this.survivalPrediction);
        } else {
          this.survivalPredictionType = "single_prediction";
          this.survivalPrediction = response['Survived'] == '1' ? true : false;
        }
      },
      (error) => {
        this.loading = false;
        console.log(error);
      }
    );
  }

  getEntries(map: boolean | { [key: string]: number }): { key: string, value: number }[] {
    return Object.entries(map).map(([key, value]) => ({ key, value }));
  }
}
