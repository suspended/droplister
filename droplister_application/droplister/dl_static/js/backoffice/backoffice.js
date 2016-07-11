/**
 * Created by lion on 6/5/16.
 */
$(function () {
    // DATA TABLE
    initTable();
    $("#sell_on_ebay").click(function (e) {
        var selected_elements = $('#example').find('tr.selected').find('td:nth-child(2)');
        if (selected_elements.length > 0) {
            var asim_arrays = new Array();
            $.each(selected_elements, function (index, elem) {
                var asim_value = $(elem).html();
                asim_arrays.push(asim_value);
            });
            console.log(asim_arrays);
            /*Show Confirm Modal*/
            $('#confirm_modal').modal({
                onApprove: function () {
                    send_items_to_ebay(asim_arrays);
                }
            }).modal('show');
        }
    });
    $("form#amazon_search_form").form({
        onSuccess: function (event) {
            $("#amazon_result").addClass("loading");
            datatable.clear().draw();
            event.preventDefault();

            data = {'query': $("input#query").val()};
            $.ajax({
                dataType: "json",
                url: amazon_search_url,
                data: data,
                success: function (response) {
                    console.log(response.data);
                    $.each(response.data, function (index, value) {
                        //console.log(value);
                        datatable.row.add(value);
                    });
                    datatable.on('click', 'tr:not(:last-child)', function (e) {
                        //$(this).toggleClass("");
                        /*Enable or disabled ebay selling button*/
                        if ($('#example').find('tr.selected').length == 0) {
                            $("#sell_on_ebay").addClass('disabled');
                            console.log("Deactivating");
                        } else {
                            $("#sell_on_ebay").removeClass('disabled');
                            console.log("Activating");
                        }
                    });
                    datatable.draw();
                },
                error: function (error) {
                    console.log(error)
                },
                complete: function () {
                    $("#amazon_result").removeClass("loading");
                }
            });
        },
        fields: {
            query: {
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your query'
                }]
            }
        }
    });
});

initTable = function () {
    datatable = $('#example').DataTable({
        select: {
            style: 'multi'
        }
    });
}