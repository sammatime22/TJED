import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultsComponent } from './results.component';

describe('ResultsComponent', () => {
  let component: ResultsComponent;
  let fixture: ComponentFixture<ResultsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ResultsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display results if an input is passed', () => {
    const searchResultsForHakobu = [{"japanese_word": "運ぶ", "kana": "はこぶ", "english_word": "to transport"},{"japanese_word": "事を運ぶ", "kana": "ことをはこぶ", "english_word": "to go ahead, to proceed, to carry on"},{"japanese_word": "持ち運ぶ", "kana": "もちはこぶ", "english_word": "to carry, to bring (to a place)"},{"japanese_word": "取り運ぶ", "kana": "とりはこぶ", "english_word": "to proceed smoothly"},{"japanese_word": "取運ぶ", "kana": "とりはこぶ", "english_word": "to proceed smoothly"}];
    component.searchTerm = "運ぶ";
    component.result = searchResultsForHakobu;
    fixture.detectChanges();
    const resultsComponentTemplate: HTMLElement = fixture.nativeElement;
    searchResultsForHakobu.forEach(searchResult => {
      for (const [key, value] of Object.entries(searchResult)) {
        expect(resultsComponentTemplate.textContent).toContain(key.replace("_", " ") + ": " + value);
      }
    });
  });
});
