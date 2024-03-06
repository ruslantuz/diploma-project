const plannerItem = document.querySelectorAll('.planner-item');
plannerItem[0].firstElementChild.classList.toggle('planner-gallery-image-active');
plannerItem[0].lastElementChild.classList.toggle('planner-active');
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