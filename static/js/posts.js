/* Js page*/

$(function() {
    $('.js-menu-icon').click(function() {

        //Executed when js-menu is checked
        //$(this): Self element, namely div.js-menu-icon
        // next():Next to div js-menu-icon,namely div.menu
        $(this).next().toggle();


    })

})