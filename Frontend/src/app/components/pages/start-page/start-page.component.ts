import { Component, OnInit } from '@angular/core';
import { HelperService } from '../../../services';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrl: './start-page.component.scss'
})
export class StartPageComponent implements OnInit {

  constructor(private helperService: HelperService) {}

  // Hashmap with strings as keys and numbers as values
  benchmarkResults: { [key: string]: number } = {};

  ngOnInit(): void {
    this.helperService.getBenchmark().subscribe((data) => {
      this.benchmarkResults = data;
    });
  }

  get benchmarkKeys(): string[] {
    return Object.keys(this.benchmarkResults).sort((a, b) => this.benchmarkResults[b] - this.benchmarkResults[a]);
  }

  formatBenchmarkValue(value: number): string {
    return (value * 100).toFixed(2) +  ' %';
  }

}
