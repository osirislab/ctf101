$('.dropdown-submenu > a').click(function(e){
    var menu = $(this);
    if (menu.attr('href') == '#'){
        var submenu = menu.parent()
        var first_link = submenu.find('.dropdown-menu a')[0]
        console.log(first_link)
        first_link.click();
    }
});
$('.container img').not(".no-zoom").attr('data-action', "zoom");