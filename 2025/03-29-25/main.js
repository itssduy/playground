import { maxSquat } from "./scripts/calculator.js";





const form = document.getElementById("maxSquat");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = {
        squat: event.target.elements.squat.value,
        reps: event.target.elements.reps.value
    }


    const max = document.getElementById("max")
    max.innerHTML = Math.ceil(maxSquat(formData.squat, formData.reps)/5)*5;

});