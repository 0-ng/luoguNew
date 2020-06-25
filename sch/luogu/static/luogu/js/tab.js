/** !
 *	tabjs
 */
(function() {
    //bk-tab_js_start
    //tab切换操作
    var bkTabNavItem = $('.bk-tab-nav .tab-nav-item');
    var bkTabContent = $('.bk-tab-pane');
    bkTabNavItem.on('click', function() {
        var index = $(this).index();
        if (!$(this).hasClass('active')) {
            $(this).addClass('active');
            $(this).siblings().removeClass('active');
            $(bkTabContent[index]).addClass('active');
            $(bkTabContent[index]).siblings().removeClass('active');
        }
    });
    //bk-tab_js_end
})();