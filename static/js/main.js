$("body").ready(function(){
    $(".show-hide-btn").click(function(){
        var id = $(this).data("id");
        $("#half-"+id).hide();
        $("#full-"+id).show();
    });
});

