/**
 * Created by carlos on 29/10/14.
 */
$(document).ready(function () {

    var App = {
        state_modal: false,
        state_drop: false,
        menu: false,
        menu2: false,
        state_detail: false,
        focus_tag: false,
        focus_editor: false,
        cont_mod: 1,
        modal_center: function (modal) {
            for(var i=0;i<modal.length;i++){

                modal[i].on("click", function(e) {
                    e.stopPropagation();
                });

                var left = $(window).width() / 2 - modal[i].width() / 2,
                    top = $(window).height() / 2 - modal[i].height() / 2;

                modal[i].css({"top": top + "px", "left": left + "px"});
            }

            var d_left = $(window).width() / 2 - $(".mod_save_changed").width() / 2;

            $(".mod_save_changed").css("left", d_left+"px");


            $(window).resize(function () {
                for(var i=0;i<modal.length;i++){
                    var left = $(window).width() / 2 - modal[i].width() / 2,
                        top = $(window).height() / 2 - modal[i].height() / 2;

                    modal[i].css({"top": top + "px", "left": left + "px"});
                }
                var d_left = $(window).width() / 2 - $(".mod_save_changed").width() / 2;

                $(".mod_save_changed").css("left", d_left+"px");
            })
        },
        show_modal: function () {
            var self = this;
            if(self.state_modal == false ) {

                $(".set_opinion").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".mod_opinion").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".add_module_pay").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".new_pay").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".cl_save_ch").on("click", function () {
                    $(".mod_save_changed").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".edit_pay_btn").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".edit_pay").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $("#boton-enviar-load").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".send_succes").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".del_acc").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".mod_delete_account").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".id_signup").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".signup_mod").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".id_login").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".login_mod").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".btn_new_pro").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".new_project").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".act_new_d").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".new_discussion").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".show_invite").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".mod_invite").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".histo_fact").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".mod_historial_fact").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".pp_likes").on("click", function () {
                    $(".back_shadow").fadeIn(200);
                    $(".mod_comments").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".show_comment").on("click", function() {
                    $(".back_shadow").fadeIn(200);
                    $(".list_comments").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".new_diss").on("click", function() {
                    $(".back_shadow").fadeIn(200);
                    $(".discuss_modal").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".new_dissc").on("click", function() {
                    $(".back_shadow").fadeIn(200);
                    $(".new_discussion").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".op_follow1").on("click", function() {
                    $(".back_shadow").fadeIn(200);
                    $(".seguidores").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                $(".op_follow2").on("click", function() {
                    $(".back_shadow").fadeIn(200);
                    $(".siguiendo").fadeIn(400);
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);
                });

                var option;
                var block;
                var flag=false;

                $("#new_modulo").on("click",".edit_this_video", function(){
                    block = $(this);
                    option=2;
                    $(".back_shadow").fadeIn(200);
                    $(".upload_modal").fadeIn(400);
                    $(".box_load").css("display","block");
                    $(".cont_complete_video").css("display","none");
                    $(".cont_load_video").css("display","none");
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);

                    if(flag==false) {
                        App.call_drag_drop();
                        flag=true;
                    }
                });

                var cont;
                $("#new_modulo").on("click",".add_video", function(e){
                    cont = $(this);
                    option=1;
                    $(".back_shadow").fadeIn(200);
                    $(".upload_modal").fadeIn(400);
                    $(".box_load").css("display","block");
                    $(".cont_complete_video").css("display","none");
                    $(".cont_load_video").css("display","none");
                    setTimeout(function(){
                        self.state_modal = true;
                    },100);

                    if(flag==false) {
                        App.call_drag_drop();
                        flag=true;
                    }
                });

                $(".done_project").on("click", function() {
                    if(option==1){
                        cont.parent().find(".add_new_video").append("<div class='char_video'><div class='cv_wrapper'>"+
                            "<div class='cv_image'><img src='img/up_video.png' alt=''/></div><div class='cv_text'><div class='cvt_cont'>"+
                            $(".mod_in_title").val()+"</div><div class='cv_state'><ul><li class='barra'><div class='porcentage'></div>"+
                            "</li><li>10%</li><li class='point'><i class='fa fa-circle'></i></li><li>Clase1.mp4</li>"+
                            "</div></div><div class='cv_option cl_delete'><i class='fa fa-close'></i> <a>Cancelar</a></div></div>");
                    } else {
                        block.parent().find(".cv_text .cvt_cont i").html($(".mod_in_title").val());
                    }

                    $(".back_shadow").fadeOut(400);
                    $(".upload_modal").fadeOut(200);
                    self.state_modal = false;
                });
                $(".delete_unit").on("click", function() {
                    if(option!=1){
                        block.parent().parent().remove();
                    }

                    $(".back_shadow").fadeOut(400);
                    $(".upload_modal").fadeOut(200);
                    self.state_modal = false;
                });

                $("#new_modulo").on("click",".cl_delete", function() {
                    $(this).parent().parent().remove();
                });
            }
        },
        call_drag_drop: function() {
            var $filequeue,
                $filelist;

            $filequeue = $(".demo .filelist.queue");
            $filelist = $(".demo .filelist.complete");

            $(".demo .dropped").dropper({
                action: "http://formstone.it/components/Dropper/demo/upload.php",
                maxSize: 1048576
            }).on("start.dropper", onStart)
                .on("complete.dropper", onComplete)
                .on("fileStart.dropper", onFileStart)
                .on("fileProgress.dropper", onFileProgress)
                .on("fileComplete.dropper", onFileComplete)
                .on("fileError.dropper", onFileError);

            $(window).one("pronto.load", function() {
                $(".demo .dropped").dropper("destroy").off(".dropper");
            });

            function onStart(e, files) {
                console.log("Start");

                var html = '';

                for (var i = 0; i < files.length; i++) {
                    html += '<li data-index="' + files[i].index + '"><span class="file">' + files[i].name + '</span><span class="progress">Queued</span></li>';
                }

                $filequeue.append(html);
            }

            function onComplete(e) {
                console.log("Complete");
                // All done!
                $(".cont_load_video").fadeOut(200);
                setTimeout(function() {
                    $(".cont_complete_video").fadeIn(200);
                },200);
            }

            function onFileStart(e, file) {
                console.log("File Start");

                $(".box_load").fadeOut(200);
                setTimeout(function() {
                    $(".cont_load_video").fadeIn(200);
                },200);

                $filequeue.find("li[data-index=" + file.index + "]")
                    .find(".progress").text("0%");
            }

            function onFileProgress(e, file, percent) {
                console.log("File Progress");

                $filequeue.find("li[data-index=" + file.index + "]")
                    .find(".progress").text(percent + "%");
            }

            function onFileComplete(e, file, response) {
                console.log("File Complete");

                if (response.trim() === "" || response.toLowerCase().indexOf("error") > -1) {
                    $filequeue.find("li[data-index=" + file.index + "]").addClass("error")
                        .find(".progress").text(response.trim());
                } else {
                    var $target = $filequeue.find("li[data-index=" + file.index + "]");

                    $target.find(".file").text(file.name);
                    $target.find(".progress").remove();
                    $target.appendTo($filelist);
                }
            }

            function onFileError(e, file, error) {
                console.log("File Error");

                $filequeue.find("li[data-index=" + file.index + "]").addClass("error")
                    .find(".progress").text("Error: " + error);
            }
        },
        close_modal: function () {
            var self = this;

            $(".general_close").on("click", function() {
                $(".back_shadow").fadeOut(400);
                $(".signup_mod").fadeOut(200);
                $(".login_mod").fadeOut(200);
                $(".mod_invite").fadeOut(200);
                $(".list_comments").fadeOut(200);
                $(".discuss_modal").fadeOut(200);
                $(".upload_modal").fadeOut(200);
                $(".new_discussion").fadeOut(200);
                $(".new_project").fadeOut(200);
                $(".mod_comments").fadeOut(200);
                $(".seguidores").fadeOut(200);
                $(".siguiendo").fadeOut(200);
                $(".new_pay").fadeOut(200);
                $(".edit_pay").fadeOut(200);
                $(".send_succes").fadeOut(200);
                $(".mod_opinion").fadeOut(200);
                $(".mod_delete_account").fadeOut(200);
                $(".mod_historial_fact").fadeOut(200);
                $(".mod_save_changed").fadeOut(200);
                self.state_modal = false;
            });

            $(".nh_close").on("click", function () {
                $(".back_shadow").fadeOut(400);
                $(".mod_invite").fadeOut(200);
                $(".new_discussion").fadeOut(200);
                self.state_modal = false;
            });
            $(".discuss_modal .close").on("click", function () {
                $(".back_shadow").fadeOut(400);
                $(".new_discussion").fadeOut(200);
                self.state_modal = false;
            });

            $(".wrapper").on("click", function() {
                if(self.state_modal == true) {
                    $(".back_shadow").fadeOut(400);
                    $(".signup_mod").fadeOut(200);
                    $(".login_mod").fadeOut(200);
                    $(".mod_invite").fadeOut(200);
                    $(".list_comments").fadeOut(200);
                    $(".discuss_modal").fadeOut(200);
                    $(".upload_modal").fadeOut(200);
                    $(".new_discussion").fadeOut(200);
                    $(".new_project").fadeOut(200);
                    $(".mod_comments").fadeOut(200);
                    $(".seguidores").fadeOut(200);
                    $(".siguiendo").fadeOut(200);
                    $(".new_pay").fadeOut(200);
                    $(".edit_pay").fadeOut(200);
                    $(".send_succes").fadeOut(200);
                    $(".mod_opinion").fadeOut(200);
                    $(".mod_delete_account").fadeOut(200);
                    $(".mod_historial_fact").fadeOut(200);
                    $(".mod_save_changed").fadeOut(200);
                    self.state_modal = false;
                }
            });
        },
        show_dropdown: function() {
            var self = this;
            $("#drop_cat").on("click", function() {
                if(self.state_drop == false) {
                    $("#lev_drop").css("display","none");
                    $("#cat_toggle").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $("#show_perfil").on("click", function() {
                if(self.state_drop == false) {
                    $("#option_per").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $("#coins").on("click", function() {
                if(self.state_drop == false) {
                    $("#dd_coins").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $("#drop_level").on("click", function() {
                if(self.state_drop == false) {
                    $("#cat_toggle").css("display","none");
                    $("#lev_drop").css("display","block");
                    $("#filter_toggle").css("display","none");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $("#drop_category").on("click", function() {
                if(self.state_drop == false) {
                    $("#cat_list").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $(".bell").on("click", function() {
                if(self.state_drop == false) {
                    $(".drop_notification").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
            $("#drop_filter").on("click", function() {
                if(self.state_drop == false) {
                    $("#cat_toggle").css("display","none");
                    $("#lev_drop").css("display","none");
                    $("#filter_toggle").css("display","block");
                    setTimeout(function(){
                        self.state_drop = true;
                    },100)
                }
            });
        },
        close_dropdown: function() {
            var self = this;
            $(".wrapper").on("click", function() {
                if(self.state_drop==true) {
                    $("#cat_toggle").css("display","none");
                    $("#lev_drop").css("display","none");
                    $("#filter_toggle").css("display","none");
                    $("#cat_list").css("display","none");
                    $(".drop_off").css("display","block");
                    $(".drop_on").css("display","none");
                    $("#option_per").css("display","none");
                    $("#dd_coins").css("display","none");
                    $(".drop_notification").css("display","none");
                    self.state_drop = false;
                }
            })
        },
        slide_down: function() {
            $("#slide_down").on("click", function() {
                setTimeout(function(){
                    $("html,body").animate({ scrollTop : $("#learn").offset().top  }, 1200 );
                },100)
            });
        },
        menu_slide: function(id_click,panel,content) {
            var self = this;
            id_click.on("click", function() {
                if(self.menu == false ) {
                    panel.animate({"left":"+0px"},300);
                    content.animate({"left":"+200px"},300);
                    setTimeout(function(){
                        self.menu = true;
                    },10)
                }
            });
            id_click.on("click", function() {
                if(self.menu == true ) {
                    panel.animate({"left":"-200px"},300);
                    content.animate({"left":"-0px"},300);
                    self.menu = false;
                }
            });
        },
        menu_slide_width: function(id_click,panel,content,width) {
            var self = this;
            id_click.on("click", function() {
                if(self.menu2 == false ) {
                    panel.animate({"left":"+0px"},300);
                    content.animate({"left":"+"+width+"px"},300);
                    setTimeout(function(){
                        self.menu2 = true;
                    },10)
                }
            });
            id_click.on("click", function() {
                if(self.menu2 == true ) {
                    panel.animate({"left":"-"+width+"px"},300);
                    content.animate({"left":"-0px"},300);
                    self.menu2 = false;
                }
            });
        },
        show_details: function() {
            var self = this;
            $(".sh_detail").on("click", function() {
                var object = $(this);
                if(self.state_detail == false) {
                    object.find("p").slideDown(300);
                    object.find(".fa-angle-up").css("display","block");
                    object.find(".fa-angle-down").css("display","none");
                    setTimeout(function(){
                        self.state_detail = true;
                    },100)
                }
            });
            $(".slide_text").on("click", function() {
                var object = $(this);
                if(self.state_detail == false) {
                    object.parent().find(".nb_body").slideDown(300);
                    object.find(".on").css("display","block");
                    object.find(".off").css("display","none");
                    setTimeout(function(){
                        self.state_detail = true;
                    },100)
                }
            });
        },
        close_details: function() {
            var self = this;
            $(".sh_detail").on("click", function() {
                var object = $(this);
                if(self.state_detail == true) {
                    object.find("p").slideUp(300);
                    object.find(".fa-angle-up").css("display","none");
                    object.find(".fa-angle-down").css("display","block");
                    self.state_detail = false;
                }
            });
            $(".slide_text").on("click", function() {
                var object = $(this);
                if(self.state_detail == true) {
                    object.parent().find(".nb_body").slideUp(300);
                    object.find(".on").css("display","none");
                    object.find(".off").css("display","block");
                    self.state_detail = false;
                }
            });
        },
        dropdown_modulo: function () {
            var load_video_act;
            $("#new_modulo").on("click",".item_modulo_select", function () {
                load_video_act=$(this).parent().children(".load_video");
                load_video_act.slideToggle(200);
            });

            $("#new_modulo").on("click",".finish_pro", function() {
                var cont = $(this).parent().parent().parent().find(".load_video");
                cont.slideUp(200);
            });

            $("#new_modulo").on("click",".delete_pro", function() {
                var cont=$(this).parent().parent().parent();
                console.log(cont,"cont")
                cont.remove();
            });
        },
        click_heart: function() {
            $(".fli_circle").on("click", function() {
                $(this).find("i").css("color","#ed656c");
            });
        },
        close_message: function() {
            $(".bm_close").on("click", function() {
                $(".block_message").slideUp(200);
            });
        },
        show_dialoge: function() {
            $("#in_title").focus(function() {
                $(".bi_message_1").fadeIn(200);
            });
            $("#in_title").focusout(function() {
                $(".bi_message_1").fadeOut(200);
            });
        },
        focus: function() {
            var self = this;

            $(".mod_in_title").focus(function() {
                $(".bi_message_modal").fadeIn(200);
            });

            $(".mod_in_title").focusout(function() {
                $(".bi_message_modal").fadeOut(200);
            });
            $("#singleFieldTags").on("click", function(e) {
                $(this).css("border","1px solid #A3CFDB");
                setTimeout(function(){
                    self.focus_tag=true;
                },100);
                e.stopPropagation();
            });
            $(".wrapper").on("click", function() {
                if(self.focus_tag==true) {
                    $("#singleFieldTags").css("border","1px solid #DCDDDC");
                    self.focus_tag=false;
                }
            })
        },
        add_modulo: function() {
            var self = this;
            $(".add_module").on("click", function() {
                $("#new_modulo").append("<div class='new_module'><h4 class='nm_h4'>Módulo <span>"+ self.cont_mod +"</span></h4>"+
                    "<input type='text' placeholder=''¿Qué es lo que los alumnos aprenderán?'/><div class='add_new_video'></div>"+
                    "<div class='char_video'><div class='cv_wrapper'><div class='cv_image'><img src='img/up_video.png' alt=''/>"+
                    "</div><div class='cv_text'><div class='cvt_cont'>1. <i>Clase 1</i></div><div class='cv_state'>"+
                    "<p><span>100</span>% cargado <i>(puede tomar hasta 30 minutos en procesar despues de guardar)</i></p>"+
                    "</div></div><div class='cv_option edit_this_video'><i class='fa fa-pencil'></i> <a>Editar</a></div>"+
                    "</div></div><div class='btn_add_video add_video'><i class='fa fa-plus-circle'></i>"+
                    "<p>Agregar video clases</p></div></div>");

                self.cont_mod = self.cont_mod + 1;
                /*$.ajax({
                    url: "new_modulo.html",
                    success: function(html)
                    {
                        if(html)
                        {
                            setTimeout(function(){
                                $("#new_modulo").append(html);
                                html.find(".nm_h4").html("100");
                            },500);

                        }
                    }
                });*/
            });
        },
        show_new_project: function() {
            $(".s_new_proj").on("click", function() {
                $(".wrapp_fade").fadeOut(200);
                setTimeout(function(){
                    $(".page_np").fadeIn(200);
                },200);
            });

            $(".back_fade").on("click", function() {
                $(".page_np").fadeOut(200);
                setTimeout(function(){
                    $(".wrapp_fade").fadeIn(200);
                },200);
            });
        },
        input_real_time: function() {
            $("#new_modulo").on("keyup",".in_name", function() {
                var cont = $(this).parent().parent().parent().find(".new_name");
                cont.text($(this).val());
            });
        },
        checkout: function() {
            $(".sh_cupon").on("click", function() {
                $(".cod_cupon").slideToggle(200);
            });

            $(".save_method_pay").on("click", function() {
                $(".back_shadow").fadeOut(400);
                $(".new_pay").fadeOut(200);
                setTimeout(function() {
                    $(".mod_type2").fadeIn(200);
                },600)
            });
        },
        valorar_like: function() {
            $(".cl_like").on("click", function() {
                $(this).css("background-color","#52e498");
                $(".cl_no_like").css("background-color","#cfcfcf");
            });
            $(".cl_no_like").on("click", function() {
                $(this).css("background-color","#ff3e3e");
                $(".cl_like").css("background-color","#cfcfcf");
            })
        }
    };
    var array_modals = [
        $(".signup_mod"),
        $(".login_mod"),
        $(".new_discussion"),
        $(".list_comments"),
        $(".discuss_modal"),
        $(".mod_invite"),
        $(".new_project"),
        $(".send_succes"),
        $(".mod_opinion"),
        $(".mod_comments"),
        $(".mod_followers"),
        $(".mod_views"),
        $(".upload_modal"),
        $(".new_pay"),
        $(".edit_pay"),
        $(".welcome_flikn"),
        $(".mod_historial_fact"),
        $(".mod_delete_account")
    ];

    App.modal_center(array_modals);

    App.show_modal();
    App.close_modal();
    App.show_dropdown();
    App.close_dropdown();
    App.slide_down();
    App.menu_slide($("#slide_right"),$(".menu_responsive"),$(".wrapper"));
    App.menu_slide_width($("#menu_slide"),$(".cc_panel"),$(".cc_body"),250);
    App.menu_slide_width($("#conf_menu"),$(".cc_panel"),$(".cc_wrapp"),200);
    App.menu_slide_width($(".s_perfil"),$(".pp_data"),$(".pp_history"),263);
    App.menu_slide_width($(".toolbar"),$(".be_panel"),$(".be_block"),198);
    App.menu_slide_width($(".menu"),$(".dp_person"),$(".dp_variable"),264);
    App.show_details();
    App.close_details();
    App.dropdown_modulo();
    App.click_heart();
    App.close_message();
    App.show_dialoge();
    App.focus();
    App.add_modulo();
    App.show_new_project();
    App.input_real_time();
    App.checkout();
    App.valorar_like();

});