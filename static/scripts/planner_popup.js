const plannerItem = document.querySelectorAll('.planner-item');

plannerItem.forEach(element => {
    element.addEventListener("mouseover", () => {
        var active = document.querySelector('.planner-active');
        active.classList.toggle('planner-active');
        var active2 = document.querySelector('.planner-gallery-image-active');
        active2.classList.toggle('planner-gallery-image-active');

        element.firstElementChild.classList.toggle('planner-gallery-image-active');
        element.lastElementChild.classList.toggle('planner-active');
    });
});