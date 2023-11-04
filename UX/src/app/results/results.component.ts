import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  @Input()
  result: object[] = [];

  @Input()
  searchTerm: string = "";

  constructor() { }

  ngOnInit(): void {
    
  }

}
