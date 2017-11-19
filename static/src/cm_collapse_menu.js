odoo.define('cm_menu_collapse.my_js', function (require) {'use strict';
    var Model = require('web.Model');
    var p = 0;
    (new Model('collapse.menu')).call('customize_collapse_menus').then(function (result) {

         $.each( result, function( e, k ){
             p = k.toString();
              $('.oe_secondary_menu').each(function (key,value) {
                  console.log(p);
                  if($(this).attr('data-menu-parent') === p){
                    this.style.cursor = "pointer";
                    this.id = "menu_selected";
                    $(this).children().each(function (key,value){
                    if($(this).attr('class')==="oe_secondary_submenu nav nav-pills nav-stacked"){
                    value.style.display = "none"};
                    if($(this).attr('class')==="oe_secondary_menu_section"){
                      if ($(this).next().attr('class')==="oe_secondary_submenu nav nav-pills nav-stacked"){
                      $(this).addClass("menu_selected_child")
                      }
                      };
                    })};
                    });

            });
        $('.menu_selected_child').click(function() {
                      $(this).next().slideToggle(500);
                    });
    });


});