document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  var contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var redirectTo = contactForm.querySelector('[name="_next"]').value;
      fetch(contactForm.action, {
        method: 'POST',
        body: new FormData(contactForm),
        headers: { 'Accept': 'application/json' }
      }).then(function (response) {
        if (response.ok) {
          window.location.href = redirectTo;
        } else {
          alert("Sorry, something went wrong sending your message. Please email jen@brightfinchcoaching.com directly.");
        }
      }).catch(function () {
        alert("Sorry, something went wrong sending your message. Please email jen@brightfinchcoaching.com directly.");
      });
    });
  }
});
