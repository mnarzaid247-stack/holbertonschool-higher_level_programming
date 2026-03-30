const btn = document.querySelector('#update_header');
const header = document.querySelector('header');

btn.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
