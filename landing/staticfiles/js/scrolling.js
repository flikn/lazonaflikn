/**
 * Created by carlos on 08/11/14.
 */
$(document).ready(function () {
    var App = {
        fixed_cont: function() {
            $(window).scroll(function () {
                var poswin = $(window).scrollTop(),
                    offset_cont = $("#wrapp_fixed").offset().top;
                if(poswin>=(offset_cont-100)) {
                    $("#cont_fixed").css({"position": "fixed","opacity":"1"});
                } else {
                    $("#cont_fixed").css({"position": "relative","opacity":"0"});
                }
            })
        }
    };

    App.fixed_cont();
});