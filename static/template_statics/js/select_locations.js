$(document).ready(function () {
    $.ajax({
        url: '/media/locations/cities.json',
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            var location_input = $('#id_location')
            $.each(response, function (index, value) {
                location_input.append($('<option/>').attr("value", value.name).text(value.name))
            })
        }
    })
})