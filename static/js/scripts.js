document.addEventListener('DOMContentLoaded', function() {
    var addOperationLink = document.getElementById('add-operation-link');
    var dropdownMenu = document.getElementById('dropdown-menu');
    var dropdownItems = dropdownMenu.getElementsByClassName('dropdown-item');

    addOperationLink.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default link behavior

        // Check the current display state
        if (dropdownMenu.style.display === 'flex') {
            // Hide the menu
            Array.from(dropdownItems).forEach((item, index) => {
                setTimeout(() => {
                    item.classList.remove('show');
                }, index * 100); // Delay each item
            });
            setTimeout(() => {
                dropdownMenu.style.display = 'none';
            }, dropdownItems.length * 100);
        } else {
            // Show the menu
            dropdownMenu.style.display = 'flex';
            Array.from(dropdownItems).forEach((item, index) => {
                setTimeout(() => {
                    item.classList.add('show');
                }, index * 100); // Delay each item
            });
        }
    });
});
