import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PredictionRequestDto } from '../dtos';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SurvivalPredictionService {

  private baseUri: string =  environment.baseUri;

  constructor(private httpClient: HttpClient) {}

  getSurvivalPrediction(data: PredictionRequestDto) {
    return this.httpClient.post<any>(`${this.baseUri}/prediction`, data);
  }
}
