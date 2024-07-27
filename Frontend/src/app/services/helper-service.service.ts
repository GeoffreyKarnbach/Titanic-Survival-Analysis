import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HelperService {

  private baseUri: string =  environment.baseUri;

  constructor(private httpClient: HttpClient) {}

  getBenchmark() : Observable<{ [key: string]: number }> {
    return this.httpClient.get<{ [key: string]: number }>(`${this.baseUri}/benchmark`);
  }

  getModels() : Observable<any> {
    return this.httpClient.get<any>(`${this.baseUri}/models`);
  }
}
