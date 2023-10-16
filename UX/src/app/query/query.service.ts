import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  readonly TJED_API_URL: string = "http://127.0.0.1:8000"; // TODO

  constructor(private http: HttpClient) { }

  /**
   * Queries the TJED API at the appropriate endpoint for the search term provided
   * 
   * @param searchTerm The term to be searched
   * @returns an array of objects returned from the search
   */
  async queryTJEDAPI(searchTerm: string) {
    var testUrl = this.TJED_API_URL;

    if ((/^[a-zA-Z]+$/).test(searchTerm)) {
      testUrl += "/api/vocab/english/" + searchTerm + "/";
    } else if (searchTerm.length > 1) {
      testUrl += "/api/vocab/japanese/" + searchTerm + "/";
    } else if (searchTerm.length == 1) {
      testUrl += "/api/kanji/" + searchTerm + "/";
    } else {
      return [];
    }
    try {
      return await firstValueFrom(this.http.get<object[]>(testUrl));
    } catch (e) {
      console.error(e);
      return [];
    }
  }
}
