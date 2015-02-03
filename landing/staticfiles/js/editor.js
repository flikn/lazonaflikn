/**
 * Created by rikhart on 08/11/14.
 */

$(document).ready(function () {

    var focus_editor = false;

    tinymce.init({
        selector: ".editor",
        menubar : false,
        statusbar: false,
        inline:false,
        skin: 'light',
        auto_focus: false,
        plugins: [
            "advlist autolink lists link image charmap print preview anchor",
            "searchreplace visualblocks code fullscreen",
            "insertdatetime media table contextmenu paste"
        ],
        toolbar: "bold italic underline | bullist numlist | link image",
        setup: function(editor) {
            editor.on('focus', function(e) {
                $(".bi_message_2").fadeIn(200);
                $(".block_inputs .ec_editor").css("border","1px solid #A3CFDB");
                setTimeout(function(){
                    focus_editor=true;
                },10);
            });
            /*editor.on('focusOut', function(e) {
                $(".bi_message_2").fadeOut(200);
            });*/
        }
    });

    var effect = {
        focus: function() {
            $(".block_inputs .ec_editor").on("click", function(e) {
                $(this).css("border","1px solid #A3CFDB");
                $(".bi_message_2").fadeIn(200);
                setTimeout(function(){
                    focus_editor=true;
                },10);
                e.stopPropagation();
            });

            $(".wrapper").on("click", function() {
                if(focus_editor==true) {
                    $(".bi_message_2").fadeOut(200);
                    $(".block_inputs .ec_editor").css("border","1px solid #DCDDDC");
                    focus_editor=false;
                }
            })
        }
    };

    effect.focus();

});