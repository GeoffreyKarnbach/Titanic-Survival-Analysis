import { Component, OnInit } from '@angular/core';
import { PredictionRequestDto } from '../../../dtos';
import { HelperService, SurvivalPredictionService } from '../../../services';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-prediction',
  templateUrl: './prediction.component.html',
  styleUrl: './prediction.component.scss'
})
export class PredictionComponent implements OnInit {
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
  constructor(
    private survivalPredictionService: SurvivalPredictionService,
    private route: ActivatedRoute,
    private helperService: HelperService
  ){}

  modelVersions: string[] = ['*'];


  ngOnInit(): void {

    this.helperService.getModels().subscribe(
      (response) => {
        this.modelVersions = response["models"];
        this.modelVersions.push("*");

        this.route.queryParams.subscribe(params => {
          this.requestDto.model = this.modelVersions.includes(params['model']) ? params['model'] : '*';
        });

      },
      (error) => {
        console.log(error);
      }
    );

  }

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
