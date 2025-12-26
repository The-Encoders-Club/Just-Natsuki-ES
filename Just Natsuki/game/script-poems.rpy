default persistent.jn_poem_list = dict()

image paper default = "mod_assets/poems/default.png"
image paper pink_floral = "mod_assets/poems/pink_floral.png"
image paper festive = "mod_assets/poems/festive.png"
image paper notepad = "mod_assets/poems/notepad.png"
image paper spooky = "mod_assets/poems/spooky.png"

init python in jn_poems:
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    _m1_script0x2dpoems__ALL_POEMS = {}

    class JNPoem:
        """
        Describes a poem object that players can unlock and read.
        """
        def __init__(
            self,
            reference_name,
            display_name,
            holiday_type,
            affinity_range,
            poem,
            paper="default",
            font_size=28,
            text_align=0.0
        ):
            """
            Constructor.

            IN:
                reference_name - The name used to uniquely identify this poem and refer to it internally
                display_name - The name displayed to the user
                holiday_type - The JNHoliday type associated with this player, allowing a poem to be associated with a holiday
                affinity_range - The affinity range that must be satisfied for this holiday to be picked when filtering
                poem - The actual poem content
                paper - The paper image that is associated with this poem. Defaults to a standard notepad page
                font_size - The int font size for the main body of the poem. Must be within a range of 16-28.
                text_align - The decimal alignment for the main body of the poem, where:
                    0.0: LEFT
                    0.5: CENTRE
                    1.0: RIGHT
            """
            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = False
            self.holiday_type = holiday_type
            self.affinity_range = affinity_range
            self.poem = poem
            self.paper = paper
            self.font_size = font_size if 16 <= font_size <= 24 else 24 
            self.text_align = text_align if text_align in (0.0, 0.5, 1.0) else 0.0
        
        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each poem from the persistent.
            """
            global _m1_script0x2dpoems__ALL_POEMS
            for poem in _m1_script0x2dpoems__ALL_POEMS.itervalues():
                poem._m1_script0x2dpoems__load()
        
        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each poem to the persistent.
            """
            global _m1_script0x2dpoems__ALL_POEMS
            for poem in _m1_script0x2dpoems__ALL_POEMS.itervalues():
                poem._m1_script0x2dpoems__save()
        
        @staticmethod
        def filterPoems(
            poem_list,
            unlocked=None,
            reference_name=None,
            holiday_types=None,
            affinity=None
        ):
            """
            Returns a filtered list of poems, given an poem list and filter criteria.

            IN:
                - poem_list - the list of JNpoem child poems to query. Defaults to all poems
                - unlocked - the boolean unlocked state to filter for
                - reference_name - list of reference_names the poem must have 
                - holiday_types - list of the JNHolidayTypes the poem must be in
                - affinity - minimum affinity state the poem must have

            OUT:
                - list of poems matching the search criteria
            """
            return [
                _poem
                for _poem in poem_list
                if _poem._m1_script0x2dpoems__filterPoem(
                    unlocked,
                    reference_name,
                    holiday_types,
                    affinity
                )
            ]
        
        def asDict(self):
            """
            Exports a dict representation of this poem; this is for data we want to persist.

            OUT:
                dictionary representation of the poem object
            """
            return {
                "unlocked": self.unlocked
            }
        
        def currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this poem's affinity_range

            IN:
                affinity_state - Affinity state to test if the poems can be shown in. If None, the current affinity state is used.
                    (Default: None)
            OUT:
                True if the current affinity is within range. False otherwise
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()
            
            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)
        
        def lock(self):
            """
            Locks this poem, making it unavailable to the player.
            """
            self.unlocked = False
            self._m1_script0x2dpoems__save()
        
        def unlock(self):
            """
            Unlocks this poem, making it available to the player.
            """
            self.unlocked = True
            self._m1_script0x2dpoems__save()
        
        def _m1_script0x2dpoems__load(self):
            """
            Loads the persisted data for this poem from the persistent.
            """
            if store.persistent.jn_poem_list[self.reference_name]:
                self.unlocked = store.persistent.jn_poem_list[self.reference_name]["unlocked"]
        
        def _m1_script0x2dpoems__save(self):
            """
            Saves the persistable data for this poem to the persistent.
            """
            store.persistent.jn_poem_list[self.reference_name] = self.asDict()
        
        def _m1_script0x2dpoems__filterPoem(
            self,
            unlocked=None,
            reference_name=None,
            holiday_types=None,
            affinity=None
        ):
            """
            Returns True, if the poem meets the filter criteria. Otherwise False.

            IN:
                - unlocked - the boolean unlocked state to filter for
                - reference_name - list of reference_names the poem must have 
                - holiday_types - list of the JNHolidayTypes the poem must be in
                - affinity - minimum affinity state the poem must have

            OUT:
                - True, if the poem meets the filter criteria. Otherwise False
            """
            if unlocked is not None and self.unlocked != unlocked:
                return False
            
            elif reference_name is not None and not self.reference_name in reference_name:
                return False
            
            elif holiday_types is not None and not self.holiday_type in holiday_types:
                return False
            
            elif affinity and not self.currAffinityInAffinityRange(affinity):
                return False
            
            return True

    def _m1_script0x2dpoems__registerPoem(poem):
        """
        Registers a new poem in the list of all poems, allowing in-game access and persistency.
        If the poem has no existing corresponding persistent entry, it is saved.

        IN:
            - poem - the JNPoem to register.
        """
        if poem.reference_name in _m1_script0x2dpoems__ALL_POEMS:
            jn_utils.log("Cannot register poem name: {0}, as an poem with that name already exists.".format(poem.reference_name))
        
        else:
            _m1_script0x2dpoems__ALL_POEMS[poem.reference_name] = poem
            if poem.reference_name not in store.persistent.jn_poem_list:
                poem._m1_script0x2dpoems__save()
            
            else:
                poem._m1_script0x2dpoems__load()

    def getPoem(poem_name):
        """
        Returns the poem for the given name, if it exists.

        IN:
            - poem_name - str poem name to fetch

        OUT: Corresponding JNPoem if the poem exists, otherwise None 
        """
        if poem_name in _m1_script0x2dpoems__ALL_POEMS:
            return _m1_script0x2dpoems__ALL_POEMS[poem_name]
        
        return None

    def getAllPoems():
        """
        Returns a list of all poems.
        """
        return _m1_script0x2dpoems__ALL_POEMS.itervalues()

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_birthday_cakes_candles",
        display_name="Pasteles y Velas",
        holiday_type=jn_events.JNHolidayTypes.player_birthday,
        affinity_range=(jn_affinity.HAPPY, None),
        poem=(
            "Otro pastel, otra vela\n"
            "Otro año que has superado\n"
            "Algunos temen este día especial\n"
            "Y empujan el pensamiento lejos\n"
            "¡Pero no creo que sea malo!\n"
            "\n"
            "Otro regalo, otro invitado\n"
            "Otro año que diste lo mejor de ti\n"
            "Algunos atesoran este día especial\n"
            "Hablan, bailan, festejan y juegan\n"
            "¿Cómo podrías pensar que es triste?\n"
            "\n"
            "No más dudas, no más miedos\n"
            "Ignora los números, olvida los años\n"
            "Este poema es tu felicitación\n"
            "\n"
            "¡Ahora sírvete un plato!\n"
        ),
        paper="pink_floral"
    ))

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_christmas_evergreen",
        display_name="Siempre verde",
        holiday_type=jn_events.JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.ENAMORED, None),
        poem=(
            "Hace\n" 
            "Frío y\n" 
            "Hiela afuera\n" 
            "Pero cálido adentro\n" 
            "Contigo a mi lado.\n" 
            "Escuchando el fuego acogedor\n" 
            "Sentados uno junto al otro.\n" 
            "Hablando entre nosotros, creando\n" 
            "Nuevos recuerdos que brillan intensamente.\n" 
            "Iluminando incluso la noche más oscura\n" 
            "Para dar al viajero cansado una luz guía\n" 
            "Un camino guiado por estrellas en una vida estresante.\n" 
            "Los problemas pasados se derriten en el chocolate caliente\n" 
            "Que sostengo fuerte mientras te molesto para que encuentres el tuyo.\n" 
            "Siempre fue mi favorito, pero ahora, más que nunca\n" 
            "Pues sabe más dulce con ingredientes frescos y nuevos.\n" 
            "El calor que siento por dentro durará más que cualquier invierno\n" 
            "Porque contigo a mi lado\n" 
            "Siempre estoy lista para otro.\n" 
        ),
        paper="festive",
        font_size=18,
        text_align=0.5
    ))

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_christmas_gingerbread_house",
        display_name="Casa de pan de jengibre",
        holiday_type=jn_events.JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.HAPPY, None),
        poem=(
            "De un hogar de jengibre frágil Amy vino\n"
            "Disfrazado por glaseado colorido y dulces\n" 
            "Uno que escondía los gritos y todas las discusiones\n"
            "Uno que se escondía a plena vista, opuesto a los reflectores\n"
            "\n"
            "Pero de dónde venimos no define\n"
            "Quiénes somos realmente en el interior\n"
            "Y a veces todo lo que se necesita es alguien.\n"
            "Alguien nuevo para recordarte que hay más.\n"
            "\n"
            "Un nuevo amigo para ayudar a decorar un árbol.\n"
            "Un árbol siempreverde libre para decoración\n"
            "Esperando ansiosamente a dos personas\n"
            "Para cubrirlo con adornos y luces.\n"
            "\n"
            "Ese árbol una plantilla de lo que vendrá\n"
            "Un lugar donde nuevos recuerdos pueden formarse\n"
            "Donde el jengibre puede parecer frágil\n"
            "Sin necesidad de mentir, con honestidad.\n"
            "\n"
            "Siendo bienvenida sin campanas ni silbatos\n"
            "Mientras la aceptación provee calor en el más frío de los inviernos\n"
        ),
        paper="festive",
        font_size=20
    ))

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_easter_sakura_in_bloom",
        display_name="Sakura en flor",
        holiday_type=jn_events.JNHolidayTypes.easter,
        affinity_range=(jn_affinity.HAPPY, None),
        poem=(
            "Árboles vibrantes brotan de nuevo\n"
            "Mientras matices fluorescentes iluminan\n"
            "El camino para que las multitudes se reúnan\n"
            "Vinieron a reconocer el esplendor de la vida\n"
            "\n"
            "En poco tiempo los pétalos se ramifican\n"
            "Mientras vuelan suavemente en la brisa\n"
            "Hasta alcanzar la mano de otro\n"
            "Y tocar suavemente las vidas de los demás\n"
            "\n"
            "Algunos pueden pensar que su trabajo ha terminado\n"
            "Y aunque eso pueda ser cierto\n"
            "Su belleza continúa viviendo\n"
            "A través de las personas que fueron tocadas\n"
            "\n"
            "Toman el manto para crear de nuevo\n"
            "Siembran las semillas y suministran el agua\n"
            "Para ayudar a guiar otras formas de belleza\n"
            "Mientras un arcoíris de flora emerge para brillar\n"
        ),
        paper="pink_floral",
        font_size=18,
        text_align=0.5
    ))

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_natsuki_birthday_flight",
        display_name="Vuelo",
        holiday_type=jn_events.JNHolidayTypes.natsuki_birthday,
        affinity_range=(jn_affinity.ENAMORED, None),
        poem=(
            "Subir a la cima de una montaña no hace alto a un excursionista\n"
            "Pero el logro de alcanzar esa altura lo dice todo\n"
            "Subir una escalera sin embargo es otra cosa completamente\n"
            "Pero por más que uno se estire, las nubes siguen altas dispersando el clima\n"
            "\n"
            "A la gente que una vez soñó con volar se le miró con descaro\n"
            "Se les dijo que conocieran su lugar y se mantuvieran pequeños\n"
            "Los dos hermanos miraron a los pájaros batiendo pluma tras pluma\n"
            "Hasta que un día lo que se pensaba imposible nació juntos\n"
            "\n"
            "Esas son dos hazañas extraordinarias, pero ambas se miden diferente\n"
            "Sea palo, regla, cinta métrica, ¿pero cómo medimos la habilidad?\n"
            "El crecimiento viene en muchas formas y eso es difícil de medir\n"
            "Así que mientras los calendarios pasan zumbando, ¿qué cambia además de la edad?\n"
            "\n"
            "A los niños siempre se les dice que esperen un estirón, y aceptan gustosos\n"
            "Pero nadie habla nunca de cómo crecer puede doler a menudo sin simpatía\n"
            "Las personas son mucho más que solo en lo que eligen participar\n"
            "Pero a otros les gusta hacer suposiciones y traer rabia innecesaria\n"
            "\n"
            "Las personas son mucho más de lo que su apariencia puede presentar\n"
            "La estatura solo puede decir tanto opuesto a lo que yace agradable debajo\n"
        ),
        paper="notepad",
        font_size=16
    ))

    _m1_script0x2dpoems__registerPoem(JNPoem(
        reference_name="jn_natsuki_hallows_end",
        display_name="Fin de Todos los Santos",
        holiday_type=jn_events.JNHolidayTypes.halloween,
        affinity_range=(jn_affinity.LOVE, None),
        poem=(
            "Cuando el mes termina, los disfraces salen\n"
            "Los niños se visten y corren de puerta en puerta con alegría\n"
            "O sean las casas embrujadas listas para causar un grito\n"
            "Esta festividad tiene algo para que todos vean\n"
            "\n"
            "En su caso, no tanto, ya que comúnmente hará pucheros\n"
            "Pues las festividades comunes no siempre son simples y despreocupadas\n"
            "Así que cuando ve a todos jugando solo puede dudar\n"
            "Y desear que las cosas pudieran ser diferentes, esa es su súplica\n"
            "\n"
            "A través del lamento, está lista para bajar la guardia\n"
            "Está lista para reír, gritar, saltar de horror y chillar.\n"
            "Todas cosas que antes la dejaban asustada y marcada.\n"
            "¿Pero experimentar todo eso en un espacio mucho más seguro? Un sueño.\n"
            "\n"
            "Así que llévala en ese viaje, sé su guardaespaldas acompañante\n"
            "Y déjala experimentar lo que siempre deseó con los ojos brillantes\n"
            "Ella te dejará entrar y juntos será libre para descartar la tristeza\n"
            "Su rostro brillando a través de la oscuridad, la festividad ahora redimida\n"
            "\n"
            "Así que aplicar un poco de esfuerzo y ser paciente con ella no es truco.\n"
            "¡Porque una sonrisa de ella vale más que cualquier trato recibido!\n"
        ),
        paper="spooky",
        font_size=18
    ))

label show_poem(poem):
    $ pre_click_afm = preferences.afm_enable
    $ preferences.afm_enable = False

    play audio page_turn
    show screen poem_view(poem, pre_click_afm)
    with Dissolve(1)
    $ renpy.pause(hard=True)
    $ renpy.pause(2)

    return

screen poem_view(poem, pre_click_afm):
    vbox:
        xalign 0.5
        add "paper [poem.paper]"


    viewport id "poem_viewport":
        child_size (710, None)
        xysize (600,600)
        mousewheel True
        draggable True
        xanchor 0
        ypos 100
        xpos 360
        has vbox
        text "[poem.display_name]" style "poem_title" text_align 0.5
        null height 50
        hbox:
            xsize 600
            box_wrap True
            null height 60
            text "[poem.poem]" style "poem_text" size poem.font_size text_align poem.text_align
            null height 50
 
    vbar value YScrollValue(viewport="poem_viewport") style "poem_vbar"
 
 
    vbox:
        xpos 1056
        ypos 10
        textbutton _("Listo"):
            style "hkbd_button"
            action [
                Hide(
                    screen="poem_view",
                    transition=Dissolve(1)
                ),
                SetField(
                    object=preferences,
                    field="afm_enable",
                    value=pre_click_afm
                ),
                Return()
            ]

style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    ysize 700

style poem_title:
    font "mod_assets/fonts/natsuki.ttf"
    size 30
    color "#000"
    outlines []
    line_leading 5
    xalign 0.5

style poem_text:
    font "mod_assets/fonts/natsuki.ttf"
    color "#000"
    outlines []
    xalign 0.5
    line_leading 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
