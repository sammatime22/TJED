import { Component, OnInit, Output, Input } from '@angular/core';
import { QueryService } from '../query/query.service';
import { SearchResults } from '../interfaces/search-results';
import { EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  readonly MAX_SEARCHED_TERMS_DISPLAYED: number = 5;

  searchedTerms: string[] = [];

  searchTerm: string =  "";

  @Output() searchTermEvent = new EventEmitter<string>();

  constructor() {

  }

  ngOnInit(): void {
  }

  /**
   * Keeps track of the last five searches and emits the search term in an event.
   */
  search() {
    this.searchedTerms.push(this.searchTerm);
    if (this.searchedTerms.length > this.MAX_SEARCHED_TERMS_DISPLAYED) {
      this.searchedTerms.splice(0, 1);
    }
    this.searchTermEvent.emit(this.searchTerm);
  }
}
