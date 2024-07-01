document.addEventListener('DOMContentLoaded', function() {
    function toggleToolFields() {
        var categorySelect = document.getElementById('id_category');
        var toolFields = [
            'id_standard', 'id_grade', 'id_shape', 'id_steel_grade',
            'id_surface_finish', 'id_place_of_origin', 'id_delivery_time',
            'id_model_number', 'id_type', 'id_application', 'id_certification'
        ];
        var isToolCategory = categorySelect.options[categorySelect.selectedIndex].text === 'Tools';

        toolFields.forEach(function(fieldId) {
            var fieldRow = document.getElementById(fieldId).closest('.form-row');
            if (isToolCategory) {
                fieldRow.style.display = '';
            } else {
                fieldRow.style.display = 'none';
            }
        });
    }

    var categorySelect = document.getElementById('id_category');
    if (categorySelect) {
        categorySelect.addEventListener('change', toggleToolFields);
        toggleToolFields();  // Initialize the form with correct visibility
    }
});


