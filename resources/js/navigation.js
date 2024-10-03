document.addEventListener("DOMContentLoaded", () => {  
  const nav = document.querySelector("nav");  
  const nav_top_offset = nav.getBoundingClientRect().top + window.pageYOffset;

  window.addEventListener("scroll", () => {
    if (window.pageYOffset >= nav_top_offset) {  
      nav.style.position = "fixed";
      nav.style.top = "0";
    } else {  
      nav.style.position = "relative";
      nav.style.top = "initial";
    }
  });
});
