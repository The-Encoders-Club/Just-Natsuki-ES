default persistent._jn_headpats_total_given = 0

init python in jn_headpats:
    import os
    import random
    import store
    import store.jn_utils as jn_utils
    import store.jn_plugins as jn_plugins

    _PATS_UI_Z_INDEX = 4
    _PATS_POPUP_Z_INDEX = 5


    _more_pats_requested = False
    _no_pat_count = 0
    _pats_finished = False
    _is_idle = True


    _last_mouse_position = None
    _cursor_in_active_area = False

    def _getMousePositionChanged():
        """
        Returns whether the current mouse position has changed compared to the last mouse position given as stored under _last_mouse_position.
        """
        if _last_mouse_position is None or _last_mouse_position != renpy.get_mouse_pos():
            return True
        
        return False

    def _setCursorInActiveArea(is_active):
        """
        Sets whether the cursor is in the active pat area for Natsuki.__capped_aff_dates.
        Needed as SetVariable on hovered/unhovered doesn't function properly on mousearea elements; thanks Ren'Py.

        IN:
            - is_active - bool state to set
        """
        global _cursor_in_active_area
        _cursor_in_active_area = is_active

    jn_plugins.registerExtrasOption(
        option_name="Headpats",
        visible_if="store.Natsuki.isLove(higher=True)",
        jump_label="headpats_start"
    )


label headpats_start:
    $ jn_headpats._pats_finished = False
    $ jn_headpats._more_pats_requested = False

    if persistent._jn_headpats_total_given == 0:
        n 1uskemlesh "¡¿E-{w=0.2}eh?!{w=0.75}{nw}"
        extend 1uwdemlsbl " ¡¿A-{w=0.1}acabas de decir...?!{w=0.75}{nw}"
        n 2kbkwrlsbl "¡[player]!{w=0.5} ¡E-{w=0.2}espera...!"
        show natsuki headpats waiting min

    elif persistent._jn_headpats_total_given < 10:
        n 1knmemlsbl "¡¿E-{w=0.2}esto otra vez?!"
        n 2kslunlsbr "[player]..."
        show natsuki headpats waiting min

    elif persistent._jn_headpats_total_given < 25:
        n 1ksqsllsbr "...¿De nuevo,{w=0.2} [player]?"
        n 2ksrcalsbl "..."
        show natsuki headpats waiting low

    elif persistent._jn_headpats_total_given < 50:
        n 1kcspulesisbl "..."
        n 2kslcaf "Bien..."
        show natsuki headpats waiting medium

    elif persistent._jn_headpats_total_given < 250:
        n 2kcscaf "...Bien."
        show natsuki headpats waiting high
    else:

        n 4nsrssf "...Está bien."
        show natsuki headpats waiting high

    show screen headpats_ui
    jump headpats_loop


label headpats_loop:
    $ current_mouse_position = renpy.get_mouse_pos()
    $ config.mouse = {"default": [("mod_assets/extra/headpats/headpats_active_cursor.png", 24, 24)]} if jn_headpats._cursor_in_active_area else None

    if jn_headpats._cursor_in_active_area and jn_headpats._getMousePositionChanged():
        python:
            global _last_mouse_position
            persistent._jn_headpats_total_given += 1
            jn_headpats._no_pat_count = 0
            jn_headpats._last_mouse_position = current_mouse_position
            jn_headpats._is_idle = False

        play audio headpat
        show headpats_effect_popup zorder jn_headpats._PATS_POPUP_Z_INDEX
        show natsuki headpats active
        $ jnPause(0.75)
        hide headpats_effect_popup

        python:
            milestone_label = "headpats_milestone_{0}".format(str(persistent._jn_headpats_total_given))
            if (renpy.has_label(milestone_label)):
                renpy.jump(milestone_label)

            elif (
                persistent._jn_headpats_total_given > 1000
                and persistent._jn_headpats_total_given % 1000 == 0
            ):
                renpy.jump("headpats_milestone_1000_plus")
    else:

        $ jn_headpats._no_pat_count += 1


        if not jn_headpats._is_idle and persistent._jn_headpats_total_given < 10:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting min

        elif not jn_headpats._is_idle and persistent._jn_headpats_total_given < 25:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting low

        elif not jn_headpats._is_idle and persistent._jn_headpats_total_given < 100:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting medium

        elif not jn_headpats._is_idle:
            $ jn_headpats._is_idle = True
            show natsuki headpats waiting high


        if (jn_headpats._no_pat_count == 12):
            jump headpats_inactive

    $ jnPause(1)
    jump headpats_loop

label headpats_inactive:
    if persistent._jn_headpats_total_given == 0:
        n 2fwmeml "¿M-{w=0.2}me estás tomando el pelo o qué?"
        show natsuki 2fcspol

    elif persistent._jn_headpats_total_given <= 10:
        n 2fcspolsbr "...¿Vas a hacer algo o qué?{w=0.75}{nw}"
        extend 1kslunl " Cielos..."
        show natsuki 1kslsll

    elif persistent._jn_headpats_total_given <= 25:
        n 1kslpul "...¿Acaso..."
        n 4knmpulsbr "...Y-{w=0.2}ya cambiaste de opinión o algo?"
        show natsuki 1knmbolsbr

    elif persistent._jn_headpats_total_given <= 50:
        n 4kwmpulsbr "...¿Y-{w=0.2}ya no tenías ganas o algo así?"
        show natsuki 4kwmbolsbr
    else:

        n 3kllbolsbr "...¿Ya terminaste,{w=0.2} o...?"
        show natsuki 4kwmbolsbr

    jump headpats_loop



label headpats_milestone_5:
    n 2fcsunlsbl "Mmmmmm..."
    n 1ksrunlsbr "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_10:
    n 4kwmpulsbr "¿T-{w=0.2}todavía sigues?{w=0.5}{nw}"
    extend 2ksrunfsbl " Cielos..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_25:
    n 1kslunl "Uuuuuuu..."
    n 3kcsemlesi "Mi cabello estará {i}tan{/i} enredado luego..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_50:
    n 1ncsemlesi "..."
    n 4fsqcal "...¿D-{w=0.2}divirtiéndote,{w=0.2} [player]?"
    n 4ksrcaf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_100:
    n 4ksqtrfsbr "...Realmente estás disfrutando esto,{w=0.2} ¿eh?"
    n 1kslcaf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_250:
    n 1ksqcal "...Aun sigues con fuerza,{w=0.2} ¿eh [player]?{w=0.75}{nw}"
    extend 4ksrfsl " Je."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_500:
    n 1ucspul "Esto...{w=0.75}{nw}"
    extend 1nslsml " no es tan malo en realidad."
    n 3fcscafsbr "U-{w=0.2}una vez que te acostumbras."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_750:
    n 4kcsssfesi "...Haah."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_1000:
    n 1kcssmf "..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_milestone_1000_plus:
    n 1kcsssfeaf "...[player]..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    jump headpats_loop

label headpats_finished:
    $ config.mouse = None
    $ jn_headpats._pats_finished = True


    if (
        persistent._jn_headpats_total_given >= 100
        and random.randint(0,3) == 1
        and not jn_headpats._more_pats_requested
    ):
        n 2kslbol "..."
        n 2kslsll "Uhmm...{w=0.75}{nw}"
        extend 4knmsll " [player]?"
        n 1klrpulsbl "¿Podrías...{w=0.75}{nw}"
        extend 2ksrbolsbl " ya sabes..."
        n 4knmbolsbr "¿Seguir haciendo eso solo un poco más?"

        show natsuki 1fcscalesssbr at jn_center
        menu:
            n "S-{w=0.2}solo un poco."
            "Por supuesto":

                n 1ksrssf "...{w=0.3}Gracias,{w=0.2} [player]."
                $ jn_headpats._more_pats_requested = True
                $ jn_headpats._pats_finished = False
                $ jn_headpats._is_idle = False
                jump headpats_loop
            "Es todo por ahora":

                n 2nslbol "...Oh."
                n 2fcsemlsbl "B-{w=0.2}bueno,{w=0.2} ¡está bien!{w=0.75}{nw}"
                extend 2fcspolsbl " Realmente no me {i}gusta{/i} tanto de todos modos."
                n 1kslpol "..."
    else:
        $ finished_start_quip = renpy.substitute(random.choice([
            "...¿Satisfecho?",
            "¿Feliz ahora,{w=0.2} [player]?",
            "...¿T-{w=0.3}terminaste ya?",
            "¿T-{w=0.2}odo listo,{w=0.2} [player]?",
            "¿E-{w=0.2}eso es todo,{w=0.2} [player]?"
        ]))
        n 1kwmpul "[finished_start_quip]"

        $ finished_end_quip = renpy.substitute(random.choice([
            "...Bien.",
            "...Y-{w=0.2}ya era hora.",
            "Finalmente...{w=0.5} cielos...",
            "T-{w=0.2}tardaste bastante.",
            "Finalmente..."
        ]))
        n 1kllpul "[finished_end_quip]"

        n 1kcsdvf "..."

    $ jn_headpats._cursor_in_active_area = False
    hide screen headpats_ui
    jump ch30_loop


transform snap_popup_fadeout:
    easeout 0.75 alpha 0


image headpats_effect_popup:
    block:
        choice:
            "mod_assets/extra/headpats/headpat_poof_a.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_b.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_c.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_d.png"
            ease 0.33 alpha 1.0 yoffset -30
        choice:
            "mod_assets/extra/headpats/headpat_poof_e.png"
            ease 0.33 alpha 1.0 yoffset -30

    snap_popup_fadeout


image natsuki headpats waiting min:
    block:
        choice:
            "natsuki 1kllemf"
        choice:
            "natsuki 1klremf"
        choice:
            "natsuki 1klrunf"
        choice:
            "natsuki 1kllunf"
        choice:
            "natsuki 1fcsunf"

        pause 5
        repeat


image natsuki headpats waiting low:
    block:
        choice:
            "natsuki 1knmpul"
        choice:
            "natsuki 1kslbol"
        choice:
            "natsuki 1ksrbol"
        choice:
            "natsuki 1kwmbol"
        choice:
            "natsuki 1kllbol"
        choice:
            "natsuki 1klrbol"
        choice:
            "natsuki 1klrunl"
        choice:
            "natsuki 1kllunl"

        pause 5
        repeat


image natsuki headpats waiting medium:
    block:
        choice:
            "natsuki 1nnmbol"
        choice:
            "natsuki 1nslbol"
        choice:
            "natsuki 1nsrbol"
        choice:
            "natsuki 1tnmsll"
        choice:
            "natsuki 1tslsll"
        choice:
            "natsuki 1tslsll"
        choice:
            "natsuki 1tsrsll"
        choice:
            "natsuki 1nslpol"
        choice:
            "natsuki 1nsrpol"
        choice:
            "natsuki 1nsqpol"

        pause 5
        repeat


image natsuki headpats waiting high:
    block:
        choice:
            "natsuki 1ksqcal"
        choice:
            "natsuki 1knmcal"
        choice:
            "natsuki 1kwmbol"
        choice:
            "natsuki 1kslfsl"
        choice:
            "natsuki 1ksrfsl"

        pause 5
        repeat


image natsuki headpats active:
    block:
        choice:
            "natsuki 4kcssmf"
        choice:
            "natsuki 1kchcaf"
        choice:
            "natsuki 1fchcaf"
        choice:
            "natsuki 2kslcaf"
        choice:
            "natsuki 2ksrcaf"
        choice:
            "natsuki 1kcscaf"
        choice:
            "natsuki 4kchpuf"

        pause 2
        repeat

screen headpats_ui():
    zorder jn_headpats._PATS_UI_Z_INDEX


    text "{0} caricias dadas".format(persistent._jn_headpats_total_given) size 30 xalign 0.5 ypos 40 text_align 0.5 xysize (None, None) outlines [(3, "#000000aa", 0, 0)] style "categorized_menu_button_text"

    mousearea:
        area (506, 109, 265, 155)
        hovered Function(jn_headpats._setCursorInActiveArea, True)
        unhovered Function(jn_headpats._setCursorInActiveArea, False)
        focus_mask None


    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 450

        textbutton _("Terminado"):
            style "hkbd_option"
            action [
                Function(renpy.jump, "headpats_finished"),
                SensitiveIf(not jn_headpats._pats_finished)
            ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
