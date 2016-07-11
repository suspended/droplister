/**
 * Created by lion on 5/30/16.
 */
validate_fields = function () {
    if (step == 1) {
        return validate_step_1();
    }
    if (step == 2) {
        return validate_step_2();
    }
}

remove_all_form_error = function () {
    $('.ui.form .field.error').removeClass("error");
    $('.ui.form.error').removeClass("error");
    $(".field .pointing.prompt").remove();
}

validate_step_1 = function () {
    remove_all_form_error();
    var band = true;
    form = $("#personal_information");
    first_name = $(form).find("input[name='first_name']").val();
    if (first_name == null | first_name.trim() == "") {
        $('#personal_information').form('add').prompt('first_name', 'Please enter your Name');
        band = false;
    }
    last_name = $(form).find("input[name='last_name']").val();
    if (last_name == null | last_name.trim() == "") {
        $('#personal_information').form('add').prompt('last_name', 'Please enter your Last Name');
        band = false;
    }
    email = $(form).find("input[name='email']").val();
    if (validateEmail(email)) {
        confirm_email = $(form).find("input[name='confirm_email']").val();
        if (email != confirm_email) {
            $('#personal_information').form('add').prompt('confirm_email', 'The E-mails addresses must match');
            band = false;
        }
    } else {
        $('#personal_information').form('add').prompt('email', 'Enter a valid E-mail address');
        band = false;
    }
    terms = $(form).find("input[name='terms']").is(":checked");
    if (!terms) {
        $('#personal_information').form('add').prompt('terms', 'You have to agree with terms and conditions');
        /*Ajustar el propmp hacia la izquierda*/
        elem = $("#terms > div.pointing.prompt");
        $(elem).removeClass("ui basic red pointing prompt label transition visible");
        $(elem).addClass("ui basic red left pointing prompt label transition visible");
        band = false;
    }
    return band;
}

validate_step_2 = function () {
    remove_all_form_error();
    var band = true;
    form = $("#personal_information");
    paypal_email = $(form).find("input[name='paypal_email']").val();
    if (validateEmail(paypal_email)) {
        confirm_paypal_email = $(form).find("input[name='confirm_paypal_email']").val();
        if (paypal_email != confirm_paypal_email) {
            $('#personal_information').form('add').prompt('confirm_paypal_email', 'The Paypal E-mails addresses must match');
            band = false;
        }
    } else {
        $('#personal_information').form('add').prompt('paypal_email', 'Enter a valid E-mail address');
        band = false;
    }
    return band;
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
