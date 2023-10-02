import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  readonly TJED_API_URL: string = "http://127.0.0.1:8000"

  constructor(private http: HttpClient) { }

  async queryTJEDAPI(searchTerm: string): Promise<string> {
    var testUrl = this.TJED_API_URL;

    if ((/^[a-zA-Z]+$/).test(searchTerm)) {
      testUrl += "/api/vocab/english/" + searchTerm + "/";
    } else if (searchTerm.length > 1) {
      testUrl += "/api/vocab/japanese/" + searchTerm + "/";
    } else {
      testUrl += "/api/kanji/" + searchTerm + "/";
    }

    const vals = await firstValueFrom(this.http.get<string>(testUrl));
    return vals;
  }
}
