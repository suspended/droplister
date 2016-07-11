/**
 * Created by lion on 6/4/16.
 */
$(function () {
    $('#purchase_table').DataTable();
    $("#purchase_button").click(function (event) {
        event.preventDefault();
        var ebay_order_id = $(this).parent().parent().find('td:nth-child(2)').html();
        alert(ebay_order_id);
        //return;
        show_ebay_order_detail(ebay_order_id, $('#info_modal'));
    });
});