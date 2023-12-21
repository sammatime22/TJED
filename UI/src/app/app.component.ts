import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { QueryService } from './query/query.service';
import { Observable } from 'rxjs';
import { SearchResults } from './interfaces/search-results';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'TJED UI';

  searchResults: SearchResults = {searchTerm: "", returnedResults: []};

  constructor(private queryService: QueryService) {
  }

  ngOnInit() {
    
  }

  /**
   * From the event, calls the appropriate QueryService method, passing a new SearchResults 
   * object to the Results Component.
   * @param searchTerm The search term used to gather the results
   */
  async search(searchTerm: string) {
    this.searchResults.searchTerm = searchTerm;
    this.searchResults.returnedResults = await this.queryService.queryTJEDAPI(this.searchResults.searchTerm);
  }
}
