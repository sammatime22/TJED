import { TestBed } from '@angular/core/testing';

import { QueryService } from './query.service';

describe('QueryService', () => {
  let service: QueryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QueryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  // it should query the english vocab endpoint as expected

  // it should query the japanese vocab endpoint as expected

  // it should query the kanji endpoint as expected

  // it should error as expected
});
