const plannerItem = document.querySelectorAll('.planner-item');
var active = plannerItem[0].firstElementChild;
var active2 = plannerItem[0].lastElementChild;
plannerItem.forEach(element => {
    element.addEventListener("mouseover", () => {
        active = document.querySelector('.planner-active');
        active.classList.toggle('planner-active');
        var active2 = document.querySelector('.planner-gallery-image-active');
        active2.classList.toggle('planner-gallery-image-active');

        element.firstElementChild.classList.toggle('planner-gallery-image-active');
        element.lastElementChild.classList.toggle('planner-active');
    });
});