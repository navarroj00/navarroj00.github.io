// Handle functionality for expanding and collapsing abstract content when abstract button is clicked
function toggleAbstract(button) {
    const abstractContent = button.nextElementSibling;
    abstractContent.classList.toggle("show");
}

// Handle functionality for expanding and collapsing course description when course description button is clicked
function toggleCourseDescription(button) {
    const courseDescription = button.nextElementSibling;
    courseDescription.classList.toggle("show");
}