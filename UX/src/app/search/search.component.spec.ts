import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchComponent } from './search.component';

describe('SearchComponent', () => {
  let component: SearchComponent;
  let fixture: ComponentFixture<SearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SearchComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('#search() should emit an event when #keyup.enter is registered', () => {
    component.searchTerm = "寿司";
    const emitSpy = spyOn(component.searchTermEvent, 'emit');

    const input = fixture.nativeElement.querySelector('input');
    input.click();
    input.dispatchEvent(new KeyboardEvent('keyup', { key: 'Enter' }));

    expect(emitSpy).toHaveBeenCalledWith("寿司");
    expect(component.searchedTerms).toEqual(["寿司"]);
  });
});
