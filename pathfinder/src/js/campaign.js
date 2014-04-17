

var def_campaign_list = function() {
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
                var btn_campaign = $('<button class="campaignLink">'+element.name+'</button>');
                var btn_remove = $('<button class="removeLink">Remove</button>');
                var btn_onoff = $('<button class="onoffLink">'+onoff+'</button>');

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
                            btn_remove
                        ).append(
                            btn_onoff
                        )
                    ).append(
                        $('<td>').text(element.status)
                    )
                    
                );
            });
        }
    });
    
};
