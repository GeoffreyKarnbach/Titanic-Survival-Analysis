import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PredictionRequestDto } from '../dtos';

@Injectable({
  providedIn: 'root'
})
export class SurvivalPredictionService {

  private predictionBaseUri: string =  'http://localhost:8000/prediction';


  constructor(private httpClient: HttpClient) {}

  getSurvivalPrediction(data: PredictionRequestDto) {
    return this.httpClient.post<any>(`${this.predictionBaseUri}`, data);
  }
}
