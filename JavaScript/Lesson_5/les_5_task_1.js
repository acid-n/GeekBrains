'use sctrict';

const modal = document.querySelector('.wrap');
const closeBtn = document.querySelector('span');
const showBtn = document.querySelector('button');

closeBtn.addEventListener('click', function() {
    modal.classList.remove('animate__rollIn');
    modal.classList.add('animate__rollOut');
    setTimeout(function() {
        modal.classList.add('hidden');
    }, 1000);
    
});

showBtn.addEventListener('click', function() {
    modal.classList.remove('animate__rollOut', 'hidden');
    modal.classList.add('animate__animated', 'animate__rollIn');
});
