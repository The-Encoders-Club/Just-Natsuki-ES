default persistent._apology_database = dict()
init offset = 5

default -5 persistent._jn_player_apology_type_on_quit = None


default -5 persistent._jn_player_pending_apologies = list()

init -5 python in jn_apologies:
    from Enum import Enum
    import store

    APOLOGY_MAP = dict()

    class ApologyTypes(Enum):
        """
        Identifiers for different nickname types.
        """
        bad_nickname = 1
        cheated_game = 2
        generic = 3
        prolonged_leave = 4
        rude = 5
        sudden_leave = 6
        unhealthy = 7
        scare = 8
        bad_player_name = 9
        
        def __str__(self):
            return self.name
        
        def __int__(self):
            return self.value

    def getAllApologies():
        """
        Gets all apology topics for the currently pending apologies, as well as the generic

        OUT:
            List<Topic> for all current pending apologies
        """
        return_apologies = [
            store.get_topic("apology_generic")
        ]
        for apology_type in store.persistent._jn_player_pending_apologies:
            return_apologies.append(store.get_topic(str("apology_{0}".format(ApologyTypes(apology_type)))))
        
        return return_apologies


label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in jn_apologies.getAllApologies()
        ]
        apologies_menu_items.sort()

    call screen scrollable_choice_menu(apologies_menu_items, ("Go back", None), 400, "mod_assets/icons/apologies.png")

    if isinstance(_return, basestring):
        $ push(_return)
        jump call_next_topic

    jump talk_menu


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por darte un nombre hiriente.",
            label="apology_bad_nickname",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:
    if persistent._jn_nicknames_natsuki_allowed:

        if Natsuki.isEnamored(higher=True):
            n 1fcssl "...[player].{w=1}{nw}"
            extend 2fsqsl " {i}Realmente{/i} tienes que preguntarte algo aquí."
            n 2fcsaj "Escúchame."
            n 2fcsbo "..."
            n 2nllpu "Estoy...{w=0.75}{nw}"
            extend 4nllsl " dispuesta...{w=1}{nw}"
            extend 4nnmca " a dejar que me llames de otra manera."
            n 1flrbo "Algo {i}diferente{/i} al nombre por el que me han llamado toda mi vida."
            n 3tnmpu "{i}Sabes{/i} de qué se trata eso,{w=0.2} ¿verdad?{w=0.75}{nw}"
            extend 3tsqsl " ¿Qué significa?"
            n 1ncsaj "Es una muestra de confianza."
            n 2fsqem "...Así que, ¿qué crees {i}seriamente{/i} que demuestra cuando usas esa confianza para {i}insultarme{/i}?"
            n 2fcspu "..."
            n 2nllsl "Me...{w=0.75}{nw}"
            extend 1kslbo " alegra que hayas elegido disculparte."
            n 1kcssl "Solo por favor...{w=0.75}{nw}"
            extend 4ksqsll " trata de considerar mis sentimientos la próxima vez."
            n 2ksrajl "Realmente {i}no{/i} es mucho pedir.{w=0.75}{nw}"
            extend 2tsqbol " ¿Verdad?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 2fcsbo "..."
            n 2ncspuesi "..."
            n 2nslsl "...Bien.{w=0.75}{nw}"
            extend 2fcsaj " Acepto tu disculpa,{w=0.2} ¿okey?"
            n 1fsqsl "Solo deja de hacerlo ya,{w=0.2} [player]."
            n 4fllpu "No es {i}gracioso{/i}.{w=0.5}{nw}"
            extend 4fnmem " No es una {i}broma{/i}."
            n 2fcsca "...Y sé que eres mejor que {i}eso{/i}."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsem "...Je.{w=0.75}{nw}"
            extend 4fsqwr " Oh,{w=0.2} ¿{i}en serio{/i}?"
            n 2fllem "...¿Estás seguro,{w=0.2} [player]?"
            n 2fcsem "Porque quiero decir...{w=0.75}{nw}"
            extend 2fsqsl " si {i}realmente{/i} te importaran mis sentimientos..."
            n 4fnman "¿Por qué siquiera {i}pensarías{/i} en hacer eso en primer lugar?"
            n 1fcsan "No eres gracioso,{w=0.2} [player]."
            extend 4flrem " No estás haciendo {i}reír{/i} a nadie."
            n 2fsqfu "...Solo estás siendo un idiota."
            n 2fcsbo "..."
            n 2fcsem "...Lo que sea.{w=0.75}{nw}"
            extend 1fslbo " Tomaré tu disculpa."
            n 1fsqsl "Pero no voy a aguantar mucha más basura de ti."
            n 2fnmsl "¿Entendido?"

            $ Natsuki.calculatedAffinityGain()
        else:

            n 2fcsan "...Honestamente no sé qué encuentro más {i}asqueroso{/i} de ti,{w=0.2} [player]."
            n 2fcsaj "El hecho de que siquiera lo hicieras en primer lugar..."
            n 4fsqful "...O que pienses que una simple disculpa hace que todo esté b-{w=0.2}bien."
            n 1fcssrl "..."
            n 1fcsanltsa "No pienses que esto cambia nada,{w=0.2} {i}[player]{/i}."
            n 4fsqsrltsb "Porque {i}no lo hace.{/i}"
    else:


        if Natsuki.isEnamored(higher=True):
            n 1ncspu "...[player]."
            n 1fcssl "Te lo advertí.{w=1}{nw}"
            extend 4fnmun " Te lo advertí {i}{w=0.3}tan{w=0.3}tas{w=0.3} veces{/i}."
            n 1fsqem "¿En serio pensaste que disculparte {i}ahora{/i} cambiaría algo?"
            n 2fcsslesi "..."
            n 2fllsl "...Mira."
            n 2nllbo "Aprecio la disculpa,{w=0.5}{nw}"
            extend 1fnmbo " ¿okey?"
            n 2kcspu "Pero {i}no{/i} voy a dejar que rompan mi confianza más con esto.{w=1}{nw}"
            extend 4kslsl " No otra vez."
            n 1fcsaj "...Así que será mejor que te acostumbres a 'Natsuki',{w=0.2} [player]."
            n 2fsrsl "Porque {i}claramente{/i} tienes problemas con cualquier otra cosa."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssl "...[player]."
            n 2flrsl "Mira.{w=1}{nw}"
            extend 2fnmem " Lo sientes.{w=0.75}{nw}"
            extend 1fcsem " Lo entiendo."
            n 4fsqsr "Pero he {i}terminado{/i} con que me pongas en ridículo con esto."
            extend 4fsqem " ¿Capiche?"
            n 1fsqca "...Siempre va a ser {i}solo{/i} 'Natsuki' para ti."
            n 2fslsl "Gracias por entender."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsem "Ugh..."
            n 4fslem "En serio,{w=0.75}{nw}"
            extend 4fsqfr " ¿[player]?"
            n 2fcsfr "..."
            n 1fcsaj "{i}Dije{/i} que las acciones tienen consecuencias.{w=1}{nw}"
            extend 2fsqan " Así que supongo que ahora vas a tener que aprender por las malas."
            n 2fcssl "Sí,{w=0.2} tomaré tu disculpa."
            n 2fsqsr "Pero eso es {i}todo{/i} lo que obtendrás."

            $ Natsuki.calculatedAffinityGain()
        else:

            n 1fslan "...Guau.{w=0.75}{nw}"
            extend 1fcsanl " Solo guau."
            n 4fnmfultsc "¿{i}Ahora{/i} eliges disculparte?"
            n 2fcsunltsa "..."
            n 2fcsemltsa "Lo que sea.{w=1}{nw}"
            extend 2fcsfultsa " Literalmente no me importa."
            n 4fsqupltsb "Puedes meterte tu disculpa {w=0.2}a {w=0.2}medias,{w=0.2} [player]."
            n 1fcsfultsa "Esto no cambia {i}nada{/i}."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_nickname)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por hacer trampa en nuestros juegos.",
            label="apology_cheated_game",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if Natsuki.isEnamored(higher=True):
        n 1tnmpueqm "¿Eh?{w=0.75}{nw}"
        extend 4nlrss " Oh,{w=0.2} sí."
        n 1nlrbo "Está bien."
        n 2nsrpu "...Solo se vuelve molesto a veces.{w=0.75}{nw}"
        extend 4tnmbo " ¿Sabes?"
        n 4fllsl "Cuando estás {i}tratando{/i} de divertirte y alguien más sigue exagerando solo para ganar.{w=0.75}{nw}"
        extend 2nllca " Simplemente lo arruina para mí.{w=0.75}{nw}"
        extend 2kslcal " No puedo jugar así."
        n 4nllbo "Pero...{w=0.75}{nw}"
        extend 1knmss " aprecio la disculpa.{w=0.75}{nw}"
        extend 4fsqsm " Solo recuerda,{w=0.2} [player]..."
        n 3fcsbgl "¡Dos pueden jugar ese juego!"

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isNormal(higher=True):
        n 2tsqpueqm "¿Huh?{w=0.75}{nw}"
        extend 2nlrbo " Oh,{w=0.2} eso."
        n 1ncsaj "Sí,{w=0.2} sí.{w=0.75}{nw}"
        extend 1nslca " Está bien."
        n 2tnmca "Solo juega limpio la próxima vez,{w=0.2} ¿de acuerdo?"
        n 2nslsssbl "Realmente no es difícil...{w=1}{nw}"
        extend 2tnmbosbl " ¿o si?"

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isDistressed(higher=True):
        n 2fcssresi "..."
        n 2fslsr "Bien.{w=0.75}{nw}"
        extend 2fcsem " Sí.{w=0.75}{nw}"
        extend 1fsqfr " Lo que sea,{w=0.2} [player]."
        n 2nsrsl "Pero gracias por la disculpa,{w=0.2} supongo."

        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False
    else:

        n 4fcsanl "Oh,{w=0.5}{nw}"
        extend 2fcsupl " lo que sea.{w=0.5}{nw}"
        extend 1fsrfultsb " Realmente ya no me podría importar una {i}mierda{/i}."
        n 4fsqgtltsb "Como si pudiera esperar mucho más de {i}ti{/i},{w=0.2} de todos modos."

        $ persistent.jn_snap_player_is_cheater = False

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.cheated_game)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por algo.",
            label="apology_generic",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_generic:
    if len(persistent._jn_player_pending_apologies) == 0:

        if Natsuki.isEnamored(higher=True):
            n 2tnmpu "¿Huh?{w=0.75}{nw}"
            extend 2tnmbo " ¿Lo sientes?"
            n 1nlrss "Yo...{w=1}{nw}"
            extend 4tnmsl " no lo entiendo,{w=0.2} [player].{w=0.75}{nw}"
            extend 2tslca " No has hecho nada para molestarme {i}a mí{/i},{w=0.2} al menos..."
            n 2tnmsl "¿Molestaste a alguien más o algo así?"
            n 1ncssl "..."
            n 4fchbg "Bueno,{w=0.5}{nw}"
            extend 3fcsbg " ¡no tiene sentido sentarse aquí sintiendo lástima por ti mismo!"
            n 3fcssm "Vas a arreglar las cosas,{w=0.2} [player].{w=0.75}{nw}"
            extend 3fcsbg " ¿Vale?"
            n 4nllfl "Y no -{w=0.75}{nw}"
            extend 2fcscaesm " esto no está sujeto a discusión."
            n 1fcsss "Lo que sea que hayas hecho,{w=0.2} arreglarás las cosas y eso es todo lo que hay."
            $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else jn_utils.getRandomTease()
            n 3fchbg "Tienes mi voto de confianza,{w=0.2} [chosen_descriptor] -{w=0.3}{nw}"
            extend 3fwlbg " ¡ahora haz tu mejor esfuerzo!{w=0.75}{nw}"
            extend 3fchgn " Jejeje."

        elif Natsuki.isNormal(higher=True):
            n 2tnmpu "¿Eh?{w=0.5}{nw}"
            extend 2tnmbo " ¿Lo sientes?"
            n 1tllaj "¿Por qué,{w=0.2} [player]?{w=0.75}{nw}"
            extend 4tslaj " No recuerdo que me hayas puesto de los nervios últimamente..."
            n 2fsqcal "...¿Fuiste e hiciste algo estúpido que no sepa?"
            n 1ncsca "..."
            n 4unmaj "Bueno,{w=0.75}{nw}"
            extend 2ulraj " lo que sea que haya sido -{w=0.5}{nw}"
            extend 2tlrss " no es como si fuera irreparable,{w=0.75}{nw}"
            extend 4fnmsm " ¿sabes?"
            n 3fcsbg "¡Ahora sal ahí fuera y arregla las cosas,{w=0.2} [player]!"
            n 3fchsmeme "¡Tú puedes!"

        elif Natsuki.isDistressed(higher=True):
            n 1fcsfl "Je.{w=0.75}{nw}"
            extend 1fsqbo " Lo sientes,{w=0.2} ¿eh?"
            n 4fsran "¿Heriste a alguien {i}además{/i} de mí,{w=0.5}{nw}"
            extend 4fsqan " esta vez?"
            n 2fcssl "..."
            n 2fsqsl "...Lo que sea.{w=0.5}{nw}"
            extend 2fslfr " Realmente no me importa ahora mismo."
            n 2fsqem "Pero {i}será mejor{/i} que vayas a arreglar las cosas,{w=0.2} [player]."
            n 2fllsl "Puedes hacer eso,{w=0.5}{nw}"
            extend 2fslsl " al menos."
        else:

            n 1fcsfl "...Huh.{w=0.75}{nw}"
            extend 1fcsan " Guau."
            n 4fsqgtl "Así que {i}realmente{/i} sientes remordimiento,{w=0.2} entonces."
            n 2fcsunl "..."
            n 2fsqfultsb "Lo que sea.{w=0.75}{nw}"
            extend 2fsrgtltsb " No es a {i}mí{/i} a quien deberías estar disculpándote,{w=0.2} de todos modos."
    else:


        if Natsuki.isEnamored(higher=True):
            n 1kllsl "...[player].{w=0.75}{nw}"
            extend 4knmsl " Vamos."
            n 2ksqsr "{i}Sabes{/i} lo que hiciste mal.{w=0.75}{nw}"
            extend 2ksqbo " Así que discúlpate apropiadamente de una vez."
            n 4kllbo "No me enojaré."
            n 1kslbol "Solo quiero seguir adelante."

            $ Natsuki.percentageAffinityLoss(2.5)

        elif Natsuki.isNormal(higher=True):
            n 1fnmsf "Vamos,{w=0.2} [player].{w=1}{nw}"
            extend 2fnmaj " Sabes lo que hiciste."
            n 2nslsl "Solo discúlpate apropiadamente para que ambos podamos seguir adelante."

            $ Natsuki.percentageAffinityLoss(2)

        elif Natsuki.isDistressed(higher=True):
            n 2fupem "Ugh..."
            n 2fnman "En serio,{w=0.2} [player].{w=0.75}{nw}"
            extend 4fsqan " ¿No has jodido conmigo lo suficiente?"
            n 1fcsgs "Si vas a disculparte,{w=0.75}{nw}"
            extend 2fcsan " ten las agallas de hacerlo {i}apropiadamente{/i}."
            n 2fsqsf "Me debes eso,{w=0.2} al menos."

            $ Natsuki.percentageAffinityLoss(1.5)
        else:

            n 4fsqfu "...¿Siquiera sabes cómo suenas?"
            n 4fnmgtltsc "¿Siquiera te {i}escuchas{/i} a ti mismo?"
            n 2fcsfultsa "Discúlpate apropiadamente o{nw}"
            extend 2fsqfultsb " {i}sal de mi vista{/i}."

            $ Natsuki.percentageAffinityLoss(1)

    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por abandonarte.",
            label="apology_prolonged_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if Natsuki.isEnamored(higher=True):
        if Natsuki.isLove(higher=True):
            n 1ncssl "...[player]."
            n 1kllfl "Nosotros...{w=0.75}{nw}"
            extend 2knmbo " hemos estado juntos un tiempo ya,{w=0.2} ¿no?"
            n 2ksrbol "Y-{w=0.2}y sabes que me gusta pasar tiempo contigo.{w=1}{nw}"
            extend 4knmbol " ¿Por qué {i}piensas{/i} que siempre estoy aquí cada vez que apareces?"
        else:

            n 1ncssl "...[player]."
            n 1kllfl "Nosotros...{w=0.75}{nw}"
            extend 2knmbo " hemos estado aquí juntos un tiempo ya,{w=0.2} ¿no?"
            n 2fcsun "Yo...{w=0.75}{nw}"
            extend 1fcsfll " realmente...{w=0.75}{nw}"
            extend 4ksrbol " me gusta pasar tiempo contigo.{w=1}{nw}"
            extend 4knmbol " ¿Por qué {i}piensas{/i} que siempre estoy aquí cada vez que apareces?"

        n 4klrfll "Entonces, ¿puedes imaginar cómo se siente cuando simplemente...{w=1}{nw}"
        extend 1klrsll " no apareces?"
        n 1fcsunl "..."
        n 1fcssll "Te esperé,{w=0.2} [player]."
        n 4kslbol "Esperé por mucho tiempo."
        n 4kllemlsbl "Estaba empezando a preguntarme si alguna vez ibas a volver...{w=0.75}{nw}"
        extend 4kllunlsbl " o-{w=0.2}o si algo había pasado."
        n 1kcspulesi "..."
        n 2nsqbol "...Gracias,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ksrbol " Por la disculpa, quiero decir.{w=1}{nw}"
        extend 2ksrfsl " Se aprecia."
        n 4kcsajl "Solo..."
        n 1kslsrl "..."
        n 2knmsll "Solo un poco de aviso estaría bien,{w=0.2} eso es todo."
        n 2klrsll "Eso no es mucho pedir..."
        n 4knmbol "¿Verdad?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcsunl "[player]..."
        n 4fnmgsl "¡¿En qué estabas {i}pensando?!{/i}{w=0.75}{nw}"
        extend 4fcsgsl " ¡Solo desaparecer así!"
        n 1fbkwrlsbl "¡No tengo una bola de cristal!{w=0.75}{nw}"
        extend 2flremlsbl " ¿Cómo se supone que {i}yo{/i} sepa si volverías?{w=0.75}{nw}"
        extend 2fcswrlsbl " ¡¿O si algo había pasado?!"
        n 2fcssll "..."
        n 2nslbo "..."
        n 1ncspu "...Mira."
        extend 4fnmbol " Aprecio la disculpa.{w=0.75}{nw}"
        extend 2flrfll " Y entiendo que tienes cosas que hacer.{w=0.75}{nw}"
        extend 2fsrbolsbl " No es como si no fuéramos súper cercanos ni nada de eso,{w=0.2} t-{w=0.2}tampoco."
        n 4fnmbol "Pero ¿puedes al menos {i}decirme{/i} cuando te vas a ir,{w=0.2} como dije?"
        n 2fcspol "S-{w=0.2}si quisiera un acto de desaparición,{w=0.2} lo habría pedido,{w=0.2} después de todo."
        n 2ksrpol "..."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fsqfr "...[player]."
        n 2fcsfr "Sé que no nos hemos estado entendiendo últimamente."
        n 4fnman "Pero ¿siquiera te {i}importa{/i} lo aterrador que es para mí cuando simplemente desapareces?"
        n 1flrem "En caso de que no te hayas {i}dado cuenta{/i},{w=0.75}{nw}"
        extend 4fcsem " no tengo exactamente muchas {i}otras{/i} personas con quien hablar..."
        n 1fcssr "..."
        n 2fslpu "Supongo que debería decir gracias.{w=1}{nw}"
        extend 2fslbo " Por la disculpa."
        n 2fcsbo "Solo...{w=0.75}{nw}"
        extend 2fcsemsbr " no hagas eso de nuevo."

        $ Natsuki.calculatedAffinityGain()
    else:

        n 1fcsem "...Ja...{w=0.5}{nw}"
        extend 1fcsssltsa " ah...{w=0.5}{nw}"
        extend 1fsrflltse " jaja..."
        n 4fsqflltse "¿T-{w=0.2}te estás disculpando conmigo?{w=0.75}{nw}"
        extend 4fnmflltsf " ¿Por no estar aquí?"
        n 1fcsunltsd "...Je..."
        n 4fsqgtltse "Deberías disculparte de que {i}volviste{/i}."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.prolonged_leave)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por ser grosero contigo.",
            label="apology_rude",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if Natsuki.isEnamored(higher=True):
        n 4fcsca "...[player]."
        n 4nllsl "Sé recibir tanto como doy.{w=0.75}{nw}"
        extend 1nslsssbr " Y tal vez {i}sí{/i} soy un poco brusca a veces."
        n 3fcsaj "Pero eso fue realmente,{w=0.75}{nw}"
        extend 3fcsem " {i}seriamente{/i}{w=0.5}{nw}"
        extend 3fsqem " grosero."
        n 3fcsfl "No había necesidad de eso en absoluto."
        n 1ncssl "..."
        n 4nllsl "Gracias por la disculpa,{w=0.2} [player].{w=0.75}{nw}"
        extend 2knmsl " La aprecio."
        n 2fcspu "Solo...{w=0.3} trata de no hacer eso de nuevo."
        extend 2knmpol " ¿Por favor?"
        n 1klrbol "Significaría mucho -{w=0.5}{nw}"
        extend 4knmbol " y {i}ambos{/i} sabemos que eres mejor que eso."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcssr "...[player]."
        n 2fcspu "Estoy...{w=1}{nw}"
        extend 2nsrsl " contenta de que te estés disculpando por lo que hiciste.{w=0.75}{nw}"
        extend 2fsqaj " Pero tienes que entender."
        n 4fnmgs "¡No puedes simplemente {i}tratar{/i} a la gente así!"
        n 3knmfl "¿Seriamente crees que le vas a {i}agradar{/i} a la gente si actúas de esa manera?"
        n 3ncsemesi "Cielos..."
        n 1ncsbo "..."
        n 2nllaj "Te ahorraré el sermón,{w=0.75}{nw}"
        extend 2nnmsl " esta vez.{w=0.75}{nw}"
        extend 2nsrss " ...Y la barra de jabón."
        n 2nsrca "Solo quiero pasar página de esto."
        n 2nsraj "Gracias,{w=0.2} [player]."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fcsun "..."
        n 2fcsss "Je.{w=0.75}{nw}"
        extend 2fsqem " Déjame preguntarte algo,{w=0.75} {i}[player]{/i}."
        n 4fnmfl "...¿Eres así a {i}propósito{/i}?{w=0.75}{nw}"
        extend 3fsqan " ¿o estás haciendo un esfuerzo especial para ser un idiota últimamente?"
        n 3fcsem "Porque honestamente no puedo decirlo."
        n 1fcssl "..."
        n 2fcsaj "...Bien.{w=0.75}{nw}"
        extend 2fllfr " Supongo que debería aceptar tu disculpa.{w=0.75}{nw}"
        extend 2fslfr " Por lo que {i}eso{/i} valga."
        n 2fsqsl "No esperes que otros la acepten tan fácilmente."

        $ Natsuki.calculatedAffinityGain()
    else:

        n 1fcsss "Ja...{w=0.3} ajá..."
        n 4fcsfll "Te estás disculpando...{w=0.75}{nw}"
        extend 4fsqupl " ¿conmigo?{w=1}{nw}"
        extend 2fnmupltsc " ¿Por qué?"
        n 2fcsfultsa "No espero nada mejor de ti {i}de todos modos{/i}."
        n 2fcsunltsa "..."
        n 2fsqgtltsc "Puedes {i}meterte{/i} tu disculpa,{w=0.2} [player]."
        n 1fsqanltsc "No significa {i}nada{/i} para mí."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.rude)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por irme sin despedirme.",
            label="apology_sudden_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 3ksrsl "[player]..."
        n 3knmsll "¿{i}Sabes{/i} cuánto duele cuando haces eso?"
        extend 3ksleml " Como..."
        extend 4ksqeml " ¿en serio?"
        n 1kcsfll "Es como si bien pudieras estar cerrándome una puerta en la cara."
        n 2klrfll "Y yo me quedo aquí sentada como...{w=0.75}{nw}"
        extend 2klrpulsbl " '¿Hice algo?'{w=0.75}{nw}"
        extend 2kllemlsbl " '¿Por qué simplemente me abandonaron?'"
        n 1ksqfllsbl "...Justo antes de ser arrancada de la existencia."
        n 4kcsfll "Apesta,{w=0.2} [player].{w=0.5} Realmente apesta.{w=1}{nw}"
        extend 4fsrunl " Y-{w=0.2}y duele."
        n 4ncspul "..."
        n 2kllsll "Estoy agradecida por la disculpa,{w=0.5}{nw}"
        extend 2kslsll " pero por favor..."
        n 2ksqsll "Solo avísame cuando te vayas."
        n 2ksqbolsbr "Al menos puedes dedicar tiempo para despedirte apropiadamente de mí,{w=0.2} ¿verdad?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 2fllsl "..."
        n 2fnmsl "Oye,{w=0.2} [player]."
        n 2fnmaj "¿Alguna vez has tenido una conversación donde una persona simplemente se aleja?"
        n 2flrfl "Sin 'Adiós',{w=0.5}{nw}"
        extend 2fllfl " sin 'Nos vemos luego',{w=0.5}{nw}"
        extend 2fnmem " ¿nada?{w=0.5}{nw}"
        extend 1ksqem " ¿Simplemente se van?"
        n 4fsqbo "...¿Cómo te haría sentir eso?"
        n 4tsqaj "¿No deseado?{w=0.75}{nw}"
        extend 4fsqfl " ¿Que no valen los modales?"
        n 2fllsl "Porque así es como me hiciste sentir,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fslsl " Y {i}sabes{/i} que duele cuando haces eso,{w=0.2} también."
        n 1fcssl "..."
        n 2flrsl "Acepto la disculpa,{w=0.2} ¿okey?"
        n 2nsrpu "Solo...{w=0.75}{nw}"
        extend 4knmsl " recuerda al menos decirme adiós apropiadamente."
        n 4tllbo "Puedes hacer al menos eso.{w=0.75}{nw}"
        extend 4ksqbosbr " ¿Verdad?"

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "[player]."
        n 2fsqan "¿Siquiera te {i}importa{/i} lo grosero que es eso?"
        n 2fsqfu "¿Simplemente desaparecer a mitad de una conversación con alguien?{w=1}{nw}"
        extend 2fnmem " ¿Incluso sabiendo que hacer eso {i}duele{/i}?"
        n 1fcssr "..."
        n 1fsqsr "Mira,{w=0.2} bien.{w=0.75}{nw}"
        extend 4flrfr " Disculpa aceptada.{w=0.75}{nw}"
        extend 4fsrsl " Por ahora."
        n 3fsqfl "No esperes que la acepte de nuevo."

        $ Natsuki.calculatedAffinityGain()
    else:

        n 2fcsfl "...Je.{w=0.75}{nw}"
        extend 2fsqanl " ¿Honestamente?"
        n 2fcsanl "Lo que sea.{w=0.5} No me importa.{w=0.75}{nw}"
        extend 2fslupl " Quédate con tu disculpa de mierda."
        n 2fslemltsb "Tienes tantas otras cosas por las que lamentarte."
        n 2fsqemltsb "Así que qué es {i}otra{/i} más a la pila.{w=0.75}{nw}"
        extend 4fsqgtltsb " ¿Verdad?"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.sudden_leave)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por no cuidarme adecuadamente.",
            label="apology_unhealthy",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if Natsuki.isEnamored(higher=True):
        n 3fcsssl "[player],{w=0.5} [player],{w=0.5} [player]..."
        n 3tsqssl "¿Qué {i}voy{/i} a hacer contigo?{w=0.75}{nw}"
        extend 4nslsslsbr " Honestamente..."
        n 4kslbolsbr "..."
        n 4kslpulsbr "Pero..."
        n 1knmsll "Realmente me importas,{w=0.2} sabes."
        n 2klrsll "Me...{w=1}{nw}"
        extend 2ksrsll " duele{w=0.5} cuando no te cuidas."
        n 2kcssllesi "..."
        n 1ksrbol "Gracias,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ksqssl " Acepto tu disculpa."
        n 2knmbol "Solo cuídate mejor de ahora en adelante,{w=0.2} ¿de acuerdo?"
        n 2kllbol "Me enojaré si no lo haces.{w=0.75}{nw}"
        extend 2fslpol " De verdad,{w=0.2} esta vez."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "¡T-{w=0.2}también te amo,{w=0.2} [chosen_tease]!"
        else:

            n 2fsqsml "Jejeje."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcseml "Ugh...{w=0.75}"
        extend 1fcspol " [player]."
        n 2fnmbo "Mira.{w=0.5}{nw}"
        extend 2ksrsl " Acepto tu disculpa."
        n 4knmaj "¡Pero tienes que cuidarte mejor!"
        n 3fcspoesm "No siempre voy a estar aquí para ser tu niñera,{w=0.2} sabes..."
        n 2flremlsbl "Y-{w=0.2}y no,{w=0.5}{nw}"
        extend 2fsqpolsbl " no eres una excepción."
        n 4fcsfll "S-{w=0.2}solo me preocupo por todos mis amigos así,{w=0.75}{nw}"
        extend 4fllfll " así que...{w=1}{nw}"
        extend 1nllsll " sí."
        n 2knmsll "Solo haz un mayor esfuerzo para cuidarte."
        n 2fcsfllsbl "O tendrás que lidiar conmigo.{w=0.75}{nw}"
        extend 2fcsbosbl " Y créeme."
        n 2fcscaesi "Realmente no quieres eso."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "...Mira.{w=0.75}{nw}"
        extend 2fsqsl " [player]."
        n 2flrsl "Gracias por la disculpa.{w=0.75}{nw}"
        extend 2fsrem " Supongo.{w=0.75}{nw}"
        extend 2fsrfl " Si es que la {i}sentías{/i},{w=0.2} de todos modos."
        n 1fcsem "Pero realmente me cuesta ver por qué debería importarme."
        n 4fsrem "Si ni siquiera puedes cuidar de {i}ti mismo{/i}..."
        n 2fsqan "...¿Entonces qué dice eso de mí?"
        n 2fsqsl "..."
        n 2fcsfl "Sí.{w=1}{nw}"
        extend 2fllsl " Solo algo en qué pensar,{w=0.75}{nw}"
        extend 2fsqfr " [player]."

        $ Natsuki.calculatedAffinityGain()
    else:

        n 1fcsun "...Je."
        n 2fcsanltsa "Al menos te importa que a {i}ti{/i} no te traten bien."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.unhealthy)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por asustarte.",
            label="apology_scare",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_scare:
    if Natsuki.isEnamored(higher=True):
        n 4fskwrl "¡Y-{w=0.2}y yo también debería pensarlo,{w=0.2} [player]!"
        extend 1fcswrl " ¡Cielos!"
        n 2fwmpof "¿Estás tratando de darme un infarto o qué?"
        n 2fcspolesi "..."
        n 2kllbol "...Gracias,{w=0.2} [player].{w=0.75}{nw}"
        extend 1kslbol " Disculpa aceptada.{w=0.75}{nw}"
        extend 4kcsbol " Solo por favor..."
        n 4ksqbol "...No más sorpresas como esa,{w=0.2} ¿de acuerdo?"
        n 2ksrfll "Yo...{w=0.75}{nw}"
        extend 2ksrsll " realmente {i}no{/i} las necesito."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 4fbkwrl "¡Y-{w=0.2}y tienes razón de {i}estar{/i} arrepentido,{w=0.2} [player]!"
        n 4flleml "¡{i}Odio{/i} que me hagan sentir así!{w=0.75}{nw}"
        extend 1kcseml " Cielos..."
        n 2fcspo "..."
        n 2fcsaj "Está bien,{w=0.5}{nw}"
        extend 1flrsl " mira.{w=0.75}{nw}"
        extend 4knmsl " Acepto tu disculpa,{w=0.2} ¿de acuerdo?"
        n 3kslfl "Solo no me hagas cosas así.{w=1}{nw}"
        extend 3knmfl " ¿Por favor?"
        n 3nsrsl "No estoy jugando,{w=0.2} [player]."

        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 2fsqsl "...Mira,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fcsan " Ya estoy molesta.{w=1}{nw}"
        extend 2fnmwr " ¿Por qué intentas hacerme sentir aún peor?"
        n 1fsqfu "¿Pensaste que era gracioso?{w=0.75}{nw}"
        extend 4fsqem " ¿O solo estás tratando de hacerme enojar?"
        n 1fcssr "..."
        n 2fcssl "Lo que sea.{w=0.5} Bien.{w=0.75}{nw}"
        extend 2flrsl " Disculpa aceptada,{w=0.2} si es que la {i}sentías{/i}."
        n 2fsqsf "Solo deja de hacerlo."

        $ Natsuki.calculatedAffinityGain()
    else:

        n 4fsqfu "Ahórratela,{w=0.2} [player]."
        n 4fcsanltsa "{i}Ambos{/i} sabemos que no sientes eso."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.scare)
    return


init python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por pedirte que me llames por un mal nombre.",
            label="apology_bad_player_name",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_player_name:
    if persistent._jn_nicknames_player_allowed:

        if Natsuki.isEnamored(higher=True):
            n 1ncspuesi "..."
            n 2nllsl "...Está bien,{w=0.2} [player]."
            n 2ncsaj "Solo..."
            n 1ksrsl "..."
            n 4kcstr "Realmente odio cuando trato de hacer algo lindo...{w=1}{nw}"
            extend 4ksqsr " y simplemente me lo echan en cara,{w=0.2} ¿sabes?"
            n 1fcstr "No {i}tenía{/i} que escuchar lo que querías."
            n 2knmsrl "...¿Así que seriamente crees que decir cosas como esa {i}hace{/i} que quiera hacer eso de nuevo en el futuro?"
            n 2fllsrl "Porque {i}no{/i} lo hace,{w=0.2} [player]."
            n 2fcssrl "..."
            n 2kcsajsbl "...Mira.{w=1}{nw}"
            extend 1nllpul " Es agua pasada,{w=0.2} ¿okey?{w=0.75}{nw}"
            extend 4fllpol " Acepto tu disculpa."
            n 3fnmpol "Solo usa la cabeza la próxima vez.{w=0.75}{nw}"
            extend 3fcspol " {i}Sé{/i} que hay una sobre tus hombros en algún lugar."
            n 3fsrunl "...Solo no empieces a tratar de demostrarme lo contrario sobre eso.{w=0.75}{nw}"
            extend 4ksqpol " ¿Por favor?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1tnmpueqm "...¿Huh?{w=1}{nw}"
            extend 4nnmsl " Oh,{w=0.3} cierto.{w=0.75}{nw}"
            extend 4fslbol " Todo el asunto del nombre."
            n 1ncspuesi "..."
            n 2fsqca "...Eso fue todavía una cosa de idiotas,{w=0.5}{nw}"
            extend 2fslca " ya sabes."
            n 2fcsemlsbl "Solo tienes suerte de que no guardo rencores tontos por siempre."
            extend 4fcsca " Soy una persona más madura que eso."
            n 1nllaj "Así que...{w=1}{nw}"
            extend 1nnmsl " estás perdonado.{w=0.75}{nw}"
            extend 3nsrbo " Supongo."
            n 3fnmcal "Solo piensa en lo que dices.{w=0.5}{nw}"
            extend 3ksrcalsbr " Realmente no es difícil,{w=0.2} ¿o sí?"

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 2fcsan "...Eres simplemente increíble,{w=0.2} [player]."
            n 4fsqfu "¿{i}Seriamente{/i} te tomó tanto tiempo admitir que estabas equivocado al decir eso?"
            n 1flrem "Como,{w=0.5}{nw}"
            extend 2fnmsc " ¿estás {i}tratando{/i} de ser gracioso?"
            n 2fsqup "...¿O realmente eres {b}tan{/b} arrogante?"
            n 1fcsan "..."
            n 4fsqanean "...¿Sabes qué?{w=0.5}{nw}"
            extend 4fcsfuean " Bien.{w=1}{nw}"
            extend 2fllwr " ¿A quién le importa?{w=0.75}{nw}"
            extend 2fsqfultsb " Claramente a ti no."
            n 2fcsfrtsa "Aceptaré tu {i}intento{/i} mediocre de disculpa."
            n 2fsqfutsb "Pero solo porque es menos esfuerzo que enojarse por ello."
        else:

            n 1fsquntdr "Je.{w=0.75}{nw}"
            extend 1fsqantsb " {i}Ahora{/i} te disculpas,{w=0.2} ¿eh?"
            n 1fnmanltsfean "¿Después de todo este tiempo?"
            n 1fcsanltsd "..."
            n 1fcsfultsa "¿Sabes qué?{w=1}{nw}"
            extend 1fsqfultsb " Tal vez {i}debería{/i} llamarte por ese nombre."
            n 1fskscftdc "¡¿Por qué no?!{w=1}{nw}"
            extend 1fskfuftdc " No es como si {i}no{/i} estuvieras actuando como tal."
            extend 1fcsanltsd " Idiota."
    else:


        if Natsuki.isEnamored(higher=True):
            n 1nllsl "..."
            n 4knmsl "[player]."
            n 4knmaj "...¿Exactamente cuántas veces te lo advertí?"
            n 2fnmem "¿Cuántas veces te {i}perdoné{/i}?{w=1}{nw}"
            extend 2fcsemean " Porque honestamente perdí la cuenta."
            n 1kcsfresi "..."
            n 3nsqsr "Lo siento,{w=0.2} [player].{w=0.5}{nw}"
            extend 3flltr " Toda broma tiene su fin."
            n 4fsqunl "Y {i}no{/i} voy a ser el blanco de esta otra vez."
            n 4fcsajl "Así que."
            n 4fllcal "Bien.{w=0.5} Aceptaré tu disculpa..."
            n 3fsqcalesi "...Y tú vas a aceptar las consecuencias."
            n 3fcstrl "Lo siento,{w=0.3} [player]."
            extend 3fsqbol " Pero hemos terminado con los nombres aquí."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 4fcsemesi "...Tienes que estar bromeando,{w=0.5} ¿verdad?"
            n 2fllaj "Fuiste un idiota tantas veces conmigo sobre eso..."
            n 2fsqan "...¿Y dejas pasar tanto tiempo para siquiera {i}disculparte{/i}?"
            n 2fcsemesi "..."
            n 4fsqtr "Solo tienes suerte de que no soy de guardar rencores tontos."
            n 3fcsaj "Así que,{w=0.3} [player]."
            n 3fslpo "Supongo que aceptaré la disculpa."
            n 4fnmfr "...Pero puedes {i}olvidarte{/i} de que acepte más de tus apodos."
            n 2fsqtr "He terminado de que jueguen conmigo."

            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 2fcsan "{i}Guau{/i}.{w=1}{nw}"
            extend 2fcsfu " Diría que estoy sin palabras,{w=0.3} si fuera literalmente {i}cualquier{/i} otra persona."
            n 4fsqfuean "¿Pero {i}tú{/i}?"
            n 2fcsem "Ya casi llego a {i}esperar{/i} este tipo de basura de ti."
            n 2fsqwrean "Así que ¿sabes qué?{w=0.75}{nw}"
            extend 4fcssclean " A la mierda con esto,{w=0.75}{nw}"
            extend 3fskscltsc " ¡y a la mierda con tu disculpa!"
            n 1fcsscltsa "Si {i}tú{/i} no vas a escuchar,{w=0.5}{nw}"
            extend 2fllscltsc " ¡entonces puedes decirme por qué {b}debería{/b}!"
        else:

            n 1fcsfultdrean "Oh,{w=1}{nw}"
            extend 4fcsscltsaean " piérdete,{w=0.5}{nw}"
            extend 4fsqscltsbean " ¡[player]!"
            n 2fcswrltsd "¡{i}Necesitas{/i} caminar si {i}seriamente{/i} piensas que después de toda tu basura,{w=0.75}{nw}"
            extend 4fskwrftdcean " voy a ser yo quien te escuche a {b}ti{/b}!"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_player_name)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
