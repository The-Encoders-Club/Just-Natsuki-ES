init python in jn_idles:
    import datetime
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    _m1_script0x2didles__ALL_IDLES = {}

    _last_idle_label = None

    def selectIdle():
        """
        Picks and returns a single random idle, or None if no idles are available.
        The same idle cannot be returned two times in a row.
        """
        global _last_idle_label
        not_label = [_last_idle_label] if _last_idle_label is not None else []
        
        idle_list = JNIdle.filterIdles(
            idle_list=getAllIdles(),
            affinity=store.Natsuki._getAffinityState(),
            not_label=not_label
        )
        return_idle = random.choice(idle_list).label if len(idle_list) > 0 else None
        _last_idle_label = return_idle
        
        return return_idle

    def getAllIdles():
        """
        Returns a list of all idles.
        """
        return _m1_script0x2didles__ALL_IDLES.values()

    class JNIdleTypes(Enum):
        reading = 1
        gaming = 2
        resting = 3
        vibing = 4
        working = 5

    class JNIdle:
        """
        Describes an idle that Natsuki can initiate in the gaps between topics randomly.
        """
        def __init__(
            self,
            label,
            idle_type,
            affinity_range=None,
            conditional=None
        ):
            """
            Constructor.

            IN:
                - label - The name used to uniquely identify this idle and refer to it internally
                - idle_type - The category of the idle
                - affinity_range - The affinity range that must be satisfied for this idle to be picked when filtering
                - conditional - Python statement that must evaluate to True for this idle to be picked when filtering
            """
            self.label = label
            self.idle_type = idle_type
            self.affinity_range = affinity_range
            self.conditional = conditional
        
        def _m1_script0x2didles__currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this idle's affinity_range.

            IN:
                - affinity_state - Affinity state to test if the holidays can be shown in. If None, the current affinity state is used.
            
            OUT:
                - True if the current affinity is within range; otherwise False.
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()
            
            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)
        
        def _m1_script0x2didles__filterIdle(
            self,
            affinity=None,
            not_label=None
        ):
            """
            Returns True if the idle meets the filter criteria, otherwise False.

            IN:
                - affinity - The affinity the idle must match in its affinity_range.
                - not_label - List of labels the idle must not match

            OUT:
                - True if all filter criteria has been passed; otherwise False.
            """
            if affinity is not None and not self._m1_script0x2didles__currAffinityInAffinityRange(affinity):
                return False
            
            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False
            
            elif not_label is not None and self.label in not_label:
                return False
            
            return True
        
        @staticmethod
        def filterIdles(
            idle_list,
            affinity=None,
            not_label=None
        ):
            """
            Returns a filtered list of idles, given an idle list and filter criteria.

            IN:
                - affinity - The affinity the idle must match in its affinity_range.
                - not_label - List of labels the idle must not match

            OUT:
                - list of idles matching the search criteria
            """
            return [
                _idle
                for _idle in idle_list
                if _idle._m1_script0x2didles__filterIdle(
                    affinity,
                    not_label
                )
            ]

    def _m1_script0x2didles__registerIdle(idle):
        """
        Registers a new idle in the list of idles, allowing it to be selected randomly between topics.
        
        IN:
            - idle - JNIdle to register.
        """
        if idle.label in _m1_script0x2didles__ALL_IDLES:
            jn_utils.log("Cannot register idle name: {0}, as an idle with that name already exists.".format(idle.label))
        
        else:
            _m1_script0x2didles__ALL_IDLES[idle.label] = idle

    def _concludeIdle():
        """
        Wraps up an idle by setting the last idle call time and jumping to the talk menu.
        This is necessary as we can't call the menu and then return like a topic.
        """
        store.LAST_IDLE_CALL = datetime.datetime.now()
        renpy.jump("talk_menu")

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_twitch_playing",
        idle_type=JNIdleTypes.gaming,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional=(
            "get_topic('event_wintendo_twitch_battery_dead').shown_count > 0"
            " or get_topic('event_wintendo_twitch_game_over').shown_count > 0"
        )
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_reading_parfait_girls",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_caught_reading_manga').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_reading_renpy_for_dummies",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_renpy_for_dummies').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_reading_a_la_mode",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional="get_topic('event_reading_a_la_mode').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_reading_step_by_step",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        conditional="get_topic('event_step_by_step_manga').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_naptime",
        idle_type=JNIdleTypes.resting,
        affinity_range=(jn_affinity.AFFECTIONATE, None)
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_daydreaming",
        idle_type=JNIdleTypes.resting,
        affinity_range=(jn_affinity.NORMAL, None)
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_poetry_attempts",
        idle_type=JNIdleTypes.working,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('event_caught_writing_poetry').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_vibing_headphones",
        idle_type=JNIdleTypes.vibing,
        affinity_range=(jn_affinity.HAPPY, None),
        conditional="persistent.jn_custom_music_unlocked"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_whistling",
        idle_type=JNIdleTypes.vibing,
        affinity_range=(jn_affinity.NORMAL, None)
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_laptop",
        idle_type=JNIdleTypes.gaming,
        affinity_range=(jn_affinity.HAPPY, None)
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_math_attempts",
        idle_type=JNIdleTypes.working,
        affinity_range=(jn_affinity.NORMAL, None),
        conditional="get_topic('talk_favorite_subject').shown_count > 0"
    ))

    _m1_script0x2didles__registerIdle(JNIdle(
        label="idle_plantcare",
        idle_type=JNIdleTypes.reading,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        conditional="jn_desk_items.getDeskItem('jn_sanjo').unlocked"
    ))

label idle_twitch_playing:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop wintendo_twitch_playing free zorder JN_PROP_ZORDER
    show natsuki gaming
    hide black with Dissolve(0.5)
    $ jnPause(0.5)
    $ jnClickToContinue(silent=False)

    n 1tnmpueqm "...?{w=1}{nw}"
    show prop wintendo_twitch_held free
    n 1unmflesu "¡Oh!{w=1}{nw}"
    extend 1fchbgsbr " ¿Qué pasa,{w=0.2} [player]?"

    if random.choice([True, False]):
        n 1fllsssbr "Solo tengo que guardar rápido..."
    else:

        n 1fsrsssbr "Solo dame un segundo..."

    show natsuki gaming
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_parfait_girls:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.right) == "jn_parfait_manga_closed":
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_parfait_manga_held"))
    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    n 1tlrbo "...{w=1}{nw}"
    n 1tnmboeqm "...?{w=1}{nw}"
    n 1unmflesu "¡Oh!{w=0.75}{nw}"
    extend 1fchbgsbl " ¡Hola!"

    if random.choice([True, False]):
        n 1fslsssbl "Déjame marcar esto muy rápido..."
    else:

        n 1fcssssbl "Solo tengo que encontrar un buen punto para parar..."

    show natsuki reading
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)

    if random.choice([True, False]):
        play audio drawer
        $ jnPause(1.3)
    else:

        play audio book_closing
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_parfait_manga_closed"))
        $ jnPause(0.3)

    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_renpy_for_dummies:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if Natsuki.getDeskItemReferenceName(jn_desk_items.JNDeskSlots.left) == "jn_renpy_for_dummies_closed":
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.left)

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_held"))
    $ Natsuki.setIsReadingToRight(True)
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    n 1fdwbo "...{w=1}{nw}"
    n 1tnmboeqm "...?{w=1}{nw}"
    n 1unmflesu "¡Oh!{w=0.75}{nw}"
    extend 1nlrsssbr " Hola.{w=1}{nw}"
    extend 1nsrsssbr " Solo déjame terminar aquí rápido."

    if random.choice([True, False]):
        n 1nsrbosbr "..."
        n 1nnmaj "...Y no.{w=1}{nw}"
        extend 1fslpo " El libro todavía apesta."
    else:

        n 1fcsflsbr "Nada de esta basura tenía sentido,{w=0.2} d-{w=0.2}de todos modos."

    show natsuki 1fcspo
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fcssmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)

    if random.choice([True, False]):
        play audio drawer
        $ jnPause(1.3)
    else:

        play audio book_closing
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_closed"))
        $ jnPause(0.3)

    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_a_la_mode:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_a_la_mode_manga_held"))
    show natsuki reading
    hide black with Dissolve(0.5)
    $ Natsuki.setIsReadingToRight(False)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1unmaj "¡Ah!{w=1}{nw}"
        extend 1unmbg " ¡[player]!{w=1}{nw}"
        extend 1fcsbg " Justo a tiempo."
        n 1fsqsm "{i}Juuuusto{/i} terminé ese capítulo~.{w=1.25}{nw}"
        extend 1fchsm " Jejeje."
    else:

        n 1tnmpu "¿Eh?{w=1}{nw}"
        extend 1unmajl " ¡Oh!{w=0.75}{nw}"
        extend 1nlrsslsbl " Je."
        n 1nsrsssbl "Yo...{w=1}{nw}"
        extend 1nslsssbl " me distraje un poco.{w=0.75}{nw}"
        extend 1fspgs " Pero viejo,{w=0.2} ¡esta es una buena lectura!"
        n 1fcsbg "No tienes {w=0.3}{i}idea{/i}{w=0.3} de lo que te estás perdiendo,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fsqsm " Jejeje."

    show natsuki 1fcssm
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_reading_step_by_step:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_step_by_step_manga_held"))
    show natsuki reading
    hide black with Dissolve(0.5)
    $ Natsuki.setIsReadingToRight(False)
    $ jnClickToContinue(silent=False)

    n 1tnmpu "¿Eh?{w=1.25}{nw}"
    extend 1unmfllesu " ¡Oh!{w=0.75}{nw}"
    extend 1ullfllsbl " ¡[player]!"

    if random.choice([True, False]):
        n 1nslbolsbl "..."
        n 1nslajl "Solo...{w=1}{nw}"
        extend 1nslssl " dame un segundo.{w=1}{nw}"
        extend 1nsrcal " Recién me estaba metiendo en eso..."
    else:

        n 1fcsbglsbr "¿Q-{w=0.2}qué pasa?{w=1}{nw}"
        extend 1nsrsslsbr " Solo voy a...{w=1}{nw}"
        extend 1nsrcal " marcar esto muy rápido."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1fchsmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_naptime:
    $ jn_globals.force_quit_enabled = False
    show natsuki sleeping
    $ jnPause(7.1)
    $ jnClickToContinue(silent=False)

    n 3kcsslesl "...Mmmnnn...{w=2}{nw}"
    n 3kwlpuesl "...¿Nnnn?{w=1}{nw}"
    extend 3ksqpul " ¿Qué...?{w=2}{nw}"
    n 3unmpulesu "¡...!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    $ jn_globals.force_quit_enabled = True
    n 4unmfllsbr "¡[player_initial]-[player]!{w=1}{nw}"
    extend 4nsrunlsbr " Cielos..."
    n 2nsrpol "¿Qué pasa?"

    $ jn_idles._concludeIdle()

label idle_daydreaming:
    show natsuki thinking
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 3flrpu "...{w=1.5}{nw}"
        n 3tnmpueqm "...?{w=1}{nw}"
        n 4unmfleex "¡Oh!{w=0.75}{nw}"
        extend 4fllsslsbr " H-{w=0.2}hola."
        n 2fcsajlsbr "Y-{w=0.2}yo {i}totalmente{/i} no estaba distraída ni nada por el estilo.{w=1}{nw}"
        extend 2fsrposbr " En caso de que te lo estuvieras preguntando."
        n 1fcsajsbr "C-{w=0.2}como sea."
    else:

        n 3tlrca "...{w=1.5}{nw}"
        n 3tnmpueqm "¿Eh?{w=1}{nw}"
        extend 4unmemeex " ¡Oh!{w=1}{nw}"
        extend 4nllfllsbr " [player]."
        n 2fcspolsbr "D-{w=0.2}deberías saber {i}realmente{/i} que no debes interrumpir a alguien pensando,{w=0.75}{nw}"
        extend 2flrposbr " sabes."
        n 2fcsajsbr "De todos modos..."

    $ jn_idles._concludeIdle()

label idle_poetry_attempts:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop poetry_attempt zorder JN_PROP_ZORDER
    show natsuki working_on_papers
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=1.25}{nw}"
        n 1unmajesu "¡Oh!{w=0.75}{nw}"
        extend 1fchbgsbl " Hola,{w=0.2} [player]."
        n 1tnmsm "..."
        n 1tnmpu "¿...Qué?{w=0.75}{nw}"
        extend 1klrflsbl " ¿A qué viene esa mirada,{w=0.5}{nw}"
        extend 1knmbosbl " tan de repente?"
        n 1udwfll "..."
        n 1udwemleex "¡A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1flremlsbl " ¿E-{w=0.2}esto?{w=0.75}{nw}"
        extend 1fcsemlsbl " ¡No es nada!{w=1}{nw}"
        extend 1fcscalsbl " N-{w=0.2}nada en absoluto."
    else:

        n 1tlrca "...{w=1.25}{nw}"
        n 1tnmcaeqm "...?{w=0.75}{nw}"
        n 1unmeml "¡A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1ulreml " ¡[player]!"
        n 1fcsajlsbr "¡S-{w=0.2}solo un segundo!{w=1}{nw}"
        extend 1fsrcalsbr " Cielos..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 1nsrcasbl
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_vibing_headphones:
    python:
        import copy

        outfit_to_restore = jn_outfits.getOutfit(Natsuki.getOutfitName())
        headphones = jn_outfits.getWearable("jn_headgear_cat_headphones")
        if not headphones.unlocked:
            headphones.unlock()

        headphones_outfit = copy.copy(outfit_to_restore)
        headphones_outfit.headgear = headphones

    show natsuki 1ncsca
    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show prop music_notes zorder JN_PROP_ZORDER
    $ jn_outfits.saveTemporaryOutfit(headphones_outfit)
    show natsuki vibing
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 4tslboeqm "...{w=1}{nw}"
        n 4tnmboeqm "...?{w=0.75}{nw}"
        hide prop
        n 1unmfllesh "¡O-{w=0.2}oh!{w=0.75}{nw}"
        extend 1flrsslsbl " ¡[player]!{w=0.75}{nw}"
        extend 2fsrdvlsbl " Je."
        n 2fcsfllsbl "S-{w=0.2}solo dame un segundo aquí."
    else:

        n 1tsqcaeqm "...?{w=1}{nw}"
        n 1uskemlesh "¡...!{w=0.75}{nw}"
        hide prop
        $ player_initial = jn_utils.getPlayerInitial()
        n 4fbkwrl "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 4fnmemlsbr " ¡¿Cuánto tiempo has estado {i}sentado ahí{/i}?!{w=1.25}{nw}"
        extend 2fslfllsbr " Cielos..."
        n 2fcsposbr "Al {i}menos{/i} déjame poner esto a cargar primero..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ jnPause(1.3)
    $ Natsuki.setOutfit(outfit_to_restore)
    show natsuki 2nsrcasbl
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_whistling:
    show natsuki whistling
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=0.75}{nw}"
        n 4unmfllesh "¡O-{w=0.2}oh!{w=0.75}{nw}"
        extend 4cllssl " H-{w=0.2}hola [player]."
        n 4tnmbo "¿Qué pasa?"
    else:

        n 4tllbo "...{w=0.75}{nw}"
        n 4tnmboeqm "...?{w=0.75}{nw}"
        n 4unmfllesh "¡A-{w=0.2}ah!{w=0.75}{nw}"
        extend 2nlrsslsbl " Je.{w=0.75}{nw}"
        extend 2nllbolsbl " Hola."
        n 2tnmbo "¿Qué sucede,{w=0.2} [player]?"

    $ jn_idles._concludeIdle()

label idle_laptop:
    show natsuki 4udwbo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)

    if random.choice([True, False]):
        show natsuki reading
    else:

        show natsuki gaming

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_laptop"))
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 4tdwbo "...{w=0.75}{nw}"
        n 4tnmfleqm "¿Eh?{w=0.75}{nw}"
        n 4unmaj "Oh.{w=0.75}{nw}"
        extend 4ulraj " Hola [player].{w=0.75}{nw}"
        extend 4cllsssbl " Déjame terminar aquí rápido..."
        show natsuki gaming
    else:

        n 4cdwpu "...{w=0.75}{nw}"
        n 4cnmpueqm "...?{w=0.75}{nw}"
        n 4unmfllesh "¿Eh?{w=0.75}{nw}"
        extend 4unmgslesh " ¡O-{w=0.2}oh!{w=0.75}{nw}"
        extend 4fllbglsbr " ¡[player]!"
        n 4cslsssbr "Je."
        n 4ccsajsbr "Yo...{w=1}{nw}"
        extend 4clrcasbr " me distraje un poco.{w=0.75}{nw}"
        extend 4ccstrsbr " S-{w=0.2}solo dame un segundo para apagar,{w=0.2} ¿de acuerdo?"
        show natsuki 4ccscasbr

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio laptop_close
    $ jnPause(0.75)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    $ jnPause(1.3)
    show natsuki 3ullbo
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_math_attempts:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    show prop math_attempt zorder JN_PROP_ZORDER
    show natsuki working_on_papers
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)

    if random.choice([True, False]):
        n 1tnmboeqm "...?{w=1.25}{nw}"
        n 1uwdajesu "¡Oh!{w=0.75}{nw}"
        extend 1fchbgsbl " H-{w=0.2}hola [player]."
        n 2fslsssbl "Y-{w=0.2}yo solo estaba..."
        n 2fslunsbl "..."
        n 2ccsfl "Ugh.{w=0.5} No importa.{w=0.75}{nw}"
        extend 2fcsposbr " Matemáticas es una materia tonta de todos modos."
    else:

        n 1tlrca "...{w=1.25}{nw}"
        n 1tnmcaeqm "...?{w=0.75}{nw}"
        n 1uwdwrlesh "¡A-{w=0.2}ah!{w=0.75}{nw}"
        extend 1cdrbol " ¡[player]!"
        n 2fcsajlsbr "¡Tú {i}seriamente{/i} necesitas aprender hablar más fuerte!{w=0.75}{nw}"
        extend 2fcsfllsbr " Cielos..."
        n 2cslbosbr "Al menos déjame limpiar este desastre..."

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 4nsrbosbl
    hide prop
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()

label idle_plantcare:
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_sanjo"))
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_plant_care_book_held"))
    $ Natsuki.setIsReadingToRight(True)
    show prop watering_can zorder JN_PROP_ZORDER
    show natsuki reading
    hide black with Dissolve(0.5)
    $ jnClickToContinue(silent=False)
    $ dialogue_choice = random.randint(1, 3)

    if dialogue_choice == 1:
        n 1cdwbo "...{w=0.75}{nw}"
        n 1tnmboeqm "...?{w=0.75}{nw}"
        n 1uwdflesu "¡Oh!{w=0.75}{nw}"
        extend 1fllbgsbr " H-{w=0.2}hola,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fchbgsbr " ¿Qué sucede?"
        n 1unmaj "Déjame terminar aquí rápido.{w=0.75}{nw}"
        extend 1ccsss " Además."
        n 1cdltr "Tengo que cuidar bien a Sanjo después de todo,{w=0.5}{nw}"
        extend 1fcscaesi " sabes."
        show natsuki 1fcsca

    elif dialogue_choice == 2:
        n 1clrpu "...{w=0.75}{nw}"
        n 1tnmpu "...¿Eh?{w=0.75}{nw}"
        n 1unmpuesu "¡Oh!{w=0.75}{nw}"
        extend 1cllsssbr " Je.{w=0.75}{nw}"
        extend 1ccssssbr " ¿Qué pasa,{w=0.2} [player]?"
        n 1clraj "Solo dame un minuto.{w=0.75}{nw}"
        extend 1nsrpo " Me estaba cansando de todo este parloteo de plantas de todos modos."
        show natsuki 1ccspo
    else:

        n 1cdwpu "...{w=0.75}{nw}"
        n 1cnmpueqm "¿Eh?{w=0.75}{nw}"
        extend 1unmaj " Oh.{w=0.75}{nw}"
        extend 1ullbo " Hola,{w=0.2} [player]."
        n 1clrss "No me hagas caso.{w=0.75}{nw}"
        extend 1fcsss " No me hagas caso para nada."
        n 1fcssmesm "¡Soooooolo me aseguro de mantener a Sanjo aquí en plena forma!"
        show natsuki 1fchsmeme

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    $ jn_idles._concludeIdle()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
