/**
Author: Chua Han Yong Darren
Date: 05/08/2023 
Application: Pat's Online Minimart
File: script.js

This JS file is adapted from an open-sourced Bootstrap template by Tutorial Republic: 
https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=crud-data-table-for-database-with-modal-form
**/
$(document).ready(function() {
    // Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();
    // Select/Deselect checkboxes
    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function() {
        if (this.checked) {
            checkbox.each(function() {
                this.checked = true;
            });
        } else {
            checkbox.each(function() {
                this.checked = false;
            });
        }
    });
    checkbox.click(function() {
        if (!this.checked) {
            $("#selectAll").prop("checked", false);
        }
    });
});

/**
 * Creates a new item in the store. 
 */
function createItem() {
    // Get the form data
    const form = document.getElementById('createItemForm');
    const formData = new FormData(form);

    // Convert the form data into a JSON object
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send the POST request to the Flask API to create a new item
    fetch('/item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Item created successfully:', responseData);

        // Close the modal after successful item creation
        $('#createItemModal').modal('hide');

        // Reload the page to update the table with the new item
        window.location.reload();
    })
    .catch(error => {
        console.error('Error creating item:', error);
    });
}
