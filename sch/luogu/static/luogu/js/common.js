/** !
 *	全局通用js
 *	Created @ 2017/2/28 by blueking
 */

(function() {
    var sideBar = $(".bk-sidebar");
    sideBar.on("click", "li>a", function() {
        if ($(this).parents(".bk-sidebar").hasClass("slide-close")) return;
        var _this = $(this).parent();
        var _thisParent = _this.siblings();
        if (_this.hasClass("pureLink")) {
            _this.addClass("open").siblings().removeClass("open");
        } else {
            _this.toggleClass("open").siblings().removeClass("open");
            _this.find(".flex-subnavs").slideToggle();
        }

        _thisParent.find(".flex-subnavs").slideUp();
    });

    sideBar.on("click", ".flex-subnavs a", function() {
        $(".flex-subnavs a").removeClass("on");
        $(this).addClass("on");
        if ($(this).parents(".bk-sidebar").hasClass("slide-close")) {
            $(this).parents("li").addClass("open").siblings().removeClass("open")
        }
    });
})();