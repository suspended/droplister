$(function () {
    $(".showpassword").each(function (index, input) {
        var $input = $(input);
        div = $("<div class='opt'/>").append(
            $("<input type='checkbox' class='showpasswordcheckbox' id='showPassword' />").click(function () {
                var change = $(this).is(":checked") ? "text" : "password";
                var rep = $("<input placeholder='Password' type='" + change + "' />")
                    .attr("id", $input.attr("id"))
                    .attr("name", $input.attr("name"))
                    .attr('class', $input.attr('class'))
                    .val($input.val())
                    .insertBefore($input);
                $input.remove();
                $input = rep;
            })
        ).append($("<label for='showPassword'/>").text("Show password")).insertAfter($input.parent());
        label = $("<label />").html("Login with:").addClass('login_with');
        $(div).prepend(label);
    });

    $('#showPassword').click(function () {
        if ($("#showPassword").is(":checked")) {
            $('.icon-lock').addClass('icon-unlock');
            $('.icon-unlock').removeClass('icon-lock');
        } else {
            $('.icon-unlock').addClass('icon-lock');
            $('.icon-lock').removeClass('icon-unlock');
        }
    });
});