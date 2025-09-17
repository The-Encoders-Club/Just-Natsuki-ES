init offset = -1









style hotkeys_text:
    font gui.interface_font
    size gui.interface_text_size
    color "#e2d1d1"
    outlines [(3, "#000000aa", 0, 0)]
    xalign 0.0
    yalign 0.5

    line_overlap_split 8
    line_spacing 8
    line_leading 8

screen hotkeys():
    tag menu
    $ config.mouse = None

    use game_menu(("Hotkeys")):
        viewport id "hotkeys":
            yoffset 0
            xoffset 50
            hbox:
                vbox:
                    box_wrap True
                    label _("All hotkeys") style "check_label"
                    null height 20
                    style_prefix "hotkeys"
                    grid 2 8:
                        xoffset 20
                        spacing 10

                        text _("Talk")
                        text _("T")

                        text _("Music")
                        text _("M")

                        text _("Extras")
                        text _("E")

                        text _("Fullscreen")
                        text _("F")

                        text _("Hide UI")
                        text _("H")

                        text _("Screenshot")
                        text _("S")

                        text _("Settings")
                        text _("Esc")

                        null width 175 height 30
                        null width 175 height 0

            if persistent.jn_snap_unlocked:
                hbox:
                    xoffset 300
                    vbox:
                        box_wrap True
                        label _("Snap hotkeys") style "check_label"
                        null height 20
                        style_prefix "hotkeys"
                        grid 2 3:
                            xoffset 20
                            spacing 10

                            text _("Place")
                            text _("1")

                            text _("Snap!")
                            text _("2")

                            null width 175 height 30
                            null width 175 height 0

            if persistent._jn_blackjack_unlocked:
                hbox:
                    xoffset 550
                    vbox:
                        box_wrap True
                        label _("Blackjack hotkeys") style "check_label"
                        null height 20
                        style_prefix "hotkeys"
                        grid 2 3:
                            xoffset 20
                            spacing 10

                            text _("Hit!")
                            text _("1")

                            text _("Stay")
                            text _("2")

                            null width 175 height 30
                            null width 175 height 0






















define prev_adjustment = ui.adjustment()
define main_adjustment = ui.adjustment()
define selected_category = None
define scroll_align = -0.1

style categorized_menu_button is choice_button:
    xysize (250, None)
    padding (25, 5, 25, 5)
    top_padding 10
    bottom_padding 5

style categorized_menu_button_text is choice_button_text:
    align (0.0, 0.0)
    text_align 0.0
    line_leading 0
    line_spacing 2

style categorized_menu_button_italic is categorized_menu_button

style categorized_menu_button_text_italic is categorized_menu_button_text:
    italic True

screen categorized_menu(menu_items, category_pane_space, option_list_space, category_length):
    style_prefix "categorized_menu"


    fixed at categorized_menu_slide_in_right:
        anchor (0, 0)
        pos (category_pane_space[0], category_pane_space[1])
        xsize category_pane_space[2]
        ysize category_pane_space[3]

        bar:
            adjustment prev_adjustment
            style "classroom_vscrollbar"
            xalign -0.1

        vbox:
            ypos 0
            yanchor 0

            viewport:

                yadjustment prev_adjustment
                yfill False

                mousewheel True
                arrowkeys True
                has vbox
                if category_length == 0:
                    textbutton _("Nevermind."):
                        action [
                                Return(False),
                                Function(prev_adjustment.change, 0),
                                SetVariable("selected_category", None)
                            ]
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                else:
                    python:
                        import random

                        go_back_text = "Go back"
                        if random.randint(0, 999) == 1:
                            go_back_text = "Go baka"

                    textbutton _(go_back_text):
                        style "categorized_menu_button"
                        action [ Return(-1), Function(prev_adjustment.change, 0) ]
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                    null height 20

                for button_name in menu_items.keys():
                    $ has_unseen = len(Topic.filter_topics(topic_list=menu_items.get(button_name), nat_says=False, is_seen=False)) > 0
                    $ display_text = "{i}[button_name]{/i}" if has_unseen else button_name

                    textbutton display_text:
                        style "categorized_menu_button"

                        action SetVariable("selected_category", button_name)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                        if has_unseen:
                            idle_background Frame("mod_assets/buttons/choice_hover_blank_star.png", gui.frame_hover_borders, tile=gui.frame_tile)

                    null height 5



    if menu_items.get(selected_category):
        fixed:
            area option_list_space

            bar:
                adjustment main_adjustment
                style "classroom_vscrollbar"
                xalign -0.1

            vbox:
                ypos 0
                yanchor 0

                viewport:
                    yadjustment main_adjustment
                    yfill False
                    mousewheel True
                    arrowkeys True

                    has vbox
                    textbutton _("Nevermind."):
                        action [
                                Return(False),
                                Function(prev_adjustment.change, 0),
                                SetVariable("selected_category", None)
                            ]
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                    null height 20

                    for _topic in menu_items.get(selected_category):
                        $ display_text = _topic.prompt if (_topic.shown_count > 0 or _topic.nat_says) else "{i}[_topic.prompt]{/i}"


                        textbutton display_text:
                            style "categorized_menu_button"

                            action [ Return(_topic.label), Function(prev_adjustment.change, 0), SetVariable("selected_category", None) ]
                            hover_sound gui.hover_sound
                            activate_sound gui.activate_sound

                            if _topic.shown_count == 0 and not _topic.nat_says:
                                idle_background Frame("mod_assets/buttons/choice_hover_blank_star.png", gui.frame_hover_borders, tile=gui.frame_tile)

                        null height 5

screen scrollable_choice_menu(items, last_item=None, option_width=560, icon_path=None, menu_caption=None):
    if icon_path and persistent._jn_display_option_icons:
        add icon_path anchor (0, 0) pos (1280 - (275 + option_width), 20)

    elif not persistent._jn_display_option_icons:
        $ option_width += 175

    if option_width > 560:
        $ option_width = 560

    if menu_caption:
        text "[menu_caption]" style "hkbd_label" pos (1280 - (40 + option_width), 20)

    $ scrollable_start_y = 60 if menu_caption else 40

    fixed:
        area (1280 - (40 + option_width), scrollable_start_y, option_width, 440)
        vbox:
            ypos 0
            yanchor 0

            if last_item:
                textbutton last_item[0]:
                    style "categorized_menu_button"
                    xsize option_width
                    action Return(last_item[1])
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound

                null height 20

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                has vbox
                for prompt, _value in items:
                    textbutton prompt:
                        id prompt
                        style "categorized_menu_button"
                        xsize option_width
                        action Return(_value)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound

                    null height 5

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align





style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(3, "#000000aa", 0, 0)]
    line_overlap_split 1.25
    line_spacing 0

style default_monika is normal:
    slow_cps 30

style default_slow is normal:
    slow_cps 10

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

    line_overlap_split -8
    line_spacing 0

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    underline True
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5
    size gui.button_text_size

style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("mod_assets/panels/slider_back_h.png", tile=False)
    thumb Frame("mod_assets/panels/slider_thumb_h.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("mod_assets/panels/slider_back_v.png", tile=False)
    thumb Frame("mod_assets/panels/slider_thumb_v.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style slider:
    ysize 18
    base_bar Frame("mod_assets/panels/slider_back_h.png", tile=False)
    thumb "mod_assets/panels/slider_thumb_small.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("mod_assets/panels/slider_back_v.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "mod_assets/panels/slider_thumb_small.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("mod_assets/panels/frame.png", gui.frame_borders, tile=gui.frame_tile)



















screen say(who, what):
    zorder 30

    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("mod_assets/panels/textbox.png", xalign=0.5, yalign=1.0)

style window_up is window:
    background Image("mod_assets/panels/textbox.png", xalign=0.5, yalign=-5.0)

style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("mod_assets/panels/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    size gui.say_text_size

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

    line_overlap_split -8
    line_spacing 0
    line_leading 8

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "mod_assets/panels/ctc.png"
    block:
        easeout 0.75 alpha 1.0 yoffset 0
        easein 0.75 alpha 0.5 yoffset -5
        repeat











image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"
    window:
        has vbox
        xalign .5
        yalign .5
        spacing 30

        text prompt style "input_prompt"
        input id "input"

style input_prompt:
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xcenter 0.5
    text_align 0.5











screen choice(items, scroll="viewport"):
    zorder 30
    style_prefix "choice"

    vbox:
        xalign 0.9
        for i in items:
            textbutton i.caption:
                action i.action
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound


screen choice_centred(items, scroll="viewport"):
    zorder 30
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound



screen choice_centred_mute(items, scroll="viewport"):
    zorder 30
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
                hover_sound None
                activate_sound None



define config.narrator_menu = True

style choice_vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style choice_bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style choice_scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style choice_vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style choice_slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style choice_vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style choice_frame:
    padding gui.frame_borders.padding
    background Frame("mod_assets/panels/frame.png", gui.frame_borders, tile=gui.frame_tile)

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []
    line_leading 6
    line_spacing 0

init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 295]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
        elif currentpos[1] > targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
    def RigMouse2():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
    def RigMouse3():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 0]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)


screen force_mouse_move():

    on "show":
        action MouseMove(x=600, y=600, duration=.3)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)
screen rigged_choice3(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse2)
screen rigged_choice2(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse3)




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("mod_assets/buttons/choice_hover_blank.png", gui.frame_borders, tile=gui.frame_tile)
    hover_background Frame("mod_assets/buttons/choice_hover_fold.png", gui.frame_hover_borders, tile=gui.frame_tile)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []






style quickmenu_text:
    color "#e2d1d1"
    hover_color "#FF8ED0"
    selected_color "#b59"
    size 14

screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            textbutton _("History"):
                text_style "quickmenu_text"
                action ShowMenu('history')
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            textbutton _("Auto"):
                text_style "quickmenu_text"
                action Preference("auto-forward", "toggle")
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            textbutton _("Settings"):
                text_style "quickmenu_text"
                action ShowMenu('preferences')
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            textbutton _("Hide"):
                text_style "quickmenu_text"
                action HideInterface()
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

default quick_menu = True




style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []











screen indicator(message):
    key "mouseup_3" action Return()
    style_prefix "game_menu"

    text (message):
        style "return_button"
        xpos 10 ypos 70

screen navigation():
    $ config.mouse = None

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("New Game"):
                action If(
                    persistent.playername,
                    true=Start(),
                    false=Show(
                        screen="name_input",
                        message="Please enter your name",
                        ok_action=Function(FinishEnterName)
                    )
                )

        else:
            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

            textbutton _("Submods") action [ShowMenu("submods_list_screen"), SensitiveIf(renpy.get_screen("submods_list_screen") == None)]

        textbutton _("Hotkeys") action [ShowMenu("hotkeys"), SensitiveIf(renpy.get_screen("hotkeys") == None)]

        textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]


        textbutton _("GitHub") action OpenURL(jn_globals.LINK_JN_GITHUB)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]








screen main_menu():
    tag menu


    style_prefix "main_menu"
    add "menu_bg"
    add "menu_art_n"

    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"

    add "menu_particles"
    if persistent.playthrough != 4:
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size











screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "mod_assets/backgrounds/menu/background.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="You wont be needing to save anymore,\nBesides it doesn't work when we're sitting doing nothing like this...", ok_action=Hide("dialog"))
        else:
            return FileAction(name)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []









define persistent.room_animation = True

screen preferences():
    tag menu
    $ config.mouse = None


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings")):

        viewport id "preferences":
            ysize 650
            yoffset -75
            xoffset 40
            scrollbars "vertical"
            mousewheel True
            draggable True

            has vbox
            yoffset 0

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        textbutton _("Menu icons") action [
                            ToggleField(
                                object=persistent,
                                field="_jn_display_option_icons",
                                true_value=True,
                                false_value=False)
                            ]

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen text") action Preference("skip", "toggle")
                    textbutton _("After choices") action Preference("after choices", "toggle")

                vbox:

                    style_prefix "radio"
                    label _("Weather")

                    textbutton _("Disabled") action SetField(
                            object=persistent,
                            field="_jn_weather_setting",
                            value=int(jn_preferences.weather.JNWeatherSettings.disabled)
                        )

                    textbutton _("Random") action SetField(
                            object=persistent,
                            field="_jn_weather_setting",
                            value=int(jn_preferences.weather.JNWeatherSettings.random)
                        )

                    if persistent._jn_weather_api_configured:
                        textbutton _("Real-time") action [
                                SetField(
                                    object=persistent,
                                    field="_jn_weather_setting",
                                    value=int(jn_preferences.weather.JNWeatherSettings.real_time)
                                ),
                                SensitiveIf(persistent._jn_weather_api_configured)
                            ]

                vbox:
                    style_prefix "check"
                    label _("Natsuki")
                    textbutton _("Auto outfits") action [
                            ToggleField(
                                object=persistent,
                                field="jn_natsuki_auto_outfit_change_enabled",
                                true_value=True,
                                false_value=False)
                        ]
                    textbutton _("Repeat topics") action [
                            ToggleField(
                                object=persistent,
                                field="jn_natsuki_repeat_topics",
                                true_value=True,
                                false_value=False)
                        ]
                    textbutton _("Idles") action [
                            ToggleField(
                                object=persistent,
                                field="_jn_natsuki_idles_enabled",
                                true_value=True,
                                false_value=False)
                        ]

                vbox:
                    style_prefix "check"
                    label _("Notifications")
                    textbutton _("Conversations") action [
                            ToggleField(
                                object=persistent,
                                field="_jn_notify_conversations",
                                true_value=True,
                                false_value=False)
                        ]

                    textbutton _("Activity") action [
                            ToggleField(
                                object=persistent,
                                field="_jn_notify_activity",
                                true_value=True,
                                false_value=False)
                        ]

                vbox:
                    if persistent._jn_blackjack_unlocked:
                        style_prefix "check"
                        label _("Blackjack")
                        textbutton _("Hand total") action [
                                ToggleField(
                                    object=persistent,
                                    field="_jn_blackjack_show_hand_value",
                                    true_value=True,
                                    false_value=False)
                            ]




            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Random chatter: {0}".format(jn_preferences.random_topic_frequency.getRandomTopicFrequencyDescription()))

                    bar value FieldValue(
                            object=persistent,
                            field="jn_natsuki_random_topic_frequency",
                            range=4,
                            style="slider",
                            step=1
                        )

                    label _("Text Speed")

                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    label _("Sunrise: {0}AM".format(jn_locations.getHourFromSunriseSunsetValue(persistent._jn_sunrise_setting)))
                    bar value FieldValue(persistent, "_jn_sunrise_setting", range=6, max_is_zero=False, style="slider")

                    label _("Sunset: {0}PM".format(jn_locations.getHourFromSunriseSunsetValue(persistent._jn_sunset_setting)))
                    bar value FieldValue(persistent, "_jn_sunset_setting", range=6, max_is_zero=False, style="slider")

                vbox:
                    if config.has_music:
                        label _("Music Volume: {0}%".format(int(preferences.get_volume("music") * 100)))

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume: {0}%".format(int(preferences.get_volume("sfx") * 100)))

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"





                vbox:
                    style_prefix "radio"
                    label _("Language")


                    textbutton "English" text_font "DejaVuSans.ttf" action [Language(None), SetField(persistent, "language", "english"), Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Hide("dialog"))]
                    textbutton "Español" text_font "mod_assets/fonts/FuzzyBubbles-Regular.ttf" action [Language("spanish"), SetField(persistent, "language", "spanish"), Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Hide("dialog"))]

    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "default"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/RifficFree-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "mod_assets/buttons/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines [(2, "#000000aa", 0, 0)]

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "mod_assets/buttons/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    color "#e2d1d1"
    hover_color "#FF8ED0"
    outlines [(2, "#000000aa", 0, 0)]

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():
    $ config.mouse = None




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

    line_overlap_split 8
    line_spacing 8
    line_leading 8

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

    line_overlap_split 8
    line_spacing 8
    line_leading 8

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width

    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

    line_overlap_split 8
    line_spacing 8
    line_leading 8

style history_label:
    xfill True

    line_overlap_split 8
    line_spacing 8
    line_leading 8

style history_label_text:
    xalign 0.5

    line_overlap_split 8
    line_spacing 8
    line_leading 8





init python:
    def FinishEnterName(launchGame=True):
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        if launchGame:
            renpy.jump_out_of_context("start")


screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen endgame(message):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

screen credits(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Done") action ok_action

init python:
    def check_ingame_state_add_apology():
        if Natsuki.isInGame():
            Natsuki.addApology(jn_apologies.ApologyTypes.cheated_game)

screen confirm_editable(message, yes_text, no_text, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(yes_text) action yes_action
            textbutton _(no_text) action no_action

screen confirm_editable_closable(message, yes_text, no_text, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        if in_sayori_kill and message == layout.QUIT:
            add "confirm_glitch" xalign 0.5

        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            textbutton _("Close") action Hide("confirm_editable_closable"):
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(yes_text) action yes_action
            textbutton _(no_text) action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "mod_assets/panels/frame.png", "mod_assets/panels/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_frame_text is choice_button_text

style confirm_prompt_text:
    color "#e2d1d1"
    outlines [(2, "#000000aa", 0, 0)]
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is choice_button_text:
    properties gui.button_text_properties("confirm_button")


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 1000
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.75 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("mod_assets/panels/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size
    line_overlap_split 8
    line_spacing 8
    line_leading 8

screen problem(message):
    zorder 100
    text "[message]" size 30 xalign 0.5 ypos 40 text_align 0.5 xysize (None, None) color "#FF0000" outlines [(2, "#000000d2", 0, 0)]

init:
    screen warn(message):
        zorder 100
        text "[message]" size 20 xpos 10 ypos 10 text_align 0 xysize (None, None) color "#FF3333" outlines [(2, "#000000d2", 0, 0)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
