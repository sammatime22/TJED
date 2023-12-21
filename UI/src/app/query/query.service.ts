import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';
import { Kanji } from 'src/app/interfaces/kanji';
import { Vocab } from 'src/app/interfaces/vocab';

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
    } else if ((/^[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f]+$/).test(searchTerm)) {
      if (searchTerm.length > 1) {
        testUrl += "/api/vocab/japanese/" + searchTerm + "/";
      } else {
        testUrl += "/api/kanji/" + searchTerm + "/";
      }
    } else {
      return [];
    }
    try {
      if (testUrl.indexOf("kanji") != -1) {
        return await firstValueFrom(this.http.get<Kanji[]>(testUrl));
      } else {
        return await firstValueFrom(this.http.get<Vocab[]>(testUrl));
      }
    } catch (e) {
      console.error(e);
      return [];
    }
  }
}
