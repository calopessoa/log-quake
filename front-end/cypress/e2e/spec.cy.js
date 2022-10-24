/* eslint-disable no-undef */
describe('empty spec', () => {
  it('passes', () => {
    cy.visit('https://quake3-log-viewer.vercel.app/')
  });

  it('must render `Kills per player` on the main screen', () => {
    cy.get('.select-left').should('contain', 'Kills per player')
  });
  it('must render `Causes of Death` on the main screen', () => {
    cy.get('.select-right').should('contain', 'Causes of Death')
  });

});