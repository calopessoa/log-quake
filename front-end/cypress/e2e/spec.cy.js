/* eslint-disable no-undef */
describe('SPA rendering and its elements', () => {
  it('should correctly visit and render the main page', () => {
    cy.visit('https://quake3-log-viewer.vercel.app/')
  });

  it('must render `Kills per player` on the main screen', () => {
    cy.get('.select-left').should('contain', 'Kills per player')
  });
  it('must render `Causes of Death` on the main screen', () => {
    cy.get('.select-right').should('contain', 'Causes of Death')
  });

});