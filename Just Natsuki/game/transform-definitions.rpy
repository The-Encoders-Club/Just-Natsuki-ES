








transform categorized_menu_slide_in_right:
    subpixel True
    xoffset 600
    easeout 0.4 xoffset 0

transform jn_tcommon(x=640):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        xcenter x yoffset -20
        easein .25 yoffset 0 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform jn_center:
    jn_tcommon(640)

transform jn_left:
    jn_tcommon(400)

transform jn_farleft:
    jn_tcommon(240)

transform jn_right:
    jn_tcommon(880)

transform jn_veryright:
    jn_tcommon(1040)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
