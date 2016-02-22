function addHistory(history){
    $.getJSON("/v1/link?request_id="+history, function(data){
        var e = "<tr>"
                   +"<td>"+history+"</td>"
                   +"<td><a href='"+data.short_url+"'>"+data.short_url+"</a></td>"
                   +"<td><button type='button' class='delete-url' data-requestid='"+history+"'>delete</button></td>"
                   +"</tr>";
        $('#history').append(e);
    });
}

$(document).ready(function(){
     var items = localStorage.getItem('history');
     if (items){
        var history = JSON.parse(items).history;
        for (var i=0; i<history.length; i++){
            addHistory(history[i]);
        }
     }

    $('#btn--short-url').on('click', function(){
        var url = $('#input--long-url').val();
        var data = {'link': url};

        $.ajax({
            method: 'POST',
            url: '/v1/link',
            data: KJUR.jws.JWS.sign('HS256', '{}', JSON.stringify(data),
                'hellominiaturespoon'),
            'processData': false,
            'dataType': 'json',
            'contentType': 'text/plain'
        }).success(function(data){
            $('#result a').prop('href', data.short_url);
            $('#result a').text(data.short_url);

            var items = localStorage.getItem('history');
            if (items){
                var history = JSON.parse(items)
                history.history.push(data.request_id);
                while (history.length>5){
                    history.splice(0, 1)
                }
                localStorage.setItem('history', JSON.stringify(history));
            }else {
                var history = {history: [data.request_id]}
                localStorage.setItem('history', JSON.stringify(history));
            }
            var e = "<tr>"
                   +"<td>"+data.request_id+"</td>"
                   +"<td><a href='"+data.short_url+"'>"+data.short_url+"</a></td>"
                   +"<td><button type='button' class='delete-url' data-requestid='"+data.request_id+"'>delete</button></td>"
                   +"</tr>";
            $('#history').append(e);
        });
    });
    
    $(document).on('click', function(event){
        if($(event.target).hasClass('delete-url')){
            var requestId = $(event.target).data("requestid");
            var data = {request_id: requestId}
            $.ajax({
                method: 'DELETE',
                url: '/v1/link',
                data: KJUR.jws.JWS.sign('HS256', '{}', JSON.stringify(data),
                    'hellominiaturespoon'),
                'processData': false,
                'dataType': 'json',
                'contentType': 'text/plain'
            }).success(function(data){
                var items = localStorage.getItem('history');
                if (items){
                    var history = JSON.parse(items).history;
                    history.splice(history.indexOf(requestId), 1);
                    localStorage.setItem('history', JSON.stringify({history: history}));
                }
            });
        }
    });
})