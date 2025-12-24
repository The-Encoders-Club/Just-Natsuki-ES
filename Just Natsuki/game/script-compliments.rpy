default persistent._compliment_database = dict()
init offset = 5
init -5 python in jn_compliments:
    from Enum import Enum
    import random
    import store

    COMPLIMENT_MAP = dict()

    class JNComplimentTypes(Enum):
        """
        Identifiers for different compliment types.
        """
        amazing = 1
        beautiful = 2
        confident = 3
        cute = 4
        hilarious = 5
        inspirational = 6
        style = 7
        thoughtful = 8


    last_compliment_type = None

    def getAllCompliments():
        """
        Gets all compliment topics which are available

        OUT:
            List<Topic> of compliments which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            COMPLIMENT_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_compliments_start:
    python:
        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in jn_compliments.getAllCompliments()
        ]
        compliment_menu_items.sort()

    call screen scrollable_choice_menu(compliment_menu_items, ("Volver", None), 400, "mod_assets/icons/compliments.png")

    if isinstance(_return, basestring):
        $ push(_return)
        jump call_next_topic

    jump talk_menu

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres asombrosa!",
            label="compliment_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_amazing").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.amazing:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 4uskemfesh "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 1fcsemfsbr " ¡Honestamente!{w=0.75}{nw}"
            extend 4kwmemfsbr " ¡¿Otra vez?!{w=1}{nw}"
            extend 4kslpofsbr " Cielos..."
            n 2nslsllsbr "..."
            n 2nslpulsbr "Pero...{w=0.75}{nw}"
            extend 1ksqcalsbr " gracias.{w=0.5} Realmente...{w=0.75}{nw}"
            extend 4ksrcalsbr " significa mucho para mí."
            n 4ksqajlsbr "...¿Y [player]?"
            n 1kslbolsbr "..."
            n 2fcstrl "...Tú también eres bastante asombroso."
            n 2fcspol "Y-{w=0.2}y será mejor que recuerdes eso."

            if Natsuki.isLove(higher=True):
                n 2kchssleaf "¡T-{w=0.2}te amo,{w=0.2} [player]!"
        else:

            n 1nslsslsbr "Cielos,{w=0.2} [player]...{w=0.5}{nw}"
            extend 1klrbolsbr " tú...{w=0.5} realmente estás repartiendo cumplidos hoy,{w=0.5}{nw}"
            extend 4ksrsslsbr " ¿eh?"
            n 2fcsajl "¡N-{w=0.2}no me malinterpretes!{w=0.5}{nw}"
            extend 2fcsbglsbl " ¡No me estoy quejando!"
            extend 2fcssmlsbl " ¡E-{w=0.2}es bueno saber que {i}ambos{/i} estamos de acuerdo!"
            extend 4nslsslsbr " Solo..."
            n 1ksqbolsbr "Asegúrate de no dejarte fuera,{w=0.2} ¿vale?"
            n 4kllsslsbr "Eres {i}casi{/i} tan asombroso,{w=0.2} d-{w=0.2}después de todo."
            n 3fsqdvlsbr "...{i}Casi{/i}."
            extend 3fchbllsbr " Jejeje."
    else:

        if Natsuki.isEnamored(higher=True):
            n 1kwmpul "...T{w=0.2}-tú realmente piensas eso,{w=0.5}{nw}"
            extend 1kllpul " ¿[player]?"
            n 4kllsrl "..."
            n 1ncsssl "Je."
            n 2fslpolsbl "Siempre es súper vergonzoso decirlo,{w=0.2} sabes."
            n 2kslbol "..."
            n 2ncspul "Pero...{w=0.75}{nw}"
            extend 2kwmbol " gracias."
            n 4fcsajlsbr "Significa...{w=0.75}{nw}"
            extend 1ksrsllsbr " mucho para mí,{w=0.5} [player]."
            n 1ksqsllsbr "En serio.{w=0.75}{nw}"
            extend 4ksqbol " Gracias.{w=0.75}{nw}"
            extend 4kcspul " Eres honestamente...{w=1}{nw}"
            $ chosen_descriptor = jn_utils.getRandomDescriptor()
            extend 1ksrcal " [chosen_descriptor],{w=0.3} [player]."
            n 1ksrfsl "..."

            if Natsuki.isLove(higher=True):
                n 4kchssf "T-{w=0.2}te amo."
        else:

            n 1uskgslesh "¡O-{w=0.2}oh!{w=0.5}{nw}"
            extend 4fllbglesssbr " ¡A-{w=0.2}aja!{w=0.5}{nw}"
            extend 2fcsbglsbr " Bueno,{w=0.2} ¡sabía que tendrías que admitirlo {i}eventualmente{/i}!"
            n 2fcssmlsbl "Solo me alegra escuchar que {i}ambos{/i} estamos de acuerdo en eso.{w=0.75}{nw}"
            extend 1fsldvlsbl " Jejeje."

            if Natsuki.isAffectionate(higher=True):
                n 3fcsssl "S-{w=0.2}solo recuerda,{w=0.2} [player]..."
                n 3fchbll "¡Eres al {i}menos{/i} el segundo mejor!"
            else:

                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchgnlsbr "¡Gracias,{w=0.2} [chosen_tease]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.amazing
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres hermosa!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_beautiful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.beautiful:
        if Natsuki.isEnamored(higher=True):
            $ player_initial = jn_utils.getPlayerInitial()
            n 1fcsanlesssbl "¡Uuuuuu-!"
            n 4kwdgslesssbl "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
            extend 1kbkwrless " ¡Ya me dijiste eso!"
            n 4ksqemlsbr "¡¿Realmente tienes que hacerlo {i}de nuevo{/i}?!"
            n 2ksrbolsbr "..."
            n 2ncsemlesisbr "..."
            n 1ncsbolsbr "...Bien.{w=0.75}{nw}"
            extend 4kslbolsbl " Lo tomaré."
            n 2fcscalsbl "El cumplido,{w=0.2} quiero decir.{w=0.75}{nw}"
            extend 2fcstrlsbl " Solo..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1ksrcal "..."
            n 4ncsssl "...Je.{w=1}{nw}"
            extend 4nslfsl " Olvídalo."

            if Natsuki.isLove(higher=True):
                n 2kslbol "G-{w=0.2}gracias de nuevo,{w=0.2} [chosen_tease]."
                n 1kslfsfeaf "...S-{w=0.2}siempre me haces sentir más bonita."
            else:

                n 2kslbol "G-{w=0.2}gracias de nuevo,{w=0.2} [chosen_tease]."
                n 1kslcaf "..."
        else:

            n 4fskgslesh "¡¿D-{w=0.2}disculpa?!"
            n 1fwmgslsbl "¡[player]!{w=0.5}{nw}"
            extend 4fbkwrlsbl " ¡¿Qué es lo que {i}literalmente{/i} te acabo de decir?!"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcsgsl " ¡¿Estás {i}intentando{/i} darme un infarto o algo así?!{w=0.75}{nw}"
            extend 2fsleml " Cielos..."
            n 2fslpol "..."
            n 4fcsajl "Q-{w=0.2}quiero decir,{w=0.75}{nw}"
            extend 3fcspol " ¡sé que ya me veo genial!{w=1}{nw}"
            extend 3fsrdvlsbl " {i}Siempre{/i} me veo de primera,{w=0.2} p-{w=0.2}por supuesto."
            n 2fcsemlsbl "Pero {i}realmente{/i} no tienes que... "
            n 2fslunlsbl "¡S-{w=0.2}seguir...!"
            n 1fcsunlsbl "..."
            n 4fcsemlsbr "¡Oh,{w=0.5}{nw}"
            extend 2flrbolsbr " olvídalo!"

            if Natsuki.isAffectionate(higher=True):
                n 2fcscalsbr "Sabes a lo que me refiero,{w=0.2} d-{w=0.2}de todas formas..."

            n 2ksrbolsbr "..."
    else:

        if Natsuki.isEnamored(higher=True):
            n 4uskemlesh "¡¿E-{w=0.2}eh?!"
            n 1fcseml "Espera..."
            n 1kllemlsbl "T-{w=0.2}tu realmente piensas que soy..."
            n 1fslunfsbl "Q-{w=0.3}que soy..."
            n 4fcsunfesssbr "..."
            n 2kcsbolsbr "..."
            n 2ksqbolsbr "[player]..."
            n 1kllbolsbr "Sabes {w=0.2}{i}bien{/i}{w=0.2} que no deberías decir cosas así... "
            n 4kwmslfsbl "¿A menos que las digas en serio?"

            if Natsuki.isLove(higher=True):
                n 1knmajlsbl "¡N-{w=0.2}no es que no te crea!{w=1}{nw}"
                extend 2klrsslsbl " ¡P-{w=0.2}por supuesto que no!"
                n 4ksrbolsbl "...Deberías saberlo a estas alturas."
                n 2ksrpulsbl "Pero..."
                n 4ksrsll "..."
                n 1ksrfsl "...Gracias,{w=0.2} [player].{w=1}{nw}"
                extend 1ksrssl " En serio{w=0.2}, je."
                n 4ksqfsl "Gracias."
                n 3fcssmless "...Solo no olvides {i}quién{/i} me ayuda a sentirme así.{w=0.75}{nw}"
                extend 3fsqbll " Tonto."
                n 4fchsmleaf "Jejeje."
            else:

                n 1kslcafsbl "..."
                n 2fcstrlesssbr "¡Q-{w=0.2}quiero decir...!"
                n 2nsrsllsbr "...{w=0.75}{nw}"
                extend 2ksrbolsbr "En serio."
                n 2ksrfslsbr "G-{w=0.2}gracias, [player]."
        else:

            n 1uskemlesh "¿Q{w=0.2}-q{w=0.2}-qué?"
            n 1fskeml "¡¿Q-{w=0.2}qué dijiste?!"
            n 4fcsanfsbr "¡Nnnnnnnnnn-!"
            n 4fbkwrfsbr "¡N-{w=0.2}no puedes simplemente {i}decir{/i} cosas así tan de repente!"
            n 2fllemlsbl "Cielos...{w=0.75}{nw}"
            extend 2fslpolsbl " vamos,{w=0.2} [player]..."
            n 1fcsbolsbr "..."
            n 1fcsemlsbr "Q-{w=0.2}quiero decir,{w=0.75}{nw}"
            extend 3fsrbglsbr " Me alegra que ambos estemos de acuerdo,{w=0.75}{nw}"
            extend 4fsrunlsbr " pero..."
            n 1fcsunlesssbl "¡Uuuuuu...!"
            n 1fcsemlsbl "Solo..."
            n 1kslcal "..."
            n 2ksqsllsbr "...Piensa un poco antes de soltar cosas así.{w=0.75}{nw}"
            extend 2fsrsllsbr " S-{w=0.2}solo hace que todo sea muy incómodo."
            n 1fsrsslsbr "...Je.{w=0.75}{nw}"
            extend 4fcsajlsbr " Y-{w=0.2}y además,{w=0.75}{nw}"
            n 3fcsbglsbl " ¡{i}Siempre{/i} me veo deslumbrante de todos modos!{w=0.75}{nw}"
            extend 3nslsslsbl " Así que...{w=0.5}{nw}"
            extend 3nslbol " sí."
            n 3kslsllsbr "..."

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.beautiful
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta lo segura que eres!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_confident").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.confident:
        n 1fcssmleme "Jejeje.{w=0.5}{nw}"
        extend 2fcsbg " Bueno,{w=0.2} ¡me alegra que sigas de acuerdo,{w=0.2} [player]!"
        n 2fllsm "Además,{w=0.5}{nw}"
        extend 2fcssm " es solo natural."

        if Natsuki.isEnamored(higher=True):
            n 4nslssl "E-{w=0.2}especialmente contigo cerca,"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 3fchbll " [chosen_tease]."
        else:

            n 2fcsbgedz "Rebosante de confianza,{w=0.5}{nw}"
            extend 2flrbs " siempre imperturbable..."
            n 3uchgnl "...Eso es justo lo que significa ser una pro,{w=0.2} ¿verdad?"
    else:

        n 4fsqct "¿Ojo?{w=1}{nw}"
        extend 3fsqcs " Lo haces,{w=0.2} ¿verdad?"
        n 3fchgn "¡Ahora eso es {i}justo{/i} lo que me gusta escuchar!"
        n 4fcsbg "Después de todo,{w=0.5}{nw}"
        extend 2fcssmeme " ¿a que simplemente {i}irradio{/i} confianza?"
        n 4tsqbg "¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
        extend 4fchgn " ¡No hay necesidad de ser tímido!{w=0.5}{nw}"
        extend 4fsqbg " ¡{i}Tienes{/i} que decírmelo!"
        n 3fllct "¿Son los ojos?"
        n 3fcsbg "¿La sonrisa?"
        n 3usqsm "¿La personalidad {i}asesina{/i}?"
        n 4fchsmedz "Jejeje."
        n 2fcsss "Bueno,{w=0.2} sea lo que sea..."

        if Natsuki.isLove(higher=True):
            n 4nsrsmsbl "..."
            n 4fcssmlsbl "E-{w=0.2}espero inspirarte tanto como tú me inspiras a mí.{w=0.75}{nw}"
            extend 4fchdvlsbl " Jejeje."
            n 1fchbgleafsbr "¡T-{w=0.2}te amo,{w=0.2} [player]!"

        elif Natsuki.isEnamored(higher=True):
            n 2fcsbg "¡Espero inspirarte algo de confianza a ti también!"
            n 2fslbglsbr "N-{w=0.2}no es que la necesites {i}demasiado{/i},{w=0.2} d-{w=0.2}de todas formas."
            n 2fchbglsbr "¡D-{w=0.2}de nada,{w=0.2} [player]!"
        else:

            n 2fchgnl "¡Será mejor que inspire algo de confianza en ti también!"
            n 2fwlsm "¡De nada,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.confident
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres linda!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_cute").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.cute:
        if Natsuki.isEnamored(higher=True):
            n 1fskwrleshsbr "..."
            n 4fcsanlsbr "..."
            n 4fcsfulsbl "..."
            n 1fcsfufsbl "¡Urgh!"
            n 4fcsgsf "¡Está bien,{w=0.5}{nw}"
            extend 1fcsemfsbl " bien!{w=0.5}{nw}"
            extend 2fcswrfsbl " ¡Bien!{w=0.5}{nw}"
            extend 2fbkwrfsbl " ¡Tú ganas,{w=0.2} ¿vale?!"
            n 2fcsunfesi "..."
            n 2fcsemf "Soy un poco...{w=0.5} tal vez...{w=0.75}{nw}"
            extend 1fslemf " algo así..."
            n 1fcsgsf "De alguna manera..."
            n 4fsqemf "En alguna forma {i}abstracta{/i}..."
            n 1fsrsrf "..."
            n 1fsqpuf "...{w=0.3}'linda'."
            n 2fsqslf "..."
            n 2fcsemf "Ahí.{w=0.75}{nw}"
            extend 2fcsgsf " Lo dije,{w=0.2} [player].{w=0.75}{nw}"
            extend 2fcspof " Lo dije.{w=0.75}{nw}"
            extend 2fllpof " {i}Hurra{/i} por ti."
            n 1fsqpof "¿Terminamos?{w=0.75}{nw}"
            extend 4fnmpof " ¿Estás feliz?{w=0.75}{nw}"
            extend 2fcsgsf " ¿Estás {i}satisfecho{/i} contigo mismo ahora?"
            n 1flrpof "Cielos..."
            n 2fsqpof "Juro,{w=0.2} que eres tan tonto a veces..."

            if Natsuki.isLove(higher=True):
                n 1fcspol "Y-{w=0.2}y además,{w=0.2} [player]."
                n 3fcsajl "¿Toda esta charla sobre {i}lindura{/i}?{w=0.75}{nw}"
                extend 3flrcal " ¿Ser {i}adorable{/i}?"
                n 1fsqssl "...Je."
                n 2fcssslsbl "S-{w=0.2}suena como una proyección bastante mala,{w=0.5}{nw}"
                extend 4fcsbglsbl " s-{w=0.2}si me preguntas."
                n 3fsqcsl "..."
                n 3fsqbgl "...¿Tengo razón,{w=0.5} {i}[player]{/i}?"
                n 3fsqsmlsbr "Jejeje."
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbllsbr "¡T-{w=0.2}te amo también,{w=0.2} [chosen_tease]~!"
            else:

                n 1fcsajl "Solo...{w=1}{nw}"
                extend 2fsrcal " no dejes que esto se te suba a la cabeza."
                n 2fsqajlsbl "...O vas a descubrir exactamente qué tan {w=0.4}{i}no{/i}{w=0.4} linda{w=0.4} puedo ser también."
                n 4fsqfsl "Jejeje."
        else:

            n 1fcsanfsbl "¡Nnnnnnn-!"
            n 4fcsgsf "¡¿C-{w=0.2}cuántas veces tengo que explicar esto?!"
            extend 4fllemf " ¿Realmente tengo que deletreártelo también,{w=0.2} [player]?!"
            n 4fcsanf "Por {i}última vez{/i}..."
            n 1fbkwrfsbl "¡¡{i}NO{w=0.3} SOY{w=0.3} LINDA!!{/i}"
            n 1flremf "Cielos..."
            n 2fsrpol "..."
            n 2fsqeml "...Solo {i}querías{/i} que dijera eso,{w=0.2} ¿verdad?"
            n 4fcspolesi "Honestamente...{w=0.75}{nw}"
            extend 3fsqcal " puedes ser tan idiota a veces,{w=0.2} [player]."

            if Natsuki.isAffectionate(higher=True):
                n 3nslcal "..."
                n 1nllajl "Bueno..."
                n 2fcspol "Solo considérate afortunado de que estés en mi lista buena."
                n 2fsqsslsbl "O-{w=0.2}o no sería {i}ni de cerca{/i} tan paciente.{w=0.75}{nw}"
                extend 2fsqsmlsbl " Jejeje."
            else:

                n 3nslcal "..."
                n 1nllajl "Bueno...{w=0.75}{nw}"
                extend 1nslpol " lo que sea."
                n 2fcscal "Solo agradece que me guardaré todo el sermón para ti."
                n 2fsqssl "...Esta vez."
    else:

        if Natsuki.isEnamored(higher=True):
            n 1fcsbslsbr "¡A-{w=0.2}Aja!{w=0.5}{nw}"
            extend 2fchbglsbr " ¡Nop!"
            n 2fsqfslsbr "..."
            n 4fsqsmlsbr "Buen intento,{w=0.2} [player]..."
            n 3fcsbgl "¡Pero no conseguirás que lo diga {i}tan{/i} fácilmente!{w=0.5}{nw}"
            extend 3fcssmlsbl " Jejeje."
        else:

            n 4uskemfesh "¿Q{w=0.2}-q{w=0.2}-qué?"
            n 4fnmemfsbl "¡¿{i}Qué{/i} acabas de decir?!"
            n 1fllunfsbl "..."
            n 1nsrsrfsbr "..."
            n 2fsrssfsbr "Yo...{w=0.75}{nw}"
            extend 2fsqunfsbr " debo haberte escuchado mal."
            n 4fcsbgl "S-{w=0.2}sí.{w=0.5}{nw}"
            extend 3fchbgl " ¡Sí!{w=0.75}{nw}"
            extend 3fcssslsbl " ¡Te escuché {i}totalmente{/i} mal!{w=0.5} C-{w=0.2}cien por ciento."
            n 3fslunlsbl "..."

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.cute
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta tu sentido del humor!",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_hilarious").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.hilarious:
        n 4usqss "¿Oh...?"
        n 3tsqcs "¿Qué es esto?{w=0.75}{nw}"
        extend 3fcsbg " ¿Un bis o algo así?"
        n 4uchgnl "Bueno,{w=0.3} ¡lo tomo!"
        n 2fsqfs "No te preocupes,{w=0.2} [player]..."

        if Natsuki.isEnamored(higher=True):
            n 2fchbgleme "¡No escaparás de {i}nuestra{/i} rutina pronto!{w=0.5}{nw}"
            extend 4fchsml " Jejeje."

            if Natsuki.isLove(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbll "¡Te amo también,{w=0.2} [chosen_tease]~!"
        else:

            n 2fchsmeme "¡No escaparás de {i}mi{/i} rutina pronto!{w=0.5}{nw}"
            extend 2nchgnl " Jajaja."
    else:

        if Natsuki.isEnamored(higher=True):
            n 4fcscs "¿Ojo?{w=0.75}{nw}"
            extend 3fcsbg " ¿Qué es eso,{w=0.2} [player]?"
            n 3fchgnlelg "¡Así que {i}sí{/i} reconoces el talento cuando lo ves!{w=0.75}{nw}"
            extend 4fcssml " Jejeje..."
            n 2nslfsl "..."
            n 2nslbol "Pero...{w=0.75}{nw}"
            extend 2tsqcal " ¿en serio,{w=0.2} [player]?"
            n 1ksrcal "..."
            n 1klrss "Honestamente...{w=0.75}{nw}"
            extend 4nsrss " me alegra un poco escuchar eso."
            n 1fcsajlsbr "S-{w=0.2}sé que es tonto.{w=0.75}{nw}"
            extend 4nslbolsbr " Pero siempre me preocupa un poco cuánto te diviertes aquí."
            n 4nlrcalsbr "Conmigo,{w=0.2} quiero decir."
            n 4ksqbolsbl "Yo...{w=0.3} no quiero que te aburras..."
            n 2fcsajlsbl "E-{w=0.2}eso sería súper patético."
            n 1kllbol "Así que...{w=0.5}{nw}"
            extend 1knmbol " gracias,{w=0.2} [player].{w=0.5}{nw}"
            extend 2klrfsl " En serio."
            n 2nsrsslsbl "Significa mucho."

            if Natsuki.isLove(higher=True):
                n 4fchsmleaf "S-{w=0.2}siempre sabes justo qué decir."
        else:

            n 1fcssm "Jejeje.{w=0.75}{nw}"
            extend 2fchgneme " Oh,{w=0.2} ¡{i}apuesta{/i} a que tengo un sentido del humor asombroso!"
            n 4ullss "Pero...{w=0.5}{nw}"
            extend 3fcsbsl " solo me alegra que ambos reconozcamos eso."

            if Natsuki.isAffectionate(higher=True):
                $ chosen_tease = jn_utils.getRandomTease()
                n 3fchbll "¡Muy agradecida,{w=0.2} [chosen_tease]!"
            else:

                n 3fchbgl "¡Muy agradecida,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.hilarious
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Eres una inspiración para mí!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_inspirational").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.inspirational:
        n 1nchgn "Jajaja.{w=0.75}{nw}"
        extend 2fcsbg " Bueno,{w=0.2} ¿qué puedo decir?{w=0.75}{nw}"
        extend 2fchsmedz " Supongo que debe ser natural~."
        n 1nchsm "¡Pero gracias,{w=0.2} [player]!"
        n 4fsqsm "No te preocupes."
        extend 3fwlbg " ¡Siempre puedes contar con su servidora para {i}todas{/i} tus necesidades de inspiración!"

        if Natsuki.isEnamored(higher=True):
            n 3fsrssl "S-{w=0.2}solo como sé que puedo contar contigo.{w=0.75}{nw}"
            extend 1fchsml " Jejeje."
    else:

        n 4unmemleex "¿E-{w=0.2}eh?{w=0.75}{nw}"
        extend 2flrbglsbr " B-{w=0.2}bueno,{w=0.2} ¡sí!{w=0.75}{nw}"
        extend 2fcsbglsbr " ¡Obvio!"
        n 2fchgnsbr "¡Por supuesto que lo soy,{w=0.2} tonto!{w=1}{nw}"
        extend 4fllct " De hecho..."
        n 1fcsct "Me atrevería a decir que te costaría encontrar un {i}mejor{/i} modelo a seguir que yo."
        n 3fsqsmeme "Jejeje."

        if Natsuki.isEnamored(higher=True):
            n 3ullaj "Bueno,{w=0.2} como sea.{w=0.75}{nw}"
            extend 4fwlbg " ¡De nada,{w=0.2} [player]!"
            n 2fchbgl "{i}Siempre{/i} estaré cerca para inspirarte."

            if Natsuki.isLove(higher=True):
                n 2nsrsmlsbl "...Tú haces lo mismo por mí,{w=0.2} d-{w=0.2}después de todo."
        else:

            n 3fcsbgedz "Bueno,{w=0.2} siéntete libre de inspirarte en mí en cualquier momento,{w=0.2} [player].{w=1}{nw}"
            extend 4fsqss " Después de todo..."
            n 2fwlbg "Eso es para lo que están los profesionales,{w=0.2} ¿verdad?"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.inspirational
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta tu estilo!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_style").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.style:
        if not Natsuki.isWearingOutfit("jn_school_uniform"):


            if Natsuki.isEnamored(higher=True):
                n 1fcssm "Jejeje.{w=0.5}{nw}"
                extend 3fcsbgeme " ¿Aún asombrado por mi sentido de la moda,{w=0.2} [player]?"
                n 3ullss "Bueno,{w=0.5}{nw}"
                extend 4tllsm " si no es otra cosa -{w=0.5}{nw}"
                extend 2fcssm " no puedes negar que me visto con estilo."

                if Natsuki.isLove(higher=True):
                    n 2fsqsml "No te preocupes.{w=0.75}{nw}"
                    extend 2uchgnledz " ¡Seguiré luciendo fabulosa sooooolo para ti~!"
                else:

                    n 2fchsml "¡Muchas gracias,{w=0.2} [player]!{w=0.75}{nw}"
                    extend 2fchgnledz " ¡Se aprecia!"
            else:

                n 4tnmaj "¿Oh?{w=0.5}{nw}"
                extend 2tsqss " Suena a que {i}alguien{/i} se muere por ganar unos puntos,{w=0.2} ¿eh?"
                n 2fsqsm "Jejeje."
                n 1fchbg "¡Relájate,{w=0.2} relájate!{w=0.5}{nw}"
                extend 1uchsm " Estoy bromeando,{w=0.2} [player].{w=0.3} No te preocupes."
                n 4fsqsm "...Mayormente."
                n 3fwlbl "¡Pero gracias de nuevo!"
        else:


            if Natsuki.isEnamored(higher=True):
                n 4usqct "¿Oh?{w=0.75}{nw}"
                extend 4fsqctl " Nunca me dijiste que tenías algo por los uniformes,{w=0.2} [player]."
                n 2fsqbglsbl "¿H-{w=0.2}hay algo que quieras decirme?{w=0.75}{nw}"
                extend 2fnmsglsbl " ¿Eh?"
                n 1flldvlsbl "..."
                n 4fchdvlesisbr "¡Pfffft-!"
                n 4fcsajl "Oh,{w=0.5}{nw}"
                extend 1fchbgl " ¡relájate,{w=0.2} [player]!{w=0.75}{nw}"
                extend 2fllbgl " Cielos..."
                n 2fchsmlsbr "Y-{w=0.2}ya deberías saber cuándo te estoy tomando el pelo,{w=0.2} tonto.{w=1}{nw}"
                extend 1fcsssl " Y además..."
                n 2flldvl "{i}Sé{/i} que luzco totalmente el look escolar."
                n 2fchbll "¡Pero gracias de todos modos!"
            else:

                n 2fsqsmlsbl "¿Todavía perdidamente enamorado del look educado,{w=0.5}{nw}"
                extend 2fcssslsbl " eh?"
                n 2fcsbglesssbl "B-{w=0.2}bueno,{w=0.75}{nw}"
                extend 2fllbglesssbr " ¡supongo que eso solo significa que puedo hacer que {i}cualquier cosa{/i} se vea bien!"
                n 1fslsslesssbr "Jajaja..."
    else:


        if not Natsuki.isWearingOutfit("jn_school_uniform"):


            if Natsuki.isEnamored(higher=True):
                n 1fchsmleme "Jejeje.{w=0.75}{nw}"
                extend 1nchsml " ¡Solo estoy feliz de que te guste este atuendo,{w=0.2} [player]!"
                n 1ulrbol "Pero entonces...{w=0.75}{nw}"
                extend 4tlrbol " ahora que lo pienso..."
                n 2tsqssl "¿Debería {i}realmente{/i} sorprenderme?"
                n 3fcsbgl "¡Y-{w=0.2}yo {i}soy{/i} la que lo lleva puesto,{w=0.5}{nw}"
                extend 3uchgnl " después de todo!"

                if Natsuki.isLove(higher=True):
                    n 3fchblleaf "¡Te amo también,{w=0.2} [player]~!"
            else:

                n 1fcsbglsbl "¡J-{w=0.2}ja!{w=0.5}{nw}"
                extend 2flrbglsbl " ¡Me alegra que estés de acuerdo!"
                n 4fcssml "Es solo natural,{w=0.2} ¿verdad?{w=0.5}{nw}"
                extend 2fcsbgledz " ¡Me gusta enorgullecerme de mi {i}soberbio{/i} sentido del estilo!"
                n 2fwlbll "¡Buen trabajo notándolo,{w=0.2} [player]!"
                extend 2fchgnl " Jejeje."
        else:


            if Natsuki.isEnamored(higher=True):
                n 1tnmpul "¿M-{w=0.2}mi sentido del estilo?"
                n 1tslpu "..."
                n 4tslaj "Tú...{w=0.75}{nw}"
                extend 2fsldv " {i}sí{/i} ves lo que llevo puesto,{w=0.75}{nw}"
                extend 2fchgn " ¿verdad?"
                n 1nlrss "Viejo...{w=0.75}{nw}"
                extend 2fsqsm " eres tan tonto a veces,{w=0.2} [player].{w=0.75}{nw}"
                extend 2fcsbg " ¡Pero la intención es lo que cuenta!"
                n 4fchsm "Jejeje."
                $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
                n 2fchgnl "¡Se aprecia como siempre,{w=0.2} [chosen_descriptor]!"
            else:

                n 1tnmpuleqm "M-{w=0.2}mi sentido del estilo..."
                n 4tsqpu "...¿Qué?{w=0.75}{nw}"
                extend 2tnmdv " ¿Te refieres a mi uniforme escolar?"
                n 4fchdvesi "¡Pfffft-!"
                n 1fchbselg "¡¿Qué clase de cumplido es {i}ese{/i}?!"
                n 2tlrsslsbl "Realmente {w=0.2}{i}no{/i}{w=0.2} eres bueno en este tipo de cosas,{w=0.5}{nw}"
                extend 2tnmsmlsbl " ¿verdad, [player]?{w=0.5}{nw}"
                extend 2fsqsmlsbl " Jejeje."
                n 1fcsbgl "Bueno,{w=0.75}{nw}"
                extend 1fllbgl " ¡s-{w=0.2}supongo que lo intentaste!{w=0.75}{nw}"
                extend 4fcssmeme " ¿Y no es eso lo que siempre importa?"
                n 3fchgn "¡Gracias de todos modos,{w=0.2} tonto!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.style
    return

init python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta lo atenta que eres!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    $ Natsuki.calculatedAffinityGain(bypass=get_topic("compliment_thoughtful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.JNComplimentTypes.thoughtful:
        if Natsuki.isEnamored(higher=True):
            n 1unmaj "...Guau.{w=0.75}{nw}"
            extend 1ulrbo " Tú...{w=0.75}{nw}"
            extend 4tnmssl " realmente sigues obsesionado con eso, ¿eh?"
            n 1ncsajl "Pero en serio,{w=0.2} [player] -{w=0.5}{nw}"
            extend 3fchbglsbl " ¡no te preocupes por eso!{w=0.75}{nw}"
            extend 3fcssmlesisbl " Está totalmente bien."
            n 1fllbol "Además,{w=0.75}{nw}"
            $ friend_type = "novia" if Natsuki.isLove(higher=True) else "amiga"
            extend 2fcseml " ¿qué clase de [friend_type] sería si {i}no{/i} estuviera al menos intentando ser atenta?"
            n 2fsrbglsbr "¡A-{w=0.2}además parece que lo estás intentando igual de todos modos!"
            n 4tsrbolsbr "..."
            n 1tsrpu "Bueno,{w=0.5}{nw}"
            extend 1fsrsssbl " si tranquiliza tu mente...{w=1}{nw}"
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            extend 3fcssml " ¡no hay problema,{w=0.2} [chosen_descriptor]!"
            n 3fchgnledz "¡No tienes que pedirme que siga así!"
        else:

            n 1unmpul "¿E-{w=0.2}eh?{w=0.75}{nw}"
            extend 1fllbgl " Oh,{w=0.2} cierto.{w=0.5}{nw}"
            extend 4fsldvl " Jajaja."
            n 2unmaj "Bueno,{w=0.5}{nw}"
            extend 2ulraj " justo como decía antes -{w=0.5}{nw}"
            extend 2fcsaj " realmente {i}no{/i} es mucho pedir en absoluto."
            n 3fchgn "...¡Así que no te preocupes por eso,{w=0.2} tonto!"
            n 3fwlsm "¡No me cuesta nada!"
    else:

        if Natsuki.isEnamored(higher=True):
            n 2nslss "Viejo...{w=0.75}{nw}"
            extend 2fchgnl " ¡haces que suene como si tuviera que esforzarme o algo así!"
            n 1fcssmlsbl "Jajaja."
            n 4ullss "Nah,{w=0.75}{nw}"
            extend 3fcsss " no es nada."
            n 1unmbo "Ser un poco atenta es lo que {i}la mayoría{/i} de la gente merece,{w=0.2} al menos.{w=1}{nw}"
            extend 2flrca " Yo medio considero eso ser una persona decente."
            n 2ulraj "Dicho esto,{w=0.2} [player]."
            n 1fcscal "No me importa esforzarme un poco más por ti..."
            n 4fsqssl "...Pero solo un {i}poco{/i}.{w=0.75}{nw}"
            extend 4fchsml " Jejeje."

            if Natsuki.isLove(higher=True):
                n 1fchgnl "¡Te amo también,{w=0.2} [player]~!"
            else:

                n 1fchbgl "¡Cuando quieras,{w=0.2} [player]!"
        else:

            n 2tnmpuleqm "¿Eh?{w=0.75}{nw}"
            extend 2tnmajl " ¿Atenta?"
            n 1fllbglesssbl "B-{w=0.2}bueno...{w=0.75}{nw}"
            extend 4fchbglsbl " ¡sí!{w=0.75}{nw}"
            extend 4fsrdvlsbl " Al menos {i}me gusta{/i} pensar eso,{w=0.2} de todas formas."
            n 3unmbo "Aunque no es mucho pedir.{w=1}{nw}"
            extend 3nllsssbr " Ser atenta,{w=0.2} quiero decir."
            n 1ulrbosbr "Honestamente,{w=0.5}{nw}"
            extend 2tlrcasbr " es realmente lo {i}menos{/i} que cualquiera puede esperar."
            n 2uchgn "¡Pero oye,{w=0.2} lo tomaré!"
            n 2fchsm "¡De nada,{w=0.2} [player]!"

    $ jn_compliments.last_compliment_type = jn_compliments.JNComplimentTypes.thoughtful
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
