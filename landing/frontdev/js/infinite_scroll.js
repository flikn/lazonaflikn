/**
 * Created by carlos on 08/11/14.
 */
$(document).ready(function() {

    var App = {
        infinite: function() {
            $(window).scroll(function()
            {
                if($(window).scrollTop() == $(document).height() - $(window).height())
                {
                    $('div#loadmoreajaxloader').css("display","block");
                    $.ajax({
                        url: "scroll.html",
                        success: function(html)
                        {
                            if(html)
                            {
                                setTimeout(function(){
                                    $("#postswrapper").append(html);
                                    $('div#loadmoreajaxloader').css("display","none");
                                },500);

                            }else
                            {
                                $('div#loadmoreajaxloader').html('<center>No more posts to show.</center>');
                            }
                        }
                    });
                }
            });
        }
    };

    App.infinite();

});