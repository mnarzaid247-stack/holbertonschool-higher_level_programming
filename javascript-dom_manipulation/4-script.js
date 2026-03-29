const btn = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

btn.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  list.appendChild(newItem);
});
