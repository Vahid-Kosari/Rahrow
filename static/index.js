document.addEventListener("DOMContentLoaded", function () {
    const questionBoxes = document.querySelectorAll(".FAQ-accordion-box-q");
  
    questionBoxes.forEach(box => {
      box.addEventListener("click", () => {
        const accordion = box.closest(".FAQ-accordion");
        accordion.classList.toggle("open");
      });
    });
  });
  