default persistent._farewell_database = dict()
init offset = 5
default -5 persistent.jn_player_first_farewell_response = None
default -5 persistent.jn_player_force_quit_state = 1

default -5 persistent._jn_player_extended_leave_response = None
default -5 persistent._jn_player_extended_leave_departure_date = None

init -5 python in jn_farewells:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    from store import Natsuki
    FAREWELL_MAP = dict()

    class JNFirstLeaveTypes(Enum):
        """
        Ways in which the player may choose to first leave Natsuki; this decides dialogue upon returning.
        """
        will_be_back = 1
        dont_know = 2
        no_response = 3
        force_quit = 4
        
        def __int__(self):
            return self.value

    class JNForceQuitStates(Enum):
        """
        Tracking for player force quits; this decides dialogue on returning.
        """
        not_force_quit = 1
        first_force_quit = 2
        previously_force_quit = 3
        
        def __int__(self):
            return self.value

    class JNExtendedLeaveResponseTypes(Enum):
        """
        Ways in which the player may respond when telling Natsuki they will be gone a while.
        """
        a_few_days = 1
        a_few_weeks = 2
        a_few_months = 3
        unknown = 4
        
        def __int__(self):
            return self.value

    def getFarewellOptions():
        """
        Returns the list of all farewell options when saying Goodbye to Natsuki.
        """
        return [
            ("Me voy a dormir.", "farewell_option_sleep"),
            ("Voy a ir a comer algo.", "farewell_option_eat"),
            ("Voy a salir a algún lado.", "farewell_option_going_out"),
            ("Voy a trabajar.", "farewell_option_work"),
            ("Voy a la escuela.", "farewell_option_school"),
            ("Voy a jugar otra cosa.", "farewell_option_play"),
            ("Voy a estudiar un poco.", "farewell_option_studying"),
            ("Voy a hacer otra cosa.", "farewell_option_misc_activity"),
            ("Voy a hacer algunos quehaceres.", "farewell_option_chores"),
            ("Me voy por un tiempo.", "farewell_option_extended_leave")
        ]

    def selectFarewell():
        """
        Picks a random farewell, accounting for affinity
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        if store.persistent.jn_player_first_farewell_response is None:
            return "farewell_first_time"
        
        kwargs = dict()
        
        farewell_pool = store.Topic.filter_topics(
            FAREWELL_MAP.values(),
            affinity=Natsuki._getAffinityState(),
            excludes_categories=["Failsafe"],
            **kwargs
        )
        
        return random.choice(farewell_pool).label

label farewell_start:
    $ Natsuki.setForceQuitAttempt(False)
    $ push(jn_farewells.selectFarewell())
    jump call_next_topic


label farewell_first_time:
    n 1uskem "E-{w=0.1}espera,{w=0.1} ¿te vas?"
    n 4fskwrlsbr "¡[player]!{w=0.2} E-{w=0.1}espera!{w=0.5}{nw}"
    extend 4fbkwrleexsbr " ¡Espera solo un segundo!"
    n 4fskemlsbl "..."
    n 2kllemlsbl "..."
    n 2kplpu "...V-{w=0.1}vas a volver,{w=0.1} ¿verdad?"
    n 2kllunsbl "..."
    n 4kwmemesssbr "...¿Verdad?"

    menu:
        "Volveré.":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.will_be_back)
            $ Natsuki.calculatedAffinityGain(bypass=True)
            n 4unmemlesu "¡...!{w=0.5}{nw}"
            n 1fllemless "¡S-{w=0.1}sí!{w=0.5}{nw}"
            extend 1fsqpolsbr " Más te vale."
            n 2flremlsbl "E-{w=0.1}eres responsable de esto,{w=0.1} como dije.{w=0.5}{nw}"
            extend 2flrpol " Así que..."
            n 2kllpol "..."
        "No lo sé.":

            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.dont_know)
            n 1kskem "..."
            n 4kskwr "¡N-{w=0.5}no!"
            n 4kcsan "¡No puedes hacerme esto!{w=0.5}{nw}"
            extend 4fcsuptsa " N-{w=0.1}no ahora..."
            n 1kcsunltsa "..."
            n 1ksqunl "..."
            n 2kplpul "Por favor,{w=0.1} [player]...{w=0.5}{nw}"
            extend 2kllpu " no es mucho pedir..."
            n 4kwmemsbr "¿Verdad?"
        "...":

            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)
            n 1knmemsbr "[player],{w=0.1} v-{w=0.5}vamos..."
            n 1kllpu "Si esto es una broma,{w=0.5}{nw}"
            extend 4fnmgs " ¡realmente no es graciosa!{w=2}{nw}"
            extend 4knmgssbl " ¡L-{w=0.1}lo digo en serio!"
            n 1kllunsbl "..."
            n 1knmaj "Por favor,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " no es mucho pedir..."
            n 4kwmem "¿Verdad?"

    return { "quit": None }


label farewell_force_quit:
    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.first_force_quit)
    if not persistent.jn_player_first_farewell_response:
        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.force_quit)

    hide screen hkb_overlay
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a
    stop music
    play audio glitch_c

    n 1uskem "¿E-{w=0.3}eh?{w=1}{nw}"
    extend 4uscwr " ¡N-{w=0.3}no!{w=0.2} ¡¡Espera!!{w=0.2} POR FAVOR-{w=0.1}{nw}"
    show natsuki 4kchupltsa zorder JN_NATSUKI_ZORDER at jn_center

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_b

    return { "quit": None }



label farewell_option_sleep:
    if jn_admissions.last_admission_type in (jn_admissions.TYPE_SICK , jn_admissions.TYPE_TIRED):

        n 2kllsl "...[player]."
        n 2knmpu "Yo...{w=0.75}{nw}"
        extend 2klrpu " creo que esa sería una buena idea.{w=0.5} Ya sabes."
        $ feeling_like = "sintiéndote enfermo" if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK else "sintiéndote cansado"
        n 2klrpu "Con lo que dijiste antes sobre estar [feeling_like] y eso."
        n 4ulraj "Así que...{w=0.75}{nw}"
        extend 4knmpo " ve a descansar un poco,{w=0.1} ¿de acuerdo?{w=1}{nw}"
        extend 2fcspol " Podemos hablar luego de todos modos."
        n 2fnmgsl "¡Ahora ponte en marcha,{w=0.1} [player]!"
        extend 4fchsml " Jejeje."

        if Natsuki.isEnamored(higher=True):
            n 3fchbgl "¡Que no te piquen las chinches!"

        elif Natsuki.isLove(higher=True):
            n 3fchblledz "¡También te amo~!"

    elif jn_get_current_hour() > 22 or jn_get_current_hour() < 6:

        n 4fwdajesh "¡Y-{w=0.2}y debería pensar eso también!{w=0.5}{nw}"
        extend 2tnmem " ¡¿En serio te tomó {i}tanto{/i} tiempo notar la hora?!"
        n 2fllposbl "Cielos...{w=0.5}{nw}"
        extend 2nllpo " pero mejor tarde que nunca,{w=0.1} supongo."
        n 4fllsm "Jejeje.{w=0.5}{nw}"
        extend 1fchsm " ¡Duerme bien,{w=0.1} [player]!"

        if Natsuki.isEnamored(higher=True):
            n 3fchbll "¡Nos vemos pronto~!"

        elif Natsuki.isLove(higher=True):
            n 3nchsml "¡Te amo~!"

    elif jn_get_current_hour() >= 21:

        n 1unmaj "Ya casi listo para ir a dormir,{w=0.1} ¿eh?"
        n 4ullaj "Eso está bien...{w=0.5}{nw}"
        extend 2fslca " supongo."
        n 4fcsct "Sé que necesitas tu sueño de belleza y todo eso."
        n 3fsqsm "...Jejeje."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "¡Duerme bien,{w=0.2} [chosen_tease]!{w=0.5}{nw}"
            extend 3uchsmledz " ¡Nos vemos mañana~!"
        else:

            n 3fchbgl "¡No te preocupes!{w=0.2} ¡Duerme bien,{w=0.1} [player]!"

    elif jn_get_current_hour() >= 19:

        n 1unmaj "¿Eh?{w=0.75}{nw}"
        extend 4tnmaj " ¿Te vas a dormir temprano?"
        n 4nnmbo "Oh.{w=0.5}{nw}"
        extend 1nllpu " Bueno..."
        n 4ullaj "Eso está bien.{w=0.75}{nw}"
        extend 2nslpo " Supongo."
        n 2fsqcal "Pero más te vale quedarte despierto conmigo más tarde.{w=0.75}{nw}"
        extend 4fsrtrl " Ya sabes."
        n 3fsqbglsbl "Para recuperar el tiempo perdido y todo eso."
        n 3fchbll "¡Noches,{w=0.1} [player]!"
    else:


        n 1tnmbo "¿Eh?{w=1}{nw}"
        extend 4tnmpu " ¿Estás tomando {i}siestas{/i} ahora?"
        n 2tsqcaesd " ...¿En serio?"
        n 2ncsemesi "Cielos...{w=1}{nw}"
        extend 2fllca " Juro que te voy a estar alimentando yo a este paso..."
        n 4fsqdv "..."
        n 3fchbg "¡Oh,{w=0.3} relájate!"
        n 3nchgnelg "¡Estoy bromeando,{w=0.1} estoy bromeando!{w=0.5}{nw}"
        extend 3tllss " Caray."
        n 4fchbg "¡Nos vemos luego,{w=0.1} [player]~!"

        if Natsuki.isLove(higher=True):
            n 1uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_eat:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fcsgs "B-{w=0.1}bueno,{w=0.1} ¡duh!{w=0.5} ¡{i}Dijiste{/i} que te morías de hambre!"
        n 2fllpoesi "Cielos..."
        n 2fdtposbr "Solo haz que sea algo saludable,{w=0.1} ¿entendido?"
        n 4fsqsm "...Jejeje."
        n 2fchbg "¡Disfruta,{w=0.1} [player]!"

    elif jn_get_current_hour() in (7, 8):
        n 1fnmgs "¡Sí!{w=0.3} ¡Más te vale!{w=0.5}{nw}"
        extend 2fsqtr " {i}Sí{/i} sabes lo que dicen sobre el desayuno,{w=0.1} ¿verdad?"
        n 4fsqsml "...Jejeje."
        n 2fchbg "¡Buen provecho,{w=0.1} [player]!"

    elif jn_get_current_hour() in (12, 13):
        n 2unmaj "¿Saliendo para el almuerzo,{w=0.1} [player]?"
        n 1ulrbo "Eso es genial,{w=0.3} eso es genial."
        n 4nsqsm "Pero solo recuerda...{w=0.3}{nw}"
        extend 2fsqss " eres lo que comes~."
        n 4fchsm "...Jejeje.{w=0.5}{nw}"
        extend 3uchsm " ¡Disfruta!"

    elif jn_get_current_hour() in (18, 19):
        n 3unmaj "Hora de la cena,{w=0.1} ¿eh?{w=0.5}{nw}"
        extend 2unmbg " ¡No hay problema!"
        n 1nlrpu "Solo...{w=0.5}{nw}"
        extend 2fdtposbr " asegúrate de que no sea comida instantánea.{w=0.5}{nw}"
        extend 2fsqpo " ¿Entendido?"
        n 2fsqsm "...Jejeje."
        n 1fchbg "¡Disfruta,{w=0.1} [player]~!"
    else:

        n 1unmaj "¿Oh?{w=0.2} ¿Vas a comer algo?"
        n 2nllaj "Está bien."
        n 2nsqpo "Pero más te vale no estarte llenando de chatarra,{w=0.1} [player]."
        n 2fsqsm "...Jejeje.{w=0.5}{nw}"
        extend 4uchbg " ¡Disfruta~!"

    return { "quit": None }

label farewell_option_going_out:
    if jnIsNewYearsEve():
        n 3tsqbg "¿Oho?{w=0.2} Saliendo para año nuevo,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 3fchbg " ¡No puedo culparte!"
        n 1ullaj "Solo...{w=0.5}{nw}"
        extend 4nsqsl " no seas un idiota allá afuera,{w=0.1} ¿okay?"
        n 2fslsl "No quiero que estés jugando con bebidas y fuegos artificiales como un completo imbécil y salgas lastimado."
        n 1ullpu "Pero...{w=0.5}{nw}"
        extend 1uchbg " ¡sí!{w=0.2} ¡Diviértete allá afuera,{w=0.1} [player]!"
        n 2usqbg "¿Y si no te veo antes?"
        n 1fchbs "¡Feliz año nuevo!"

    elif jnIsEaster():
        n 1unmaj "¿Oh?{w=0.2} ¿Te vas ahora?"
        n 4unmbg "¿Tenías una comida planeada para hoy o algo?"
        n 4tlrsm "{i}Es{/i} Pascua,{w=0.1} ¡después de todo!{w=0.5}{nw}"
        extend 3uchsm " Jejeje."
        n 4ullss "Bueno,{w=0.1} como sea.{w=0.5}{nw}"
        extend 2uchgn " ¡Nos vemos luego,{w=0.1} [player]!"

    elif jnIsHalloween():
        n 3usqss "¿Ooh?{w=0.2} ¿Saliendo por Halloween,{w=0.1} [player]?"
        n 3fsqsm "Solo no olvides..."
        n 2fsqbg "¡Quiero mi parte de los dulces también!"
        n 2fchgn "Jejeje.{w=0.5}{nw}"
        extend 1fchbg " ¡Diviértete~!"

    elif jnIsChristmasEve():
        n 1unmbo "¿Oh?{w=0.2} ¿Saliendo por Nochebuena?"
        n 1kllsl "Bueno...{w=0.3} okay."
        n 4kllajl "...Pero volverás a tiempo para Navidad...{w=0.5}{nw}"
        extend 4knmsll " ¿verdad?"
        n 2nsrssl "...Jajaja.{w=0.3}"
        extend 1nchbgsbl " ¡Nos vemos luego,{w=0.1} [player]!"
        n 1kslslsbl "..."

    elif jnIsChristmasDay():
        n 1unmbo "¿Eh?{w=0.2} ¿Te vas ahora?"
        n 2kllsl "Bueno...{w=0.3} está bien."
        n 2kllss "Gracias por pasar por aquí hoy,{w=0.1} [player]."
        n 4kcsssl "Realmente...{w=0.3} significó mucho para mí."
        n 4kchss "¡Nos vemos luego,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1kchbg " ¡Y Feliz Navidad!"
    else:

        n 2unmaj "¿Oh?{w=0.2} ¿Sales,{w=0.1} [player]?"
        n 2fchbg "¡No te preocupes!{w=0.2} ¡Te veo luego!"
        n 2nchbg "¡Hasta luego~!"

    if Natsuki.isLove(higher=True):
        n 4uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_work:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1knmaj "¿Eh?{w=0.2} ¿Vas a trabajar ahora?"
        $ time_concern = "tarde" if jn_get_current_hour() >= 20 else "temprano"
        n 4kllajsbr "Pero...{w=0.5}{nw}"
        extend 4knmgssbr " es súper [time_concern],{w=0.1} [player]..."
        n 1kllsll "..."
        n 1kllajl "¿Vas a..."
        show natsuki 4tnmbol

        menu:
            n "¿Vas a trabajar desde casa hoy,{w=0.2} o...?"
            "Sí, trabajaré desde casa.":

                n 1ncsssl "Je.{w=0.75}{nw}"
                extend 2nllpul " {i}Supongo{/i} que eso es algo,{w=0.75}{nw}"
                extend 2nslsll " al menos."
                n 4fslpol "Eso no significa que tenga que gustarme,{w=0.2} sin embargo."
                n 4fcspol "Solo..."
                n 1kllbol "...Mantén un ojo en el reloj.{w=0.75}{nw}"
                extend 1knmbol " ¿De acuerdo?"
                n 2fsqcal "No quiero escuchar sobre ti quedándote hasta tarde ni nada."

                if Natsuki.isLove(higher=True):
                    n 2fchsml "¡Tómatelo con calma,{w=0.2} [player]!{w=0.75}{nw}"
                    extend 2fchssleafsbl " ¡T-{w=0.2}te amo!"
                else:

                    n 2fchssl "¡Tómatelo con calma,{w=0.2} [player]!"
                    n 2kslsll "..."
            "No, tengo que salir.":

                n 4kcsemlesi "Hombre...{w=1}{nw}"
                extend 4ksqbol " ¿{i}en serio{/i}?"
                n 1ksrsllsbr "..."
                n 1fcspusbr "Solo...{w=1}{nw}"
                extend 4kllsl " ten cuidado,{w=0.2} ¿de acuerdo?"
                n 2fsqpol "Y más te vale venir a visitar cuando regreses."

                if Natsuki.isLove(higher=True):
                    n 2fnmcal "¡Cuídate,{w=0.1} [player]!{w=1}{nw}"
                    extend 4kchsmleaf " ¡Te amo!"
                    n 4kllcalsbr "..."
                else:

                    n 2fnmcal "¡Cuídate,{w=0.1} [player]!"
    else:

        n 1unmajesu "¿Oh?{w=0.2} ¿Trabajas hoy?"

        if jnIsEaster():
            n 1uskgs "...¿Y en Pascua,{w=0.1} de todos los días?{w=0.5}{nw}"
            extend 1fslpo " Hombre..."

        elif jnIsChristmasEve():
            n 4fskgsl "...¿En Nochebuena?{w=0.5}{nw}"
            extend 2kcsemledr " Tienes que estar bromeando..."

        elif jnIsChristmasDay():
            n 4fskwrl "...¡¿En {i}Navidad{/i}?!{w=0.5}{nw}"
            extend 1kcsemledr " Ugh..."
            n 2fslpol "..."
            n 2fslajl "Bueno..."

        elif jnIsNewYearsEve():
            n 4fskgsl "...¡¿Y en Año Nuevo,{w=0.1} también?!{w=0.5}{nw}"
            extend 1kcsemledr " Cielos..."

        elif jnIsPlayerBirthday():
            n 1kwdgsl "...¡¿Y en tu {i}cumpleaños{/i} también?!{w=1}{nw}"
            extend 1kslanl " Ay,{w=0.75}{nw}"
            extend 1kslsll " [player]..."

        elif not jn_is_weekday():
            n 1uwdaj "Y-{w=0.1}y en fin de semana,{w=0.1} ¿también?{w=0.5}{nw}"
            extend 2kslpu " Hombre..."

        n 2nlrpo "Apesta que tengas que trabajar,{w=0.1} pero lo entiendo.{w=0.5}{nw}"
        extend 2nsrpo " Supongo."
        n 4fnmpo "...Pero más te vale venir a visitar cuando termines."
        n 4fsqsm "Jejeje."
        n 3fchbg "¡Tómatelo con calma,{w=0.1} [player]!{w=0.2} ¡No dejes que nadie te mangonee!"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 3uchbgf "¡Tú puedes,{w=0.1} [chosen_endearment]!{w=0.2} ¡Te amo~!"

        elif Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3uchbgl "¡Creo en ti,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_school:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1tnmem "...¿Escuela?{w=1}{nw}"
        extend 4fskgsesh " ¿A-{w=0.1}A esta hora?"

        if jnIsEaster():
            n 1kwdgs "...¿Y en {i}Pascua{/i},{w=0.1} de todos los días?"

        elif jnIsChristmasEve():
            n 1fskgsl "...¿Y en {i}Nochebuena{/i}?"

        elif jnIsChristmasDay():
            n 1fskwrl "...¡¿Y en {i}Navidad{/i}?!"

        elif jnIsNewYearsEve():
            n 1fskgsl "...¡¿Y en Año Nuevo,{w=0.1} también?!"

        if not jn_is_weekday():
            extend 1uskwr " ¡¿Y-{w=0.1}y en un {i}fin de semana{/i} también?!"

        n 4fbkwrean "¡¿Qué clase de escuela es eeesaaaa?!"
        n 2kllpo "Cielos.{w=0.5}{nw}"
        extend 2fslsr " Y yo pensé que mi experiencia escolar era lo suficientemente mala."
        n 2kcspu "Solo...{w=0.5}{nw}"
        extend 4knmpu " cuídate al llegar,{w=0.1} ¿de acuerdo?"
        $ time_concern = "tarde" if jn_get_current_hour() >= 20 else "temprano"
        extend 1fllsrsbl " Es realmente [time_concern],{w=0.1} después de todo."
        n 4kllss "¡Estudia duro,{w=0.1} [player]!"
    else:

        if jnIsEaster():
            n 4uskgs "...¿Y en Pascua,{w=0.1} de todos los días?{w=0.5}{nw}"
            extend 2fslpo " Hombre..."

        elif jnIsChristmasEve():
            n 4fskgsl "...¿En Nochebuena?{w=0.5}{nw}"
            extend 2fcseml " Tienes que estar bromeando..."

        elif jnIsChristmasDay():
            n 4fskwrl "...¡¿En {i}Navidad{/i}?!{w=0.5}{nw}"
            extend 2fcseml " Ugh..."
            n 2fslpol "..."
            n 2fslajl "Bueno..."

        elif jnIsNewYearsEve():
            n 4fskgsl "...¡¿Y en Año Nuevo,{w=0.1} también?!{w=0.5}{nw}"
            extend 2fcseml " Cielos..."

        elif jn_is_weekday():
            n 2unmaj "¿A la escuela,{w=0.1} [player]?{w=0.5}{nw}"
            extend 2nchsm " ¡No hay problema!"
        else:

            n 1tnmpu "¿Eh?{w=0.2} ¿Estás en la escuela hoy?{w=0.5}{nw}"
            extend 2nsqpu " ...¿En un {i}fin de semana{/i}?"
            n 2fslpu "..."
            n 2fsqpo "Qué asco..."

        n 2tsqsm "Apesta ser tú,{w=0.1} ¿eh?{w=0.5}{nw}"
        extend 2fchsm " Jejeje."
        n 3fchbg "¡Nada de holgazanear,{w=0.1} [player]!{w=0.2} ¡Te veré luego!"

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4uchbgf "¡Te amo!"

    return { "quit": None }

label farewell_option_misc_activity:
    n 1knmpu "¿H-{w=0.1}huh?{w=0.5}{nw}"
    extend 1kllaj " ¿Y tienes que irte para hacer eso también?"
    n 4fcsun "Mmmmmm...{w=0.5}{nw}"
    extend 1kcsaj " okay."
    n 2fnmpol "...Pero más te vale venir a visitar cuando termines.{w=1}{nw}"
    extend 2klrpo " ¿Entendido?"
    n 2kllpo "¡Nos vemos pronto,{w=0.1} [player]!"

    if Natsuki.isLove(higher=True):
        n 4kllssf "¡Te amo!"

    return { "quit": None }

label farewell_option_play:
    n 1fsqaj "...¿En serio,{w=0.5} [player]?"
    n 4nslpu "Preferirías en serio jugar algún {i}juego{/i}...{w=0.5}{nw}"
    extend 2fsqsf " ¿que pasar el rato {i}conmigo{/i}?"
    n 2fcssl "..."
    n 2uchgneme "¡Bueno,{w=0.1} tú te lo pierdes!{w=0.5}{nw}"
    extend 2fchbgelg " ¡Jajaja!"
    n 1nllbg "No,{w=0.1} no.{w=0.2} Está bien.{w=0.2} Ve a hacer eso,{w=0.1} [player].{w=0.5}{nw}"
    extend 4nsqbg " Además..."
    n 2usqct "Seguro que podrías usar la práctica,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 2fchsm " Jejeje."
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchbg "¡Te veo luego,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_studying:
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fskgs "¡[player_initial]-{w=0.1}[player]!"
    n 2fllansbr "¡Si hubiera sabido que debías estar estudiando te habría echado yo misma!{w=0.5}{nw}"
    extend 2fcspoesi " Cielos..."
    n 2nsqposbl "Realmente espero que no tengas exámenes mañana o algo así..."
    n 2flrpo "Pero de cualquier forma,{w=0.1} estarás bien.{w=0.2} ¡Solo vete!{w=0.5}{nw}"
    extend 4fwdaj " ¡Vete!"
    n 4fchgn "...¡Largo,{w=0.1} tonto!{w=0.2} Jejeje.{w=0.5}{nw}"
    extend 4fchbl " ¡Hablamos luego!"

    if Natsuki.isLove(higher=True):
        n 1uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_chores:
    if store.jn_get_current_hour() >= 20 or store.jn_get_current_hour() <= 4:
        n 1tnmaj "...¿Quehaceres?{w=0.5}{nw}"
        extend 2tsqem " ¿A {i}esta{/i} hora?"
        n 2nllbo "Tengo que decirlo,{w=0.1} [player]."
        n 2nsqdv "O eres muy dedicado o estás desesperado.{w=0.5}{nw}"
        extend 1nchsm " Jejeje."
        n 1ullss "Bueno,{w=0.1} como sea.{w=0.5}{nw}"
        extend 3tnmss " Solo apresúrate y ve a dormir,{w=0.1} ¿'kay?"

        if Natsuki.isLove(higher=True):
            n 3uchbg "¡Hasta luego,{w=0.1} [player]!"
            extend 4uchbgf " ¡Te amo~!"
        else:

            n 3fchbg "¡Hasta luego,{w=0.1} [player]!"
    else:

        n 2tnmsg "Atrapado en el deber de limpieza,{w=0.1} ¿eh?"
        n 2nchsm "Jejeje.{w=0.2} Sí,{w=0.1} está bien.{w=0.5}{nw}"
        extend 2fchgn " ¡Ve y encárgate de tu racha de limpieza!"

        if Natsuki.isLove(higher=True):
            n 3uchbg "¡Hasta luego,{w=0.1} [player]!{w=0.5}{nw}"
            extend 3uchbgf " ¡Te amo~!"
        else:

            n 3fchbg "Jejeje.{w=0.2} ¡Hasta luego,{w=0.1} [player]!"
    return { "quit": None }

label farewell_option_extended_leave:
    n 1tnmpueqm "¿Eh?{w=0.75}{nw}"
    extend 1knmaj " ¿Un tiempo?"
    n 2fnmsr "..."
    n 2fsqaj "...¿Qué quieres decir con 'un tiempo',{w=0.2} [player]?{w=0.75}{nw}"
    extend 4fnmgs " ¿Eh?"
    n 3fllem "¿Estás tratando de evitarme?{w=1}{nw}"
    extend 3knmem " ¿{i}No{/i} soy la mejor compañía?"
    n 4fbkwrl "¡¿E-{w=0.2}es {i}eso{/i}?!"
    n 2fsqpol "..."
    n 2fsqsml "..."
    n 2fcsaj "¡Oh,{w=0.5}{nw}"
    extend 2fchgn " relájate,{w=0.2} [player]!{w=1}{nw}"
    extend 4ullss " ¡Caray!"
    n 4fchbg "Ya deberías saber cuando te estoy tomando el pelo,{w=0.75}{nw}"
    extend 1fchbl " bobo."
    n 1ulrss "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
    extend 2ulraj " Está totalmente bien."
    n 2fcsajsbl "Puedo manejar {i}fácilmente{/i} unos días sola.{w=0.75}{nw}"
    extend 2fchbgsbl " ¡Sin sudar!"
    n 4nslbosbl "..."
    n 4nslaj "Pero...{w=0.75}{nw}"
    extend 4nllsl " solo para saber...."
    show natsuki 2knmbo

    menu:
        n "¿Planeabas estar fuera mucho tiempo,{w=0.2} o...?"
        "Unos pocos días.":

            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_days)
            n 1kchdvesi "¡Pffff-!{w=0.75}{nw}"
            extend 2tsqbg " ¡Y pensar que probablemente te estabas preocupando por eso también!{w=0.75}{nw}"
            extend 2fcssm " Jejeje."
            n 3fcsbg "Sí,{w=0.2} eso no es problema en absoluto.{w=1}{nw}"
            extend 3fchgn " ¡Ahora vete de una vez!"

            if Natsuki.isLove(higher=True):
                n 3kchbgl "¡Nos vemos luego,{w=0.2} [player]!{w=0.75}{nw}"
                extend 4fchsmleafsbl " ¡T-{w=0.2}te amo!"

            elif Natsuki.isEnamored(higher=True):
                n 3fchbg "¡Nos vemos luego,{w=0.2} [player]!"
                n 4kslsssbl "..."
        "Unas pocas semanas.":

            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_weeks)
            n 2tnmpu "Unas pocas semanas,{w=0.75}{nw}"
            extend 2tnmbo " ¿eh?"
            n 4kllbo "..."
            n 4kllss "Eso es...{w=0.75}{nw}"
            extend 2nslsl " un poco más de lo que esperaba."
            n 2fcsgslsbl "¡P-{w=0.2}pero estaré bien!{w=0.75}{nw}"
            extend 2fcspolsbl " {i}Totalmente{/i} tengo esto bajo control.{w=1}{nw}"
            extend 2fcsbglsbl " ¡No te preocupes!"
            n 2nslsslsbl "Jejeje..."
            n 1fchbgsbl "¡L-{w=0.2}luego, [player]!"

            if Natsuki.isLove(higher=True):
                n 1kchsmlsbl "¡Te amo!"
                n 4ksrsll "..."

            elif Natsuki.isEnamored(higher=True):
                n 4kcspuesi "..."
        "Unos pocos meses.":

            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.a_few_months)
            n 4knmpu "...¿Unos pocos {i}meses{/i}?"
            n 2kslpu "..."
            n 2kslaj "Eso es...{w=1}{nw}"
            extend 1klrsl " mucho más de lo que esperaba."
            n 1fcsca "..."
            n 2fcsajlsbl "Q-{w=0.2}quiero decir,{w=0.75}{nw}"
            extend 2fcsgslsbl " ¡estaré totalmente bien!"
            n 2kslbolsbl "Pero..."
            n 1ncsbolesi "..."
            n 1nsrbol "O-{w=0.2}olvídalo.{w=0.75}{nw}"
            extend 2fcstrl " ¡Tengo esto!{w=1}{nw}"
            extend 2nslsslsbl " ...Creo."
            n 3klrbolsbl "C-{w=0.2}cuídate,{w=0.2} [player]."
            extend 3knmbolsbl " ¿'Kay?"

            if Natsuki.isLove(higher=True):
                n 3fcsajlsbr "...Sabes cuánto significas para mí,{w=1}{nw}"
                extend 4kllbolsbr " d-{w=0.2}después de todo..."

            elif Natsuki.isEnamored(higher=True):
                n 3fnmcalsbr "Me enojaré si no lo haces."
                n 3kslbolsbr "..."
            else:

                n 3kslbolsbr "..."
        "No estoy seguro.":

            $ persistent._jn_player_extended_leave_response = int(jn_farewells.JNExtendedLeaveResponseTypes.unknown)
            n 1uskemlesh "...¿H-{w=0.2}huh?{w=0.75}{nw}"
            extend 4knmemlsbr " ¿Ni siquiera {i}sabes{/i} cuándo volverás?"
            n 4kllunlsbr "..."
            n 4kllpulsbr "Pero...{w=0.75}{nw}"
            extend 4klrbolsbl " {i}volverás{/i}...{w=1}{nw}"
            extend 4knmbolsbl " ¿verdad?"
            n 1ksqbol "..."
            n 1kcsemlesi "..."
            n 1kslpol "...Estaré bien.{w=1}{nw}"
            extend 2nslpol " Supongo.{w=1}{nw}"
            extend 2kslpul " Solo..."
            n 4fcsunl "..."
            n 2kcseml "No me hagas esperar demasiado.{w=0.75}{nw}"
            extend 4knmbol " ¿Por favor?"

            if Natsuki.isLove(higher=True):
                n 2ksrbofsbr "...Sabes cuánto significas para mí,{w=0.75}{nw}"
                extend 4ksqbofsbr " d-{w=0.2}después de todo..."

            elif Natsuki.isEnamored(higher=True):
                n 2kslajlsbl "...Luego,{w=0.2} [player]."
                n 2kslsllsbl "..."
            else:

                n 2kslajl "Luego,{w=0.2} [player]."
                n 2kslsll "..."

    $ import datetime
    $ persistent._jn_player_extended_leave_departure_date = datetime.datetime.now()

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_you_mean_the_world_to_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_you_mean_the_world_to_me:
    n 1kllpul "Aww...{w=1}{nw}"
    extend 4kplsfl " ¿te vas ahora,{w=0.2} [player]?"
    n 4klrcal "Bueno...{w=1}{nw}"
    extend 2ksrcal " okay."
    n 2fnmtrf "¡M-{w=0.2}mejor cuídate mucho,{w=0.2} [player]!{w=0.5}{nw}"
    extend 4kchssfeaf " ¡Significas el mundo para mí!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_dont_like_saying_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_dont_like_saying_goodbye:
    n 4fsqtrl "Sabes que no me gusta decir adiós,{w=0.1} [player]..."
    n 4kcssllesi "..."
    n 2fcsgsfess "¡E-{w=0.2}estaré bien!{w=1}{nw}"
    extend 2fcsajf " Solo..."
    n 4knmpof "...Vuelve pronto,{w=0.2} ¿de acuerdo?"
    n 1kchssfeaf "¡T-{w=0.2}te amo,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_counting_on_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_counting_on_you:
    n 1fcsunl "Uuuu...{w=0.75}{nw}"
    extend 2fslpol " Nunca me gusta decirte adiós..."
    n 2kslbol "Pero...{w=0.5}{nw}"
    extend 2kslssl " supongo que a veces no se puede evitar."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 2fcsajl "¡E-{w=0.2}entonces!"
    n 4fsqtrf "Más te vale cuidarte allá afuera,{w=0.1} [chosen_endearment]."
    n 3fchgnl "...¡Porque cuento contigo!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fchblleaf "¡Hasta luego,{w=0.2} [chosen_tease]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_do_your_best",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_do_your_best:
    n 1unmajl "¿Oh?{w=0.5}{nw}"
    extend 3tnmbol " ¿Te vas ahora?"
    n 4flrpol "Eso está...{w=0.5} bien.{w=0.75}{nw}"
    extend 2fsrsll " Supongo."
    n 2kplcal "...Sabes que realmente te voy a extrañar,{w=0.1} [player]."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 2flrssfsbr "¡A-{w=0.2}así que será mejor que des lo mejor de ti por mí,{w=0.1} [chosen_endearment]!"
    n 4fchsmf "Jejeje.{w=0.75}{nw}"
    extend 2uchsmfeaf " ¡Nos vemos pronto!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_rooting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_rooting_for_you:
    n 3unmajl "¿Eh?{w=0.5}{nw}"
    extend 3tnmsll " ¿Te vas ahora?"
    n 1fcssll "Siempre odio cuando tienes que ir a algún lado..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1kcssml "...Pero sé que siempre volverás por mí,{w=0.1} [chosen_endearment]."
    n 2fllssfsbl "N-{w=0.2}no como si tuvieras {i}opción{/i},{w=0.2} ¡obviamente!{w=0.75}{nw}"
    extend 2fsqsmf " Jejeje."
    n 4fchblfeaf "¡Hazme sentir orgullosa,{w=0.2} [player]!{w=0.5}{nw}"
    extend 4fchsmfeaf " ¡Estoy apoyándote!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_me_to_deal_with",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_me_to_deal_with:
    n 1unmajl "¿Te vas ahora,{w=0.1} [player]?"
    n 4kllpul "Awww...{w=0.75}{nw}"
    extend 2kllpol " bueno, está bien."
    n 1fnmcal "Cuídate mucho,{w=0.2} ¿entendido?"
    extend 3fcsssl " ¡O tendrás que vétrselas conmigo!"
    n 3fsqsml "Jejeje."
    n 3fchbgfeaf "¡Adiós por ahora!{w=0.5} ¡Te amo~!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_wish_you_could_stay_forever",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_wish_you_could_stay_forever:
    n 3kwmpol "¿Hora de irse,{w=0.1} [player]?"
    n 3kllssl "A veces desearía que pudieras quedarte para siempre..."
    n 4fcsajf "Pero entiendo que tienes cosas que hacer."
    n 2fslssfsbl "...Incluso si {i}no{/i} son siempre tan importantes como yo.{w=0.75}{nw}"
    extend 2nchgnl " Jejeje."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 1fchbgf "¡Hasta luego,{w=0.2} [chosen_endearment]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_that_time_again",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_that_time_again:
    n 4nslss "Je.{w=0.75}{nw}"
    extend 2nllfl " Esa hora de nuevo,{w=0.75}{nw}"
    extend 2tnmbo " ¿eh?"
    n 1csrsll "..."
    n 1ccsajlsbr "Deberías saber a estas alturas que nunca espero esto,{w=0.2} [player].{w=0.75}{nw}"
    extend 4csrcalsbr " Pero supongo que tiene que hacerse en algún momento."
    n 3fsqssl "...Eso no significa que te libres de volver, sin embargo.{w=0.5}{nw}"
    extend 3fsqsml " Jejeje."
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fcsbgl "¡Mejor no me hagas esperar,{w=0.2} [chosen_tease]!"
    n 4fchbgleafsbl "¡T-{w=0.2}te amo!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_stranger",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_stranger:
    n 4ccsfllesi "Hombre...{w=1}{nw}"
    extend 4tnmfll " ¿Ya?{w=0.75}{nw}"
    extend 2csqeml " Estás bromeando,{w=0.2} ¿verdad?"
    n 1kllsll "..."
    n 1ccsfllesi "..."
    n 2cdrfll "Sí,{w=0.2} sí.{w=0.75}{nw}"
    extend 2ccsajl " Lo sé,{w=0.2} [player].{w=0.75}{nw}"
    extend 2csrtrl " Ya lo he escuchado suficientes veces."
    n 4ccspol "...Pero no significa que tenga que gustarme."
    n 4fsqsml "Jejeje."
    n 7ccsbgl "Ya conoces el trato.{w=0.75}{nw}"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    extend 7fchbgl " ¡Mejor no seas un extraño,{w=0.2} [chosen_endearment]!"
    n 3fchblleaf "¡T-{w=0.2}te amo!"

    return { "quit": None }



init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_was_having_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_was_having_fun:
    n 3unmajl "¿Eh?{w=0.5}{nw}"
    extend 3tnmpul " ¿Te vas ahora?"
    n 4kcsemesi "Hombre..."
    n 1fllpol "Y yo que me estaba divirtiendo,{w=0.2} también...{w=1}{nw}"
    extend 2fsqpol " vaya aguafiestas,{w=0.2} [player]."
    n 2fcspol "..."
    n 1fchbll "Bueno,{w=0.1} ¡si te tienes que ir,{w=0.1} te tienes que ir!"
    n 2nchgnl "¡Ahora sal allá afuera,{w=0.1} tonto!{w=1}{nw}"
    extend 2fwlbgl " ¡Nos vemos luego!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_waiting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_waiting_for_you:
    n 2unmajl "¿Te vas,{w=0.1} [player]?"
    n 2fcsanl "Uuuuu...{w=1.5}{nw}"
    extend 1kllpol " okay."
    n 4fsqgsl "Pero más te vale volver pronto."
    extend 3fcsajf " Es grosero hacer esperar a alguien por ti,{w=0.2} d-{w=0.1}después de todo."
    n 4fslssfsbl "Jajaja."
    n 3fchbglsbr "¡L-{w=0.1}luego,{w=0.1} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_ill_be_okay",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_ill_be_okay:
    n 1unmajlesu "¿Huh?{w=0.5}{nw}"
    extend 4knmajlsbl " ¿Te vas?"
    n 4fslunl "..."
    n 1fcsgsfsbl "¡E-{w=0.1}está bien!{w=1}{nw}"
    extend 1fcsssledz " ¡Estaré bien!"
    n 2fsqpol "Que es más de lo que puedo decir de ti si me haces esperar de nuevo,{w=0.2} [player]..."
    n 2fsqsml "Jejeje."
    n 3nchgnl "¡Nos vemos luego~!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_dont_make_me_find_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_dont_make_me_find_you:
    n 2unmbol "¿Oh?{w=0.5}{nw}"
    extend 2unmajl " ¿Saliendo ahora,{w=0.1} [player]?"
    n 1kllpol "Deseo...{w=0.75}{nw}"
    extend 4kslpol " que no tuvieras que hacerlo..."
    n 4fcsajl "Pero entiendo que tienes cosas que hacer."
    n 2fsqcal "Pero más te vale venir a verme luego.{w=0.5}{nw}"
    extend 2fsqtrl " ¿Promesa?"
    n 2fcsbgl "¡No me hagas ir a buscarte!"
    n 4fchgnl "...¡Ahora márchate de una vez,{w=0.2} tonto!{w=0.75}{nw}"
    extend 3fchbll " ¡Nos vemos pronto!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_take_care_for_both",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_take_care_for_both:
    n 1unmpul "¿Mmm?{w=0.5}{nw}"
    extend 3tnmajl " ¿Te vas ahora,{w=0.1} [player]?"
    n 3kcsemlesi "...Bien,{w=0.3} bien.{w=1.25}{nw}"
    extend 4fsqtrl " ¡Pero con una condición!"
    n 4kslcalsbr "..."
    n 2knmtrlsbr "..Solo cuídate,{w=0.5}{nw}"
    extend 2knmsllsbr " ¿okay?"
    n 2fcspofsbl "Y-{w=0.1}y no solo por tu propio bien."
    extend 2kslssfsbl " Je."
    n 1kchssfesssbl "¡Nos vemos luego!"
    n 4kslslfsbr "..."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_enjoy_our_time_together",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_enjoy_our_time_together:
    n 2tnmajl "¿Te vas ahora,{w=0.2} [player]?"
    n 2fllcal "Nnnnnn...{w=0.5}{nw}"
    extend 4ksltrl " está bien."
    n 2fcsgsl "Pero más te vale volver luego,{w=0.2} ¿oíste?"
    n 2fllajl "Yo...{w=0.75}{nw}"
    extend 4kslcafsbr " disfruto nuestro tiempo juntos."
    n 2kchssfsbl "¡Nos vemos pronto,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_see_me_soon:
    n 1ullajl "Bueno,{w=0.3}{nw}"
    extend 1fllcal " supongo que tenías que irte eventualmente."
    n 2fsqpol "Eso no significa que tenga que gustarme,{w=0.2} sin embargo..."
    n 4knmpol "Ven a verme pronto,{w=0.2} ¿'kay?"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_making_it_up",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_making_it_up:
    n 4kslfl "Hombre...{w=1}{nw}"
    extend 4cnmfll " ¿en serio?{w=0.75}{nw}"
    extend 4csreml " ¡Vamos!{w=0.75}{nw}"
    n 2ccsslesi "..."
    n 2fcstr "Bien,{w=0.2} bien."
    n 2fcspo "...Pero {i}totalmente{/i} me lo compensarás cuando regreses.{w=0.75}{nw}"
    extend 4fchbleme " ¡Lo siento~!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fcsbglsbr "¡A-{w=0.2}ahora sal de aquí de una vez,{w=0.2} [chosen_tease]!"
    n 3fchbgl "¡Te veo luego!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_stranger",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_stranger:
    n 1ccsflesi "..."
    n 1kllfl "Hombre...{w=1}{nw}"
    extend 4tnmfl " ¿En serio?{w=0.75}{nw}"
    extend 4ksqflsbr " ¿Estás seguro de que no puedes quedarte un poco más?"
    n 2ccsemlesisbr "..."
    n 2clrfllsbr "Sí,{w=0.2} sí.{w=0.75}{nw}"
    extend 2cdrfll " Lo entiendo.{w=0.75}{nw}"
    $ chosen_tease = jn_utils.getRandomTeaseName()
    extend 2csqcal " Gran [chosen_tease]."
    n 4fsqsml "Jejeje."
    n 7fcsbglsbr "¡N-{w=0.2}no seas un extraño,{w=0.2} [player]!"

    if Natsuki.isEnamored(higher=True):
        n 7fchbglsbr "¡N-{w=0.2}nos vemos pronto!"

    return { "quit": None }



init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_going_now",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_going_now:
    n 2unmaj "¿Te vas ahora,{w=0.2} [player]?{w=0.75}{nw}"
    extend 2nchsm " ¡Nos vemos luego!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_heading_off",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_heading_off:
    n 1unmaj "¿Te vas ya,{w=0.2} [player]?"
    n 3nnmsm "¡Está bien!{w=0.5}{nw}"
    extend 3fchsm " ¡Cuídate!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_stay_safe",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_stay_safe:
    n 1nchss "¡Okaaay!{w=0.75}"
    extend 2tnmss " Supongo que te veré luego entonces."
    n 2fchsm "¡Mantente a salvo,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_take_care",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_take_care:
    n 4nnmbg "¡Nos vemos luego,{w=0.2} [player]!"
    n 4fchsm "¡Cuídate!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_see_me_soon:
    n 1nchbg "¡Adiós,{w=0.2} [player]!"
    n 4fchsmlsbr "Ven a verme pronto,{w=0.2} ¿de acuerdo?"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_catch_you_later",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_catch_you_later:
    n 1tnmboeqm "¿Eh?{w=0.75}{nw}"
    extend 2unmaj " ¿Te vas ahora?"
    n 2fcsbg "¡Entendido!{w=0.75}{nw}"
    extend 2fchbgl " ¡Te veo luego,{w=0.2} [player]!"
    n 2csrsllsbl "..."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_stranger",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_stranger:
    n 7tnmpueqm "¿Eh?{w=0.75}{nw}"
    extend 7tnmfl " ¿Te vas ahora,{w=0.2} entonces?"
    n 2tllsl "..."
    n 2tllaj "Bueno...{w=1}{nw}"
    extend 2clrfl " Supongo que está bien.{w=0.75}{nw}"
    extend 1ccscal " Esta vez."
    n 4ccsssl "Je."
    n 3ccsbgl "¡N-{w=0.2}no seas un extraño,{w=0.5} [player]!"
    n 3ksrbolsbl "..."

    return { "quit": None }



init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_you_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_you_later:
    n 1nchsm "¡Nos vemos luego,{w=0.2} [player]!"
    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_later:
    n 2nnmss "¡Hasta luego,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_goodbye:
    n 4nchsm "¡Adiós,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_kay",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_kay:
    n 1fcsbg "¡Okay!{w=0.5}{nw}"
    extend 2fchbg " ¡Adiós por ahora!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_ya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_ya:
    n 3nchbg "¡Nos vemos,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_oh_right",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_oh_right:
    n 1tnmfleqm "¿Huh?{w=0.75}{nw}"
    extend 1ullbo " Oh,{w=0.2} cierto."
    n 1cchsm "¡Hasta luego,{w=0.2} [player]!"

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_stranger",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_stranger:
    n 1tsqpueqm "¿Eh?{w=0.75}{nw}"
    extend 2cnmfl " ¿Terminaste aquí por ahora,{w=0.2} [player]?{w=1.5}{nw}"
    extend 2cdlpu " Huh."
    n 7cdlbo "..."
    n 7cdlfl "Bueno..."
    n 3tnmaj "No seas un extraño entonces,{w=0.5}{nw}"
    extend 3clrbo " supongo."
    n 4kdrbosbl "..."

    return { "quit": None }



init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_bye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_bye:
    n 1nnmsl "Adiós,{w=0.2} [player]."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_later",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_later:
    n 2nnmsf "Luego,{w=0.2} [player]."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_kay",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_kay:
    n 3fllsf "Okay.{w=0.2} Luego."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_goodbye:
    n 1nnmbo "Oh.{w=0.5}{nw}"
    extend 2fslsf " Adiós."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_see_you_around",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_see_you_around:
    n 2fsqsf "Te veo por ahí."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_yeah_bye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_yeah_bye:
    n 1fslfl "...Sí.{w=1}{nw}"
    extend 1fsqsl " {b}Adiós{/b}."

    return { "quit": None }



init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yeah",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yeah:
    n 2fcssfltsa "Sí."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yep",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yep:
    n 2fcsupltsa "Sip."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_uh_huh",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_uh_huh:
    n 1fsqsrltsb "Ajá."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_nothing_to_say:
    n 2fcssftsa "..."
    n 4kcsupltsa "..."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_kay",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_kay:
    n 3fslsrltsb "Okay."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_good",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_good:
    n 4fsqanltse "{i}Bien{/i}."

    return { "quit": None }

init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_door_hit_you",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_door_hit_you:
    n 2fsqemltsb "Espero que la puerta te golpee al salir.{w=0.75}{nw}"
    extend 2fsranltsb " Idiota."

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n 1uskwrlesh "¿Qué?{w=0.75}{nw}"
    extend 4knmemlsbl " ¿Te vas?{w=1}{nw}"
    extend 4fnmgslsbl " P-{w=0.1}pero apenas has estado aquí hoy,{w=0.2} [player]!"
    $ time_in_session_descriptor = jn_utils.getTimeInSessionDescriptor()
    n 3fcsgslsbr "Quiero decir,{w=0.75}{nw}"
    extend 3fnmpol " ¡literalmente solo has estado aquí por [time_in_session_descriptor]!"

    show natsuki 3knmpol zorder JN_NATSUKI_ZORDER at jn_center
    menu:
        n "¿En serio no puedes quedarte solo un poco más?"
        "Seguro, puedo quedarme un poco más.":

            n 4uchbsl "¡Yay{nw}{w=0.33}!"
            n 4uskgsl "¡Q-{w=0.2}quiero decir...!"

            if Natsuki.isLove(higher=True):
                n 1kllssl "G-{w=0.1}gracias,{w=0.1} [player]. Significa mucho para mí."
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 2kplssl "En serio.{w=0.2} Gracias,{w=0.1} [chosen_endearment]."
                n 4ksrunl "..."
            else:

                n 1fnmbgl "¡S-{w=0.2}sí!{w=0.5}{nw}"
                extend 2fcsbgl " ¡Eso pensé!"
                n 2fcssslsbl "Sí..."
                n 2fnmunl "..."
                n 4fbkwrf "¡Deja de mirarme así,{w=0.1} cielos!"
                n 3fllpof "Ugh..."

            n 1fllbgl "A-{w=0.1}ahora,{w=0.1} ¿dónde estábamos?"
            $ jn_globals.player_already_stayed_on_farewell = True
        "Si tú lo dices.":

            n 1kllpol "...[player]."
            n 2fcspulsbr "No te estoy...{w=1}{nw}"
            extend 2knmsllsbr " {i}forzando{/i} a estar aquí.{w=1}{nw}"
            extend 2kllsslsbr " {i}Sabes{/i} eso,{w=0.5}{nw}"
            extend 4knmpulsbl " ¿verdad?"
            n 1ksrsrlsbl "..."
            n 4ksrbolsbl "Entonces..."
            show natsuki 3ksqsrlsbl zorder JN_NATSUKI_ZORDER at jn_center

            menu:
                n "¿Estás seguro de que quieres quedarte?"
                "Sí, estoy seguro.":

                    n 3klrpol "Bueno...{w=0.5}{nw}"
                    extend 4ksqpol " si tú lo dices."
                    n 1fllcal "Solo quiero asegurarme de no estar siendo una imbécil al respecto."
                    n 4kllpul "Pero..."

                    if Natsuki.isLove(higher=True):
                        $ chosen_endearment = jn_utils.getRandomEndearment()
                        n 4knmssl "Gracias,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
                        extend 1kchsslsbl " Realmente lo aprecio."

                    elif Natsuki.isEnamored(higher=True):
                        n 4knmssl "Gracias,{w=0.2} [player].{w=0.75}{nw}"
                        extend 1kchsslsbl " Yo...{w=0.3} realmente lo aprecio."
                    else:

                        n 4flrcaf "Gracias,{w=0.2} [player].{w=0.75}{nw}"
                        extend 1fcscafsbl " Significa mucho."

                    $ Natsuki.calculatedAffinityGain()
                    $ jn_globals.player_already_stayed_on_farewell = True
                "No, me tengo que ir.":

                    n 3knmcal "Bueno...{w=0.3} okay,{w=0.1} [player]."
                    n 4knmpol "Cuídate allá afuera,{w=0.1} ¿de acuerdo?"
                    n 4fchsmlsbl "¡Nos vemos luego!"

                    if Natsuki.isEnamored(higher=True):
                        n 2kslcalsbr "..."

                    elif Natsuki.isAffectionate(higher=True):
                        n 2kslbolsbr "..."
                    else:

                        n 2kslbosbr "..."

                    return { "quit": None }
        "Lo siento, [n_name]. Realmente tengo que irme.":

            n 1fllanl "¡Nnnnnn-!"
            n 4kcssll "..."
            n 4klrsll "Bueno...{w=0.3} okay."
            n 2kllpol "Solo no tardes demasiado,{w=0.1} ¿de acuerdo?"
            n 2fchsmlsbr "¡Nos vemos luego,{w=0.1} [player]!"

            if Natsuki.isEnamored(higher=True):
                n 2kslcalsbr "..."

            elif Natsuki.isAffectionate(higher=True):
                n 2kslbolsbr "..."
            else:

                n 2kslbosbr "..."

            return { "quit": None }

    return


init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask_alt",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask_alt:
    n 4knmajl "¡E-{w=0.2}espera un segundo,{w=0.2} [player]!{w=1}{nw}"
    extend 2fcsgsl " ¡E-{w=0.2}esto no es justo en absoluto!"
    $ time_in_session_descriptor = jn_utils.getTimeInSessionDescriptor()
    n 2flleml "Apenas has estado aquí [time_in_session_descriptor],{w=0.75}{nw}"
    extend 2fnmajl " ¿y {i}ya{/i} te vas?"

    show natsuki 2fcsgslsbl zorder JN_NATSUKI_ZORDER at jn_center
    menu:
        n "¡Vamos!{w=0.5} Te quedarás un poco más,{w=0.2} ¿no?"
        "Seguro, puedo quedarme un rato.":

            n 3fcsbsl "¡J-{w=0.3}Ja!{w=0.75}{nw}"
            extend 3fsqsslsbr " Lo sabía."
            n 4fsqsml "Jejeje.{w=0.5}{nw}"
            extend 1fsqbgleme " ¡Parece que gano de nuevo,{w=0.1} [player]!"

            show natsuki 3fcsbgledzsbl zorder JN_NATSUKI_ZORDER at jn_center
            menu:
                n "¿O-o tal vez simplemente no pudiste obligarte a dejar a alguien tan {i}asombrosa{/i} como yo?"
                "Me atrapaste, [n_name]. No podría dejarte ni aunque lo intentara.":

                    n 2uskwrfesh "¿Q-{w=0.3}qué...?"
                    n 4fcsanf "¡Nnnnnnn-!"
                    $ player_initial = jn_utils.getPlayerInitial()
                    n 1fbkwrfess "¡[player_initial]-{w=0.3}[player]!{w=0.75}{nw}"
                    extend 4fllwrf " ¡No salgas con cosas como esa!"
                    n 2fcspofesi "Yeesh..."

                    if Natsuki.isEnamored(higher=True):
                        extend 2flrpof " Juro que llevas las cosas demasiado lejos a veces."
                        n 4fsrunfess "..."
                        n 2fcsemlsbr "¡C-{w=0.2}como sea!"

                    elif Natsuki.isAffectionate(higher=True):
                        extend 2fsqpolsbl " ¿estás {i}tratando{/i} de darme un ataque al corazón o algo?"
                        n 2fcsajlsbl "C-{w=0.2}como sea."
                    else:

                        extend 2fslsslsbl " tu rutina de comedia {i}definitivamente{/i} necesita más trabajo,{w=0.2} ¡te diré eso!"
                        n 2fcsbolsbl "Bueno,{w=0.2} como sea..."
                "Lo que sea, Natsuki.":

                    $ player_was_snarky = True
                    n 3tsqssl "¿Oh?{w=0.75}{nw}"
                    extend 3fcsbgl " ¿Qué pasa,{w=0.1} [player]?"
                    n 4fsqbgleme "¿Un poco {i}demasiado{/i} cerca de la verdad?"
                    extend 4nchgnl " Jejeje."
                    n 1nllssl "Bueno,{w=0.2} de cualquier modo."

            n 3fcsbglsbl "Solo me alegra que hayas visto la luz."
            extend 3fchbll " Incluso si tomó un poco de persuasión."
            n 1ullaj "Así que...{w=0.75}{nw}"
            extend 3fchsm " ¿hay algo más de lo que quieras hablar?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()
        "Está bien, supongo.":

            n 1fsqpu "...¿Tú {i}supones{/i}?"
            n 3fnmgsl "¡¿Qué quieres decir con,{w=0.2} {i}tú supones{/i}?!"
            n 3fcspolesi "Cielos...{w=1}{nw}"
            extend 4kslcal " haces que suene como si te hubiera encadenado al escritorio o algo así..."
            n 1fcsajl "Bueno,{w=0.2} como sea."
            n 2nllbo "Supongo que un agradecimiento está en orden entonces."
            n 2nsqbo "..."
            n 2flrem "...{i}Supongo{/i}."
            n 4fsgsm "..."
            n 4uchgnlelg "¡Oh,{w=0.2} anímate,{w=0.2} [player]!"
            extend 3fchbglelg " ¡Hombre!"
            n 3fchgnl "¡Deberías {i}saber{/i} a estas alturas que doy tanto como recibo!"
            n 3fchsml "Jejeje."
            n 1tllss "Ahora,{w=0.2} ¿dónde estábamos?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()
        "Lo siento [n_name], no puedo ahora mismo.":

            n 1fcsunl "Uuuu-"
            n 1kcspulesi "..."
            n 4fslsll "...Supongo que está bien."
            n 3fcsbol "Tienes cosas que hacer.{w=0.5}{nw}"
            extend 3fsrcal " Lo entiendo."
            n 1fnmtrl "Pero {i}definitivamente{/i} vas a venir a visitar más tarde."
            n 2kllcal "..."
            n 2knmcasbl "¿Verdad?"

            return { "quit": None }
    return


init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n 4unmboesu "¿Eh?{w=0.75}{nw}"
    extend 2knmaj " Realmente no {i}tienes{/i} que irte ya,{w=0.1} ¿verdad?"
    n 1fcsgsl "Quiero decir,{w=0.5}{nw}"
    extend 2fllgslsbr " ¡vamos!{w=1}{nw}"
    extend 2fnmsf " ¡Se siente como si apenas hubieras estado aquí!"
    n 3fcseml "D-{w=0.2}de hecho,{w=0.75}{nw}"
    extend 3fcsgslsbl " ¡apuesto a que podrías pasar el rato conmigo {i}fácilmente{/i} un poco más!"
    n 1fnmajlsbl "¿Verdad,{w=0.2} [player]?"
    n 1fllunlsbr "..."
    show natsuki 4knmbolsbr zorder JN_NATSUKI_ZORDER at jn_center

    menu:
        n "...¿Verdad?"
        "¡Verdad!":

            n 3fcsbgfsbl "¡A-{w=0.3}Ajá!{w=0.75}{nw}"
            extend 3flrsslsbl " ¡Lo sabía!"
            n 1fcsgsl "N-{w=0.2}no como si te necesitara aquí, o algo tonto como eso.{w=1.25}{nw}"
            extend 2fcspolesi " {i}Obviamente{/i}."
            n 2fslemlsbr "Tendrías que ser bastante solitario para ser {i}tan{/i} dependiente de alguien más."
            n 2kslsllsbr "..."
            n 1fcswrfesh "Bueno,{w=0.2} c-{w=0.2}como sea!{w=1}{nw}"
            extend 4fcspol " ¡Suficiente de eso!"
            n 2fllajl "Ya dijiste que te quedarías,{w=0.2} así que..."
            n 4fsldvlsbr "..."

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()
        "Lo siento, realmente necesito irme.":

            n 1fllsll "...Je.{w=1}{nw}"
            extend 1fslcal " Cierto."
            n 2fslunl "..."
            n 2fcswrlsbr "B-{w=0.2}bueno,{w=0.2} ¡está bien!"
            n 3flrpolesi "Supongo que eso significa que tendré que probar tu obediencia en otro momento.{w=1}{nw}"
            extend 3fsrdvless " Jejeje."
            n 3fcsbgless "¡L-{w=0.2}luego,{w=0.2} [player]!"

            return { "quit": None }
    return


init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_pleading_ask:
    n 4kskwrfesh "¡N-{w=0.3}no!{w=0.5}{nw}"
    extend 4fbkwrfess " ¡No puedes irte aún!"
    n 1klluplsbr "..."
    n 2fcsunl "..."
    n 2fcspulesi "..."
    n 1fnmcal "[player]..."
    n 1fcsemfsbr "Yo...{w=0.75}{nw}"
    extend 2fcsunfesssbr " realmente...{w=1}{nw}"
    extend 2kslunfesssbr " te quiero aquí ahora mismo."

    show natsuki 4ksqslfsbl zorder JN_NATSUKI_ZORDER at jn_center

    menu:
        n "¿Solo unos minutos más?{w=0.5} ¿Por favor?"
        "¡Por supuesto!":

            n 4kchbsf "¡Sí!{w=0.66}{nw}"
            n 3fllwrfesh "¡Q-{w=0.2}quiero decir...!"
            n 3kllslfsbl "..."
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            n 4kllcaf "G-{w=0.2}gracias,{w=0.1} [player].{w=3}{nw}"
            extend 4fcspofess " Eres [chosen_descriptor],{w=0.3} ¿lo sabías?"
            n 1kllssf "En serio.{w=1.5}{nw}"
            extend 4kslssf " Gracias."
            n 2fcsajfsbr "A-{w=0.2}ahora,{w=0.75}{nw}"
            extend 2tnmssfsbr " ¿dónde estábamos?"
            n 4flrdvfsbr "Je..."

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()
        "No puedo ahora mismo.":

            n 1kslbof "...Oh."
            n 2fcsajlsbl "Bueno,{w=0.3} si tienes que irte,{w=0.3} no se puede evitar,{w=0.75}{nw}"
            extend 2ksrcal " supongo..."
            n 4ksqsll "Solo vuelve pronto,{w=0.3} ¿está bien?"
            n 1kslpul "..."
            n 4knmbol "...¿Y [player]?"
            n 4ksqbof "..."

            if Natsuki.isLove(higher=True):
                show natsuki 4kslsgf zorder JN_NATSUKI_ZORDER at jn_center
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                play audio clothing_ruffle
                $ jnPause(3.5)
                play audio kiss
                $ jnPause(2.5)
                n "¡T-{w=0.2}te amo!"
            else:

                n 1kcsunfess "...te extrañaré.{w=0.75}{nw}"
                show natsuki 4kllunfess
                $ jnPause(1.5)

            return { "quit": None }
    return


init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_gentle_ask:
    n 1kllsrf "[player]...{w=0.75}{nw}"
    extend 4knmsrf " ¿realmente tienes que irte ahora?"
    n 3kcsbof "Sé que tienes cosas que hacer,{w=0.5} pero..."

    show natsuki 3knmpuf zorder JN_NATSUKI_ZORDER at jn_center
    menu:
        n "¿Estás seguro de que no puedes quedarte ni un poco más?"
        "Puedo quedarme un poco más.":

            n 4kwmssfeaf "[player]..."
            n 4fcsbofesssbr "G-{w=0.2}gracias.{w=0.75}{nw}"
            extend 2ksrsgf " Eso...{w=0.5} realmente significa mucho para mí."
            n 2ksqcaf "De verdad.{w=0.5} Gracias..."
            n 1ksrcaf "..."

            show natsuki 1fbkcaf zorder JN_NATSUKI_ZORDER at jn_center
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            play audio clothing_ruffle
            $ jnPause(3.5)
            show natsuki 1ncspuf zorder JN_NATSUKI_ZORDER at jn_center
            hide black with Dissolve(1.25)

            n 1kslsmfsbl "..."
            n 4kslssfsbl "Así que..."
            extend 3knmsslsbr " ¿dónde estábamos?"

            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculatedAffinityGain()
        "Lo siento, realmente tengo que irme.":

            n 1kllsrf "Oh..."
            n 2fcsemf "Estaría mintiendo si dijera que no estoy decepcionada...{w=1.5}{nw}"
            extend 2kslcaf " pero entiendo."
            n 1kwmsrf "Solo ten cuidado allá afuera,{w=0.1} ¿okay?"
            n 1kllsrf "..."
            n 4kwmsmf "T-{w=0.1}te amo,{w=0.1} [player]..."
            n 4kchssfsbl "Te veré luego."

            if (random.choice([True, False])):
                show natsuki 1ksrsgfsbl zorder JN_NATSUKI_ZORDER at jn_center
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                play audio clothing_ruffle
                $ jnPause(3.5)
                play audio kiss
                $ jnPause(2.5)

            return { "quit": None }
    return






init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_early_morning_going_this_early",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_early_morning_going_this_early:
    n 1unmpuesu "¿Eh?{w=1}{nw}"
    extend 3nllsl " Oh."
    n 3nllaj "Bueno...{w=0.75}{nw}"
    extend 1tnmss " Supongo que realmente no debería sorprenderme.{w=1}{nw}"
    extend 1nlrpol " Debes haber tenido una razón para estar despierto tan temprano."
    n 4nsrsslsbr "...Espero,{w=0.2} al menos."
    n 3fcssslsbr "Ten cuidado allá afuera,{w=0.1} ¿de acuerdo?{w=1}{nw}"
    extend 3nchgnlelg " ¡No hagas nada tonto!"

    if Natsuki.isLove(higher=True):
        n 3fchsmfeaf "¡Te amo,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 3fchbll "¡Te veo luego,{w=0.2} [chosen_tease]!"
    else:

        n 3fchsml "¡Nos vemos!"

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_morning_heading_off",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_morning_heading_off:
    n 3unmaj "¿Te vas ya,{w=0.2} [player]?{w=1}{nw}"
    extend 3fchbg " ¡No hay problema!"

    if Natsuki.isEnamored(higher=True):
        n 3fchbglsbr "¡Espero que tu día sea tan asombroso como tú!"

        if Natsuki.isLove(higher=True):
            n 4nchsmf "Jejeje.{w=0.75}{nw}"
            extend 4fchbgfeaf " ¡Te amo,{w=0.1} [player]~!"
        else:

            n 3uchsml "¡Hasta luego!"
    else:

        n 3fchsml "¡Nos vemos!"

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_afternoon_come_visit_soon",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_afternoon_come_visit_soon:
    n 1unmaj "¿Oh?{w=0.75}{nw}"
    extend 2unmbo " ¿Saliendo un poco más tarde hoy,{w=0.1} [player]?"
    n 2ullaj "Supongo que está bien...{w=1}{nw}"
    extend 1fnmca " solo recuerda venir de visita pronto,{w=0.2} ¿okay?"

    if Natsuki.isAffectionate(higher=True):
        n 3fsqcal "Me enojaré si no lo haces."
        n 3fsqsml "Jejeje.{w=0.75}{nw}"
        extend 3nchgnlelg " ¡Cuídate,{w=0.2} [player]!"
    else:

        n 3fchsmlsbl "¡Cuídate!"

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_evening_good_evening",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_evening_good_evening:
    n 4unmboesu "¿Eh?{w=0.75}{nw}"
    extend 1unmaj " ¿Te vas ahora,{w=0.1} [player]?"
    n 2ullaj "Bueno...{w=1}{nw}"
    extend 2nslcal " está bien."
    n 3fchsmlsbl "¡Ten una buena noche!"

    if Natsuki.isAffectionate(higher=True):
        n 3kslsllsbl "..."
        n 3kwmbol "...Y ven a verme pronto,{w=0.2} ¿de acuerdo?"

        if Natsuki.isLove(higher=True):
            n 4kchsmleafsbl "¡T-{w=0.2}te amo!"

    return { "quit": None }




init python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_night_good_night",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_night_good_night:
    n 3unmaj "¿Oh?{w=0.75}{nw}"
    extend 3tnmsl " ¿Te vas a dormir ya?"
    n 4ulraj "Bueno...{w=1}{nw}"
    extend 1nlrca " No puedo culparte.{w=1.25}{nw}"
    extend 2fsqsm " Jejeje."
    n 2uchsm "¡Buenas noches,{w=0.2} [player]!"

    if Natsuki.isAffectionate(higher=True):
        n 3uchbgl "¡Dulces sueños!"

    return { "quit": None }
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
