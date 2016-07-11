/**
 * Created by lion on 6/5/16.
 */
$(document).ready(function () {
    $('#orders_table').DataTable();
});

$(function () {
    $("#buy_on_amazon").click(function (e) {
        var selected_elements = $('#orders_table').find('tr.selected').find('td:nth-child(1)');
        if (selected_elements.length > 0) {
            var order_ids_arrays = new Array();
            $.each(selected_elements, function (index, elem) {
                var ebay_order_id = $(elem).html();
                order_ids_arrays.push(ebay_order_id);
            });
            console.log(order_ids_arrays);
            /*Show Confirm Modal*/
            $('#confirm_modal').modal({
                onApprove: function () {
                    orders_form = $("form#form_orders");
                    $("form#form_orders input#input_orders").val(order_ids_arrays.toString());
                    $(orders_form).submit();
                }
            }).modal('show');
        }
    });

});
