#!/usr/bin/node

document.querySelector('#add_item').addEventListener('click', function () {
  const list = document.querySelector('ul.my_list');
  const item = document.createElement('li');

  item.textContent = 'Item';
  list.appendChild(item);
})
