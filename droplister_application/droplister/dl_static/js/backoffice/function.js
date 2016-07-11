/**
 * Created by lion on 6/5/16.
 */
$(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
            xhr.setRequestHeader('Content-Type', 'application/json');
        }
    });
    // create sidebar and attach to menu open
    $('.ui.sidebar').sidebar('attach events', '.launch.icon.item');
    $('#user_dropdown').dropdown();
});