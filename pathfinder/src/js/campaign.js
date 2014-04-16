$.ajax({ 
    type: 'GET', 
    url: '/campaign/list/', 
    data: {}, 
    dataType: 'json',
    success: function (data) { 
        $.each(data, function(index, element) {
            $('#camp_list').append(
                $('<li>').append( 
                    $('<a>').attr('href',element.slug+'/').text(element.name)
                )
            );
        });
    }
});
