import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { QueryService } from './query/query.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'TJED UI';

  searchTerm: string = "";

  searchResults: string = "";

  constructor(private queryService: QueryService) {
  }

  ngOnInit() {
    
  }

  async search(searchTerm: any) {
    this.searchResults = await this.queryService.queryTJEDAPI(searchTerm);
    console.log(searchTerm);
    console.log(this.searchResults);
  }
}
