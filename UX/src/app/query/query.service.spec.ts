import { TestBed } from '@angular/core/testing';

import { QueryService } from './query.service';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

@NgModule({
  imports: [HttpClientModule]
})
class DynamicTestModule {}

describe('QueryService', () => {
  let service: QueryService;
  let queryTJEDAPIhttpSpy: any;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        DynamicTestModule
      ]
    });
    service = TestBed.inject(QueryService);
    queryTJEDAPIhttpSpy = spyOn<any>(service['http'], 'get');
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should query the English vocab endpoint as expected', () => {
    service.queryTJEDAPI("apples");
    expect(queryTJEDAPIhttpSpy).toHaveBeenCalledOnceWith(service.TJED_API_URL + "/api/vocab/english/apples/");
  });

  it('should query the Japanese vocab endpoint as expected', () => {
    service.queryTJEDAPI("りんご");
    expect(queryTJEDAPIhttpSpy).toHaveBeenCalledOnceWith(service.TJED_API_URL + "/api/vocab/japanese/りんご/");
  });

  it('should query the Kanji endpoint as expected', () => {
    service.queryTJEDAPI("林")
    expect(queryTJEDAPIhttpSpy).toHaveBeenCalledOnceWith(service.TJED_API_URL + "/api/kanji/林/");
  });

  it('should return nothing if the string isn\'t English or Japanese', () => {
    service.queryTJEDAPI("");
    expect(queryTJEDAPIhttpSpy).toHaveBeenCalledTimes(0);
  });
});
