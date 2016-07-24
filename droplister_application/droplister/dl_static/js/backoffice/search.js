/**
 * Created by lion on 6/5/16.
 */
$(function () {
    // DATA TABLE
    initTable();
    $("#sell_on_ebay").click(function (e) {
        var selected_elements = $('#example').find('tr.selected');
        if (selected_elements.length > 0) {
            $.ajax({
                dataType: 'json',
                url: ebay_store_info,
                success: function (data) {
                    console.log(data);
                    //create table
                    items_table = $('#ebay_listing_table');
                    $(items_table).find('tbody > tr').remove();
                    var asim_arrays = new Array();
                    $.each(selected_elements, function (index, elem) {
                        item_row = $('<tr/>');
                        var asim_value = $(elem).find('td:nth-child(2)').html();
                        var title_value = $(elem).find('td:nth-child(3)').html();
                        $(item_row).append($('<td/>').html(title_value));
                        $(item_row).append($('<td/>').html(createComboBoxFromCategories(data.categories, asim_value)));
                        $(items_table).append(item_row);
                        asim_arrays.push(asim_value);
                    });
                    //console.log(asim_arrays);
                    /*Show Confirm Modal and atach approve event*/
                    $('#sell_on_ebay_modal').modal({
                        closable: false,
                        observeChanges: true,
                        onApprove: function () {
                            var elements_to_send_ebay = new Array();
                            $.each(asim_arrays, function(index, elem){
                                elements_to_send_ebay.push({'asin': elem, 'category': $("#"+elem).val()});
                            });
                            //console.log(elements_to_send_ebay);
                            //return;
                            send_items_to_ebay(elements_to_send_ebay);
                        }
                    }).modal('show');
                },
                error: function (error) {
                    console.error(error);
                }
            });
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

createComboBoxFromCategories = function (categories, combo_id) {
    select = $('<select />').addClass("ui dropdown").attr('id', combo_id);
    $.each(categories, function (index, elem) {
        console.log(elem.name + " - " + elem.id);
        $('<option/>').attr('value', elem.id).html(elem.name).appendTo(select);
    });
    return select;
}