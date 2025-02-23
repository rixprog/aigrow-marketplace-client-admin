let new_item = document.querySelector(".new-item");
let new_item_button = document.querySelector(".add");
let input_fields = new_item.querySelector(".input-fields");
let input_field = document.querySelectorAll('.input-fields input');
let add_item = document.querySelector(".add-item");
let main_container = document.querySelector(".main-container"); // Reference to the main container
let flex_container= document.querySelector('.flex-container');
let arrow=document.querySelector('.arrow');
let plusIcon = new_item_button.querySelector(".plus-icon");
let arrowIcon = new_item_button.querySelector(".arrow");

new_item_button.addEventListener('click', () => {
    // Toggle the display of the input fields
    if (input_fields.style.display === "none" || input_fields.style.display === "") {
        input_fields.style.display = "block"; // Show the input fields
        plusIcon.style.display = "none"; // Hide the plus icon
        arrowIcon.style.display = "block"; // Show the arrow icon
    } else {
        input_fields.style.display = "none"; // Hide the input fields
        plusIcon.style.display = "block"; // Show the plus icon
        arrowIcon.style.display = "none"; // Hide the arrow icon
    }
    console.log('button clicked');
});

add_item.addEventListener('click',()=>{
    let newDashboard=document.createElement('div');
    newDashboard.classList.add('dashboard');

    let head=document.createElement('div');
    head.classList.add('head');
    head.innerText='Your item';

    let boxContainer=document.createElement('div');
    boxContainer.classList.add('box-container');

    let cropNameBox = createBox('Crop Name', input_field[0].value);
    let speciesBox = createBox('Species', input_field[1].value);
    let perKgBox = createBox('Per KG', input_field[2].value);
    let yieldBox = createBox('Yield', input_field[3].value);

    main_container.appendChild(flex_container);
    flex_container.appendChild(newDashboard);

    newDashboard.appendChild(head);
    

    boxContainer.appendChild(cropNameBox);
    boxContainer.appendChild(speciesBox);
    boxContainer.appendChild(perKgBox);
    boxContainer.appendChild(yieldBox);

    newDashboard.appendChild(boxContainer);
    
     // Append the "Add new item" div after the new item
     main_container.appendChild(document.querySelector('.new-item'));

     // Clear input fields after adding
     input_field.forEach(input => input.value = '');
 
     // Optionally hide the input fields again
     input_fields.style.display = "none";

})

function createBox(heading,description){
    let boxes=document.createElement('div');
    boxes.classList.add('boxes');

    let headingDiv=document.createElement('div');
    headingDiv.classList.add('box-heading');

    let descriptionDiv=document.createElement('div');
    descriptionDiv.classList.add('box-description');

    headingDiv.innerText=heading;
    descriptionDiv.innerText=description;

    boxes.appendChild(headingDiv);
    boxes.appendChild(descriptionDiv);

    return boxes;

}

