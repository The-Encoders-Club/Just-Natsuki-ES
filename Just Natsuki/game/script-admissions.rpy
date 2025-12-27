default persistent._admission_database = dict()
init offset = 5

default -5 persistent._jn_player_admission_type_on_quit = None

default -5 persistent._jn_player_admission_forced_leave_date = None

init -5 python in jn_admissions:
    import random
    import store

    ADMISSION_MAP = dict()


    TYPE_ANGRY = 0
    TYPE_ANXIOUS = 1
    TYPE_ASHAMED = 2
    TYPE_BORED = 3
    TYPE_CONFIDENT = 4
    TYPE_EXCITED = 5
    TYPE_HAPPY = 6
    TYPE_HUNGRY = 7
    TYPE_INSECURE = 8
    TYPE_PROUD = 9
    TYPE_SAD = 10
    TYPE_SICK = 11
    TYPE_TIRED = 12


    last_admission_type = None

    def getAllAdmissions():
        """
        Gets all admission topics which are available

        OUT:
            List<Topic> of admissions which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            ADMISSION_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_admissions_start:
    python:
        admission_menu_items = [
            (_admission.prompt, _admission.label)
            for _admission in jn_admissions.getAllAdmissions()
        ]
        admission_menu_items.sort()

    call screen scrollable_choice_menu(admission_menu_items, ("Volver", None), 400, "mod_assets/icons/admissions.png")

    if isinstance(_return, basestring):
        $ push(_return)
        jump call_next_topic

    jump talk_menu

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Enojado",
            label="admission_angry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_angry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY:
        n 1kcsemesi "Por dios, {w=0.2}[player]... {w=1}{nw}"
        extend 2ksqposbl "¿de verdad sigues tan alterado?"
        n 2fnmpo "... ¿En realidad fuiste a pasar algún tiempo afuera, {w=0.2}como dije?"
        n 2klrsl "..."
        n 4klrsssbl "Sinceramente no sé qué más puedo sugerir, {w=0.75}{nw}"
        extend 4knmbosbl "en realidad."
        n 1fcsflsbl "Solo... {w=1}{nw}"
        extend 1fnmajsbl "intenta mantener la calma, {w=0.75}{nw}"
        extend 2fcscasbl "y pensar las cosas {i}adecuadamente{/i}."
        n 2knmca "¿Está bien?"
        n 1kllsl "Lo último que alguien necesita es que te vayas furioso y te lastimes, {w=0.75}{nw}"
        extend 4kllfl "o haciendo algo..."
        n 4kslsr "... Que no podrás recuperar fácilmente."
        n 2ncsaj "Confía en mí. {w=0.75}{nw}"
        extend 2tnmfl "¿Hacer cosas con enojo, {w=0.2}porque dejaste que todo te afectara? {w=0.75}{nw}"
        extend 2fcssl "De esa manera nunca sale mejor."
        n 2kslsl "Debería saberlo."
        n 1ncsaj "Así que date algo de tiempo, {w=0.2}[player]. {w=1}{nw}"
        extend 1ullbo "Espacio también, {w=0.2}si lo necesitas."
        n 4fcsca "{i}Entonces{/i} tómalo como viene."
        n 4nlrpu "Al menos puedes lograrlo.{w=0.75}.{w=0.75}.{w=0.75}{nw}"

        if Natsuki.isEnamored(higher=True):
            extend 4knmpu " ¿verdad?{w=1}{nw}"
            extend 4knmsslsbl " ¿P-{w=0.2}por mí?"
            n 3knmsllsbl "Y para ti,{w=0.75}{nw}"
            extend 3klrbolsbl " Si no hay nada más."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 4fchsmlsbl "Tú puedes con esto,{w=0.2} [chosen_endearment]!{w=0.5}{nw}"
                extend 4fchbgleafsbl " ¡Como siempre!"
        else:

            extend 4knmpu " ¿verdad?"
            n 2fcsbolsbl "Te debes mucho a ti mismo,{w=0.2} al menos."
    else:

        n 4tnmpu "¿Eh?{w=0.75}{nw}"
        extend 4knmfl " ¿Estás enojado?"
        n 1kllan "¡Rayos!{w=0.75}{nw}"
        extend 2knmaj " ¿Qué te tiene tan alterado?{w=0.75}{nw}"
        extend 2fcsgs " ¡Eso no sirve de nada,{w=0.2} [player]!"
        n 2fcsflsbl "S-{w=0.2}sé que probablemente sea irónico que lo diga yo,{w=0.75}{nw}"
        extend 4fcstr " Pero vamos a enfriar las cosas un poco.{w=0.5}{nw}"
        extend 4knmca " ¿de acuerdo?"
        n 1fcsaj "El simple hecho de estar enojado nunca ha resuelto nada,{w=0.2} así que centrémonos."
        n 2ncsfl "Esta bien.{w=0.75}{nw}"
        extend 2nlrfl " Ahora, {w=0.2} ¿qué haría {i}I{/i} si algo -{w=0.5}{nw}"
        extend 2fsrca " o alguien -{w=0.5}{nw}"
        extend 4tnmsl " ¿De verdad me puse nerviosa?"
        n 1tllaj "Personalmente, si me pongo muy furioso,{w=0.75}{nw}"
        extend 3fcsss " Me gusta pasear.{w=0.75}{nw}"
        extend 3unmaj " Sabes -{w=0.5}{nw}"
        extend 3nlrbo " distanciarme del problema."
        n 4fcscs "A mí me funcionó cuando estaba en el club,{w=0.2} después de todo."
        n 3fcsbg "¡Es realmente sorprendente lo que un poco de aire fresco y una caminata rápida pueden hacer!"
        n 3ulraj "Entonces...{w=1}{nw}"
        extend 1tnmbo " ¿Por qué no intentarlo primero, {w=0.2} [player]?"
        n 4nsrsssbr "Incluso si no es una gran ayuda para saber cómo te sientes..."
        n 2fcsbgsbr "¡Un poco de ejercicio nunca le hizo daño a nadie!{w=0.75}{nw}"
        extend 4fchsmsbr " Jejeje."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANGRY
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Ansioso",
            label="admission_anxious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_anxious:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANXIOUS:
        n 4knmpu "¿Aún te sientes ansioso,{w=0.2} [player]?"
        n 1nsrun "Uuuuuuuu..."
        n 2ksrflsbr "Realmente {w=0.3}{i}no{/i}{w=0.3} soy la mejor persona para este tipo de cosas..."
        n 2knmbosbr "¿Pero quizás podrías intentar algunas distracciones para mantener tu mente alejada de lo que sea que esté sucediendo?"
        n 4kllsssbr "Podrías retomar una serie que no hayas terminado,{w=0.75}{nw}"
        extend 4tllbosbr " o continuar con un hobby o algo."
        n 1fslunsbl "Nnnnnn...{w=0.75}{nw}"
        extend 4kslemsbl " Qué otra cosa..."
        n 1unmajesu "¡Oh!{w=0.5}{nw}"
        extend 3fcspo " Intentá evitar los refrescos, el café y cosas así también."
        n 3flrca "Quiero decir,{w=0.75}{nw}"
        extend 1fsrss " De todos modos, no son buenos para ti.{w=1}{nw}"
        extend 4nsrslsbl " Pero creo que cargarte de cafeína y azúcar es lo {i}último{/i} que necesitas ahora mismo."
        n 4tnmbo "Además de eso,{w=0.5}{nw}"
        extend 1kllss " Generalmente encuentro que escuchar música funciona para mí.{w=0.75}{nw}"
        extend 4unmaj " Pero no te sientas obligado a hacer cualquier cosa que a mí me ayude.{w=0.5}{nw}"
        extend 3fchbgsbr " ¡Deberías hacer aquello que habitualmente te resulta reconfortante!"
        n 3unmbo "No es necesario forzar el barco ni nada:{w=0.5}{nw}"
        extend 4ullfl " un juego favorito,{w=0.5}{nw}"
        extend 2nsrsm " alguna vieja y tonta serie de manga...{w=1}{nw}"
        extend 2fchbg " ¡Lo que sea que mantenga esa cabeza tuya ocupada!"
        n 4fsqcs "...¿Y si no se te ocurre nada más?"
        n 4fchgn "¡Siempre puedes meterte de lleno en algún buen trabajo rutinario!"
        n 2uslss "Siempre hay algún tipo de tarea que debe hacerse de todos modos,{w=0.75}{nw}"
        extend 2usqcs " ¿bien?"
        n 1fsqsm "Jejeje."
        n 3fcsbs "¡No te preocupes -{w=0.5}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
        extend 3uchgnl " tú puedes con esto{w=0.2} [chosen_descriptor]!"
    else:

        n 4tnmpu "¿Eh?{w=0.75}{nw}"
        extend 4knmfl " ¿Te sientes ansioso,{w=0.5}{nw}"
        extend 4knmbo " [player]?"
        n 1kllsssbl "...¿Qué provocó esto,{w=0.5}{nw}"
        extend 1knmsssbl " tan de repente?{w=0.75}{nw}"
        extend 2knmcasbl " No tendrás ningún gran acontecimiento próximamente, ¿verdad?"
        n 2ksrslsbl "..."
        n 2ksrsssbr "B-{w=0.2}bueno,{w=0.75}{nw}"
        extend 4ksrpusbr " Tengo que admitirlo.{w=1}{nw}"
        extend 1knmslsbr " Realmente no sé qué tipo de consejo puedo darte esta vez,{w=0.2} [player]..."
        n 3fcssllsbr "Pero lo que sí sé es esto."
        n 3fcsbol "Todo va a estar bien."
        n 4fcsssl "Todo {i}saldrá{/i} bien,{w=0.2} eventualmente.{w=0.75}{nw}"
        extend 4fchbgl " ¡Siempre lo hace!"
        n 1fllss "Quiero decir,{w=0.5}{nw}"
        extend 2fslss " Puede que no siempre sea como esperas,{w=0.75}{nw}"
        extend 2tslbo " o incluso necesariamente de la manera que {i}quieres{/i}..."
        n 4fnmbo "Pero estresarse por algo no lo hará más fácil,{w=0.2} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1fchsml "Y sabes que siempre estaré aquí para escucharte."
        else:

            n 1fcscal "Además, si no pasa nada más,{w=0.2} siempre estaré aquí para escuchar."

        n 2nlrbo "Entonces...{w=0.75}{nw}"
        extend 2knmbosbr " Intenta quedarte tranquilo,{w=0.2} ¿de acuerdo?"
        n 1fcsbol "S-{w=0.2}sé que es difícil...{w=0.75}{nw}"
        extend 1kllsll " pero solo inténtalo,{w=0.75}{nw}"
        extend 4knmsll " ¿está bien?"

        if Natsuki.isEnamored(higher=True):
            n 4klrssl "Y-{w=0.2}y además."
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            n 1fchsml "Deberías saber que {i}siempre{/i} te respaldaré a estas alturas,{w=0.75}{nw}"
            extend 1fchbll " [chosen_descriptor]."

            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "¡Te amo,{w=0.2} [player]~!"
            else:

                n 4fchsml "Jejeje."
                $ chosen_tease = jn_utils.getRandomTease()
                n 4fchbgl "Haz lo mejor que puedas,{w=0.2} [chosen_tease]."
        else:

            n 4fcssslsbl "A-{w=0.2}además..."
            n 2fsqbglsbl "¿Con alguien como {i}yo{/i} apoyándote?{w=0.75}{nw}"
            extend 2fsrdvlsbl " Bien..."
            n 3fchbgl "¡Me atrevo a decir que no tienes nada de qué preocuparte,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3fchsmleme " Jejeje."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANXIOUS
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Avergonzado",
            label="admission_ashamed",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_ashamed:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ASHAMED:
        n 1knmbo "[player]...{w=0.75}{nw}"
        extend 4ksrslsbl " No estarás {i}en serio{/i} sintiéndote todavía avergonzado de ti mismo,{w=0.5}{nw}"
        extend 4ksqsrsbl " ¿verdad?"
        n 2fcsbo "..."
        n 2fcsfl "Bueno,{w=0.5}{nw}"
        extend 1fcsgs " lo siento [player] -{w=0.5}{nw}"
        extend 4fchgn " ¡Pero no voy a renunciar a ti tan fácilmente!"
        n 3flrss "Y oye,{w=0.5}{nw}"
        extend 3fnmbg " Noticia de última hora:{w=0.75}{nw}"
        extend 3fsqbg " ¡Tampoco te rendirás tan fácilmente!"

        if Natsuki.isEnamored(higher=True):
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
        else:

            $ chosen_descriptor = player

        n 4fcsbs "Ahora ve y arregla las cosas.{w=0.2} [chosen_descriptor]!"

        if Natsuki.isEnamored(higher=True):
            n 4fchsml "¡Creo en ti!"
        else:

            n 4fwlsm "¡Será mejor que no me decepciones!"
    else:

        n 1unmem "¿Eh?{w=1}{nw}"
        extend 4kcsfl " ¿Espera,{w=0.75}{nw}"
        extend 4knmfl " qué?"
        n 4kllbo "¿Te sientes...{w=0.75}{nw}"
        extend 2knmbo " avergonzado?{w=0.75}{nw}"
        extend 2knmflsbr " ¿De ti mismo?"
        n 2ksrpu "...¿Por qué,{w=0.5} [player]?{w=0.75}{nw}"
        extend 2fnmpol " No saliste e hiciste algo {w=0.2}{i}realmente{/i}{w=0.2} tonto,{w=0.2} ¿verdad?"
        n 2fcscal "..."
        n 4fcstrl "Bueno...{w=0.3} lo que sea que hayas hecho,{w=0.5}{nw}"
        extend 2fcsgsl " ¡E-{w=0.2}estoy segura que no lo decías en serio!"
        n 3fnmfl "Y lo más importante,{w=0.5}{nw}"
        extend 3fcsss " Vas a trabajar muy duro para arreglar las cosas.{w=0.75}{nw}"
        extend 3fcssmedz " ¡Lo sé!"
        n 4fcsbg "Vas a dar un paso al frente,{w=0.2} y eso es todo lo que hay que hacer."
        n 2nllaj "Entonces...{w=0.75}{nw}"
        extend 2fnmca " No me decepciones,{w=0.2} ¿entiendes?"
        n 2fnmaj "Y tú tampoco te vas a decepcionar."

        show natsuki 2fnmca
        menu:
            "¿Bien?"
            "¡Bien!":

                n 1fchbs "¡Exactamente!{w=0.5}{nw}"
                extend 4fsqcs " ¿Ves?{w=0.75}{nw}"
                extend 4fcssmeme " ¡Tal como te lo dije!"
            "...":

                n 1nsqbo "..."
                n 2fcssr "No creo que lo entiendas,w=0.2} [player]."
                n 2uchgn "... ¡Así que supongo que tendremos que hacer las cosas de la manera difícil!"
                n 4fcsbg "Ahora,{w=0.5}{nw}"
                extend 1fnmss " repite después de mí:{w=0.5}{nw}"
                extend 2fcsss " '¡No me voy a defraudar!'"

                show natsuki 2fcscs
                menu:
                    "¡No me voy a defraudar!":
                        n 2usqcsesm "¿Ves?{w=1}{nw}"
                        extend 2fchbg " ¡Sabía que lo tenías dentro!{w=0.5}{nw}"
                        extend 2fsqcs " Jejeje."

        n 4fchbg "¡Ahora ve a por ello,{w=0.2} [player]!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ASHAMED
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Aburrido",
            label="admission_bored",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_bored:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_BORED:
        n 4nslsssbl "Guau...{w=1}{nw}"
        extend 4nslflsbl " Supongo que realmente no estabas exagerando entonces.{w=0.5}{nw}"
        extend 4tnmbosbl " ¿eh?"
        n 2fsqfl "¿Realmente intentaste hacer lo que te sugerí?{w=0.75}{nw}"
        extend 2fcsca " ¡Caramba!"
        n 1nlrsl "..."
        n 4ulraj "Bien,{w=0.75}{nw}"
        extend 3tlraj " Si realmente no hay nada que hacer aquí..."
        n 3fcsbg "Entonces, ¿por qué no echar un vistazo a lo que están haciendo los demás para variar?"
        n 4ullbo "Amigos,{w=0.5}{nw}"
        extend 4ulraj " familia...{w=0.75}{nw}"
        extend 3fsqcs " Ese colega con el que siempre planeas pasar el rato...{w=1}{nw}"
        extend 3fcsgs " ¡Alguien tiene que tener algo que ver,{w=0.2} [player]!"
        n 4fchgn "... ¡Así que levántate ya y descúbrelo!{w=0.75}{nw}"
        extend 4ullss " ¡Llama por teléfono o algo así!"
        n 2tnmsl "O, {w=0.2} ya sabes..."
        n 2tsqsmesm "¿Retomas ese juego o libro que {i}totalmente{/i} ibas a revisar en algún momento...?"
        n 2usqcs "..."
        n 2fnmss "¿Qué?{w=0.75}{nw}"
        extend 4fcsbg " ¿Te llamé una vez más, {w=0.2} [player]?{w=0.75}{nw}"
        extend 1fsqcs " Jejeje."
        n 2fnmfl "¡Ahora vamos!{w=0.75}{nw}"
        extend 2fcsbg " Nunca faltan cosas que hacer para pasar el tiempo.{w=1}{nw}"
        extend 2uchgn " ¡Es hora de que te levantes y vayas a buscarlo!"

        if Natsuki.isAffectionate(higher=True):
            $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
            n 4fwlsm "Allá vamos,{w=0.2} [chosen_descriptor]!"

            if Natsuki.isLove(higher=True):
                n 1fchsml "¡Te amo~!"


    elif not persistent.jn_snap_unlocked:
        $ persistent.jn_snap_unlocked = True
        n 4fcsfl "Espera...{w=0.75}{nw}"
        extend 4tnmpu " ¿Estás aburrido?{w=0.75}{nw}"
        n 1fcsflsbr "E-{w=0.2}espera un momento."
        n 2fnmeml "Y-{w=0.2}¡¿Y qué estás tratando de decir, {w=0.2}exactamente?!{w=1}{nw}"
        extend 2fnmgsl " ¿Eh?"
        n 2fcsgslsbr "¿Cómo es posible que te aburras con alguien tan genial como yo cerca?"
        n 2fslposbr "Cielos,{w=0.2} [player]..."
        n 4fcsposbl "Haces que parezca que no {i}estoy{/i} tratando de animar las cosas por aquí o algo así."
        n 1nsrposbl "..."
        n 4tsrfl "Aunque..."
        n 3nlrss "Bueno,{w=0.2} incluso yo admito.{w=1}{nw}"
        extend 3tnmfl " que no hay {i}exactamente{/i} muchas cosas que hacer aquí.{w=0.75}{nw}"
        extend 3fcscal " Además de mí,{w=0.2} quiero decir."
        n 1fslsl "Tiene que haber algo más por aquí."
        n 1nslss "Esto es...{w=0.75}{nw}"
        extend 2tslpu " ¿era...?{w=0.75}{nw}"
        extend 2tnmbo " Un salón de clases,{w=0.2} ¿verdad?"
        n 4tlrca "Tiene que haber {i}algo{/i} que alguien dejó en un escritorio,{w=0.2} o..."
        n 4unmfleex "¡...!{w=0.75}{nw}"
        n 4fnmbg "¡Ajá!{w=0.5}{nw}"
        extend 1fchbg " ¡Acabo de acordarme!{w=0.75}{nw}"
        extend 1fcssm " Solo dame un segundo..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio drawer
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
        show natsuki 4fchgn
        $ jnPause(4)
        hide black with Dissolve(1)

        n 4uchgn "¡Sí!{w=0.75}{nw}"
        extend 4fchsmeme " ¡Sabía que todavía estaban aquí!"
        n 2fsqcs "Apuesto a que no sabías que tenía cartas de juego escondidas,{w=0.2} ¿eh?"
        n 2fchbl "Resulta que estos cajones de escritorio {i}son{/i} útiles,{w=0.2} ¡después de todo!{w=1}{nw}"
        extend 2fcssm " Y {i}siempre{/i} hay que tener algo preparado para un día lluvioso en la escuela."
        n 4nllss "Yo...{w=0.75}{nw}"
        extend 1nsrca " no conozco exactamente muchos juegos de cartas...{w=0.75}{nw}"
        extend 1fsrpo " todavía."
        n 3fsqss "Pero te diré una cosa,{w=0.2} [player]."
        n 3fchbs "¡Tengo una mano increíble en el Snap!{w=0.75}{nw}"
        extend 4fsqbs " Y me {i}muero{/i} por demostrarlo ahora mismo."
        n 2fsqss "Entonces..."
        n 2tnmsm "¿Qué dices entonces,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2tsqsm " ¿Quieres probar tu valía?"

        show natsuki 2fsqcs
        menu:
            n "No es como si tuvieras alguna excusa para no hacerlo,{w=0.2} ¿verdad?"
            "¡Claro,{w=0.2} por qué no!":

                jump snap_intro
            "Ahora no":

                n 4usqct "¿Oh?{w=0.75}{nw}"
                extend 4tsqsm " ¿Ahora no,{w=0.2} dices?"
                n 3ullss "Bien,{w=0.2} bien.{w=0.75}{nw}"
                extend 3fcsbg " Me parece bien."
                n 3uchgn "¡Solo significa que puedo esperar patear tu trasero más tarde!{w=0.75}{nw}"
                extend 4nchgn " Jejeje."

                show natsuki 1fchsmeme
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(2)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
                $ jnPause(1)
                hide black with Dissolve(1.25)
    else:

        n 1tnmfl "¿Eh?{w=0.75}{nw}"
        extend 4tnmpu " ¿Estás aburrido?"
        n 2fnmgsl "Y-{w=0.2}¡¿y qué se supone que significa {i}eso{/i},{w=0.2} [player]?!"
        n 2flreml "¿Soy aburrida?{w=0.75}{nw}"
        extend 4fcsgsl " ¿Eh?{w=1}{nw}"
        extend 4fnmfll " ¿No soy lo suficientemente divertida para estar conmigo?"
        n 4fbkwrl "¡¿No estás entretenido?!"
        n 2fsqpol "..."
        n 2fsqdvl "..."
        n 1fcsajl "Oh,{w=0.5}{nw}"
        extend 4uchgnl " ¡anímate un poco,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4flrss " Hombre..."
        n 3fcsbg "Pero en serio,{w=0.2} ¡vamos!{w=0.75}{nw}"
        extend 3tnmfl " Si estás lo suficientemente aburrido como para decírmelo..."
        n 4fchbg "¡Entonces levanta el trasero y haz algo,{w=0.2} tonto!{w=0.75}{nw}"
        extend 2tsqss " ¡{i}Tienes{/i} un mundo más allá de esta pantalla,{w=0.2} sabes!{w=0.75}{nw}"
        extend 2fcspolsbl " ¡E-{w=0.2}eso es mucho más de lo que {i}yo{/i} tengo!"
        n 2tllss "Y si {i}eso{/i} no es suficiente,{w=0.75}{nw}"
        extend 4fchbgedz " ¡hay uno aún {i}más grande{/i} justo al alcance de tus dedos!"
        n 3fcsbg "Ahora bien, si {i}esas{/i} no son grandes oportunidades para vencer el aburrimiento..."
        n 3fchbg "¡Entonces no sé qué lo es!{w=0.75}{nw}"
        extend 1fchsm " Jejeje."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 1fnmbg "¡Ahora deja de quejarte y muévete,{w=0.2} [chosen_descriptor]!"
        n 2fsqbl "¡El tiempo se acaba!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_BORED
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Confidente",
            label="admission_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_confident:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_CONFIDENT:
        n 2nchsm "Jajaja.{w=0.75}{nw}"
        extend 4tsqcs " ¡Todavía llena de confianza,{w=0.2} ya veo!"

        if Natsuki.isEnamored(higher=True):
            n 4ullaj "Aunque no es ninguna gran sorpresa ni nada de eso,{w=0.2} sin embargo.{w=0.75}{nw}"
            extend 1ullbo " Digo..."
            n 2fchbgl "¡Me gusta pensar que tienes un montón de cosas por las que tener confianza!"
        else:

            n 4fsqcs "...Y me pregunto a quién tienes que agradecerle por eso?"

        n 2fcssm "Jejeje."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 2fchbl "¡De nada,{w=0.2} [chosen_descriptor]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 2fcssmeme "Jejeje.{w=0.75}{nw}"
        extend 2tnmbg " ¿Ves,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fchbgsbr " ¡{i}Sabía{/i} que saldrías de eso eventualmente!"

        if Natsuki.isEnamored(higher=True):
            n 3nllpu "Pero...{w=0.75}{nw}"
            extend 3tnmsl " ¿hablando en serio?"
            n 4nlrpul "Estoy simplemente...{w=0.75}{nw}"
            extend 1ksrsll " muy contenta de saber que estás mejor ahora,{w=0.2} [player]."
            n 2fcssml "Eso es todo lo que importa."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 4kchsmleafsbl "T-{w=0.2}te amo,{w=0.2} [chosen_endearment]."

        elif Natsuki.isAffectionate(higher=True):
            n 2fcsfllsbr "N-{w=0.2}no es que me importe {i}tanto{/i}, ¡p-{w=0.2}por supuesto!"
            n 2nlrbolsbr "Pero...{w=0.75}{nw}"
            extend 4ncsajl " Me alegra saber que estás bien ahora,{w=0.2} [player]."
            n 2fcscaesi "Eso es lo que importa."
            n 2kslca "..."
        else:

            n 2tsqcs "No hay que adivinar a quién tienes que agradecer,{w=0.2} ¿eh?{w=0.75}{nw}"
            extend 1fsqsm " Jejeje."
            n 4fcsbgedz "¡De nada!"
    else:

        n 2tsqct "¿Oh?{w=0.75}{nw}"
        extend 2tsqbg " Te sientes con confianza hoy,{w=0.75}{nw}"
        extend 2tsqcs " ¿eh?"
        n 4fchbg "Bueno,{w=0.2} ¡más poder para ti!"
        n 1fcssmesm "Nunca es malo tener más confianza en uno mismo.{w=0.75}{nw}"
        extend 1ullss " Quiero decir...{w=1}{nw}"
        extend 3fchgn " ¡mírame!"
        n 3unmaj "Sin embargo, no me malinterpretes -{w=0.5}{nw}"
        extend 4nlrss " No digo que siempre sea {i}fácil{/i},{w=0.75}{nw}"
        extend 4nlrsl " obviamente."
        n 1tnmsl "Especialmente si te equivocaste o algo así,{w=0.75}{nw}"
        extend 1tslss " o si no te sientes muy genial."
        n 4tnmss "¡Pero oye!{w=0.75}{nw}"
        extend 2tsqsm " ¿Si así es como te sientes?{w=0.75}{nw}"
        extend 2fchbg " ¡Bueno,{w=0.2} no te lo voy a robar!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_CONFIDENT
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Emocionado",
            label="admission_excited",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_excited:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_EXCITED:
        n 2fllss "Viejo...{w=0.75}{nw}"
        extend 2tsqss " {i}realmente{/i} debes estar entusiasmado si sigues hablando de ello,{w=0.5}{nw}"
        extend 2tsqcs " ¿eh?"
        n 4fchsm "Jejeje."
        n 3fchbg "¡Bien por ti,{w=0.2} [player]!"
    else:

        n 4fspgs "¡Oh!{w=0.5} ¡Oh!{w=0.75}{nw}"
        extend 4unmbg " ¿Pasó algo?{w=0.75}{nw}"
        extend 4fnmtr " ¿Va a pasar algo?"
        n 4fnmca "..."
        n 2tnmaj "¿Y bien?"
        n 3fnmgs "¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
        extend 3fnmfl " ¡Suéltalo!{w=0.75}{nw}"
        extend 4fbkwr " ¡Tienes que decirme!"
        n 2fsqpo "No me digas que vas a acaparar todas las noticias para ti..."
        n 2fsqcs "..."
        n 2fchsm "Jejeje.{w=0.5}{nw}"
        extend 4fllss " Nah,{w=0.2} está bien.{w=0.75}{nw}"
        extend 2fcsbg " ¡Me alegra saber que tienes cosas que te emocionan!{w=0.75}{nw}"
        extend 2flrss " Bueno..."
        n 2fcsssedz "Además de ver a su servidora,{w=0.2} {i}obviamente{/i}.{w=0.75}{nw}"
        extend 1fchsmeme " Jejeje."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_EXCITED
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Feliz",
            label="admission_happy",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_happy:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HAPPY:
        n 3nlraj "Guau...{w=0.75}{nw}"
        extend 3unmaj " todo es sol y arcoíris contigo hoy,{w=0.2} ¿no es así?"
        n 4fsqsm "Jejeje."

        if Natsuki.isEnamored(higher=True):
            n 2uchgn "¡Sigue con esas sonrisas,{w=0.2} [player]!"
        else:

            n 2fchbg "¡Bien por ti,{w=0.2} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 2tnmsl "...¿Te sientes mejor ahora,{w=0.2} [player]?"
        n 2kllbo "..."
        n 4kllpu "Lo admitiré.{w=1}{nw}"
        extend 4nslsll " Me estaba empezando a preocupar.{w=1}{nw}"
        extend 2kslcal " Odio ver a mis amigos molestarse."
        n 2ncscal "La vida es demasiado corta para todo eso."

        if Natsuki.isEnamored(higher=True):
            n 2knmbolsbl "Y mereces ser feliz también,{w=0.2} sabes."
            n 2ncssll "Recuerda eso."
            n 2ksrbol "..."
            n 2nsrajl "E-{w=0.2}entonces...{w=0.75}{nw}"
            extend 4tnmsllsbl " ¿dónde estábamos?"
        else:

            n 2nslsll "Todo el mundo merece al menos ser feliz,{w=0.2} después de todo."
            n 2flrbolsbl "A-{w=0.2}ahora volvamos a ello."
            n 2ksrbolsbl "..."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4tnmsl "¿Te sientes mejor,{w=0.2} [player]?{w=0.75}{nw}"
        extend 4fnmfl " ¡No me sorprende!"
        n 2fcstr "Simplemente no eres tú mismo cuando tienes hambre."
        n 2nslss "Créeme...{w=0.75}{nw}"
        extend 1nslslsbr " Yo lo sabría."
        n 2fcsaj "¡Solo no dejes que se ponga {i}tan{/i} mal la próxima vez!"
        n 2fsqfl "...O realmente te daré una palmada.{w=1}{nw}"
        extend 1fsqsm " Jejeje."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3nchgnl "¡Te amo,{w=0.2} [chosen_tease]~!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1fcssm "Jejeje.{w=0.75}{nw}"
        extend 2fwlbg "¡Me alegra ver que estás de vuelta en acción, [player]!"
        n 2ullaj "Es un poco gracioso,{w=0.2} en realidad."
        n 2tnmfl "Nada te hace apreciar sentirte normal más que estar enfermo,{w=0.2} ¿eh?"
        n 4fchgn "¡Supongo que ahora lo sabrías mucho mejor!"

        if Natsuki.isLove(higher=True):
            n 4fchblleaf "¡También te amo,{w=0.2} [player]!"
    else:

        n 4tnmss "¿Oh?{w=0.75}{nw}"
        extend 4usqsm " ¡Alguien está de buen humor hoy!"
        n 3fcsbgedz "¿Estará ayudando que cierto {i}alguien{/i} esté cerca,{w=0.2} me pregunto?"
        n 3fsqsmeme "Jejeje."
        n 4fchbg "¡Bien por ti,{w=0.2} [player]!"

        if Natsuki.isEnamored(higher=True):
            n 2fcssmesm "Si tú eres feliz,{w=0.2} ¡yo soy feliz!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HAPPY
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Hambriento",
            label="admission_hungry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_hungry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4fcsfl "...Espera.{w=1}{nw}"
        extend 4tsqpu " ¿Qué?{w=0.75}{nw}"
        extend 2tnmfl " ¿{i}Todavía{/i} tienes hambre?"
        n 2fsqfl "...¿O en serio no conseguiste nada cuando te lo dije antes?"
        n 1fcsfl "De cualquier manera,{w=0.75}{nw}"

        if Natsuki.isEnamored(higher=True):
            extend 2fchgn " ¡No soy tu niñera!{w=0.75}{nw}"
            extend 2fsrdvlsbl " ¡A-{w=0.2}aunque desearías que fuera!"
        else:

            extend 2fchgn " ¡No soy tu niñera!"

        n 2fcsaj "¡Ahora levanta el trasero y resuelve algo de una vez!{w=1}{nw}"
        extend 2flrss " Yeesh..."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 4fcsbg "¡Solo mantenlo saludable,{w=0.2} [chosen_descriptor]!"

        if Natsuki.isAffectionate(higher=True):
            n 4fsqbg "Alguien tiene que asegurarse de que te mantengas en plena forma,{w=0.2} después de todo.{w=0.5}"
            extend 2fchsmleme " Jejeje."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 2knmbo "...[player]."
        n 2ncssl "Yo...{w=1}{nw}"
        extend 4knmca " entiendo si tienes habre,{w=0.2} ¿bueno?{w=0.75}{nw}"
        extend 4knmaj " De verdad.{w=1}{nw}"
        extend 1fcssl " Todo el mundo tiene que comer."
        n 1kllfl "Solo..."
        n 1kslbo "..."
        n 4ncsbo "No uses la comida o los bocadillos como una forma de sentirte mejor si te sientes deprimido.{w=1}{nw}"
        extend 4ksqbol " ¿Está bien?"
        n 2unmeml "¡N-{w=0.2}no estoy tratando de ser tu madre ni nada!{w=0.5}{nw}"
        extend 2fcspol " Por supuesto que no.{w=0.75}{nw}"
        extend 2ksrsll " Pero sería una pésima amiga si no dijera al menos {i}algo{/i} al respecto."
        n 1ncspu "Así que por favor.{w=0.75}{nw}"
        extend 4ksqca " Simplemente no exageres."
        n 3nlrsl "Un capricho está bien,{w=0.2} y podría ayudarte a sentirte mejor."
        extend 3nsrpu " Puedo entender eso."
        n 3ksqbo "Pero no va a arreglar lo que te hizo sentir así en primer lugar."

        if Natsuki.isEnamored(higher=True):
            n 4klrbol "Y sabes que puedes venir a hablar conmigo si realmente lo necesitas...{w=1}{nw}"
            extend 4knmbol " ¿verdad?"

        elif Natsuki.isAffectionate(higher=True):
            n 4fcsbol "Y-{w=0.2}y siempre puedes venir a hablar conmigo,{w=0.2} ya sabes."
            n 4ksrcal "..."
        else:

            n 4ksrbo "...Disfruta tu comida,{w=0.2} [player]."
    else:

        n 4tnmpu "¿Eh?{w=0.75}{nw}"
        extend 4tsqem " ¿Tienes {i}hambre{/i}?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 2tnmfl "...¿Entonces para qué me lo dices a {i}mí{/i}?{w=0.75}{nw}"
        extend 2fchgn " ¡Ve a buscar algo de comer,{w=0.2} gran tonto!"

        if Natsuki.isEnamored(higher=True):
            n 1fcsaj "Honestamente...{w=0.75}{nw}"
            extend 2tsqss " ¿qué voy a hacer contigo,{w=0.2} eh?"
        else:

            n 1fcsaj "Honestamente...{w=0.75}{nw}"
            extend 2fllfl " ¿qué soy,{w=0.5}{nw}"
            extend 2fsqpo " tu mamá o algo así?"
            n 2nsrfl "Cielos..."

        n 1fcsaj "¡Ahora ve a hacer algo de una vez!"
        n 4nsrslsbr "...Y no,{w=0.2} [player],{w=0.75}{nw}"
        extend 4nsqsl " antes de que preguntes."
        n 3fcsbg "¡La comida basura no cuenta!"

        if (
            (jnIsNatsukiBirthday() and jn_events.getHoliday("holiday_natsuki_birthday").isCompleted())
            or (jnIsPlayerBirthday() and jn_events.getHoliday("holiday_player_birthday").isCompleted())
        ):
            n 3ullaj "Oh,{w=0.5}{nw}"
            extend 3csqss " y no vas a recibir nada de ese pastel de antes tampoco.{w=1.25}{nw}"
            extend 3fchgnelg " ¡Lo siento~!"

        elif Natsuki.isAffectionate(higher=True):
            n 3fsqsm "No eras un bote de basura la última vez que revisé.{w=0.75}{nw}"
            extend 3fchgnelg " ¡Así que nada de basura para ti~!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HUNGRY
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Inseguro",
            label="admission_insecure",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_insecure:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 2knmbosbr "¿{i}Todavía{/i} te sientes abatido por eso,{w=0.2} [player]?"
        n 2klrbosbr "..."
        n 2nlrfl "Tú...{w=0.75}{nw}"
        extend 2fnmbol " recuerdas lo que dije,{w=0.2} ¿verdad?"
        n 1fcsfl "Todo el mundo tiene su propio ritmo.{w=0.75}{nw}"
        extend 4fcsca " Tú no eres la excepción.{w=0.75}{nw}"
        extend 2tnmaj " ¿Y honestamente?"
        n 2fcsbo "Realmente no me importa lo que sea.{w=1}{nw}"

        if Natsuki.isEnamored(higher=True):
            extend 2tnmbol " ¿Mientras estemos juntos?"
        else:

            extend 2tnmfl " ¿Mientras seamos amigos?"

        n 2fcstrl "Tendremos que encontrarlo juntos."
        n 1nllcal "..."
        n 4nsleml "...Viejo,{w=0.75}{nw}"
        extend 4fslsslsbr " eso fue cursi.{w=0.75}{nw}"
        extend 1fnmpu " Pero en serio,{w=0.2} [player]."
        n 3fchbgsbr "¡No te preocupes!"
        n 3fcsbgsbr "Además..."
        n 3fsrcs "¿Cuando alguien como {i}yo{/i} te cubre las espaldas?"
        n 4fcsbgledz "¡Me atrevo a decir que no tienes nada de qué preocuparte!{w=0.75}"
        extend 1nchgnl " Jejeje."

        if Natsuki.isLove(higher=True):
            n 1fchsmleaf "¡Te amo,{w=0.2} [player]~!"
    else:

        n 1fcsfl "...Espera,{w=0.5}{nw}"
        extend 2knmpu " ¿qué?"
        n 2tnmbo "¿Te sientes inseguro?"
        n 1knmslsbr "...¿Qué provocó esto tan de repente,{w=0.2} [player]?"
        n 4ncspu "..."
        n 4ncsaj "Yo...{w=0.75}{nw}"
        extend 4klrsl " realmente no puedo comentar sobre lo que te hizo sentir de esa manera.{w=1}{nw}"
        extend 1ksrbo " Y no voy a fingir que puedo."
        n 2fnmbol "Pero será mejor que escuches aquí,{w=0.2} [player] -{w=0.75}{nw}"
        extend 2fsqbol " y escucha bien."
        n 2fcseml "No me importa si piensas que no le agradas a la gente.{w=0.75}{nw}"
        extend 2fnmbolsbr " A {i}mí{/i} me agradas."
        n 4flrfll "No me importa si la gente piensa que no tienes talento.{w=0.75}{nw}"
        extend 1fcscalesi " {i}Yo{/i} sé que lo tienes."
        n 1fcstrl "No me importa si la gente piensa que te estás quedando atrás.{w=0.75}{nw}"
        extend 2fnmsll " {i}Yo{/i} sé que te pondrás al día."
        n 2fcsajl "Solo..."
        n 2kslbol "..."
        n 4kcsfll "Date tiempo y espacio,{w=0.2} [player].{w=0.75}{nw}"
        extend 4knmbol " ¿Está bien?"

        if Natsuki.isEnamored(higher=True):
            n 1knmbol "Entiendo cómo te sientes.{w=0.75}{nw}"
            extend 2knmpul " Realmente lo hago.{w=1}{nw}"
            extend 2ksqsfl " He {i}estado{/i} ahí."
        else:

            n 2fcsbol "Entiendo lo mal que probablemente te sientas en este momento."

        n 2fcstrl "Y no voy a dejar que un amigo se siga sintiendo así sin luchar.{w=0.75}{nw}"
        extend 2fnmtrl " Pero tú también necesitas poner un poco de esfuerzo."
        n 4fllfll "Puedes hacer eso...{w=0.75}{nw}"

        show natsuki 4knmbol
        menu:
            extend " ¿verdad?"
            "Verdad":

                n 1fcsbo "...Bien.{w=0.75}{nw}"
                extend 4flrfl " O tendrás que tratar conmigo también.{w=0.75}{nw}"
                extend 4fnmfl " Y créeme."
                n 2fsqpo "...{i}Realmente{/i} no quieres eso.{w=1}{nw}"
                extend 2flrss " Jajaja."
                n 4klrbo "Entonces..."
                n 2knmsssbr "¿Querías hablar de otra cosa?"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_INSECURE
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Orgulloso",
            label="admission_proud",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_proud:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_PROUD:
        n 2nslaj "Guau...{w=1}{nw}"
        extend 2tnmpo " {i}todavía{/i} tienes humor para regodearte,{w=0.2} ¿verdad?"
        n 4ucsfl "Está bien.{w=0.75}{nw}"
        extend 4ncsfl " Está bien.{w=1}{nw}"
        extend 4nlrfl " Siempre y cuando no te estés dejando llevar demasiado."
        n 1nnmca "Solo recuerda,{w=0.2} [player] -{w=0.5}{nw}"
        extend 3fnmss " si hay algo en lo que soy buena..."
        n 3fcsbg "...¡Es en bajarle los humos a la gente!"
        n 4ullfl "Bueno...{w=0.5}{nw}"
        extend 2fchgn " cuando lo necesitan,{w=0.2} de todos modos.{w=1}{nw}"
        extend 1nchgneme " Jejeje."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchblleme "¡También te amo,{w=0.2} [chosen_tease]~!"
    else:

        n 2tnmct "¿Oh?{w=0.75}{nw}"
        extend 2fsqbg " ¿Y de qué estás tan orgulloso {i}tú{/i}?{w=1}{nw}"
        extend 2fnmbg " ¿Eh?"
        n 4fsqsm "¿Y bien?"
        n 4fsqbg "¡Suéltalo,{w=0.2} [player]!{w=1}{nw}"
        extend 3fcsbg " Debe ser bastante increíble,{w=0.2} después de todo.{w=1}{nw}"
        extend 4fsqss " ¿Verdad?"
        n 2tsqcs "..."
        n 2fchcs "Jejeje."
        n 4ullaj "Bueno,{w=0.75}{nw}"
        extend 4tnmbo " lo que sea que sea.{w=0.75}{nw}"
        extend 3fcsbg " ¡Debes estar bastante presumido al respecto para compartirlo conmigo!"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 3fchbg "¡Buen trabajo,{w=0.2} [chosen_descriptor]!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_PROUD
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Triste",
            label="admission_sad",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sad:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        if Natsuki.isEnamored(higher=True):
            n 2kllbo "...¿Sigues sintiéndote triste,{w=0.5}{nw}"
            extend 2knmbo " [player]?"
        else:

            n 1ksrpusbl "Viejo...{w=0.75}{nw}"
            extend 4knmflsbl " ¿todavía te sientes deprimido,{w=0.2} [player]?"

        n 2kslbosbr "..."
        n 2kslajsbr "Yo...{w=1}{nw}"
        extend 4kslsssbr " no puedo creer que no lo haya mencionado antes,{w=0.2} pero...{w=0.75}{nw}"
        extend 4knmbosbr " ¿has hablado con alguien sobre esto?"
        n 1fcsajlsbr "A-{w=0.2}además de mí,{w=0.75}{nw}"
        extend 1nllsllsbr " quiero decir.{w=1.25}{nw}"
        extend 4knmsllsbr " Hablo en serio."
        n 4knmbolsbr "...¿Tienes a alguien más con quien puedas compartir esto?"

        show natsuki 4klrbolsbr
        menu:
            n "¿Como amigos, familia,{w=0.2} o...?"
            "Sí,{w=0.2} tengo":

                n 1knmbo "...Entonces tal vez deberías compartir cómo te sientes,{w=0.2} [player].{w=1}{nw}"
                extend 2nsrss " Incluso si es vergonzoso."
                n 2tlrsssbl "Sabes lo que dicen,{w=0.75}{nw}"
                extend 2tnmsssbl " ¿verdad?{w=1}{nw}"
                extend 2fcsbgsbl " ¡Un problema compartido es un problema dividido!"
                n 4ksqcasbr "Pero en serio,{w=0.2} [player].{w=0.75}{nw}"
                extend 1ksrcasbr " No tengas miedo de pedir ayuda,{w=0.2} ¿de acuerdo?"
                n 1fcscalsbr "Nunca es algo de lo que avergonzarse.{w=0.5}{nw}"
                extend 4fcsbolsbl " Créeme."
                n 2kslbol "...Y a mí también me tomó mucho tiempo aprender eso."
            "No tengo":

                n 4nlrsslsbr "Eso es...{w=0.75}{nw}"
                extend 4ksrsllsbr " realmente {i}no{/i} es lo que esperaba escuchar,{w=0.75}{nw}"
                extend 1ksqbolsbr " honestamente."
                n 1ncsflsbr "Yo...{w=1}{nw}"
                extend 1knmbosbr " lamento escuchar eso,{w=0.2} [player].{w=0.75}{nw}"
                extend 2kllbosbr " De verdad."

                if Natsuki.isEnamored(higher=True):
                    n 2kslcalsbl "...Y lamento haber preguntado."

                n 4knmbosbr "Solo avísame si puedo ayudar de alguna manera.{w=1.25}{nw}"
                extend 4klrbosbr " ¿De acuerdo?"
            "Ya lo saben":

                n 2fcsfllsbr "¡Bien!{w=0.75}{nw}"
                extend 2fcscalsbr " Bien..."
                n 3fllbol "Solo espero que te hayan apoyado,{w=0.2} [player]."
                n 3kllbolsbl "Al menos mereces eso."

        if Natsuki.isEnamored(higher=True):
            n 4knmbol "...¿Y [player]?"
            n 1kslbol "..."

            show natsuki 4kcscal at jn_center
            play audio chair_out
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(4)
            play audio clothing_ruffle
            show natsuki 1knmcal at jn_center
            $ jnPause(6)
            play audio chair_in
            $ jnPause(4)
            hide black with Dissolve(1.25)

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 1klrcal "S-{w=0.2}sabes que te amo.{w=1}{nw}"
                extend 4knmsll " ¿Verdad?{w=0.75}{nw}"
                extend 4knmssl " Independientemente de cómo te sientas en este momento."

            n 4klrsslsbl "Espero que empieces a sentirte mejor pronto,{w=0.2} [player]."
        else:

            n 4klrsslsbl "Espero que empieces a sentirte mejor pronto."
            n 4ksrbolsbl "..."
    else:

        if Natsuki.isEnamored(higher=True):
            n 2kllbo "Oh...{w=0.75}{nw}"
            extend 2knmsl " ¿en serio?{w=1.25}{nw}"
            extend 2klrflsbl " Cielos..."
            n 4ksrpusbl "Fue...{w=1}{nw}"
            extend 4knmpusbl " ¿pasó algo,{w=0.2} o...?{w=0.75}{nw}"
            extend 2fcsfllsbr " N-{w=0.2}no tienes que decirme si no quieres,{w=0.2} por supuesto."
            n 2flrsllsbr "No juzgaré.{w=0.75}{nw}"
            extend 2klrsllsbr " Así que..."
        else:

            n 1uskfl "H-{w=0.2}he?{w=0.75}{nw}"
            extend 4knmboeqm " ¿Te sientes triste ahora?"
            n 2klrflsbr "...¿De dónde vino eso de repente?"
            n 2ksrflsbr "Hombre...{w=0.75}{nw}"
            extend 2fcsfllsbl " realmente {i}tenías{/i} que elegir a la peor persona para manejar este tipo de cosas,{w=0.75}{nw}"
            extend 2ksrsllsbl " ¿no es así?"

        n 1kcsbolesi "..."
        n 4ncsfl "Bien.{w=1}{nw}"
        extend 4nnmfl " Okey,{w=0.2} [player].{w=1.25}{nw}"
        extend 4nnmca " Escúchame."
        n 4ncstrl "Y-{w=0.2}y concéntrate en tu respiración.{w=0.75}{nw}"
        extend 1ncsfl " Inhala,{w=1.5}{nw}"
        extend 1ncspu " y exhala."
        n 1nnmbo "Justo así."
        n 1ncspu "Y otra vez."
        n 4ncssl "..."
        n 2ncsfl "...Bien.{w=1.25}{nw}"
        extend 2nnmsl " [player]."
        n 2nllaj "Lo que sea que haya pasado,{w=0.2} tienes que entender una cosa."
        n 4kllbo "Cómo te sientes...{w=0.75}{nw}"
        extend 4knmca " solo va a ser temporal.{w=1}{nw}"
        extend 1fcscal " {i}Siempre{/i} es temporal.{w=1}{nw}"
        extend 1flrpul " No importa lo que estés pensando ahora...{w=1.5}{nw}"
        extend 4knmcal " así es como es."
        n 2fcsfllsbr "I-{w=0.2}I know it sucks!{w=0.75}{nw}"
        extend 2nslsll " Believe me.{w=0.75}{nw}"
        extend 4kslbol " And it must have been bad if you had to open up to me about it."

        if Natsuki.isAffectionate(higher=True):
            n 4fcsajlsbr "N-{w=0.2}no es que sea un problema ni nada."

        n 3klrss "Pero incluso si no puedes arreglar lo que sea que te molestó en este momento..."
        n 3knmbo "Al menos puedes empezar a tratar de arreglar cómo te sientes al respecto."

        show natsuki 4knmsssbr
        menu:
            n "...¿Verdad?"
            "Verdad":

                pass

        n 4fcssssbr "Jejeje.{w=0.75}{nw}"
        extend 4fchbgsbl " ¿V-{w=0.2}ves?{w=1}{nw}"
        extend 2fcssmsbl " ¡Ese es el espíritu!"
        n 1ullaj "Así que solo...{w=0.75}{nw}"
        extend 1tnmbo " tómate tu tiempo con ello.{w=1}{nw}"
        extend 2tlrss " No tienes que sentirte mejor {i}al instante{/i}."
        n 2nsrpo "...De hecho, estaría celosa si pudieras."
        n 4fcsss "Ponte ropa cómoda,{w=0.75}{nw}"
        extend 4fllss " pon algún viejo y tonto anime..."
        n 4fcssm "¡Lo que sea que creas que ayude mejor!"

        if Natsuki.isEnamored(higher=True):
            n 1fsrdvl "...Como pasar más tiempo con tu servidora,{w=0.2} p-{w=0.2}por ejemplo."

        n 2ullfl "No será una solución instantánea,{w=0.75}{nw}"
        extend 4fnmsl " pero ese no es el punto.{w=1}{nw}"
        extend 3fchbg " ¡Solo estamos impulsando tu recuperación,{w=0.2} eso es todo!"
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
        n 3fcsaj "Ahora salta a ello,{w=0.2} [chosen_descriptor] -{w=0.5}{nw}"
        extend 3fsqbgsbr " ¡Quiero verte sonreír de nuevo lo antes posible!{w=0.75}{nw}"
        extend 4fchsmlsbr " Jejeje."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SAD
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Enfermo",
            label="admission_sick",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sick:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1kcsem "Hombre...{w=1}{nw}"
        extend 4knmflsbr " ¿realmente {i}todavía{/i} te sientes enfermo?{w=0.75}{nw}"
        extend 4ksrbosbr " Cielos,{w=0.2} [player]..."

        show natsuki 2knmbosbr
        menu:
            n "¿Cuánto tiempo te has sentido así realmente?"
            "Unas pocas horas":

                n 2tslfl "...Eh."
                n 2fcsajsbl "B-{w=0.2}bueno,{w=0.75}{nw}"
                extend 2flrsssbl " al menos no es tanto tiempo."
                n 4fsqpol "Pero eso no significa que debas descuidarte tampoco."
                n 1ullbo "Así que...{w=1}{nw}"
                extend 4tnmbo " solo asegúrate de tomártelo con calma,{w=0.2} ¿de acuerdo?"
                n 4fcsbgsbr "Lo siento,{w=0.2} [player].{w=0.75}{nw}"
                extend 2fchgn " ¡Parece que no habrá aventuras para ti hoy!{w=0.75}{nw}"
                extend 2fchsm " Jejeje."
            "Unos pocos días":

                n 4tnmfl "...Estás bromeando,{w=0.2} ¿verdad?{w=0.75}{nw}"
                extend 4knmflsbl " ¿Ya han pasado días?"
                n 1ncsbo "..."
                n 2nlrfl "Okey,{w=0.2} mira.{w=0.75}{nw}"
                extend 2fnmca " Entiendo que conoces tus límites.{w=0.75}{nw}"
                extend 2fcspu " Solo..."
                n 1fsrpol "...No seas tonto al respecto.{w=1}{nw}"
                extend 4fnmajlsbl " En serio.{w=0.75}{nw}"
                extend 2fnmbolsbl " No quiero escuchar que empeoraste porque trataste de resistirlo como una especie de macho."
                n 2tnmbolsbl "¿Capiche?"

                if Natsuki.isEnamored(higher=True):
                    n 4kllsllsbr "...Y trata de descansar un poco más también.{w=0.75}{nw}"
                    extend 4kllsslsbr " ¿P-{w=0.2}por mí?"
                    n 1ksqbol "Suenas como si lo necesitaras."
                else:

                    n 4kllbolsbr "...Y al menos trata de descansar un poco más también."

                n 2knmbo "Mejórate pronto,{w=0.2} ¿de acuerdo?"
            "Una semana o algo así":

                n 2flrbo "[player]..."
                n 2fnmbol "Ya deberías saber que odio regañar.{w=1}{nw}"
                extend 2ksqsllsbl " A nadie le gusta un regañón.{w=1}{nw}"
                extend 2fcssllsbl " Pero sería una pésima amiga si al menos no {i}preguntara{/i}."
                n 4klrbol "Entonces...{w=1}{nw}"
                extend 4klraj " esta...{w=0.75}{nw}"
                extend 4knmbo " enfermedad tuya."
                n 4tsrpu "...{i}Has{/i} visto a alguien por esto..."

                show natsuki 4ksqpul
                menu:
                    n "¿Verdad?"
                    "Sí,{w=0.2} lo he hecho":

                        n 2fsrpol "Bueno...{w=1.25}{nw}"
                        extend 2nsrpol " está bien."
                        n 2nsraj "Yo...{w=1}{nw}"
                        extend 1ksqbo " solo espero que hayan podido ayudarte,{w=0.2} [player]."
                        n 4ksqsl "Asegúrate de descansar un poco más,{w=0.2} ¿de acuerdo?"
                    "No,{w=0.2} no lo he hecho":

                        n 3tnmem "...¿En serio?{w=0.75}{nw}"
                        extend 3ksqgs " ¡Vamos,{w=0.2} [player]!{w=1}{nw}"
                        extend 3fcswrlsbr " ¿Cómo se supone que vas a mejorar si ni siquiera sabes qué te pasa?"
                        n 2ncsbolsbl "..."
                        n 2nslemlsbl "Sí...{w=0.3} ya lo sé.{w=0.75}{nw}"
                        extend 4nslpol " No soy ingenua.{w=1}{nw}"
                        extend 4kslsll " Entiendo si tienes que pagar para ver a un médico,{w=0.2} o lo que sea."
                        n 1knmsl "...O si simplemente no hay ayuda cerca."
                        n 1fcssl "Solo..."
                        n 4ksrsl "..."
                        n 2ksqpusbr "Tómatelo con calma.{w=0.75}{nw}"
                        extend 2knmpusbr " ¿Por favor?"
                        n 2ncsfl "Si realmente no puedes -{w=0.75}{nw}"
                        extend 2nslfl " o no quieres -{w=0.75}{nw}"
                        extend 2nslsl " ver a alguien..."
                        n 4fnmsll "Entonces lo menos que puedes hacer es tratar de recuperarte lo mejor que puedas."

                        if Natsuki.isEnamored(higher=True):
                            n 2knmbol "Al menos puedes lograr eso.{w=0.75}{nw}"
                            extend 2kllbol " Sé que puedes.{w=0.75}{nw}"
                            extend 2kllajl " Y además."
                            n 4kslsllsbl "...Sabes que tu salud realmente me importa.{w=1.25}{nw}"
                            extend 4ksqcalsbl " ¿Verdad?"
                        else:

                            n 2flrcal "Al menos puedes hacer eso...{w=1.25}{nw}"
                            extend 2knmbol " ¿verdad?"


                        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
                n 4knmslsbl "E-{w=0.2}espero que te sientas mejor pronto,{w=0.2} [chosen_descriptor]."
                n 1ksrbolsbl "..."
            "Más tiempo":

                n 2knmbosbl "..."
                n 2klrajsbl "Yo...{w=1.25}{nw}"
                extend 2ksrbosbr " honestamente no sé realmente qué decirte,{w=0.2} [player]."
                n 4ksqbolsbr "Solo espero que te sientas mejor pronto."
                n 4knmbosbr "Tómatelo con calma,{w=0.2} ¿de acuerdo?"

                if Natsuki.isEnamored(higher=True):
                    n 1knmsslsbr "¿Por mí?"
                    n 1ksrbolsbl "..."


                $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4fcsfl "...Espera.{w=1}{nw}"
        extend 2tnmfl " ¿No dijiste que tenías hambre antes,{w=0.2} [player]?"
        n 2fsqsl "Tú {i}sabes{/i} que no comer puede hacerte sentir tan mal como estar enfermo,{w=0.75}{nw}"
        extend 2tsqsl " ¿verdad?"

        show natsuki 1fcsflsbl
        menu:
            n "No me digas que te saltaste tus comidas hoy o algo así."
            "He comido":

                n 4tsqpu "...Eh.{w=1}{nw}"
                extend 2tllpueqm " ¿Entonces tal vez fue algo que comiste?{w=0.75}{nw}"
                extend 2tnmbo " ¿Como algo mal cocinado o algo así?"
                n 1tsrbo "..."
                n 4nlraj "Bueno,{w=0.75}{nw}"
                extend 4nlrbo " supongo que no importa {i}realmente{/i}.{w=0.75}{nw}"
                extend 2tllsll " Solo asegúrate de descansar si lo necesitas."
                n 2knmbol "¿Entendido?"
            "No,{w=0.2} no he comido":

                n 4fcsbglsbl "¡J-{w=0.2}jah!{w=1}{nw}"
                extend 4fnmgs " ¡Lo sabía!{w=0.75}{nw}"
                extend 2fbkwrsbr " ¿Qué {i}esperabas{/i} en serio,{w=0.2} [player]?"
                n 2fllflsbr "¡Por {i}supuesto{/i} que te vas a sentir miserable si estás funcionando con los humos!{w=0.75}{nw}"
                extend 2fcsposbr " ¡Cualquiera lo haría!"
                n 1nsqposbr "...Y créeme.{w=1}{nw}"
                extend 4kslbolsbr " Yo lo sabría."
                n 3fcsfllsbr "¡Ahora ve a resolver algo de una vez,{w=0.2} tonto!"
                extend 3fchsm " Jejeje."
    else:

        n 2tnmbosbr "¿Sintiéndote mal,{w=0.2} [player]?"
        n 2fsqbolsbr "Será mejor que no te estés esforzando por estar aquí.{w=1}{nw}"
        extend 2fnmfllsbr " Lo digo en serio."
        n 4fcsfllsbr "¡N-{w=0.2}no es que no aprecie la compañía!{w=0.75}{nw}"
        extend 4knmbolsbl " ¡Lo hago!{w=1}{nw}"
        extend 4ksrslsbl " Es solo..."
        n 1fcssll "Realmente no quiero interponerme en el camino de que te sientas mejor.{w=0.75}{nw}"
        extend 2kllbol " No soy egoísta de esa manera."
        n 1ncsajl "Solo...{w=0.75}{nw}"
        extend 4nlrsll " avísame si tienes que ir a descansar.{w=0.75}{nw}"
        extend 4knmbol " ¿De acuerdo?"

        if Natsuki.isEnamored(higher=True):
            n 4fcspulsbr "Tu salud tiene que ser lo primero,{w=0.2} d-{w=0.2}después de todo."
            n 1ksrbolsbr "..."

            if Natsuki.isLove(higher=True):
                $ chosen_endearment = jn_utils.getRandomEndearment()
                n 1ksrsslsbr "...Incluso si realmente te quiero aquí,{w=0.2} [chosen_endearment]."
                n 4knmboleaf "Realmente espero que te recuperes pronto."
        else:

            n 4fllajlsbr "No me voy a molestar ni nada,{w=0.75}{nw}"
            extend 4fllbolsbr " así que..."
            n 1kllbolsbr "..."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Cansado",
            label="admission_tired",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_tired:

    $ total_hours_in_session = jn_utils.get_current_session_length().total_seconds() / 3600

    if jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1tnmpu "¿Eh?{w=0.75}{nw}"
        extend 2tsqem " ¿{i}Todavía{/i} estás cansado?"
        n 2fnmfl "...¿Entonces qué haces dando vueltas por aquí?{w=0.5}{nw}"
        extend 2fllem " Cielos."
        n 2fcspo "Suena a que alguien necesita otra ronda de sueño,{w=0.2} si me preguntas.{w=0.75}{nw}"
        extend 4fsqsm " Jejeje."
        n 4tsqfl "¿Y bien?{w=0.75}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 4fcsbg " ¡Vete,{w=0.2} [chosen_descriptor]!{w=0.75}{nw}"
        extend 1fchbg " ¡Duerme bien!"

        if Natsuki.isLove(higher=True):
            n 1fchsmleaf "¡Te amo!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fchbleme "¡No dejes que las chinches piquen~!"

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        $ persistent._jn_player_admission_forced_leave_date = datetime.datetime.now()
        $ Natsuki.setForceQuitAttempt(False)

        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 4nllsl "...Sí.{w=0.75}{nw}"
        extend 4tnmfl " ¿Sabes qué?{w=1}{nw}"
        extend 2tnmbo " Probablemente sea lo mejor."
        n 2klraj "Si te sientes enfermo y todo eso,{w=0.75}{nw}"
        extend 2klrbo " como dijiste."
        n 1fcsajlsbr "No te preocupes,{w=0.2} estaré bien.{w=1}{nw}"
        extend 4fcsbglsbr " Siempre lo estoy.{w=1}{nw}"
        extend 2fcssm " Jejeje."
        n 2fchbglsbr "¡Tómatelo con calma,{w=0.2} [player]!"

        if Natsuki.isLove(higher=True):
            n 4fchsmleafsbr "¡T-{w=0.2}te amo!"
            n 4klrbolsbr "..."

        elif Natsuki.isEnamored(higher=True):
            n 4ksrbolsbr "..."
        else:

            n 4ksrbosbl "..."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
        $ Natsuki.setForceQuitAttempt(False)
        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_SICK
        $ persistent._jn_player_admission_forced_leave_date = datetime.datetime.now()

        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 4fcsfl "Bueno,{w=0.75}{nw}"
        extend 4fcsgs " ¡obvio!{w=1}{nw}"
        extend 2fchgn " ¡Por supuesto que te vas a sentir cansado si tienes hambre!"
        n 2tsqflsbr "¿De verdad {i}no{/i} sabías eso?{w=1}{nw}"
        extend 2fcsslsbr " Cielos."
        n 4fcsaj "¡Ahora deja de ser perezoso,{w=0.2} levanta el trasero y ve a buscar algo de una vez!"
        n 4fcsfl "Lo siento [player],{w=0.75}{nw}"
        extend 3fchgn " ¡pero no te lo voy a preparar yo!"

    elif total_hours_in_session >= 18:
        n 2fnmgsl "¡Y-{w=0.2}y a quién tienes que agradecerle por eso?!"
        n 4fbkwrl "¡Has estado aquí por {i}siglos{/i},{w=0.2} [player]!{w=1}{nw}"
        extend 4fnmpol " ¿{i}En serio{/i} no te diste cuenta de la hora?"
        n 1fcsfl "Hombre...{w=0.75}{nw}"
        extend 2fsrpo " {i}realmente{/i} necesitas irte."
        n 2unmfll "¡No me malinterpretes!{w=0.75}{nw}"
        extend 4fcsfllsbl " ¡N-{w=0.2}no es que no te quiera aquí ni nada!{w=1}{nw}"

        if Natsuki.isEnamored(higher=True):
            extend 4ksrpolsbl " ¡P-{w=0.2}por supuesto que sí!{w=1}{nw}"
        else:

            extend 4fcscalsbl " Obviamente."

        n 4fcsajl "Pero claramente {i}alguien{/i} tiene que poner algunos límites por aquí."
        n 3fcspol "...Así que supongo que ese 'alguien' tendré que ser yo.{w=0.75}{nw}"
        extend 3fsqsm " Jejeje."
        $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isAffectionate(higher=True) else player
        n 3fcsbg "¡Ahora vete de una vez,{w=0.2} [chosen_descriptor]!{w=0.75}{nw}"
        extend 4fchbg " ¡Nos vemos luego!"

        if Natsuki.isLove(higher=True):
            n 4fchsml "¡Te amo~!"

        elif Natsuki.isEnamored(higher=True):
            n 4fchsmlsbl "¡D-{w=0.2}dulces sueños!"


        $ Natsuki.addApology(jn_apologies.ApologyTypes.unhealthy)
        $ Natsuki.setForceQuitAttempt(False)
        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        $ persistent._jn_player_admission_forced_leave_date = datetime.datetime.now()

        return { "quit": None }
    else:

        n 2tlraj "¿Sintiéndote cansado,{w=0.75}{nw}"
        extend 2tnmss " ¿eh?"
        n 1tllss "Bueno...{w=1}{nw}"
        extend 4fcsbg " ¿por qué no tomas algo para animarte?{w=0.75}{nw}"
        extend 4fchbg " ¡Duh!"
        n 3ulraj "Digo...{w=0.75}{nw}"
        extend 3nsrsssbr " No me gustan mucho cosas como el café.{w=1}{nw}"
        extend 4fchgn " ¡Pero mentiría si dijera que Monika no se veía renovada después de un trago de esa cosa!"
        n 4ullbo "O...{w=0.75}{nw}"
        extend 4fllsm " ya sabes.{w=0.75}{nw}"
        extend 4fsqbg " Solo ve y échate un poco de agua fría en la cara o algo así."
        n 2fsqsm "Jejeje.{w=0.75}{nw}"
        extend 1nlrss " Nah,{w=0.2} ¿hablando en serio?{w=0.75}{nw}"
        extend 2tnmbo " No sientas que tienes que quedarte ni nada."
        n 2fchgnelg "...¡Solo avísame si te vas {i}antes{/i} de que te golpees la cara contra el escritorio!{w=0.75}{nw}"
        extend 2fchsm " Jejeje."

        if Natsuki.isLove(higher=True):
            n 1fwrsml "¡También te amo,{w=0.2} [player]~!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
