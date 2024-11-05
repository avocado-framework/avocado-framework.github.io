$(document).ready(() => {
    let typingElement = $('.typing');
  
    typingElement.on('click', (e) => {
      typingElement.removeClass('animate');
      setTimeout(() => typingElement.addClass('animate'), 1);
    })
  });
