/**
 * Created by lion on 6/4/16.
 */
send_items_to_ebay = function (elements_to_send_ebay) {
    console.log("Sending " + elements_to_send_ebay)
    $.ajax({
        dataType: "json",
        url: ebay_sell_url,
        data: JSON.stringify(elements_to_send_ebay),
        type: 'POST',
        success: function (response) {
            console.log(response.data);
        },
        error: function (error) {
            console.log(error)
        },
        complete: function () {
            alert("done'");
        }
    });
}

show_ebay_order_detail = function (ebay_order_id, modal_object) {
    var data_array = {
        ebay_order_id: ebay_order_id
    };
    console.log(data_array);
    $.get(
        ebay_order_detail_url,
        {
            ebay_order_id: ebay_order_id
        }, function (data) {
            change_modal_content($("#info_modal"), data);
            $(modal_object).modal('show');
        }, 'html'
    );
}