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
 * Sends a request to the Flask API server.
 * 
 * @param url       The URL of the Flask API server.
 * @param method    The HTTP method to be used.
 * @param data      The data to be sent to the Flask API server.
 * @returns         The response from the Flask API server.
 */
async function sendRequest(url, method, data = null) {
    const csrfToken = document.querySelector('body').getAttribute('data-csrf');

    // Define the headers and options for the request
    const headers = {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    };
  
    const options = {
      method,
      headers
    };
  
    // Add the data to the request if it exists
    if (data) {
      options.body = JSON.stringify(data);
    }
  
    // Send the request to the Flask API server
    const response = await fetch(url, options);
    return response.json();
}

/**
 * Creates a new item in the store.
 * 
 * @throws Error   If failed to create item in the store.
 */
async function createItem() {
    try {
        // Get the form data
        const form = document.getElementById('createItemForm');
        const formData = new FormData(form);

        // Convert the form data into a JSON object
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value; 
        });

        // print the form data
        console.log(data);

        // Send the POST request to the Flask API to create a new item
        const responseData = await sendRequest('/item', 'POST', data);

        // Close the modal after successful item creation
        console.log('Item created successfully in the store:', responseData);
        $('#createItemModal').modal('hide');

        // Reload the page to update the table with the new item
        window.location.reload();
    } catch (error) {
        console.error('Failed to create item in the store:', error);
    }
}

/**
 * Opens the update item modal.
 * 
 * @param itemId    The ID of the item to be updated.
 * @throws Error    If failed to retrieve item from the store.
 */
let updateItemId;

async function openUpdateModal(itemId) {
    try {
        updateItemId = itemId;

        // Send the GET request to the Flask API to retrieve the specific item
        const responseData = await sendRequest(`/item/${updateItemId}`, 'GET');

        const updateItemForm = document.getElementById('updateItemForm');
        updateItemForm.elements['item_name'].value = responseData.name;
        updateItemForm.elements['item_description'].value = responseData.description;
        updateItemForm.elements['item_price'].value = responseData.price;
        updateItemForm.elements['item_quantity'].value = responseData.quantity;

        $('#updateItemModal').modal('show');
    } catch (error) {
        console.error('Failed to retrieve item from the store:', error);
    }
}

/**
 * Updates an item in the store.
 * 
 * @throws Error   If failed to update item in the store.
 */
async function updateItem() {
    try {
        // Get the form data
        const form = document.getElementById('updateItemForm');
        const formData = new FormData(form);

        // Convert the form data into a JSON object
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send the PUT request to the Flask API to update the specific item
        const responseData = await sendRequest(`/item/${updateItemId}`, 'PUT', data);

        // Close the modal after successful item update
        console.log('Item updated successfully in the store:', responseData);
        $('#updateItemModal').modal('hide');

        // Reload the page to update the table with the updated item
        window.location.reload();
    } catch (error) {
        console.error('Failed to update item in the store:', error);
    }
}

/**
 * Opens the delete item modal.
 * 
 * @param itemId    The ID of the item to be deleted.
 * @throws Error    If failed to retrieve item from the store.
 */
let deleteItemId;

async function openDeleteItemModal(itemId) {
    try {
        deleteItemId = itemId;

        // Send the GET request to the Flask API to retrieve the specific item
        const responseData = await sendRequest(`/item/${deleteItemId}`, 'GET');

        document.querySelector('#deleteItemModal span').innerHTML = responseData.name;
        $('#deleteItemModal').modal('show');
    } catch (error) {
        console.error('Failed to retrieve item from the store:', error);
    }
    
}

/**
 * Deletes an item in the store.
 * 
 * @throws Error   If failed to delete item from the store. 
 */
async function deleteItem() {
    try {
        // Send the POST request to the Flask API to delete the specific item
        const responseData = await sendRequest(`/item/${deleteItemId}`, 'DELETE');

        // Close the modal after successful item deletion
        console.log('Item deleted successfully from the store:', responseData);
        $('#deleteItemModal').modal('hide');
    
        // Reload the page to update the table with the remaining items
        window.location.reload();
    } catch (error) {
        console.error('Failed to delete item from the store:', error);
    }
}