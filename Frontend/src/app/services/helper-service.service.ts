import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PredictionRequestDto } from '../dtos';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HelperService {

  private helperBaseUri: string =  'http://localhost:8000';

  constructor(private httpClient: HttpClient) {}

  getBenchmark() : Observable<{ [key: string]: number }> {
    return this.httpClient.get<{ [key: string]: number }>(`${this.helperBaseUri}/benchmark`);
  }
}
