/**
 * Created by lion on 5/30/16.
 */
$(function () {
    show_corresponding_elemts();
    activate_steps();
    $("#next_button").click(function (event) {
        event.preventDefault();
        var band = validate_fields();
        if (band) {
            currentContent = 'content_step_' + step;
            step = step + 1;
            nextContent = 'content_step_' + step;
            activate_steps();
            $('#' + currentContent).transition({
                    animation: 'fade right',
                    duration: 1000,
                    onComplete: function () {
                        $('#' + nextContent).transition({animation: 'fly left', duration: 1000});
                    }
                }
            );
        }
    });
    /*Form Validation*/
    booking_form = $('form#personal_information').form({
        inline: true,
    });
});

activate_steps = function () {
    /*activate the corrresponding step*/
    $('.step').addClass('disabled');
    $(".steps .step:nth-child(" + step + ")").addClass("active").removeClass('disabled');
    if (step == max_steps) { //de momento 2 es el maximo
        /*change the text of next button*/
        $("#next_button").find("span").html("Authorize eBay");
        $("#next_button").off().on('click', function (e) {
            var band = validate_fields();
            if (band) {
                //$("#personal_information").attr('action', ebay_url).submit();
                $("#personal_information").submit();
            }
        })
    }
}

show_corresponding_elemts = function () {
    /*the step 1 for default is active and the others ones are disabled*/
    /*show the content of the step*/
    content_step_id = "content_step_" + step;
    $("#" + content_step_id).slideToggle();
}