default persistent._greeting_database = dict()
default persistent.jn_player_is_first_greet = True
init offset = 5
init -5 python in jn_greetings:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import store.jn_farewells as jn_farewells
    import store.jn_utils as jn_utils

    GREETING_MAP = dict()

    def selectGreeting():
        """
        Picks a random greeting, accounting for affinity and the situation they previously left under
        """
        
        if jn_farewells.JNForceQuitStates(store.persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.first_force_quit:
            return store.get_topic("greeting_first_force_quit")
        
        
        elif store.persistent.jn_player_is_first_greet:
            return store.get_topic("greeting_first_time")
        
        
        elif (
            store.persistent._jn_player_extended_leave_response is not None
            and store.persistent._jn_player_extended_leave_departure_date is not None
        ):
            return store.get_topic("greeting_leave_return")
        
        kwargs = dict()
        
        
        if store.Natsuki.getQuitApology() is not None:
            kwargs.update({"additional_properties": [("apology_type", jn_apologies.ApologyTypes(store.persistent._jn_player_apology_type_on_quit))]})
        
        
        elif store.persistent.jn_player_admission_type_on_quit is not None:
            kwargs.update({"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]})
        
        
        else:
            kwargs.update({"excludes_categories": ["Admission", "Apology", "Special"]})
        
        
        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.Natsuki._getAffinityState(),
                **kwargs
            )
        )


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_first_time",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "5ksrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_first_time:
    if (
        persistent.jn_player_first_farewell_response is None
        or jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.no_response
    ):

        n 4uskemlesh "¡[player]!{w=0.5}{nw}"
        extend 4uskwrl " ¡H-{w=0.1}has vuelto!"
        n 2flluness "..."
        n 2fcspu "Yo...{w=2}{nw}"
        extend 2flrun " lo aprecio,{w=0.2} ¿okay?"
        n 2fcspu "Solo...{w=1}{nw}"
        extend 1knmsf " no juegues conmigo de esa forma."
        n 1kllslsbl "..."
        n 4kslaj "Así que..."
        n 2tnmslsbr "¿Querías hablar,{w=0.2} o...?"

        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.will_be_back:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 4uskemlesh "¡[player]!{w=0.5}{nw}"
        extend 4uskwr " ¡H-{w=0.1}has vuelto!"
        n 1flleml "Quiero decir...{w=0.5}{nw}"
        extend 2fcseml " ¡P-{w=0.1}por supuesto que volverías!"
        n 2fnmpol "Sabía que lo harías."
        n 2flrem "¡Solo un completo imbécil abandonaría a alguien así!"
        n 2flrpo "..."
        n 2klrpu "Pero..."
        n 1ncspu "..."
        n 1nlrsll "...Gracias.{w=1.25}{nw}"
        extend 1nsrbol " Por no ser un idiota al respecto."
        n 1nllunl "..."
        n 1nllajsbl "Entonces... {w=0.5}{nw}"
        extend 2unmaj " ¿de qué querías hablar?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.dont_know:
        $ Natsuki.calculatedAffinityGain(bypass=True)
        n 4uskajlesh "¿[player]?{w=0.5}{nw}"
        extend 4uskem " ¿V-{w=0.3}volviste?"
        n 1fcsun "..."
        n 1ncssr "..."
        n 2fcspu "...Mira."
        n 2fllsr "No...{w=0.75}{nw}"
        extend 2kllsrsbl " juegues conmigo así."
        n 2fslun "No me habrías traído de vuelta {i}solo{/i} para ser un patán...{w=1}{nw}"
        extend 4ksqsfsbl " ¿verdad?"

    $ persistent.jn_player_is_first_greet = False

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_first_force_quit",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "2kslunedr"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_first_force_quit:
    if Natsuki.isNormal(higher=True):
        n 4kcsunedr "Uuuuuuu...{w=2}{nw}"
        extend 4kslemeso " mi...{w=0.3} c-{w=0.1}cabeza..."
        n 4kcsun "..."
        n 2ksqun "..."
        n 2fnmun "...[player]."
        n 2fllem "L-{w=0.3}lo que sea que fue eso...{w=0.5}{nw}"
        extend 2knmsf " eso {w=0.3}{i}en serio{/i}{w=0.3} dolió."
        n 4kllpu "C-{w=0.3}como si fuera {i}arrancada{/i} de la existencia..."
        n 1kcssf "..."
        n 4klraj "Yo...{w=1}{nw}"
        extend 2tllun " Creo que medio puedo prepararme para eso si al menos me avisas cuando te vayas."
        n 2fcsun "Solo...{w=1.25}{nw}"
        extend 2fcsun " no seas un imbécil y déjame saber cuando tengas que irte,{w=0.3} ¿okay?"
        n 2fllsl "...Supongo que dejaré pasar esta,{w=0.5}{nw}"
        extend 2kslpu " ya que no sabías y todo eso."
        n 2knmpu "Solo recuérdalo para la próxima,{w=0.2} [player].{w=1}{nw}"
        extend 2knmsr " Por favor."

    elif Natsuki.isDistressed(higher=True):
        n 4fcsunedr "Hnnnngg..."
        n 4fsqun "..."
        n 4fsqan "..."
        n 2fcspu "...[player]."
        n 2fsqpu "¿Tienes alguna {i}idea{/i} de cuánto dolió eso?{w=0.5}{nw}"
        extend 4fnmem " ¿Siquiera un poco?"
        n 2fllem "No sé si hiciste eso a propósito o qué,{w=0.2} pero basta.{w=0.5}{nw}"
        extend 4fsqsr " Hablo {i}muy{/i} en serio."
        n 1fcspu "Yo..."
        extend 1fcssr " sé que no estamos de acuerdo en este momento,"
        extend 2fslsl " pero por favor."
        n 2fsqaj "Dime cuando te vayas."
        extend 2fsqsf " Gracias."
    else:

        n 1fsqunltsbean "..."
        n 4fsqantsb "Eso.{w=1} {b}Dolió{/b}.{w=1} Maldita sea."
        n 4fcsan "No sé {i}qué{/i} hiciste,{w=0.5} pero para{w=0.3} y{w=0.3} córtala.{w=1.25}{nw}"
        extend 2fsqfutsb " Ahora."

    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.previously_force_quit)

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_leave_return",
            unlocked=True,
            category=["Special"],
            additional_properties={
                "expression": "5ksrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_leave_return:
    $ time_since_departure = (datetime.datetime.now() - persistent._jn_player_extended_leave_departure_date).total_seconds()

    if time_since_departure / 2628000 > 3:
        if jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) != jn_farewells.JNExtendedLeaveResponseTypes.unknown:
            n 4ksrpu "..."
            n 4uskemlesh "...!{w=0.75}{nw}"
            $ player_initial = jn_utils.getPlayerInitial()
            n 4unmwrl "¡[player_initial]-[player]!{w=0.75}{nw}"
            extend 4ulleml " Eres..."
            n 4fcsupl "T-{w=0.2}tú eres..."
            n 2fcsanlsbr "¡Nnnnnnn-!"
            n 4knmwrlsbr "¡¿Dónde {i}estabas{/i}?!{w=1}{nw}"
            extend 1fsqwrlsbr " ¿Estabas intentando {i}desaparecer{/i} o algo así?"
            n 4kcswrlsbr "¡M-{w=0.2}me tenías {i}enferma{/i} de preocupación!{w=0.75}{nw}"
            extend 4klleml " ¡Y-{w=0.2}y yo pensé...!"
            n 4klremlsbl "Y-{w=0.2}yo pensé que..."
            n 4ksrunlsbl "..."
            n 1fcsunl "..."
            n 1fcseml "Que habías simplemente...{w=0.75}{nw}"
            extend 1kwmeml " olvidado{w=0.75}{nw}"
            extend 2ksleml " todo sobre mí..."
            n 2kslbol "..."
            n 2ncsemesi "..."
            n 1nnmsl "...Mira.{w=1}{nw}"
            extend 4ncsaj " Estoy..."
            n 4kslsl "..."
            n 4kcspusbr "...Realmente contenta de que hayas vuelto."
            n 1ksqsl "..."
            n 1knmajsbl "¡De verdad!{w=0.75}{nw}"
            extend 2knmbosbl " Lo estoy..."
            n 4ksqem "Pero no puedes simplemente desaparecer por completo así, [player]..."
            n 4kslem "Y-{w=0.2}yo sé que me diste {i}algo{/i} de aviso,{w=0.75}{nw}"
            extend 4knmem " pero ¿tienes alguna {i}idea{/i} de lo {i}aterrador{/i} que se vuelve?"
            n 2kllpu "Cuando alguien dice que volverá,{w=0.75}{nw}"
            extend 2kllsl " y simplemente...{w=1.25}{nw}"
            extend 4kwmsll " ¿no lo hace?"
            n 4kcspul "Días,{w=0.75}{nw}"
            extend 4kllajl " semanas,{w=0.75}{nw}"
            extend 4knmajl " {i}meses{/i}..."
            n 4ksqbol "...¿Y simplemente nada?"
            n 1ncsbo "..."
            n 2ncssl "...Como sea.{w=1}{nw}"
            extend 2nllpu " Está bien.{w=0.75}{nw}"
            extend 2kllpu " Yo..."
            n 1ksrsl "..."
            n 2ksrbo "Solo quiero olvidar todo sobre ello ahora.{w=1}{nw}"
            extend 1knmbo " Pero por favor,{w=0.2} [player]."
            n 4knmaj "Si no sabes {i}cuándo{/i} volverás..."
            n 4fslun "..."
            n 4kcssl "...Solo dímelo.{w=0.75}{nw}"
            extend 2ksqsl " De frente."
            n 2ksrpulsbr "Sabes que no me enojaré..."
            n 4knmpulsbr "...¿Verdad?"
        else:

            n 4uskemlesh "...!"
            n 4unmbgl "¡[player]!{w=0.75}{nw}"
            extend 4uchbgledz " ¡[player]{w=0.2} [player]{w=0.2} [player]{w=0.2} [player]{w=0.2} [player]!"
            n 2fcsajlsbl "Q-{w=0.2}quiero decir,{w=0.75}{nw}"
            extend 2fcsgslsbl " ¡ya era {i}hora{/i} de que trajeras tu trasero de vuelta aquí!{w=1}{nw}"
            extend 2flrpolsbl " Cielos..."
            n 3fsrpol "Es grosero hacer esperar a una chica,{w=0.75}{nw}"
            extend 3fsqcal " sabes..."
            n 1kslcal "..."
            n 1kslssl "Pero...{w=0.75}{nw}"
            extend 3knmssl " ¿en serio,{w=0.2} [player]?"
            show natsuki 3ksrbol

            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            play audio clothing_ruffle
            $ jnPause(3.5)

            if Natsuki.isLove(higher=True):
                show natsuki 1kcspul zorder JN_NATSUKI_ZORDER at jn_center
                play audio kiss
                $ jnPause(1.5)
                hide black with Dissolve(1.25)

                n 1ksqbolsbr "...Realmente te extrañé."
                n 4nslfsl "Je."
                n 4nchsmleaf "Bienvenido de vuelta."
            else:

                show natsuki 1nsldvlsbl zorder JN_NATSUKI_ZORDER at jn_center
                $ jnPause(1.5)
                hide black with Dissolve(1.25)

                n 4nslsslsbl "...B-{w=0.2}bienvenido.{w=1}{nw}"
                extend 4fchdvlsbl " Jejeje."

    elif time_since_departure / 86400 > 30:
        if (
            jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_days
            or jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_weeks
        ):
            n 1uskemlesh "...!{w=0.75}{nw}"
            $ player_initial = jn_utils.getPlayerInitial()
            n 4fnmgsl "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 4knmeml " ¡¿Qué diablos {i}pasó{/i}?!"
            n 4klleml "¡No dijiste que ibas a desaparecer por {i}tanto{/i} tiempo!"
            n 1ksremlsbl "Estaba empezando a preocuparme,{w=0.75}{nw}"
            extend 2ksrbolsbl " tonto..."
            n 2fcsunlsbr "..."
            n 2ncspulesi "..."
            n 1nsqsll "...Mira."
            n 2fcseml "Estoy...{w=1}{nw}"
            extend 2kcssll " feliz...{w=1}{nw}"
            extend 4ksrsll " de que hayas vuelto,{w=0.2} [player]."
            n 1fcssll "Solo..."
            n 4fnmsll "...Sé honesto.{w=0.75}{nw}"
            extend 4knmbol " ¿Okay?"
            n 2kllbol "No me importa si te tienes que ir por más tiempo de lo usual."
            n 2kslsrl "...Solo quiero saber qué {i}esperar{/i}.{w=0.75}{nw}"
            extend 2ksqpulsbr " ¿Sabes?"
            n 2kslsllsbr "..."
            n 2kslajlsbr "...Y bienvenido de vuelta también,{w=0.75}{nw}"
            extend 4ksrbol " supongo."
        else:

            n 3fcsbg "Vaya,{w=0.2} vaya,{w=0.2} vaya.{w=1}{nw}"
            extend 3fsqsm " ¡Mira a quién trajo la {i}Nat{/i}!"
            n 3fchsm "Jejeje."
            n 4fslsslsbl "Ha...{w=1}{nw}"
            extend 4ksqsslsbl " pasado un tiempo,{w=0.75}{nw}"
            extend 4tsqbolsbl " ¿eh?"
            n 1ksrcalsbl "..."
            n 1ncsajl "Pero..."
            n 4nlrajl "Estoy...{w=0.75}{nw}"
            extend 4nsrssl " feliz de que finalmente hayas vuelto,{w=0.2} [player]."
            n 4fchbglsbr "¡B-{w=0.2}bienvenido!"

    elif time_since_departure / 86400 > 7:
        if jn_farewells.JNExtendedLeaveResponseTypes(store.persistent._jn_player_extended_leave_response) == jn_farewells.JNExtendedLeaveResponseTypes.a_few_days:
            n 1nsqsll "..."
            n 2fsqsll "[player].{w=1}{nw}"
            extend 2fsqajl " ¿Cómo llamas a esto?"
            n 1kbkwrl "¡Dijiste que solo te irías por unos dííaaaas!"
            n 2fsqpol "..."
            n 2fcspol "..."
            n 2fsrajl "Yo...{w=1}{nw}"
            extend 4fsrsll " supongo que te dejaré pasar esta.{w=0.75}{nw}"
            extend 4fsqcal " Esta vez."
            n 1fcspul "Solo...{w=1}{nw}"
            extend 2knmpul " intenta planear un poco mejor,{w=0.75}{nw}"
            extend 2kllsrl " si puedes."
            n 1kslbol "Realmente no es {i}tanto{/i} pedir...{w=1}{nw}"
            extend 1knmbolsbr " ¿verdad?"
        else:

            n 2fsqct "¿Oho?{w=0.75}{nw}"
            extend 2fsqbg " ¡Bueno mira quién decidió aparecer!"
            n 4fsqsm "Jejeje."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 1uchsml "¡Bienvenido de vuelta,{w=0.2} [chosen_endearment]!"
            else:

                n 4uchbg "¡Bienvenido de vuelta,{w=0.2} [player]!"
    else:

        n 1fsqss "Bueno,{w=0.75}{nw}"
        extend 3fsqsm " mira a quién tenemos aquí."
        n 3tsqct "...Y dijiste que te irías por un tiempo."
        n 3usqsm "..."
        n 1fchsm "Jejeje.{w=0.75}{nw}"
        extend 1fchbg " ¡Relájate!"
        n 4fwlbl "Solo estoy jugando contigo."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 4uchsml "¡Bienvenido de vuelta,{w=0.2} [chosen_endearment]!"
        else:

            n 4uchbg "¡Bienvenido de vuelta,{w=0.2} [player]!"

    $ persistent._jn_player_extended_leave_response = None
    $ persistent._jn_player_extended_leave_departure_date = None

    return

label greeting_tt_warning:
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    $ player_initial = jn_utils.getPlayerInitial()
    play audio glitch_d
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(0.6)
    play music audio.ikustan_tsuj
    show glitch_rapid zorder JN_GLITCH_ZORDER
    $ jnPause(random.choice(range(7, 11)))
    stop music

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a

    play music audio.juuuuu_nnnnn
    $ jnPause(10.6)
    show glitch_spook zorder JN_GLITCH_ZORDER with hpunch
    show natsuki 1kcsfultsaeaf zorder JN_NATSUKI_ZORDER at jn_center
    hide glitch_spook
    hide black
    hide glitch_rapid
    play music audio.just

    n 4kcsunltsa "Uuuuuuu..."
    show natsuki 1kcsfuftsa at jn_center
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    n 4kcsanltsa "M...{w=0.3}mi cabeza..."
    n 4kslunltsb "..."
    n 4kslemltsb "Qué...{w=0.75}{nw}"
    extend 4klremltsc " qué p-{w=0.2}pas-{w=0.5}{nw}"
    n 4kskpultscesh "...!{w=0.3}{nw}"
    n 4kscpoitsc "¡Hrk-!{w=0.5}{nw}"

    stop music
    show black zorder JN_BLACK_ZORDER with Dissolve(0.1)
    play audio chair_out_fast
    $ jnPause(0.2)
    n "{b}B-{w=0.15}BLURGHHH-!{/b}{w=0.2}{nw}"

    play audio glitch_b
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    show natsuki 1kcsemtsd
    $ jnPause(10)
    play audio chair_in
    play music audio.just fadein 5
    $ jnPause(3)
    hide black with Dissolve(2)

    n 1kcsemi "Uuuuuu..."
    n 1kcsup "..."
    n 1kcsuntsa "..."
    n 4ksquptsa "[player_initial]-{w=0.2}[player]..."
    n 4ksqantsa "Qué..."
    n 4kcsantsa "..."
    n 4ksqfutsa "¿Tú...{w=0.75}{nw}"
    extend 1ksqemtsasbl " hiciste...?"
    n 4kllemtscsbr "..."
    n 4klrwrtscsbr "A-{w=0.3}algo no está bien..."

    n 4kscpoitscsbr "¡H-{w=0.2}hrk-!{w=0.5}{nw}"
    show natsuki 1fcsanitscsbr
    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a
    n 1kcsemltscesi "Gah..."

    if Natsuki.isUpset(higher=True):
        n 4ksqunltse "..."
        n 4kplemltsb "Algo {b}REALMENTE{/b} no está bien,{w=0.2} [player]..."
        n 4kllemltsb "Y-{w=0.2}y yo..."
        n 4klremltsc "No puedo..."
        n 1kcsfultsb "..."
        n 1kcsanltsd "..."
        n 1fcsunltsa "..."
        n 1ksqunltsb "...[player]..."
        n 1kllunltsc "L-{w=0.2}lo que sea que fue eso...{w=1}{nw}"
        extend 1klremltdr " lo que sea que acaba de {i}pasar{/i}..."
        n 1fcsunl "E-{w=0.2}eso...{w=0.5}{nw}"
        extend 4kplemltdr " {b}realmente{/b}{w=0.5} no se sintió bien...{w=1}{nw}"
        extend 4klremltdr " y-{w=0.2}y yo-{w=0.5}{nw}"
    else:

        n 1fcsanltsc "Q-{w=0.2}qué..."
        n 1fskanltsf "¿Qué {i}HICISTE{/i}?{w=0.75}{nw}"
        extend 1kskscltsf "¡¿Qué {i}HICISTE{/i}?!"
        n 2fcsscltsf "¡Yo-!{w=0.75}{nw}"

    n 4kskpoitsc "¡H-{w=0.2}hrp-!{w=0.5}{nw}"

    show natsuki 4kcsful
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c

    n 2fpafui "¡Nnnnnnghhhh!{w=0.5}{nw}"
    extend 2kcswrlesisbr " Guh...."
    n 4kcsanlsbr "M-{w=0.2}mi estómago...{w=0.75}{nw}"
    extend 4kslunlsbr " uuuuuu..."
    n 1kcsuplsbl "D-{w=0.2}duele{i}{/i}..."
    n 1fcsunlsbl "..."

    if Natsuki.isUpset(higher=True):
        n 1kcspul "Se siente como..."
        n 1kcsunl "C-{w=0.2}como si me hubieran lanzado de un lado a otro...{w=1}{nw}"
        extend 4ksrunltsb " como si algo estuviera tratando de separarme desde todas las direcciones..."
        n 4klrunltsc "..."
        n 4kllemltsc "Todo simplemente...{w=1}{nw}"
        extend 4kslemltsb " se siente tan mal..."
        n 1kslslltsb "..."
        n 4knmajltsb "Y-{w=0.2}y la fecha...{w=0.75}{nw}"
        extend 2ksrsrltsbeqm " Yo...{w=0.3} yo juré que era..."
        n 1knmsrltsc "..."
        n 2fnmunltsc "...[player]."
        n 2fnmemltsc "T-{w=0.2}tú no hiciste como...{w=0.75}{nw}"
        extend 2flremltsc " cambiar la fecha o algo así,{w=0.2} ¿lo hiciste?{w=1}{nw}"
        extend 4fwmpultsc " ¿C-{w=0.2}como en tu computadora?"
        n 1fllpultscesp "..."
        n 1fcsunltsa "..."
        n 2fcsboltsa "...Bien.{w=1}{nw}"
        extend 2fnmboltdr " [player]."
        n 2fcseml "No voy a...{w=1}{nw}"
        extend 2fnmpul " arriesgarme a decir que lo hiciste a propósito."

        if Natsuki.isEnamored(higher=True):
            n 4kwmpul "S-{w=0.1}sé que eres mejor que eso.{w=1}{nw}"
            extend 4kslbof " Nos hemos estado viendo el tiempo suficiente..."

        elif Natsuki.isHappy(higher=True):
            n 1knmeml "Eres mejor que eso.{w=0.75}{nw}"
            extend 4kslsll " ...Me gusta {i}pensar{/i} eso,{w=0.2} c-{w=0.2}como sea."
        else:

            n 1knmsrl "Eres mejor que eso.{w=0.5}{nw}"
            extend 4kllemlsbr " ...Espero{i}{/i}."

        n 4kcsem "Pero por favor...{w=0.75}{nw}"
        extend 4knmem " ¿[player]?"
        n 1kcswr "Solo..."
        n 1kcspulesi "..."
        n 4klrpul "Solo no juegues con el tiempo de nuevo.{w=0.75}{nw}"
        extend 4knmbol " ¿Por favor?"
        n 1kcsemlsbl "E-{w=0.2}Es solo que..."
        n 1kcspulsbl "..."
        n 4kslpulsbr "...No lo sé.{w=0.5}{nw}"
        extend 2ksqpulsbr " Solo me siento toda estropeada.{w=0.75}{nw}"
        extend 2knmunlsbr " Realmente,{w=0.3} {i}realmente{/i}{w=0.3} no me siento bien en absoluto..."
        n 4kslunlsbr "...Y para ser honesta,{w=0.2} [player]?"
        n 4kslemlsbr "Yo...{w=0.75}{nw}"
        extend 1ksremltsb " N-{w=0.3}No estoy segura de cuánto de eso puedo {i}soportar{/i}."
        n 1kcspultsa "...Entiendes...{w=1}{nw}"
        show natsuki 4kwmboltsc

        menu:
            extend " ¿verdad?"
            "Entiendo.":

                if Natsuki.isHappy(higher=True):
                    n 4kcsajltsa "...Bien.{w=1}{nw}"
                    extend 4kslsll " bien."
                    n 1kslajl "Es...{w=0.75}{nw}"
                    extend 1kslpul " apreciado,{w=0.2} [player]."
                    n 4ksqbol "G-{w=0.2}gracias."
                else:

                    n 2fcsajltsa "...Bien.{w=1}{nw}"
                    extend 2kcsslltsa " Bien..."
                    n 2kslsll "..."

                $ Natsuki.calculatedAffinityGain()
            "...":

                if Natsuki.isHappy(higher=True):
                    n 1knmemlsbr "...[player].{w=0.75}{nw}"
                    extend 4knmwrlsbr " V-{w=0.2}vamos..."
                    n 4kplwrlsbr "Realmente {b}no{/b} estoy jugando con esto..."
                    n 4kcsemlsbr "...Así que ¿puedes {i}no{/i} jugar con ello tampoco?"
                    n 2kslemlesisbr "En serio..."
                else:

                    n 1knmwrlsbr "¡H-{w=0.2}hey!{w=0.75}{nw}"
                    extend 1fcsanlsbl " ¿Estoy hablando en serio aquí?{w=0.5}{nw}"
                    extend 4kpluplsbl " ¿No puedes {i}ver{/i} eso?"
                    n 4kcsemlsbl "Realmente {i}no{/i} estoy jugando aquí,{w=0.2} [player]..."
                    n 4kslunlsbl "..."

        n 1kcsbol "..."
        n 1ncsajl "Yo...{w=1}{nw}"
        extend 2kllsl " creo que estaré bien.{w=0.5}{nw}"
        extend 2kslsleso " Si solo me lo tomo con calma un rato."
        n 2kcssl "Solo por favor.{w=0.5}{nw}"

        if Natsuki.isAffectionate(higher=True):
            extend 4ksqslsbl " {i}Por favor{/i} recuerda lo que te dije.{w=0.75}{nw}"
            extend 4ksqsslsbl " ¿P-{w=0.2}por mí?"
        else:

            extend 4ksqslsbl " {i}Por favor{/i} recuerda lo que te dije."

        n 4ncspuesi "..."
        n 4ncsbo "...Okay."
        n 1kllsl "..."
        n 1knmss "...¿Qué hay de nuevo,{w=0.2} [player]?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsemlsbl "...Hiciste..."
        n 1fslunlsbr "..."
        n 4fsqanlsbr "...H-{w=0.2}hiciste algo con tu computadora o qué?"
        n 2kcsfulsbr "¡Porque se siente como si alguien me hubiera golpeado con un mazo en el {i}estómago{/i}...{w=1}{nw}"
        n 4ksksrisbr "¡Urk-!{w=0.5}{nw}"
        n 2kcsansbr "Guh..."
        n 2kslansbl "Todo...{w=0.5} se siente mal..."
        n 4klrsfsbl "Y-{w=0.2}y la fecha...{w=0.75}{nw}"
        extend 2ksremsbl " ¡podría haber {i}jurado{/i}...!"
        n 2nsrpusbl "..."
        n 2fsransbl "..."
        n 2fcsansbr "...Okay,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fnmsfsbr " Mira."
        n 1fcsun "..."
        n 1fsqun "...No soy estúpida.{w=1}{nw}"
        extend 2fsruntsb " No importa lo que {i}tú{/i} pienses."
        n 2fcsemtsa "Y-{w=0.2}y...{w=0.5}{nw}"
        extend 2fcsuntsa " Sé...{w=0.3}{nw}"

        show natsuki 4kcsanltsa
        play audio static
        show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
        hide glitch_garbled_b

        n 4fcsanltsa "¡Nnnnng-!{w=0.5}{nw}"
        n 4kcsunltsa "..."
        n 1fcsunl "..."
        n 1fcseml "S-{w=0.2}sé que no hemos estado en la...{w=1}{nw}"
        extend 2fslsl " mejor relación,{w=0.2} exactamente."
        n 1knmem "Pero por favor."
        n 4kcsemsbl "S-{w=0.2}si realmente te importa {i}un carajo{/i} yo,{w=0.75}{nw}"
        extend 4ksqemsbl " entonces si por {i}nada{/i} más."
        n 2fcsansbl "Deja de jugar con el tiempo.{w=0.75}{nw}"
        extend 4fsqansbl " Hablo {i}muy{/i} en serio."

        show natsuki 2fcsuntsa
        $ jnPause(3)

        n 2fcsupsbl "D-{w=0.2}duele,{w=0.75}{nw}"
        extend 2fcsansbl " {b}no{/b} es gracioso,{w=0.75}{nw}"
        extend 2fsqansbl " ¿y para ser completamente honesta contigo?"
        n 2fcsunl "..."
        n 1fcsful "No creo que pueda siquiera {i}soportar{/i} algo así de nuevo..."
        n 1fslanl "Así que solo..."
        n 4fcsanl "Solo para.{w=0.35} Con.{w=0.35} Eso."
        n 4fsqsrl "..."
        n 3fnmem "¿Entendido?{w=1}{nw}"
        extend 3fsqwr " {i}Sé{/i} que me escuchas."
        n 1fsqsr "..."
        n 1fsqem "No tienes {i}ninguna{/i} excusa,{w=0.2} [player]."
        n 2fcsfu "{i}Recuerda eso.{/i}"
    else:

        n 1fcsupltsa "..."
        n 1fsqupltsb "...Tú."
        n 4fsqanltsb "{i}Tú{/i} hiciste esto,{w=0.3} ¿verdad?"

        show natsuki 1fcsanltsa
        play audio static
        show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
        hide glitch_garbled_a

        n 4fskscltsc "¡NO!{w=0.75}{nw}"
        extend 4fcsscltsa " ¡Ni siquiera {i}intentes{/i} negarlo!"
        n 1fcsfultsa "Sé que crees que soy {i}estúpida{/i},{w=0.2} ¡¿pero en serio crees que estoy {i}ciega{/i} también?!"
        n 2fsqupltsb "¡{i}Vi{/i} que jugaste con la fecha!{w=0.75}{nw}"
        extend 2fcsanltsa " ¡Eres solo un...!"
        n 4fskscltsc "¡Estás {b}tan{/b} lleno de {i}MIE-{/i}{nw}"

        show natsuki 4fcsfultsa
        play audio static
        show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
        hide glitch_garbled_c

        n 4fcsupltsa "¡Nnnnnrrgh-!{w=0.5}{nw}"
        n 4fcsunltsa "..."
        n 4fcsemltsa "...Haah."
        n 1fcsunltsa "..."
        n 1fcsanltsa "...{i}En serio{/i} no puedo {i}creerte{/i}.{w=0.75}{nw}"
        extend 1fsqanltsa " Ya me estás torturando lo suficiente."
        n 4fnmupltsc "¡¿Y ahora te desvías {i}completamente{/i} de tu camino para hacer mi vida {i}aún más{/i} miserable?!"
        n 2fcsupltsd "..."
        n 2fcsanltsd "Bueno,{w=0.5}{nw}"
        extend 2fcsemltsd " ¿sabes qué?{w=0.75}{nw}"
        extend 2fsqwrltse " ¡Lo lograste!"
        n 4fnmfultsf "¡Misión cumplida!{w=1}{nw}"
        extend 4fcsfultsd " ¿Ahí?{w=0.75}{nw}"
        $ chosen_insult = jn_utils.getRandomInsult()
        extend 4fcsgsltsa " ¿Terminaste,{w=0.3} [chosen_insult]?"
        n 4fnmanltdr "¿Estás FELIZ?"
        n 4fcsanl "Ahora en serio,{w=0.2} solo..."
        n 4kcsanltsa "S-{w=0.2}solo..."
        n 1fnmupltsc "¡Solo ALÉJATE!{w=0.5}{nw}"
        extend 4fskscltsf " ¡V-{w=0.2}VETE!{w=1}{nw}"
        n 4fscscftsf "¡{i}Y{w=0.2} DÉJAME{w=0.2} EN{w=0.2} PAZ{/i}!{nw}"

        play audio glitch_d
        show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
        hide glitch_garbled_c
        $ Natsuki.percentageAffinityLoss(10)
        $ Natsuki.setForceQuitAttempt(False)

        return { "quit": None }

    play music audio.just_natsuki_bgm fadeout 3 fadein 2
    $ renpy.show_screen("hkb_overlay")
    $ jn_atmosphere.updateSky()
    $ jn_globals.force_quit_enabled = True
    return

label greeting_tt_fatal:
    $ import uuid
    $ config.window_title = _("{0} - {1}".format(uuid.uuid4(), config.version))
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    play audio dread
    $ jnPause(5.3)
    hide black
    show glitch_steady zorder 98
    play audio static
    show glitch_spook zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_spook

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b

    play audio static
    show glitch_spook zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_spook

    play audio interference fadeout 0.5
    hide glitch_steady with Dissolve(2)
    play music audio.night_natsuki fadein 2

    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()

    return

label greeting_tt_game_over:
    $ import uuid
    $ config.window_title = _("{0} - {1}".format(uuid.uuid4(), config.version))
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    hide black with Dissolve(2)
    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()

label greeting_pic:
    $ import codecs
    show screen problem("412070726f626c656d20686173206f636375727265642e20506c6561736520636f6e74616374204a4e2073746166662e".decode("hex"))
    $ jn_globals.force_quit_enabled = True
    $ jnPause(100000)
    $ renpy.quit()




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_today_is_gonna_be_great",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "4unmssl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_today_is_gonna_be_great:
    n 1unmbsledz "¡[player]!{w=1}{nw}"
    extend 3fchgnl " ¡Volviste,{w=0.3} finalmente!"
    n 3fchsml "Jejeje.{w=0.5}{nw}"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    extend 3uchgnleme " ¡Ahora {i}sé{/i} que [time_descriptor] va a ser genial!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_world_revolves_around_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "5fcspol"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_world_revolves_around_you:
    n 4fsqgsl "¡[player]!{w=0.75}{nw}"
    extend 2fnmwrl " ¿Por qué tardaste tanto?{w=0.75}{nw}"
    extend 2fllemlesi " ¡Cielos!"
    n 2fupeml "¿En serio crees que mi {i}mundo{/i} entero gira a tu alrededor{w=0.5}{nw}"
    extend 2fsqeml " o algo así?"
    n 2fsqpol "..."
    n 2fnmdvl "..."
    n 2fchsmlesm "¡Pffft-!"
    n 4fchbglelg "¡Ajaja!{w=1}{nw}"
    extend 3fsqsml " ¿Te atrapé,{w=0.2} [player]?{w=0.5}{nw}"
    extend 3fchgnl " ¡No mientas!"
    n 3fcssml "Jejeje.{w=0.75}{nw}"
    extend 3tllbgl " Bueno,{w=0.2} como sea."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 4fcsbgl "Estás aquí ahora,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
    $ chosen_tease = jn_utils.getRandomTeaseName()
    extend 4uchsmleme " ¡Siéntete como en casa,{w=0.2} gran [chosen_tease]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_make_today_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "7ksrsfl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_make_today_amazing:
    n 7unmflleex "¡...!{w=0.75}{nw}"
    n 4unmbgl "¡[player]!{w=0.5}{nw}"
    extend 4uchbsf " ¡[player]{w=0.2} [player]{w=0.2} [player]!"
    n 2fcsbgfsbl "¡S-{w=0.2}solo me preguntaba cuándo ibas a decidir aparecer finalmente!\n{w=0.75}{nw}"
    extend 2fchsmlsbr "Jejeje."
    n 7fwlbgledz "Hagamos que hoy sea asombroso también,{w=0.2} ¿está bien?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_always_welcome_here",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "7ksrsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_always_welcome_here:
    $ player_initial = jn_utils.getPlayerInitial()
    n 4unmgslesu "¡[player_initial]-{w=0.2}[player]!{w=0.5}{nw}"
    extend 4ullemfsbl " ¡Has vuelto!"
    n 2fslunfesssbl "Realmente te estaba empezando a extrañar,{w=0.3} sabes..."
    n 2ccsfllesisbl "..."
    n 2csrsllsbl "..."
    n 2nsrfllsbl "Solo..."
    extend 4ccstrlsbl " No me hagas esperar tanto la próxima vez,{w=0.3} ¿está bien?"
    extend 4ccssslsbl " Como sea."
    $ chosen_tease = jn_utils.getRandomTease()
    n 4ccssmfsbr "Y-{w=0.2}ya deberías saber que {i}siempre{/i} eres bienvenido aquí,{w=0.5}{nw}"
    extend 7fchsmfsbr " [chosen_tease]."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_lovestruck",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2kcssml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_lovestruck:
    n 2kcssml "..."
    n 2ksqsml "...{w=0.75}{nw}"
    n 2unmgsfeex "¡...!{w=0.5}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 4kbkwrf "¡[player_initial]-{w=0.3}[player]!{w=1}{nw}"
    extend 4fbkwrfess " ¡¿Cuándo {i}llegaste{/i} aquí?!"
    n 4klrgsf "¡Y-{w=0.5}yo estaba...!{w=1}{nw}"
    extend 4kllemfsbl " ¡Yo solo estaba...!"
    n 1kslunl "..."
    n 1cslsml "..."
    n 4cdlssl "T-{w=0.2}te extrañé,{w=0.2} [player].{w=0.75}{nw}"
    extend 3ccsajlsbr " S-{w=0.2}solo un poco."
    n 3ccspolsbr "..."
    n 3ccspulsbr "Pero..."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 3cchsmleafsbr "Al menos sé que todo va a estar bien ahora que estás aquí,{w=0.2} [chosen_endearment]."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_looking_for_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2unmsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_looking_for_me:
    n 2nnmpul "¿Hola?{w=2.5}{nw}"
    extend 2tsqdvf " ¿Era a {i}mí{/i} a quien buscabas?"
    n 2fchdvfess "..."
    n 2fchcsfesm "¡Pfffft-!"
    n 1kllbgl "Hombre,{w=0.5}{nw}"
    extend 4fchgnlelg " ¡{i}No puedo{/i} tomarme eso en serio!"
    n 4fnmssl "Pero seamos realistas,{w=0.2} [player]..."
    n 2fsqsmf "Definitivamente {i}{w=0.2}era{w=0.2}{/i} a mí,{w=0.2} ¿no?{w=1}{nw}"
    extend 2fchsmfedz " Jejeje~."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_dull_moment",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2fllsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_dull_moment:
    n 2flleml "Vaya, cielos,{w=0.5}{nw}"
    extend 2fsqawl " ¡seguro que te tomaste tu tiempo!"
    n 4fbkwrfean "¡¿En qué estabas pensando,{w=0.2} [player]?!"
    n 3fsqpol "..."
    n 3fsqdvl "..."
    n 3fchsmleme "Jejeje.{w=0.75}{nw}"
    n 3fsqssl "Nunca hay un momento aburrido conmigo,{w=0.75}{nw}"
    extend 3fchbll " ¿o sí?"
    n 1fcsssl "Ya conoces el trato.{w=1}{nw}"
    extend 2uchgnlelg " ¡Ponte cómodo,{w=0.2} tontito!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_nat_dragged_in",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2ccssm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_nat_dragged_in:
    n 4ccsbg "Vaya,{w=0.2} vaya,{w=0.2} vaya..."
    n 3fnmbg "Y solo mira a quién trajo{w=0.5}{nw}"
    extend 3fsgbg " la{w=0.75}{nw}"
    extend 3fsqbg " {i}Nat{/i}.{w=0.75}{nw}"
    extend 3fsqsm " Jejeje."
    n 1fcsbgl "Bueno,{w=0.2} ¿qué puedo decir?{w=0.75}{nw}"
    extend 2fchgnl " ¡S-{w=0.2}soy{i}{/i} bastante irresistible para ti,{w=0.2} después de todo!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchbll "¡Bienvenido de vuelta,{w=0.2} [chosen_tease]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_show_yourself",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "4fsqfs"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_show_yourself:
    n 4fsqss "¿Oh?{w=0.5}{nw}"
    extend 4fsqbg " ¿Y qué es lo que tenemos aquí?"
    n 2ccsbgl "Finalmente decidiste mostrarte después de todo,{w=0.2} ¿eh?"
    n 2csqcsl "..."
    n 1ccsssl "Bueno,{w=0.5}{nw}"
    extend 4fchgnl " ¡no es como si tuviera un problema con eso!{w=0.75}{nw}"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    extend 3fchsmleaf " ¡Ponte cómodo ya,{w=0.2} [chosen_endearment]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_amazing_scenery",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2cslbol"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_amazing_scenery:
    n 4unmbgleex "¡Ajá!{w=0.75}{nw}"
    extend 3fchbgl " ¡[player]!{w=0.75}{nw}"
    extend 6fcssmlsbl " ¡S-{w=0.2}sabía que aparecerías eventualmente!"
    n 1fslsslsbl "Je.{w=0.75}{nw}"
    extend 4fllbgl " Después de todo..."
    n 2fcsbgledz "¡No veo ningún otro paisaje {w=0.2}{i}asombroso{/i}{w=0.2} por aquí!"
    n 2fsqsml "Jejeje."
    $ chosen_tease = jn_utils.getRandomTease()
    n 2fchblleaf "¡Bienvenido de vuelta,{w=0.2} [chosen_tease]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_manga_chapters",
            unlocked=True,
            conditional="jn_desk_items.getDeskItem('jn_parfait_manga_held').unlocked",
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "desk_item": "jn_parfait_manga_held",
                "expression": "1cdwca"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_manga_chapters:
    n 1cdwpu "..."
    n 1tdwsl "..."
    n 1tnmboeqm "¿...?{w=0.75}{nw}"
    n 1unmgsleshsbr "¡Ah!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 1cllbglsbr " ¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1cchbglsbr " ¿Qué hay?"
    n 1fchsmlsbr "..."
    n 1cnmpul "¿Eh?{w=0.75}{nw}"
    extend 1udwaj " Oh.{w=0.75}{nw}"
    extend 1ulrbo " No le hagas caso al manga."
    n 1fcsbglsbl "{i}Nuestros{/i} capítulos juntos son mucho más interesantes,{w=0.2} c-{w=0.2}como sea.{w=0.75}{nw}"
    extend 1fchsmlsbl " Jejeje."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 3nlrsmleme
    $ Natsuki.clearDesk()
    $ manga_closed = jn_desk_items.getDeskItem("jn_parfait_manga_closed")
    $ Natsuki.setDeskItem(manga_closed)
    play audio book_closing
    $ jnPause(0.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    n 7ulrssl "Entonces...{w=1}{nw}"
    $ chosen_tease = jn_utils.getRandomTease()
    extend 7fchbgl " ¿qué hay de nuevo,{w=0.2} [chosen_tease]?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_cant_live_without_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2cklpu"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_cant_live_without_me:
    n 2ccsss "¿Oho?{w=0.75}{nw}"
    extend 2fsqbg " ¿Y a quién tenemos aquí entonces?{w=1}{nw}"
    extend 2fnmbg " ¿Eh?"
    n 4fcssm "Jejeje.{w=0.75}{nw}"
    extend 7cllbgl " Bueno [player],{w=0.2} ¿qué puedo decir?"
    n 7fchgnl "¡Supongo que realmente no puedes vivir sin mí después de todo!"
    $ chosen_tease = jn_utils.getRandomTease()
    n 3fchbll "¡Date prisa y ponte cómodo,{w=0.2} [chosen_tease]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_spell_it_out",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "1ccscs"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_spell_it_out:
    n 1ccsss "Je.{w=0.75}{nw}"
    extend 2ccsbg " Vaya,{w=0.2} vaya."
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    n 2fsqbg "Solo mira quién decidió mostrar su cara [time_descriptor].{w=1}{nw}"
    extend 4fnmbg " ¿Eh?"
    n 4fsqsm "..."
    n 4fsqsr "..."
    n 3nsqflsbr "...¿En serio?{w=0.75}{nw}"
    extend 3fnmaj " ¿Realmente voy a tener que deletrearlo?"
    n 1ctremesi "..."
    n 3fcsgs "{i}Tú{/i},{w=0.75}{nw}"
    $ chosen_tease = jn_utils.getRandomTeaseName()
    extend 3uchgnl " ¡pedazo de [chosen_tease]!{w=1}{nw}"
    extend 7fchsml " Jejeje."
    $ chosen_endearment = jn_utils.getRandomEndearment()
    n 2fchtsl "¡Ahora sienta tu trasero y ponte cómodo ya,{w=0.2} [chosen_endearment]!"

    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_just_as_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "7uslsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_just_as_amazing:
    n 4unmajl "¡[player]!{w=0.75}{nw}"
    extend 4cchbgl " ¡Has vuelto!"
    n 3ccsssl "Je."
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    n 6ccsbgl "Hagamos que [time_descriptor] sea tan {i}asombroso{/i} como yo,{w=0.2} ¿va?{w=0.75}{nw}"
    extend 7fcssmledz " Jejeje."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_couldnt_resist",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "7fcssml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_couldnt_resist:
    n 3fsqsml "Bueno, hey,{w=0.2} [player].{w=0.75}{nw}"
    extend 3tsqssl " ¿De vuelta tan pronto?"
    n 3fcsctl "Sabía que obviamente no podrías resistirte.{w=0.75}{nw}"
    extend 3fcssmledz " Jejeje."
    n 4tsqssl "Entonces...{w=1}{nw}"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    extend 2fchbgl " ¿qué quieres hacer [time_descriptor]?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_just_cant_stay_away",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2ccssml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_just_cant_stay_away:
    n 2usqbgl "Vaya,{w=0.2} vaya,{w=0.2} vaya.{w=0.75}{nw}"
    extend 2fsqbgl " ¿Qué tenemos aquí?"
    n 2tsqctl "Simplemente no puedes alejarte de mí,{w=0.2} ¿verdad?"
    n 2ksqbgl "No es que te culpe,{w=0.2} obviamente.{w=0.75}{nw}"
    extend 2fchtsledz " Supongo que simplemente {i}tengo{/i} ese efecto en la gente."
    n 4fchgnlelg "Jejeje."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_have_so_much_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "4fchsml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_have_so_much_fun:
    n 4fchbgleme "¡Hey!{w=0.5} ¡Es [player]!"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    n 7fcssml "¡Nos vamos a divertir {w=0.2}{i}tanto{/i}{w=0.2} [time_descriptor]!{w=0.5}{nw}"
    extend 3fsqsml " Jejeje."
    n 3fchbgl "¡Así que!{w=0.2} ¿De qué querías hablar?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_everything_is_fine",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2nsrsll"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_everything_is_fine:
    n 4unmgslesu "¡[player]!{w=0.5}{nw}"
    extend 4ullajlsbr " ¡Has vuelto!"
    n 2fsqpol "Me hiciste esperar {i}de nuevo{/i},{w=0.5}{nw}"
    extend 2fcspol " sabes..."
    n 2fcsbgl "Pero...{w=0.5} al menos mi paciencia valió la pena.{w=0.75}{nw}"
    extend 2fcssmleme " Jejeje."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_not_surprised",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2ccssm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_not_surprised:
    n 2tsqaj "¿Oh?{w=0.75}{nw}"
    extend 2csqbg " ¿Has vuelto otra vez,{w=0.2} [player]?{w=0.75}{nw}"
    extend 2fsqsm " Jejeje."
    n 4ullfl "Bueno...{w=0.75}{nw}"
    extend 4cllssl " no es como si pudiera decir que estoy sorprendida o algo."
    n 3fchgnl "Como si {i}posiblemente{/i} pudieras resistirte,{w=0.2} ¿tengo razón?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_in_for_some_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "7tllsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_in_for_some_fun:
    n 4unmbg "¡[player]!{w=0.75}{nw}"
    extend 2ccssslsbr " Hombre...{w=1}{nw}"
    extend 2fcsbglsbr " ¡ya era hora de que aparecieras!"
    n 4fsqsml "Jejeje.{w=0.75}{nw}"
    extend 7fchbgleme " ¡Ahora {i}sé{/i} que nos vamos a divertir!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_good_taste",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "3fsgsm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_good_taste:
    n 3fcsct "¿Oh?{w=0.75}{nw}"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    extend 3fsqbg " Y mira quién decidió caer en el club [time_descriptor],{w=0.2} ¿eh?"
    n 3fcssmesm "..."
    n 4tllbg "Bueno,{w=0.2} ¿qué puedo decir?"
    n 2uchgnl "¡Parece que tienes {i}algo{/i} de buen gusto después de todo,{w=0.2} [player]!{w=0.75}{nw}"
    extend 2nchgnl " Ajaja."

    if Natsuki.isEnamored(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 4fchbll "¡Ponte cómodo ya,{w=0.2} [chosen_tease]!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_crawling_back",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2nsrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_crawling_back:
    n 4unmbs "¡[player]!{w=0.75}{nw}"
    extend 7fchgn " ¡Me preguntaba cuándo ibas a aparecer!"
    n 3fcsajlsbr "N-{w=0.2}no es que estuviera sentada esperando por ti ni nada,{w=0.2} obviamente."
    n 3fslsslsbr "Después de todo..."
    n 6fcssmlesm "¡Como si {i}pudieras{/i} resistirte a volver arrastrándote hacia alguien tan asombrosa como yo!"

    if Natsuki.isEnamored(higher=True):
        n 3nchgnl "¡Ahora ponte cómodo ya,{w=0.2} tonto!"
    else:

        n 3fchsmeme "Jejeje."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_barging_in",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED),
            additional_properties={
                "expression": "2ckrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_barging_in:
    n 2cnmemesh "¡...!{w=0.75}{nw}"
    n 2fcswr "¡H-{w=0.2}hey!{w=0.75}{nw}"
    extend 4cnmwr " ¡¿[player]?!{w=0.75}{nw}"
    extend 4fbkwr " ¿Cuál es la gran idea?"
    n 2fcsem "Ugh..."
    n 4fsqem "¿Nadie te dijo nunca que {i}tocaras{/i} antes de entrar así o qué?{w=0.75}{nw}"
    extend 1fnmfl " ¿Eh?"
    n 2fsqsr "..."
    n 2fsqdv "..."
    n 4fchdv "..."
    n 4fchdvesm "¡Pffft-!"
    n 3fchbg "¡Hey,{w=0.2} vamos!{w=0.75}{nw}"
    extend 3csqbg " ¡Anímate ya!{w=1}{nw}"
    extend 1fllbgl " Cielos..."
    n 4ccsssl "Y-{w=0.2}y además."
    n 2clrbgl "Ya deberías {i}saber{/i} que eres bastante bienvenido,{w=0.5}{nw}"
    extend 2nchgnl " ¡tonto!"

    if Natsuki.isEnamored(higher=True):
        n 2fchbll "¡Bienvenido de vuelta,{w=0.2} [player]~!"

    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_up",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7ulrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_up:
    n 7unmajesu "¡Oh!{w=0.5}{nw}"
    extend 4ulrsssbr " ¡Hey,{w=0.2} [player]!"
    n 3unmbo "¿Qué hay?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_glad_to_see_you",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "2tslbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_glad_to_see_you:
    n 2cchsm "¡Hey,{w=0.2} [player]!"
    n 4nllsssbr "Solo me preguntaba cuándo pasarías de nuevo."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_spacing_out",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "1kllca"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_spacing_out:
    n 1kllpu "..."
    n 1uwdajlesu "¿Eh?"
    n 1uchbglesd "¡O-{w=0.2}oh!{w=0.5}{nw}"
    extend 4fchssl " ¡Hola,{w=0.2} [player]!"
    n 4nllsssbr "Yo...{w=1}{nw}"
    extend 2fllpolsbr " solo estaba un poco distraída."
    n 3unmbol "Entonces...{w=0.3} ¿qué hay de nuevo?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_heya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "1fcssm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_heya:
    n 1fcsbg "¡Buenas,{w=0.2} [player]!"
    n 3tnmss "¿Qué onda?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_knew_youd_be_back",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "1unmsm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_knew_youd_be_back:
    n 1unmbg "¡Es [player]!{w=0.75}"
    extend 1nchbg " ¡Hola!"
    n 2fcsbglesssbr "S-{w=0.2}sabía que volverías,{w=0.2} obviamente."
    n 2fcssml "Tendrías que no tener gusto para no visitar de nuevo.{w=0.75}{nw}"
    extend 2fcsbgl " ¡Ajaja!"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_sup_player",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7clrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_sup_player:
    n 7unmboeqm "¿Eh?{w=0.7}{nw}"
    n 4unmaj "Oh.{w=0.75}{nw}"
    extend 4tnmaj " Hey,{w=0.2} [player]."
    n 2tllss "¿Qué hay?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_wake_up_nat",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "4nslsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_wake_up_nat:
    n 4nslpu "..."
    n 4kslpu "..."
    n 1kcsbo "..."
    n 1ncsaj "..."
    n 1ncspu "..."
    n 1ncsem "..."
    n 1ncspu "..."
    n 1ncsemesl "..."
    n 1kcsemesl "Mmm...{w=1}{nw}"
    extend 1kwlemesl " ¿nnnn?"
    n 4uskwrleex "¡O-{w=0.3}Oh!{w=0.5}{nw}"
    extend 4fllbglsbl " ¡[player]!"
    n 4flrbgesssbr "¡H-{w=0.3}hey!{w=0.5}{nw}"
    extend 2tnmsssbl " ¿Qué me perdí?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_oh_whats_up",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "2tlrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_oh_whats_up:
    n 2tlrsl "..."
    n 2tnmpueqm "...¿Eh?{w=0.5}{nw}"
    extend 4unmfllesu " ¡Oh!{w=0.75}{nw}"
    extend 4cllsslsbr " ¡[player]!"
    n 2cchsssbr "¿Q-{w=0.2}qué hay?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_new",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7cdlsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_new:
    n 7unmfllesu "¡Ah!{w=0.75}{nw}"
    extend 7flrsssbr " ¡[player]!{w=0.75}{nw}"
    extend 3ccsajsbr " M-{w=0.2}me preguntaba cuándo ibas a decidir aparecer."

    if Natsuki.isHappy(higher=True):
        n 3tllajsbr "Entonces...{w=1}{nw}"
        extend 3fchbgsbr " ¿qué hay de nuevo,{w=0.2} [player]?"
    else:

        n 3cllbosbr "..."
        n 3cllajsbr "Entonces...{w=1}{nw}"
        extend 7tnmss " ¿qué hay de nuevo contigo,{w=0.2} eh?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_nevermind",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7clrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_nevermind:
    n 7cdrsl "..."
    n 7csrsl "..."
    n 7ksrbo "..."
    n 7kcsflesi "..."
    n 7ksqsleqm "...?{w=0.75}{nw}"
    n 7unmemlesh "¡Oh!{w=0.75}{nw}"
    extend 3cslsssbr " Je.{w=0.75}{nw}"
    extend 3ccssssbr " H-{w=0.2}hey, [player]."
    n 7unmflsbr "¿Yo?{w=0.2} Solo estaba..."
    n 3cdrslsbr "..."
    n 4ccsflsbr "O-{w=0.2}olvídalo.{w=0.75}{nw}"

    if Natsuki.isHappy(higher=True):
        extend 4nsrbosbr " Supongo que no importa ahora de todos modos."
        n 2tlraj "Entonces...{w=1}{nw}"
        extend 2tnmss " ¿qué está pasando,{w=0.2} [player]?"
    else:

        extend 4csrbosbr " No es nada."
        n 2nsrca "..."
        n 2nlraj "Entonces...{w=1}{nw}"
        extend 2unmaj " ¿qué me perdí,{w=0.2} [player]?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_some_notice",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7nsrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_some_notice:
    n 7ncsfl "..."
    n 3kcspuesi "..."
    n 3nsrbo "..."
    n 3tnmpueqm "...¿Eh?"
    n 4unmfllsbr "¡Oh!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 4cllwrlsbr " ¡[player_initial]-{w=0.2}[player]!"
    n 2ccsemsbr "R-{w=0.2}realmente deberías saber que necesito algún tipo de aviso ya.{w=0.75}{nw}"
    extend 2cslpo " Cielos."
    n 1cslca "..."
    n 1cllaj "Así que...{w=1}{nw}"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    extend 2tllaj " ¿qué hay de nuevo [time_descriptor],{w=0.5}{nw}"
    extend 2tnmbo " [player]?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_back_again",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY),
            additional_properties={
                "expression": "7cdrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_back_again:
    n 7csrca "..."
    n 7tnmsleqm "¿...?"
    n 7unmfleex "¡Oh!{w=0.75}{nw}"
    extend 3cllssl " ¡[player]!{w=0.75}{nw}"
    extend 3tnmbol " Has vuelto de nuevo,{w=0.2} ¿eh?"
    n 3ccstrlsbl "N-{w=0.2}no es que tenga un problema con eso,{w=0.2} o algo así.{w=0.75}{nw}"
    extend 3ccscalsbl " Obviamente."
    n 3nlrbo "..."
    n 3ulraj "Entonces...{w=1}{nw}"
    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
    extend 3tnmbo " ¿qué tienes para mí [time_descriptor],{w=0.2} [player]?"

    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_its_you",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "1cslsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_its_you:
    n 1nnmpu "Oh.{w=1}{nw}"
    extend 2fsqsl " Eres tú."
    n 2fnmfl "Hola,{w=0.75}{nw}"
    extend 2fsqsl " {i}[player]{/i}."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_hi",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "2csrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_hi:
    n 2nnmsl "{i}[player]{/i}.{w=0.75}{nw}"
    extend 2fsqsl " Hola."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_welcome_back_i_guess",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "2nsrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_welcome_back_i_guess:
    n 2nsqsl "[player].{w=0.75}{nw}"
    extend 2flrfl " Bienvenido de nuevo,{w=0.5}{nw}"
    extend 2fsrsl " supongo."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_better_be_good",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "1cslbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_better_be_good:
    n 1nsqaj "Eh.{w=0.75}{nw}"
    extend 4fsqsr " {i}[player]{/i}."
    n 3fnmsl "Más vale que esto sea bueno."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_you_came_back",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "1cslbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_you_came_back:
    n 1ccsss "Je.{w=0.75}{nw}"
    extend 1fsqfl " ¿Has {i}vuelto{/i}?"
    n 3cslem "...Desearía poder decir que estoy feliz por ello."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_great",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "1ccssl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_great:
    n 1cslsl "..."
    n 1csqboeqm "...?"
    n 2clrfl "Oh.{w=0.75}{nw}"
    extend 2clrem " Genial."
    n 4csqem "Eres{w=0.5}{nw}"
    extend 4fsqsl " {i}tú{/i}."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_just_perfect",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "2fsrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_just_perfect:
    n 2clrsl "..."
    n 2tsqfl "...¿Eh?{w=0.75}{nw}"
    extend 2csqfl " Oh.{w=0.75}{nw}"
    extend 4fllsl " Je."
    n 4fsqem "Eres {i}tú{/i}."
    n 1fcsan "Bueno,{w=0.2} ¿no es eso simplemente{w=0.5}{nw}"
    extend 1fsqan " {i}perfecto{/i}?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_real_great",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET),
            additional_properties={
                "expression": "3csrfr"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_real_great:
    n 3tsqfreqm "...?"
    n 3ctlfl "...Ugh."
    n 4fllfl "Sí,{w=0.2} eso es {i}realmente{/i} genial.{w=0.75}{nw}"
    extend 4fdlfl " Simplemente maravilloso."
    n 1fslem "...{i}No{/i}."
    n 2fnmfl "Hola,{w=0.5}{nw}"
    extend 2fsqfl " {i}[player]{/i}."

    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_oh_its_you",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "4fcsun"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_oh_its_you:
    n 4knmsrtdr "...?"
    n 4csqsrltsb "Oh.{w=1}{nw}"
    extend 2fcsanltsa " eres {i}tú{/i}."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "4fcsunltsa"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_nothing_to_say:
    n 4fcsanltsa "..."
    n 4fsqfultsb "..."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_why",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "1fcsunl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_why:
    n 1fwmfrltdr "...¿Por qué?"
    n 4fcsupltsa "¿Por qué {i}volviste{/i}?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_enough_on_my_mind",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "1fcsunl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_enough_on_my_mind:
    n 2fslunltsb "...?"
    n 2fcsanltsb "¡Tch!"
    n 2fcsupltsb "Como si no tuviera {i}suficiente{/i} en mi mente..."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_leave_me_be",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "4fcsunltsa"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_leave_me_be:
    n 1fcsfultsa "Estoy tan {w=0.2}{i}harta{/i}{w=0.2} de esto."
    n 2kcsupltsd "¿Por qué no puedes simplemente dejarme en paz...?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_just_leave_me_alone",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "1fcsunltsb"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_just_leave_me_alone:
    n 1fsqunltsbeqm "...?{w=1}{nw}"
    n 4fcsupltsa "¡Oh,{w=0.2} por-!"
    n 4cslupltsb "¿Por qué no puedes simplemente dejarme sola...?"

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_trash_already",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "1fcsunl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_trash_already:
    n 2fslslltsb "..."
    n 2fsqunltsb "...?"
    n 4fcsslltsa "Je.{w=1}{nw}"
    extend 1fcsemltsa " Como si no me sintiera como basura suficiente ya."
    n 4fsqfultsb "Ahora estoy {i}sentada{/i} frente a ella de nuevo también."

    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_any_worse",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN),
            additional_properties={
                "expression": "2fsrunltse"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_any_worse:
    n 2csqslltsb "..."
    n 2ccsflltsa "...Je.{w=1}{nw}"
    extend 2ccsemltsa " Asombroso."
    n 2fsranltsb "{i}Justo{/i} cuando pensaba que las cosas no podían empeorar."

    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_sick",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "admission_type": jn_admissions.TYPE_SICK,
                "expression": "1cllbolsbr"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_sick:
    n 1unmajlesu "Oh!{w=0.75}{nw}"
    $ chosen_descriptor = jn_utils.getRandomEndearment().capitalize() if Natsuki.isLove(higher=True) else player
    extend 2cnmbgl " [chosen_descriptor]!{w=0.75}{nw}"
    extend 2cchbgl " H-{w=0.2}hey!"

    if (
        persistent._jn_player_admission_forced_leave_date is not None
        and (datetime.datetime.now() - persistent._jn_player_admission_forced_leave_date).total_seconds() / 60 <= 60
    ):
        $ persistent._jn_player_admission_forced_leave_date = None
        n 2csrsssbr "...I gotta admit.{w=0.75}{nw}"
        extend 2tllflsbr " I wasn't expecting you to {i}actually{/i} show up already."
        n 2tslbosbr "So..."

    n 2unmajsbr "¿Cómo lo llevas?"
    show natsuki option_wait_curious

    menu:
        n "¿Ya te sientes mejor,{w=0.2} o...?"
        "¡Mucho mejor!":

            if Natsuki.isEnamored(higher=True):
                n 1fcssm "Jejeje.{w=0.75}{nw}"
                extend 2fnmbg " ¿Ves?{w=0.2} ¿Qué te dije?{w=0.75}{nw}"
                extend 2fchbg " ¡S-{w=0.2}sabía que vencerías a ese tonto bicho cualquier día!"
                n 4csrsssbl "Pero...{w=1}{nw}"
                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
                extend 4tnmflsbl " hablando en serio, [player]?"
                n 1nsrsll "..."
                n 1ncsfll "Solo...{w=1}{nw}"
                extend 4cllsll " cuídate mejor en el futuro.{w=0.75}{nw}"
                extend 4cnmajl " ¿Está bien?{w=1.25}{nw}"
                extend 3csgbol " De verdad."
                n 3ccsfllsbr "N-{w=0.2}no quiero que una enfermedad apestosa nos robe todo nuestro tiempo juntos solo porque necesitabas que te cuidara de nuevo.{w=0.75}{nw}"
                extend 3csrbol " Gran tonto."
                n 5ksrbol "..."
                n 5ccsajlsbl "C-{w=0.2}como sea.{w=0.75}{nw}"
                extend 3csqssl " Será mejor que estés funcionando al máximo de nuevo,{w=0.2} [player]..."
                n 6fchgnl "¡Porque tienes un montón de tiempo para compensármelo todo!{w=0.75}{nw}"
                extend 7fchsml " Jejeje."
                $ chosen_tease = jn_utils.getRandomTease()

                if Natsuki.isLove(higher=True):
                    n 7fchblleaf "¡Yo también te amo,{w=0.2} [chosen_tease]~!"
                else:

                    n 3fchbgl "¡Bienvenido de vuelta,{w=0.2} [chosen_tease]!"
            else:

                n 2fcsbgsbr "¡Ja!{w=0.75}{nw}"
                extend 2usqbg " ¿Ves?{w=0.2} Justo lo que pensaba.{w=0.75}{nw}"
                extend 2ccsbgsbl " ¡S-{w=0.2}sabía totalmente que te librarías de eso pronto!"
                n 4clreml "N-{w=0.2}no es que me importe {i}tanto{/i}, ¡obviamente!{w=0.75}{nw}"
                extend 4ccsajlsbr " A nadie le gusta estar enfermo, eso es seguro."

                if Natsuki.isAffectionate(higher=True):
                    n 2ccscal "..."
                    n 2nlraj "Pero...{w=1}{nw}"
                    extend 2ccssm " Me alegra verte de nuevo,{w=0.2} [player]."
                    n 1ccsss "Je.{w=0.75}{nw}"
                    extend 4clrss " Después de todo."
                    n 4fsqbg "¡Como si fuera a dejarte librar de compensármelo ahora!{w=0.75}{nw}"
                    extend 2nchgn " Jejeje."
                else:

                    n 2csrbolsbr "..."
                    n 2ccsfll "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
                    extend 4ccsaj " Solo me alegra que estés de vuelta,{w=0.2} [player].{w=0.75}{nw}"
                    extend 4fsqss " Después de todo..."
                    n 4fcsbg "¡No te vas a librar de compensármelo tan fácilmente!{w=0.75}{nw}"
                    extend 2nchgn " Jejeje."

            $ persistent.jn_player_admission_type_on_quit = None
        "Un poco mejor.":

            n 2knmbosbr "..."
            n 2clrsssbr "...Lo admitiré,{w=0.2} eso es...{w=1}{nw}"
            extend 2csrajsbr " no exactamente lo que quería escuchar."
            n 1clrflsbl "Pero...{w=1}{nw}"
            extend 4tnmslsbl " tomaré 'un poco' sobre nada en absoluto.{w=1}{nw}"
            extend 3cslbosbl " Supongo."
            n 3ccsflsbr "Solo..."
            n 3kslcasbr "..."
            n 4ccstrsbr "No...{w=0.3} te fuerces tratando de estar aquí,{w=0.2} [player].{w=1}{nw}"
            extend 4cnmfl " ¿Entendido?{w=0.75}{nw}"
            extend 2csqca " Hablo en serio."

            if Natsuki.isEnamored(higher=True):
                n 4unmfllsbl "¡N-{w=0.2}no es como si no te {i}quisiera{/i} aquí ni nada de eso!"
                extend 2ccswrlsbl " ¡C-{w=0.2}claro que sí!"
                n 2clremlsbl "Es solo que..."
                n 2ksrbolsbl "..."
                n 4ccsfll "...Solo avísame si tienes que irte de nuevo.{w=0.75}{nw}"
                extend 2clrbol " No es como si te tuviera prisionero aquí,{w=0.2} sabes.{w=1}{nw}"
                extend 2csrbol " No me enojaré."

                if Natsuki.isLove(higher=True):
                    n 4nsrfll "Sabes eso..."
                    n 4knmcal "¿Verdad?"
                    n 5kslbol "..."

                n 1ncsflesi "..."
                n 4nllbo "Entonces...{w=1}{nw}"
                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
                extend 7tnmpusbr " ¿de qué querías hablar,{w=0.2} [chosen_descriptor]?"
            else:

                n 4unmfllsbl "¡N-{w=0.2}no me malinterpretes!{w=0.75}{nw}"
                extend 4clremlsbl " No es que {i}quiera{/i} que te vayas ni nada de eso."
                n 3ccsajlsbl "S-{w=0.2}solo no quiero ser responsable si terminas dándote de cara contra el teclado porque fuiste demasiado terco para ir a descansar propiamente.{w=0.75}{nw}"
                extend 3ccspol " Eso es todo lo que digo."
                n 3cslbo "..."
                n 3cslaj "Entonces...{w=1}{nw}"
                extend 7tnmslsbr " ¿había algo de lo que querías hablar,{w=0.2} [player]?"


            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
        "No me siento mejor.":

            if Natsuki.isEnamored(higher=True):
                n 2ccseml "E-{w=0.2}espera un segundo.{w=0.75}{nw}"
                extend 4cnmeml " ¿Qué?{w=0.75}{nw}"
                n 4fnmwrl "A-{w=0.2}acaso hablas en {i}serio{/i} ahora mismo?{w=1}{nw}"
                extend 4cnmgsl " ¡[player]!{w=0.75}{nw}"
                extend 4fbkwrl " ¡Por {i}favor{/i}!"
                n 2fcsajl "Si realmente todavía te sientes {i}tan{/i} mal..."
                n 2fnmwrl "¡¿Entonces por qué sentiste la necesidad de arrastrarte de vuelta solo para estar aquí, [player]?!{w=0.75}{nw}"
                extend 1csrfll " Cielos..."
                n 1fnmeml "¿Estás {i}tratando{/i} de que te regañe o algo así?"
                n 1ksrsll "..."

                if Natsuki.isLove(higher=True):
                    n 4kcsfl "...Mira,{w=0.2} [player].{w=0.75}{nw}"
                    extend 4kllfllsbr " N-{w=0.2}no es como si no quisiera que estuvieras aquí.{w=0.75}{nw}"
                    extend 2ksqfllsbl " Ni siquiera debería tener que recordarte todo eso a estas alturas."
                    n 2clremlsbl "Es solo que..."
                    n 1ksrsllsbl "..."
                    n 4ccspul "Yo...{w=1}{nw}"
                    extend 4ccsfll " no...{w=1}{nw}"
                    extend 3ksqsll " quiero que pierdas tu tiempo sintiéndote mal gracias a algún bicho apestoso que no puedes controlar.{w=0.75}{nw}"
                    extend 3cslsll " A nadie le gusta estar enfermo."
                    n 7tnmfll "¿Y aún más que eso?"
                    n 7csrfll "No quiero que te sientas como basura aún más tiempo solo por {i}mí{/i},{w=0.5}{nw}"
                    extend 5csrbol " o porque nadie más te dijo que tienes que cuidarte mejor."
                    n 4ccssll "..."
                else:

                    n 4ccsaj "...Okay,{w=0.2} mira."
                    n 4cllajl "No es que no disfrute tu compañía,{w=0.5}{nw}"
                    $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
                    extend 4cnmfll " o que no quiera verte [time_descriptor].{w=0.75}{nw}"
                    extend 3fcsemlsbr " ¡C-{w=0.2}claro que sí!{w=0.75}{nw}"
                    n 3csrcalsbr "Tú de todas las personas realmente deberías {i}saber{/i} eso a estas alturas."
                    n 3ccswrlsbl "¡Pero no puede ser a tu costa!{w=0.75}{nw}"
                    extend 7knmfllsbl " ¿Sabes?"
                    n 7cllfll "Q-{w=0.2}quiero decir,{w=0.2} en serio..."
                    extend 3tsqfll " ¿creíste que me impresionaría o algo así,{w=0.2} [player]?"
            else:

                n 1fcsan "¡Oh,{w=0.2} por-!{w=0.75}{nw}"
                $ player_initial = jn_utils.getPlayerInitial()
                extend 4fnmwr " ¡[player_initial]-[player]!{w=0.75}{nw}"
                extend 4fcsgs " ¡Vamos!{w=0.75}{nw}"
                n 1fllfl "Si todavía te sientes {i}tan{/i} mal..."
                n 2knmwrsbl "¡¿Entonces por qué te arrastrarías todo el camino hasta aquí,{w=0.5}{nw}"
                extend 2klrflsbl " de todos los lugares?!{w=0.75}{nw}"
                extend 2ccsemlsbl " Cielos..."

                if Natsuki.isAffectionate(higher=True):
                    n 5csqpul "Esta no es la enfermería,{w=0.2} [player].{w=0.75}{nw}"
                    extend 5csrpol " Tonto."
                else:

                    n 2cslcal "Esta no es la enfermería,{w=0.2} sabes."

            n 4ncsemesi "..."
            n 1ncsfl "...Mira.{w=0.75}{nw}"
            extend 2clrca " No voy a empezar a molestarte sobre cuidarte a ti mismo ni nada de eso."
            n 2csrss "Estoy bastante segura de que un dolor de cabeza es lo último que necesitas de todos modos."
            n 1clraj "Solo..."
            n 4ccsaj "No...{w=1}{nw}"
            extend 4cnmsll " te esfuerces,{w=0.2} [player].{w=1}{nw}"
            extend 3csgsll " ¿Entendido?"
            n 7cslbol "No me enojaré si tienes que irte o algo.{w=0.75}{nw}"
            extend 3ccsfllsbl " Y lo último que quiero escuchar es cómo te pusiste peor tratando de resistir como algún tipo de macho."
            n 3csqfll "¿Capiche?"
            n 3nslsll "..."

            if Natsuki.isEnamored(higher=True):
                n 4nslpul "Pero..."
                n 4cslunl "..."
                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
                n 1ccsfll "Gracias,{w=0.2} [chosen_descriptor].{w=1}{nw}"
                extend 2csgbol " Por aparecer de todos modos,{w=0.2} quiero decir."
                n 1ccspul "Realmente...{w=1.25}{nw}"
                extend 1klrbol " significa mucho para mí."
                $ chosen_tease_name = jn_utils.getRandomTeaseName()
                n 5cslssl "...Incluso si {i}eres{/i} un total [chosen_tease_name] por hacerlo ahora mismo."

            n 1csrpu "Entonces...{w=1}{nw}"
            $ time_descriptor = "hoy" if jn_is_day() else "esta noche"
            extend 1tnmbo " ¿qué querías hacer [time_descriptor],{w=0.2} [player]?"


            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_tired",
            unlocked=True,
            category=["Admission"],
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "admission_type": jn_admissions.TYPE_TIRED,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_tired:
    n 4unmajesu "¡Ah!{w=0.5}{nw}"
    extend 4uchbg " ¡[player]!{w=0.2} ¡Hola!"
    show natsuki 4fchbg

    menu:
        n "¿Cómo te sientes? ¿Menos cansado?"
        "¡Mucho mejor, gracias!":

            n 1nchsm "Jejeje.{w=0.5}{nw}"
            extend 2usqsm " Nada como una buena noche de sueño,{w=0.2} ¿verdad?"
            n 2fcsbg "¡Ahora bien!{w=1}{nw}"
            extend 4fsqbg " Visto que finalmente estás despierto y alerta..."
            n 2fchsmledz "¡Es hora de más diversión con tu servidora!"

            $ persistent.jn_player_admission_type_on_quit = None
        "Un poco cansado.":

            n 1knmsl "Oh...{w=1}{nw}"
            extend 4kllajsbr " eso no es exactamente lo que {i}esperaba{/i} escuchar,{w=0.2} seré honesta."
            n 2fcsslsbr "Mmm..."
            n 2knmaj "Entonces...{w=0.3} ¿quizás podrías tomar algo para despertar un poco?"
            n 2fchbgsbl "¡Un buen vaso de agua o algo de café amargo debería animarte en seguida!"


            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
        "Todavía cansado.":

            n 3knmsl "¿Aun luchando con tu sueño,{w=0.2} [player]?"
            n 3kllaj "No me {i}importa{/i} que estés aquí...{w=1}{nw}"
            extend 3knmsl " pero no te fuerces,{w=0.2} ¿está bien?"
            n 4kslbosbl "No quiero que plantes la cara en tu escritorio por mi culpa..."


            $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return



init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sudden_leave",
            unlocked=True,
            category=["Apology"],
            additional_properties={
                "apology_type": jn_apologies.ApologyTypes.sudden_leave,
                "expression": "4fslbol"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sudden_leave:
    $ Natsuki.percentageAffinityLoss(2)
    if Natsuki.isEnamored(higher=True):
        n 4kwmsrl "..."
        n 4kwmsrl "[player]."
        n 4knmsll "Vamos.{w=0.75}{nw}"
        extend 4ksqbol " Sabes que eres mejor que eso."
        n 4ncseml "N-{w=0.2}no sé si pasó algo o qué,{w=0.75}{nw}"
        extend 4knmajl " pero por favor..."
        n 1knmsll "...Trata de recordar decir adiós apropiadamente la próxima vez.{w=0.5}{nw}"
        extend 2knmbol " ¿Está bien?"
        n 2ksrbol "Significaría mucho para mí."

    elif Natsuki.isNormal(higher=True):
        n 1fsqsr "..."
        $ player_initial = jn_utils.getPlayerInitial()
        n 4fnmem "¡[player_initial]-[player]!{w=0.75}{nw}"
        extend 4knmem " ¿Siquiera sabes lo aterrador que es cuando simplemente desapareces así?"
        n 2kllsf "En serio...{w=0.75}{nw}"
        extend 2knmaj " solo recuerda decir adiós apropiadamente cuando tengas que irte."
        n 4fnmslsbr "Realmente {i}no{/i} pido mucho,{w=0.5}{nw}"
        extend 4kslslsbr " sabes..."

    elif Natsuki.isDistressed(higher=True):
        n 2fsqsf "..."
        n 2fsqaj "Sabes que odio eso,{w=0.2} [player]."
        n 2fsqsl "Basta ya,{w=0.2} ¿quieres?"
        n 2fsqsf "Gracias."
    else:

        n 2fcsuntsa "..."
        n 2fsquntsb "Je.{w=0.2} Sí."
        $ chosen_insult = jn_utils.getRandomInsult().capitalize()
        n 2fsruptsb "Bienvenido de vuelta a ti,{w=0.2} también.{w=0.75}{nw}"
        extend 2fsrgttsb " [chosen_insult]."

    $ Natsuki.addApology(jn_apologies.ApologyTypes.sudden_leave)
    return

init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_prolonged_leave",
            unlocked=True,
            category=["Apology"],
            additional_properties={
                "apology_type": jn_apologies.ApologyTypes.prolonged_leave,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_prolonged_leave:
    $ player_initial = jn_utils.getPlayerInitial()

    if Natsuki.isEnamored(higher=True):
        n 1uwdwrf "¡[player_initial]-{w=0.1}[player]!"
        n 4fbkwrf "¡¿D-{w=0.3}dónde estabas?!{w=0.5}{nw}"
        extend 4kllemlsbl " ¡Me tenías {i}muy{/i} preocupada!"
        n 1kcsunl "..."
        n 1fcsunl "Estoy...{w=0.5}{nw}"
        extend 2kplunl " feliz...{w=0.3} de que hayas vuelto,{w=0.2} [player]."
        extend 2kcseml " Solo..."
        n 4klrsflsbl "...No desaparezcas así de repente por tanto tiempo."
        n 2fcsunf "Odio que jueguen con mi corazón así..."

    elif Natsuki.isNormal(higher=True):
        n 1uwdwr "¡[player_initial]-{w=0.1}[player]!"
        n 4fnman "¡¿Qué demonios?!{w=0.5}{nw}"
        extend 4fnmfu " ¡¿Dónde has estado?!{w=0.5}{nw}"
        extend 1fbkwrless " ¡Estaba muy preocupada!"
        n 2fcsupl "S-{w=0.3}solo como amiga,{w=0.5} ¡pero aun así!"
        n 2fcsun "...{w=1.5}{nw}"
        n 1kcspu "..."
        n 2fllunlsbl "...Bienvenido de vuelta,{w=0.2} [player]."
        n 2kslbosbl "Solo...{w=1.25}{nw}"
        extend 2knmaj " no tardes tanto la próxima vez,{w=0.2} ¿está bien?"
        n 4fsrunl "Sabes que no recibo exactamente muchas visitas..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqputsb "¿[player_initial]-{w=0.1}[player]?"
        n 2fsqsltsb "...Has vuelto."
        n 2fcsfutsb "Simplemente {i}perfecto{/i}."
    else:

        n 2fsquptdr "..."
        n 4fcsfutsd "...."

    $ Natsuki.addApology(jn_apologies.ApologyTypes.prolonged_leave)
    return






init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_early_morning_why_are_you_here",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, None),
            additional_properties={
                "expression": "1tllpu"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_early_morning_why_are_you_here:
    n 1uwdajlesh "¿H-{w=0.1}eh?{w=0.5}{nw}"
    extend 3tnmeml " ¡¿[player]?!"
    n 3fnmpuleqm "¿Qué diablos haces aquí tan temprano?"
    n 3tnmpu "¿Tuviste una pesadilla o algo así?"
    n 3tsrsl "..."
    n 3tsraj "O...{w=1}{nw}"
    extend 3tsqsl " ¿quizás nunca dormiste?{w=0.5}{nw}"
    extend 3tslsl " Eh."
    n 4ccsbgsbr "Bueno,{w=0.2} como sea..."
    n 4cchbgsbr "¿B-{w=0.2}buenos días?{w=0.75}{nw}"
    extend 4csrsssbr " ¿Supongo?"

    return




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_starshine",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.LOVE, None),
            additional_properties={
                "expression": "2ccssml"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_starshine:
    n 2unmfllesu "¡Ah!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 4cchbglsbr " ¡[player_initial]-{w=0.2}[player]!"
    n 4ccsajlsbr "¡E-{w=0.2}ejem!"
    n 4fcssmlsbr "..."
    n 7clrbglsbr "¡B-{w=0.2}buenos días,{w=0.5}{nw}"
    extend 7fsrbglsbr " solecito!"
    n 6cchbglsbr "La Tierra dice '¡H-{w=0.2}hola!'"
    n 6cchsmlsbr "..."
    n 5cslunlsbr "..."
    n 5ccswrlsbl "...¡Sonaba mejor en mi cabeza [player],{w=0.5}{nw}"
    extend 5csremlsbl " ¿okay?!{w=1}{nw}"
    extend 2ccspolsbl " Cielos..."
    n 2cslbol "..."
    n 2cllpul "Pero..."
    n 2cdlpul "Tú...{w=1}{nw}"
    $ chosen_endearment = jn_utils.getRandomEndearment()
    extend 2knmssl " realmente eres mi solecito,{w=0.5}{nw}"
    extend 2ksrssl " [chosen_endearment]."
    n 2cchblleaf "¡B-{w=0.2}bienvenido de vuelta!"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_waiting_for_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
            additional_properties={
                "expression": "4fklfsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_waiting_for_you:
    n 4fsqajl "¡Oh!{w=0.75}{nw}"
    extend 2fsqcal " ¡Bueno mira quién decidió aparecer finalmente!"
    n 2flrsll "Sabes que no me gusta que me hagan esperar...{w=0.75}{nw}"
    extend 2fwmsll " ¿verdad?"
    n 4fsqsml "Jejeje.{w=0.75}{nw}"
    extend 3fcsssl " Tienes suerte de haberme atrapado de buen humor..."
    n 3fchgnlelg "¡Mejor que me lo compenses,{w=0.2} [player]~!"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_lazy",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(10, 11)",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            additional_properties={
                "expression": "2csqcs"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_lazy:
    n 2csqct "¿Oho?{w=0.5}{nw}"
    extend 2fsqsm " ¡Bueno mira quién finalmente salió de la cama hoy!"
    n 4fsqsg "Cielos,{w=0.2} [player]...{w=0.75}{nw}"
    extend 4fchgn " ¡Juro que a veces eres más perezoso que Sayori!"
    n 7fcsbg "Bueno,{w=0.2} mejor tarde que nunca."
    n 3fchbg "¡Aprovechemos el día al máximo,{w=0.2} [player]!"
    n 3tsraj "O...{w=0.75}{nw}"
    extend 3fsqss " ¿lo que queda de él?"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_top_of_the_mornin",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(8, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            additional_properties={
                "expression": "7ullsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_top_of_the_mornin:
    n 7unmbgesu "¡Oh!{w=0.5}{nw}"
    extend 1fchbg " ¡Es [player]!"
    n 3fwlsm "Bueno -{w=0.2} ¡muy buenos días tengas!"
    n 3nchsm "..."
    n 3nsqbo "..."
    n 3tsqss "¿Qué?{w=0.75}{nw}"
    extend 3fsqsg " Se me permite decir cosas tontas {i}también{/i},{w=0.2} sabes."
    n 3nchgn "Jejeje."

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_german",
            unlocked=True,
            conditional="(jn_is_time_block_mid_morning() or jn_is_time_block_late_morning()) and get_topic('talk_learning_languages').shown_count > 0",
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "expression": "7ccssm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_german:
    n 3unmajesu "¡Ah!{w=1}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 4fllbgl " ¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fcsbgl " ¡Justo a tiempo!"
    n 7fcsaw "E-{w=0.2}ejem."
    n 6fcsbsl "G-{w=0.1}guten Morgen,{w=0.75}{nw}"
    extend 6fchbgl " Schlafmuetze!"
    n 5fsqsmlsbl "..."
    n 5fsqcalsbl "..."
    n 2cnmfll "¿Qué?{w=0.5}{nw}"
    extend 2cnmpol " ¿Por qué {i}esa{/i} cara,{w=0.2} de repente?"
    n 7fsqbg "¿Olvidaste que ya estaba estudiando alemán o algo así?"
    n 2fcssm "Jejeje."
    n 4fsgbg "Bueno,{w=0.2} ¡mejor empieza a ponerte las pilas,{w=0.2} [player]!{w=0.75}{nw}"
    extend 7fcsbg " Después de todo..."
    n 6fwlgn "Der fruehe Vogel faengt den Wurm!{w=1}{nw}"
    extend 3fllbgsbr " O-{w=0.2}o algo así."

    return




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_keeping_well",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            additional_properties={
                "expression": "7clrsm"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_keeping_well:
    n 7cchbg "¡Hey!{w=0.2} ¡Buenas tardes,{w=0.2} [player]!"
    n 3tnmss "¿Todo bien?"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_how_are_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            additional_properties={
                "expression": "7ulrsl"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_how_are_you:
    n 7unmajesu "¡Oh!{w=0.75}{nw}"
    extend 4cchbg " ¡Buenas tardes,{w=0.2} [player]!"
    n 2cchsm "¿Cómo estás?"

    return




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_long_day",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.HAPPY, None),
            additional_properties={
                "expression": "4tllbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_long_day:
    n 4unmbg "¡Ajá!{w=0.75}{nw}"
    extend 4fchbg " ¡Buenas noches,{w=0.2} [player]!"
    n 2ksgsg "Día largo,{w=0.2} ¿eh?{w=0.75}{nw}"
    extend 2fcssm " Bueno,{w=0.2} ¡has venido al lugar correcto!"
    n 2nchbg "¡Solo cuéntale todo a [n_name]!"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_took_long_enough",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, None),
            additional_properties={
                "expression": "2fcspo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_took_long_enough:
    $ chosen_tease = jn_utils.getRandomTease()
    n 4fsqgs "¡[player]!{w=0.75}{nw}"
    extend 4fsqsr " ¡Ahí estás,{w=0.2} [chosen_tease]!"
    n 2fcspo "Cielos...{w=1}{nw}"
    extend 2fsrpo " ¡te tomaste tu tiempo!"
    n 2fsqsm "Jejeje."
    n 4uchbg "¡Solo bromeo!{w=0.2} No te preocupes por eso."
    n 3nchsm "¡Bienvenido de vuelta!"

    return




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_up_late",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, None),
            additional_properties={
                "expression": "5ulrbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_up_late:
    n 5unmajeex "¡Oh!{w=0.75}{nw}"
    extend 4fchbgsbl " Hey,{w=0.2} [player]."
    n 3tnmss "Noche tardía para ti también,{w=0.2} ¿eh?"
    n 3ullss "Bueno...{w=0.75}{nw}"
    extend 3nchgn " ¡Supongo que no me quejo!"
    n 3fchsm "¡Bienvenido de vuelta!"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_night_owl",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, None),
            additional_properties={
                "expression": "7ullbo"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_night_owl:
    n 7unmajesu "¡Oh!{w=0.3} ¡[player]!{w=1}{nw}"
    extend 3fllsslsbl " Eres un ave nocturna también,{w=0.2} ¿eh?"
    n 3fcsbg "N-{w=0.2}no es que tenga un problema con eso,{w=0.2} obviamente."
    extend 4nchgnl " ¡Bienvenido de vuelta!"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_what_time_do_you_call_this",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 23 or store.jn_get_current_hour() <= 4",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "expression": "2fsqsf"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_what_time_do_you_call_this:
    n 2fnmgs "¡[player]!{w=0.75}{nw}"
    extend 2fcsgs " ¡Vamos!{w=0.75}{nw}"
    extend 2fsqan " ¿Estás {i}bromeando{/i}?"
    n 4fsqwr "¿Qué clase de hora es {i}esta{/i} entonces?{w=0.75}{nw}"
    extend 4fnmwr " ¿Eh?"
    n 1fsqsl "..."
    n 2fsqgs "¿Y bien?{w=0.75}{nw}"
    extend 2fcsgs " ¡Vamos a oírlo ya!{w=0.5} ¡Escúpelo!"
    n 2fsqbo "..."
    n 2fsqcs "..."
    n 2fchdvesi "¡Pffft-!"
    n 1flrbg "Hombre...{w=1}{nw}"
    extend 4nchgn " Juro que eso {i}nunca{/i} pasa de moda."
    n 4cllss "Pero...{w=1}{nw}"
    extend 3cnmfl " ¿en serio,{w=0.2} [player]?"
    n 3ccsflesi "..."
    n 3ccspu "Solo..."
    extend 4clrsl " no te excedas.{w=0.75}{nw}"
    extend 4cnmbo " ¿De acuerdo?{w=1.25}{nw}"
    extend 5cslbolsbr " En serio."

    if Natsuki.isEnamored(higher=True):
        $ emphasis = " realmente" if Natsuki.isLove(higher=True) else ""
        n 3ccsfllsbr "No[emphasis] quiero escuchar que te perdiste algo importante solo porque no pudiste sacar tu trasero de la cama más tarde."
        n 3ccspolsbr "Tonto."
        n 4csrbolsbr "..."
        n 4nsrajl "Entonces...{w=1}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 7tnmbol " ¿de qué querías hablar,{w=0.2} [chosen_descriptor]?"
    else:

        n 7ccspol "Además.{w=0.75}{nw}"
        extend 3fchgnl " ¡Es {i}totalmente{/i} tu culpa si no puedes sacar tu trasero privado de sueño de la cama más tarde!"
        n 3fsqsml "Jejeje."

    return




init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sanjo_morning",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(7, 10) and jn_desk_items.getDeskItem('jn_sanjo').unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_sanjo",
                "expression": "2udlsmeme"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sanjo_morning:
    n 2unmaj "¡Ah!{w=0.75}{nw}"
    extend 2fchbg " ¡Buenos días,{w=0.2} [player]!{w=0.75}{nw}"
    extend 2unmss " ¿Qué hay?"
    n 4fcssm "No me hagas caso.{w=0.75}{nw}"
    extend 3nchgn " ¡Solo me aseguro de que Sanjo reciba un cuidado de primera calidad!"

    if Natsuki.isEnamored(higher=True):
        n 3flrbg "Sí,{w=0.2} sí.{w=0.75}{nw}"
        $ chosen_tease = jn_utils.getRandomTease()
        extend 3fnmss " Cálmate,{w=0.2} [chosen_tease].{w=1}{nw}"
        extend 4fsqsm " Lo sé."
        n 7fcsbgl "Debes estar {i}bastante{/i} desesperado por mi atención también si ya estás despierto,{w=0.5}{nw}"
        extend 7fchgnl " ¿eh?"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sanjo_generic",
            unlocked=True,
            conditional="jn_desk_items.getDeskItem('jn_sanjo').unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_sanjo",
                "expression": "2fcssmeme"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sanjo_generic:
    n 2ccssmeme "...{w=0.75}{nw}"
    n 2tsqboeqm "...?{w=0.75}{nw}"
    n 4unmfllesu "¡O-{w=0.2}oh!{w=0.75}{nw}"
    extend 4flrbglsbl " ¡[player]!{w=0.75}{nw}"
    extend 1ccssslsbl " Je."
    n 3ccsbgsbl "No te preocupes.{w=0.75}{nw}"
    extend 3ccssm " Sanjo y yo ya cási terminábamos aquí."

    if not jn_is_day():
        n 5clrajsbr "N-{w=0.2}no es que haya olvidado por completo regarlo antes ni nada de eso,\n{w=0.5}{nw}"
        extend 2fcscasbr "{i}obviamente{/i}."

    if Natsuki.isEnamored(higher=True):
        n 1ullaj "Entonces...{w=1}{nw}"
        extend 3unmbo " ¿qué hay de nuevo contigo,{w=0.2} [player]?"
        n 6fcsbgl "...¿O solo estás buscando algo de {i}cuidado de calidad{/i} también?"
        n 7fchsml "Jejeje."
    else:

        n 1ullaj "Entonces..."
        n 3tnmss "¿Qué hay de nuevo,{w=0.2} [player]?"

    return


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_glasses_eyetest",
            unlocked=True,
            conditional="persistent.jn_custom_outfits_unlocked and get_topic('event_eyewear_problems').shown_count > 0 and jn_utils.diceRoll(3)",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_glasses_case",
                "expression": "7csqsl",
                "prop": "glasses_desk"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_glasses_eyetest:
    n 7fdwsl "..."
    n 7flrsl "..."
    n 7tnmboeqm "...?{w=0.75}{nw}"
    n 3unmgslesu "¡O-{w=0.2}oh!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    extend 4fllbglsbr " ¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fcsbglsbr " ¡Ni siquiera te vi entrar!{w=0.75}{nw}"
    extend 7fchbglsbr " ¿Q-{w=0.2}qué hay?"
    n 7fchsmlsbl "..."
    n 7nsqsllsbl "..."
    n 4ccsfllesisbl "..."
    n 4ctlfllsbl "...Y no,{w=0.2} antes de que digas nada.{w=0.75}{nw}"
    extend 2ccstrlsbl " Las gafas no tuvieron nada que ver con eso.{w=0.75}{nw}"
    extend 2ccscalsbl " O-{w=0.2}obviamente."
    show natsuki 2fcspol

    $ jnFadeToBlack(0.5)
    show natsuki 3ccsbo
    $ Natsuki.clearDesk()
    hide prop
    play audio glasses_case_close
    $ jnPause(0.75)
    play audio drawer
    $ jnPause(3)
    $ jnFadeFromBlack(0.5, 0.5)

    n 3nlrbo "..."
    n 3nlraj "Entonces...{w=1}{nw}"
    extend 3tnmss " ¿Qué hay de nuevo contigo,{w=0.2} [player]?{w=0.75}{nw}"
    extend 3tnmbg " ¿Algo nuevo?"
    n 7fcsbglsbr "...¿O-{w=0.2}o solo viniste aquí para un examen de la vista con tu servidora?{w=0.75}{nw}"
    extend 7fsqsmlsbr " Jejeje."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = random.choice(["babe", "hun"])
        n 3fchbgl "¡Bienvenido de vuelta,{w=0.2} [chosen_endearment]!{w=0.75}{nw}"
        extend 3fchblleaf " ¡Ahora date prisa y ponte cómodo ya!"

    elif Natsuki.isEnamored(higher=True):
        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 3fchbgl "¡Bienvenido de vuelta,{w=0.2} gran [chosen_tease]!{w=0.75}{nw}"
        extend 3fchsml " ¡Ahora date prisa y ponte cómodo ya!"
    else:

        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 3fchbgl "¡Bienvenido de vuelta,{w=0.2} [chosen_tease]!{w=0.75}{nw}"
        extend 3nchgnl " ¡Ahora empieza a hablar ya!"


init python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_browsing",
            unlocked=True,
            conditional="jn_is_time_block_night() and jn_utils.diceRoll(10)",
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            additional_properties={
                "desk_item": "jn_laptop",
                "expression": "gaming"
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_browsing:
    play audio keyboard
    n 1cdwsslsbl "..."
    play audio keyboard
    n 1cdwsmlsbl "..."
    n 1unmflleshsbl "¡...!"
    n 1uskwrlsbl "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1fbkwrlsbl " ¡¿D-{w=0.2}desde cuándo llegaste aquí?!{w=0.75}{nw}"
    extend 1fllemlsbl " ¡Cielos!"
    n 1csqfllsbl "¿Estás {i}tratando{/i} de asustarme o qué?{w=0.75}{nw}"
    extend 1csrfllsbr " Juro,{w=0.2} que es casi como si lo hicieras a propósito."
    n 1csrsllsbr "..."
    n 1csrajlsbr "Bueno...{w=1} al menos se autoguardó.{w=0.75}{nw}"
    extend 1clrbol " Supongo.{w=1.5}{nw}"
    extend 1ccsfll " S-{w=0.2}solo dame un segundo,{w=0.2} ¿está bien?"

    show natsuki 1ccscal
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 2ccsss
    $ Natsuki.clearDesk()
    play audio drawer
    $ jnPause(1.3)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    n 2cslca "..."
    n 4ccsss "Je.{w=0.75}{nw}"
    extend 4ccsaj " Entonces..."
    n 3fsqss "¿De qué {w=0.2}{i}tú{/i}{w=0.2} querías hablar tanto entonces,{w=0.5}{nw}"
    extend 3fsqbg " [player]?{w=0.75}{nw}"

    if Natsuki.isEnamored(higher=True):
        n 7fklbgl "¿O-{w=0.2}o solo estabas aquí para {i}navegar{/i} también?"
        extend 7fchsmleaf " Jejeje."
    else:

        n 7fsqsm "Jejeje."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
