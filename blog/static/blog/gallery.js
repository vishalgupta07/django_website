const galleryWrapper = document.getElementById('gallery'),
galleryControllers = galleryWrapper.querySelectorAll('.gallery__controller');

galleryControllers.forEach(controller => {
  controller.addEventListener('click', event => {
    if (controller.classList.contains('gallery__controller--prev'))
    galleryGoBack();
    else
    galleryGoForward();
  });
});

function galleryGoBack() {
  const active = galleryWrapper.querySelector('img.active');
  active.classList.remove('active');

  if (active.previousElementSibling)
  active.previousElementSibling.classList.add('active');
  else
  this.galleryWrapper.querySelector('img:last-child').classList.add('active');
}

function galleryGoForward() {
  const active = galleryWrapper.querySelector('img.active');
  active.classList.remove('active');

  if (active.nextElementSibling)
  active.nextElementSibling.classList.add('active');
  else
  this.galleryWrapper.querySelector('img').classList.add('active');
}
