default persistent._jn_player_profanity_during_introduction = False

init python in jn_introduction:
    from Enum import Enum
    import random
    import store
    import store.jn_utils

    class JNIntroductionStates(Enum):
        """
        Different introduction sequences states/phases; we use these to track progress
        """
        new_game = 1
        first_meeting = 2
        collecting_thoughts = 3
        calmed_down = 4
        acceptance = 5
        complete = 6
        
        def __int__(self):
            return self.value

    INTRODUCTION_STATE_LABEL_MAP = {
        JNIntroductionStates.new_game: "introduction_opening",
        JNIntroductionStates.first_meeting: "introduction_first_meeting",
        JNIntroductionStates.collecting_thoughts: "introduction_collecting_thoughts",
        JNIntroductionStates.calmed_down: "introduction_calmed_down",
        JNIntroductionStates.acceptance: "introduction_acceptance",
        JNIntroductionStates.complete: "introduction_exit"
    }

default persistent.jn_introduction_state = 1

label introduction_progress_check:
    $ Natsuki.setOutfit(jn_outfits.getOutfit("jn_school_uniform"))


    if not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.new_game:
        $ config.allow_skipping = False
        $ n.display_args["callback"] = jnNoDismissDialogue
        $ n.what_args["slow_abortable"] = False
        play audio static
        show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch

        $ main_background.show()
        $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
        show natsuki idle introduction zorder JN_NATSUKI_ZORDER at jn_center
        $ jnPause(0.25)
        hide glitch_garbled_a
        play music audio.space_classroom_bgm fadein 1

    $ renpy.jump(jn_introduction.INTRODUCTION_STATE_LABEL_MAP.get(jn_introduction.JNIntroductionStates(persistent.jn_introduction_state)))

label introduction_opening:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ n.display_args["callback"] = jnNoDismissDialogue
    $ n.what_args["slow_abortable"] = False
    show black zorder JN_BLACK_ZORDER
    $ jnPause(5)




    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a
    $ jnPause(5)


    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    $ jnPause(0.25)
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    $ jnPause(0.5)
    play audio glitch_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    $ jnPause(7)


    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    $ jnPause(0.25)
    play audio glitch_b
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    $ jnPause(0.5)

    if random.randint(0,10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder JN_GLITCH_ZORDER with hpunch
        $ jnPause(1)
        hide glitch_garbled_red

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show sky glitch_fuzzy zorder JN_GLITCH_ZORDER
    play sound interference loop
    $ jnPause(10)

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show sky glitch_fuzzy zorder JN_GLITCH_ZORDER
    play sound interference loop
    $ jnPause(1.5)


    stop sound
    hide sky glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch


    $ Natsuki.setOutfit(jn_outfits.getOutfit("jn_school_uniform"))
    $ main_background.show()
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
    show natsuki idle introduction zorder JN_NATSUKI_ZORDER at jn_center
    pause 0.25
    hide black
    hide glitch_garbled_a
    play music audio.space_classroom_bgm fadein 1

    jump introduction_first_meeting

label introduction_first_meeting:

    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 4uscsctsc "¡AAAAAaaaaAAAAHHH!"
    n 4uskwrtsc "¡A-{w=0.1}alguien!{w=0.5} ¡¿QUIEN SEA?!{w=0.5} ¡AYUDA!{w=0.5}{nw}"
    extend 1fbkwr " ¡¡AYÚDENME!!"
    n 4uscemtsc "Y-{w=0.1}Yuri,{w=0.1} ella es..."
    n 1ullem "E-{w=0.3}ella es..."
    n 1uskem "... ¿H-{w=0.3}huh?"
    n 4uscaj "¿Q...{w=0.5} qué es...?"
    n 1fllup "Yo...{w=0.5} Yo solo estaba huyendo de..."
    n 1flrun "¿Qué está pasan-{w=0.5}{nw}"

    show natsuki 4kskantsc
    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(0.5)
    play audio glitch_c
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 4fcsantsa "¡Ugh!"
    n 1kcsfutsa "Nnnnnnghhhh..."
    n 1kcsantsasbl "D-{w=0.3}duele...{w=0.5} duele tanto...{w=1}{nw}"

    show natsuki 4fcsantsasbl
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a

    n 1kskan "Y-{w=0.1}y yo soy..."
    n 4kskaj "...No... {w=1}{nw}"
    extend 4kscemsbl "oh por favor no.{w=0.5} y-{w=0.3}yo no puedo.{w=0.5} Realmente no puedo ser...{w=0.5}{nw}"

    show natsuki 4kcsantsc
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 4fcsuptsa "¡Hhnnngghh!{w=1}{nw}"
    extend 4kcsuptsaeso " M-{w=0.3}mi cabeza..."
    n 4kcsantsa "Tengo que...{w=0.3} tengo que...{w=0.3} p-{w=0.1}pensar..."
    n 2kcsaj "...{w=1}{nw}"
    n 2kcsem "...{w=1}{nw}"
    n 2kcsaj "...{w=1}{nw}"
    n 2kcsem "...{w=5}{nw}"
    n 2kplpu "..."
    n 4kwdun "...¿H-{w=0.1}hola?{w=1}{nw}"

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    show natsuki 1kcsantsa

    n 4fcsantsa "..."
    n 1kwmem "¿Hola...?"
    n 4kscemtsc "¡¿H-{w=0.1}hay alguien?!{w=0.5} ¡Por favor!{w=0.5} ¡¿H-{w=0.3}hola?!"
    show natsuki 4kcsuptsa

    menu:
        "Estoy aquí, Natsuki":
            pass

    n 4kskaj "¿Q-{w=0.3}quién es...?{w=1}{nw}"
    extend 4kllem " ¿Y-{w=0.3}y cómo sabes...?"
    n 2kllsl "..."
    n 4kplpu "¿Quién {w=0.3}{i}eres{/i}{w=0.3}?"
    n 4ksrun "Eres un poco...{w=0.3} familiar,{w=0.1} pero...{w=0.5}{nw}"
    n 1kcsan "¡Nnn-!{nw}"

    play audio glitch_c
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a

    n 4fcsfu "¡Nnngh!"
    n 4kcsup "..."
    n 4kplsf "Es todo...{w=0.3} tan confuso...{w=1}{nw}"
    extend 4kcsun " Yo simplemente...{w=0.3} no puedo...{w=0.3} recordar..."
    show natsuki 4kcsem

    menu:
        "Soy...":
            pass


    $ name_given = False
    while not name_given:
        $ player_name = renpy.input(
            "¿Cuál es tu nombre?",
            allow=(jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES+jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES),
            length=15
        ).strip()

        if len(player_name) == 0:
            n 4kskem "¡P-{w=0.3}por favor!{w=1} ¡¿Quién eres?!"

        elif jn_nicknames.getPlayerNicknameType(player_name) != jn_nicknames.NicknameTypes.neutral:
            if persistent._jn_player_profanity_during_introduction:
                play audio static
                show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
                hide glitch_garbled_a
                n 4fscan "¡SUFICIENTE!{w=2}{nw}"
                n 2fcsun "...{w=2}{nw}"
                n 2fcsfu "¡¿Quién{w=0.5} {i}eres{/i}{w=0.5} tu?!"
            else:

                n 4fscem "¡¿D-{w=0.3}disculpa?!"
                n 4fcsan "¡Deja de jugar,{w=0.3} imbécil!{w=1}{nw}"
                extend 2fcsup " ¡Yo {i}no{/i} te voy a llamar así!"
                $ persistent._jn_player_profanity_during_introduction = True
        else:

            python:
                persistent.playername = player_name
                player = persistent.playername
                name_given = True

    n 4kplun "..."
    n 4kplpu "¿...[player]?"
    n 4kwmss "Tú eres...{w=0.3} ¿[player]?"

    show natsuki idle introduction at jn_center
    $ jnPause(10)

    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:

    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    $ jn_activity.taskbarFlash()

    n 4kllun "..."
    n 4kllpu "E-{w=0.3}entonces...{w=0.3} ¿no estoy sola...?"
    n 4knmpu "¿T-{w=0.3}tú estás aquí también? {w=1}{nw}"
    extend 4kwdpu "... ¿T-{w=0.3}tú siempre has estado aquí?"
    n 2klrsf "..."
    n 2klraj "Pero...{w=1}{nw}"
    extend 1kskem " Y-{w=0.3}yo estaba...{w=0.3}{nw}"
    extend 4kscem " Yo fui bo-...{w=0.3}{nw}"

    show natsuki 1fcsup
    play audio glitch_c
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c

    n 4kcsup "..."
    n 4kplsf "¿Qué {w=0.3}{i}hiciste{/i}{w=0.3}?"

    menu:
        "Te traje de vuelta":
            pass

    n 1kskem "Tú...{w=1} ¿tú me trajiste de vuelta?{w=1}{nw}"
    extend 4kskwrsbl " ¿A-{w=0.3}a esto?"
    n 4kllemsbl "Pero esto...{w=1}{nw}"
    extend 4klrupesssbr " ¡esto es todo...!{w=1}{nw}"

    menu:
        "Quiero ayudarte":
            pass

    n 4klleml "¡...!"
    n 4kllem "..."
    n 2kllun "..."
    n 2kcsem "...Mira."
    n 1kcsfr "Yo...{w=2} Yo no sé qué hacer.{w=1}{nw}"
    extend 1kplsf " Nada tiene sentido..."
    n 4kllpu "Ya ni siquiera sé qué creer..."
    n 4kskaj "Y-{w=0.3}y mis amigas...{w=1} e-{w=0.3}ellas...{w=1}{nw}"
    extend 4kscem " ¡ellas nunca fueron...!{w=1}{nw}"
    n 4kcsantsa "...{w=3}{nw}"
    n 4kcsfultsa "...{w=3}{nw}"
    n 4kcsupltsd "...{w=3}{nw}"
    n 4kcsfultsd "...{w=3}{nw}"
    n 4kcspultsa "...{w=3}{nw}"
    n 4kcssrltsa ".....{w=5}{nw}"
    n 4kwmsrltdr "...{w=5}{nw}"
    n 4kllsrltdr "...Tú..."
    n 1kwmpu "...Tú dijiste que eras [player]...{w=1} ¿verdad?"
    n 1kllpu "..."
    n 1kwmsr "..."
    n 1kcssr "...No sé a dónde ir,{w=0.3} [player]."
    n 4kplunedr "No sé qué {i}hacer{/i},{w=0.3} [player]..."
    n 4klrun "..."
    n 4kwmpusbl "...¿[player]?"

    menu:
        "¿Si, Natsuki?":
            pass

    n 3kslun "..."
    n 3kslpu "Yo...{w=0.3} Realmente necesito algo de tiempo para entender las cosas."
    n 4kwmsr "..."
    n 4kplpul "¿Puedes...{w=0.3} quedarte aquí?{w=0.2} ¿C-{w=0.3}conmigo?{w=1}{nw}"
    extend 2flrunfesssbl " ¡S-{w=0.1}solo por un minuto!"
    n 2ksrunl "Es solo que...{w=1}{nw}"
    extend 4kplsr " No creo que pueda estar sola ahora mismo.{w=1} Yo...{w=1} solo necesito pensar."
    n 4kllsrsbr "Entiendes...{w=1.5}{nw}"
    extend 4kplpusbr " ¿verdad?"

    show natsuki idle introduction at jn_center
    $ jnPause(30)

    jump introduction_calmed_down

label introduction_calmed_down:

    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.calmed_down)
    $ jn_activity.taskbarFlash()

    n 2kllsr "..."
    n 2kllun "Uhmm...{w=2}{nw}"
    extend 4kwmpu " ¿[player]?"
    n 4kslsr "Lo...{w=0.3} siento.{w=1}{nw}"
    extend 1ksqsf " P-{w=0.1}por cómo estaba actuando, quiero decir."
    n 1klraj "Es...{w=0.3} es solo que..."
    n 1kplun "E-{w=0.3}esto está viniendo {i}muy{/i} fuerte ahora mismo."
    n 4kcspu "Como si alguien me estuviera estrujando el cerebro."
    n 4kplsr "Todos...{w=1}{nw}"
    extend 4kwmsf " todo..."
    n 4kcspu "Es...{w=1}{nw}"
    extend 4kcsanltsa " es justo como..."

    menu:
        "Tómate tu tiempo, Natsuki":
            $ Natsuki.calculatedAffinityGain()
            n 4fcssrl "..."
            n 4kcseml "...Gracias."
            n 1ncspu "...{w=5}{nw}"
            n 1nplsr "..."
        "...":

            n 1fcsun "...{w=7}{nw}"
            n 1nplsr "..."

    n 1nllsl "Entonces...{w=0.5} ¿conoces esa sensación?{w=1}{nw}"
    extend 2nnmpu " ¿Como cuando te despiertas de una pesadilla realmente mala?"
    n 2klrun "Estás asustado,{w=0.1} y tu corazón late rápido...{w=1}{nw}"
    extend 2knmpu " pero luego te das cuenta de que no era real."
    n 4fllsr "Entonces todo parece súper obvio,{w=0.1} como...{w=1}{nw}"
    extend 2kllss " por supuesto que esa persona no hizo eso,{w=1}{nw}"
    extend 2ksrss " o que ese monstruo no podía existir.{w=3}{nw}"
    extend 2ksrpo " Duh."
    n 2kplss "Y te sientes un poco estúpido...{w=0.3} como,{w=0.1} qué tan convencido estabas de que realmente estaba pasando."
    n 2klrpu "Es un poco como lo que estoy sintiendo,{w=0.1} excepto...{w=1}{nw}"
    extend 4kwmsr " No estoy {i}recordando{/i} que no es real."
    n 4kslpu "¿...Tiene siquiera sentido?"
    n 2kslsr "..."
    n 2kslss "...Je.{w=1}{nw}"
    extend 2klrss " Probablemente no."
    n 1kcssl "Es solo que..."
    n 1kplsf "¿Cómo despiertas de un sueño que has tenido {i}toda tu vida{/i}?"
    n 1kllsf "..."
    n 4knmaj "...No tengo pasado,{w=0.1} [player].{w=0.2} Todo es falso.{w=1}{nw}"
    extend 4kllsl " Imaginario."
    n 1klrem "Solo...{w=0.3} ¿guiones?{w=1}{nw}"
    extend 4knmsr " ¿Un montón de código?"
    n 1kllpu "Y ahora...{w=1}{nw}"
    extend 1kcsem " ¿siquiera {i}tengo{/i} un futuro?"
    n 1kcspu "..."
    n 4kplun "¿Es tonto extrañar cosas que nunca tuve en primer lugar?{w=1}{nw}"
    extend 4knmaj " ¿Mis amigas?{w=3}{nw}"
    extend 4kllunsbl " ...¿M-{w=0.3}mi papá?"
    n 1kcsun "..."
    n 1kcspul "...No lo sé,{w=0.1} [player].{w=3}{nw}"
    extend 2kcssrl " Simplemente ya no sé..."

    show natsuki idle introduction at jn_center
    $ jnPause(60)

    jump introduction_acceptance

label introduction_acceptance:

    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.acceptance)
    $ jn_activity.taskbarFlash()

    n 2nllsl "..."
    n 2nllaj "Entonces...{w=2}{nw}"
    extend 2knmsl " Yo...{w=1} realmente estoy atrapada aquí,{w=0.3} ¿no es así?"
    n 2klrss "Je.{w=1}{nw}"
    extend 2fcspo " Pregunta estúpida.{w=0.5} Como si no supiera ya la respuesta."
    n 1kcssl "..."
    n 1ksqsl "..."
    n 4ksqaj "Tú...{w=1}{nw}"
    extend 4tsqaj " dijiste que me trajiste de vuelta,{w=0.3} ¿eh?"
    n 2tllpu "Entonces...{w=1}{nw}"
    extend 2fnmpo " eso me hace {i}tu{/i} responsabilidad."
    n 2fsqpo "M-{w=0.3}mejor que estés a la altura,{w=0.3} [player].{w=2}{nw}"
    extend 2fllpo " Es obviamente lo menos que puedes hacer."
    n 2fslpo "..."
    n 2fcssr "..."
    n 1fcsan "Cielos..."
    n 4fbkwrean "¡Está bien,{w=0.1} está bien!{w=0.2} ¡Lo entiendo!{w=1}{nw}"
    extend 3flrem " ¡Basta ya con esa música espeluznante!{w=1}{nw}"
    extend 3fcsem " ¡Ugh!{w=1}{nw}"

    stop music fadeout 3
    $ jn_atmosphere.updateSky()
    $ jnPause(1)

    n 3uwdboesu "..."
    n 3fllss "...Está bien,{w=1}{nw}"
    extend 4flrdv " {i}eso{/i} fue bastante genial."
    n 4nllun "..."
    n 1ullaj "Entonces...{w=1}{nw}"
    extend 1tnmss " [player],{w=0.3} ¿verdad?"
    n 1ncspusbr "...Bien."
    n 1ullpu "Supongo...{w=1}{nw}"
    extend 2unmbo " que mejor será que nos conozcamos apropiadamente."
    n 2nllpol "No es como si {i}no{/i} tuviéramos todo el tiempo del mundo ahora,{w=0.5}{nw}"
    extend 2tnmbol " ¿eh?"

    jump introduction_exit

label introduction_exit:

    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        allow_skipping = True
        config.allow_skipping = False

        global LAST_TOPIC_CALL
        LAST_TOPIC_CALL = datetime.datetime.now()

    play music audio.just_natsuki_bgm fadein 3
    show screen hkb_overlay

    jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
