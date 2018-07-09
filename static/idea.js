$("document").ready(function() {

    $.ajax({
        type: "POST",
        method: "POST",
        url: "http://localhost:8000/",
        data: "",
        success: function(data) {
            $(".show").html(data)
        }
    });

    $("#get").on('click', function() {
        $.ajax({
            type: "POST",
            method: "POST",
            url: "http://localhost:8000/get",
            data: "",
            success: function(data) {
                $(".show").html(data)
            }
        });
    })


})