#!/usr/bin/node

const clickChangeColor = document.querySelector('#red_header');
const changeColor = document.querySelector('header');

clickChangeColor.addEventListener('click', () => {
  changeColor.style.color = '#FF0000'
})