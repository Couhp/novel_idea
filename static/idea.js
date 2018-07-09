$("document").ready(function() {

    $.ajax({
        type: "POST",
        method: "POST",
        url: "https://novelidea.herokuapp.com/",
        data: "",
        success: function(data) {
            $(".show").html(data)
        }
    });

    $("#get").on('click', function() {
        $.ajax({
            type: "POST",
            method: "POST",
            url: "https://novelidea.herokuapp.com/get",
            data: "",
            success: function(data) {
                $(".show").html(data)
            }
        });
    })


})
