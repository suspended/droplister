/**
 * Created by lion on 7/10/16.
 */

change_modal_title = function (modal_id, title) {

}

change_modal_content = function (modal_object, content) {
    $(modal_object).find("div.content > div.description").html(content);
}