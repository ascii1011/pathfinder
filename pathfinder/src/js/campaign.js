

var def_campaign_list = function() {
    $.ajax({ 
        type: 'GET', url: '/campaign/list/', 
        data: {}, dataType: 'json',
        success: function (data) { 
            $('#camp_list_div').empty();
            $.each(data, function(index, element) {

                var onoff = '';
                if (element.onoff == 1) { 
                    onoff = 'Stop';
                } else {
                    onoff = 'Start';
                }
                var btn_remove = $('<button class="removeLink">Remove</button>');
                btn_remove.click(function() {
                    $.ajax( "{% url 'campaign-del' %}", {
                        data: {id:element.id},
                        type: 'POST', dataType: 'json',
                        success: function(data, status, xhr) {
                            def_campaign_list();
                            }
                        });
                    });
                        
                var btn_onoff = $('<button class="onoffLink">'+onoff+'</button>');

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
                        $('<td>').text(element.status_display+'('+element.status+')')
                    )
                    
                );
            });
        }
    });
    
};
