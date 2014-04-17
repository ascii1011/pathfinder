$.ajax({ 
    type: 'GET', 
    url: '/campaign/list/', 
    data: {}, 
    dataType: 'json',
    success: function (data) { 
        $.each(data, function(index, element) {
            var onoff = '';
            if (element.onoff == 1) { 
                onoff = 'Stop';
            } else {
                onoff = 'Start';
            }
            $('#camp_list').append(
                $('<li>').append( 
                    $('<a>').attr('href',element.slug+'/').text(element.name)
                )
            );
            $('#camp_list_div').append(
                $('<tr>').append(
                    $('<td>').append(
                        $('<a>').attr('href',element.slug+'/').text(element.name)
                    )
                ).append(
                    $('<td>').append(
                        $('<a>').attr('class','removeLink').attr('href','/del/'+element.slug+'/').text('remove')
                    ).append(
                        $('<a>').attr('class','onoffLink').attr('href','/onoff/'+element.slug+'/').text(onoff)
                    )
                ).append(
                    $('<td>').text(element.status)
                )
                        
            );
        });
    }
});
