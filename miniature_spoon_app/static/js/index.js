$(document).ready(function(){
    $("#btn--short-url").on('click', function(){
        var url = $("#input--long-url").val();
        var data = {"link": url};
        $.ajax({
            method: "POST",
            url: "127.0.0.1:8080/v1/link",
            data: KJUR.jws.JWS.sign("HS256", "{}", JSON.stringify(data),
                "hellominiaturespoon")
        }).success(function(data){
            console.log(data)
        });
    });
})