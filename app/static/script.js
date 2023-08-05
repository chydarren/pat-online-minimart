/**
Author: Chua Han Yong Darren
Date: 05/08/2023 
Application: Pat's Online Minimart
File: script.js

This JS file is adapted from an open-sourced Bootstrap template by Tutorial Republic: 
https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=crud-data-table-for-database-with-modal-form
**/

/* ========================================================================================================
PROVIDED BY TUTORIAL REPUBLIC
======================================================================================================== */
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

/* ========================================================================================================
HELPER FUNCTIONS TO INTERACT WITH THE BACKEND API SERVER
======================================================================================================== */
/**
 * Creates a new item in the store. 
 * 
 * @throws Error   If failed to create item in the store.
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
        console.log('Item created successfully in the store:', responseData);

        // Close the modal after successful item creation
        $('#createItemModal').modal('hide');

        // Reload the page to update the table with the new item
        window.location.reload();
    })
    .catch(error => {
        console.error('Failed to create item in the store:', error);
    });
}

/**
 * Opens the update item modal.
 * 
 * @param itemId    The ID of the item to be updated.
 * @throws Error    If failed to retrieve item from the store.
 */
let updateItemId;

function openUpdateModal(itemId) {
    updateItemId = itemId;

    fetch(`/item/${updateItemId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(responseData => {
        document.getElementById('updateItemForm').elements['item_name'].value = responseData.name;
        document.getElementById('updateItemForm').elements['item_description'].value = responseData.description;
        document.getElementById('updateItemForm').elements['item_price'].value = responseData.price;
        document.getElementById('updateItemForm').elements['item_quantity'].value = responseData.quantity;

        $('#updateItemModal').modal('show');
    })
    .catch(error => {
        console.error('Failed to retrieve item from the store:', error);
    });
}

/**
 * Updates an item in the store.
 * 
 * @throws Error   If failed to update item in the store.
 */
function updateItem() {
    // Get the form data
    const form = document.getElementById('updateItemForm');
    const formData = new FormData(form);

    // Convert the form data into a JSON object
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Send the PUT request to the Flask API to update the specific item
    fetch(`/item/${updateItemId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Item updated successfully in the store:', responseData);

        // Close the modal after successful item update
        $('#updateItemModal').modal('hide');

        // Reload the page to update the table with the updated item
        window.location.reload();
    })
    .catch(error => {
        console.error('Failed to update item in the store:', error);
    }); 
}

/**
 * Opens the delete item modal.
 * 
 * @param itemId    The ID of the item to be deleted.
 */
let deleteItemId;

function openDeleteItemModal(itemId) {
    deleteItemId = itemId;

    fetch(`/item/${deleteItemId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(responseData => {
        document.querySelector('#deleteItemModal span').innerHTML = responseData.name;
        $('#deleteItemModal').modal('show');
    })
}

/**
 * Deletes an item in the store.
 * 
 * @throws Error   If failed to delete item from the store. 
 */
function deleteItem() {
    // Send the POST request to the Flask API to delete the specific item 
    fetch(`/item/${deleteItemId}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Item deleted successfully from the store:', responseData);

        // Close the modal after successful item deletion
        $('#deleteItemModal').modal('hide');

        // Reload the page to update the table with the remaining items
        window.location.reload();
    })
    .catch(error => {
        console.error('Failed to delete item from the store:', error);
    });
}