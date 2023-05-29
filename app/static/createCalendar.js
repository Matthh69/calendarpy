"use a strict";
// Script pour les effets visuels et l'esthétique

// Changement de couleur au survol des onglets du menu
const menuItems = document.querySelectorAll('nav ul li a');

menuItems.forEach(item => {
  item.addEventListener('mouseover', () => {
    item.style.color = '#ff0000';
  });

  item.addEventListener('mouseout', () => {
    item.style.color = '#fff';
  });

  item.addEventListener('click', event => {
    event.preventDefault();
    location.reload();
  });
});
