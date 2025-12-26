default persistent._jn_joke_list = dict()
default persistent._jn_daily_jokes_unlocked = False
default persistent._jn_daily_joke_given = False
default persistent._jn_daily_jokes_enabled = True

image joke_book = "mod_assets/props/joke_book_held.png"

init python in jn_jokes:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils

    _m1_script0x2djokes__ALL_JOKES = {}

    class JNJokeCategories(Enum):
        neutral = 1
        funny = 2
        corny = 3
        bad = 4
        confusing = 5

    class JNJoke:
        def __init__(
            self,
            label,
            display_name,
            joke_category,
            conditional=None,
        ):
            self.label = label
            self.display_name = display_name
            self.is_seen = False
            self.shown_count = 0
            self.joke_category = joke_category
            self.conditional = conditional
        
        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each joke from the persistent.
            """
            global _m1_script0x2djokes__ALL_JOKES
            for joke in _m1_script0x2djokes__ALL_JOKES.values():
                joke._m1_script0x2djokes__load()
        
        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each joke to the persistent.
            """
            global _m1_script0x2djokes__ALL_JOKES
            for joke in _m1_script0x2djokes__ALL_JOKES.values():
                joke._m1_script0x2djokes__save()
        
        @staticmethod
        def filterJokes(
            joke_list,
            is_seen=None,
            shown_count=None
        ):
            """
            Returns a filtered list of jokes, given a joke list and filter criteria.

            IN:
                - label - list of labels the joke must have 
                - is_seen - bool is_seen state the joke must be
                - shown_count - int number of times the joke must have been seen before

            OUT:
                - list of jokes matching the search criteria
            """
            return [
                _joke
                for _joke in joke_list
                if _joke._m1_script0x2djokes__filterJoke(
                    is_seen,
                    shown_count
                )
            ]
        
        def asDict(self):
            """
            Exports a dict representation of this joke; this is for data we want to persist.

            OUT:
                dictionary representation of the joke object
            """
            return {
                "is_seen": self.is_seen,
                "shown_count": self.shown_count
            }
        
        def setSeen(self, is_seen):
            """
            Marks this joke as seen.
            """
            self.is_seen = is_seen
            self.shown_count += 1
            self._m1_script0x2djokes__save()
        
        def _m1_script0x2djokes__load(self):
            """
            Loads the persisted data for this joke from the persistent.
            """
            if store.persistent._jn_joke_list[self.label]:
                self.is_seen = store.persistent._jn_joke_list[self.label]["is_seen"]
                self.shown_count = store.persistent._jn_joke_list[self.label]["shown_count"]
        
        def _m1_script0x2djokes__save(self):
            """
            Saves the persistable data for this joke to the persistent.
            """
            store.persistent._jn_joke_list[self.label] = self.asDict()
        
        def _m1_script0x2djokes__filterJoke(
            self,
            is_seen=None,
            shown_count=None
        ):
            """
            Returns True, if the joke meets the filter criteria. Otherwise False.

            IN:
                - is_seen - bool is_seen state the joke must be
                - shown_count - int number of times the joke must have been seen before

            OUT:
                - True, if the joke meets the filter criteria. Otherwise False
            """
            if is_seen is not None and not self.is_seen == is_seen:
                return False
            
            elif shown_count is not None and self.shown_count < shown_count: 
                return False
            
            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False
            
            return True

    def _m1_script0x2djokes__registerJoke(joke):
        if joke.label in _m1_script0x2djokes__ALL_JOKES:
            jn_utils.log("Cannot register joke name: {0}, as a joke with that name already exists.".format(joke.label))
        
        else:
            _m1_script0x2djokes__ALL_JOKES[joke.label] = joke
            if joke.label not in store.persistent._jn_joke_list:
                joke._m1_script0x2djokes__save()
            
            else:
                joke._m1_script0x2djokes__load()

    def getJoke(joke_name):
        """
        Returns the joke for the given name, if it exists.

        IN:
            - joke_name - str joke name to fetch

        OUT: Corresponding JNJoke if the joke exists, otherwise None 
        """
        if joke_name in _m1_script0x2djokes__ALL_JOKES:
            return _m1_script0x2djokes__ALL_JOKES[joke_name]
        
        return None

    def getAllJokes():
        """
        Returns all jokes.
        """
        return _m1_script0x2djokes__ALL_JOKES.values()

    def getUnseenJokes():
        """
        Returns a list of all unseen jokes, or None if zero that are unlocked and unseen exist.
        
        OUT:
            - List of JNJoke jokes, or None
        """
        joke_list = JNJoke.filterJokes(
            joke_list=getAllJokes(),
            is_seen=False
        )
        
        return joke_list if len(joke_list) > 0 else None

    def getShownBeforeJokes():
        """
        Returns a list of all jokes shown at least once previously, or None if zero that are unlocked and shown before exist.
        
        OUT:
            - List of JNJoke jokes, or None
        """
        joke_list = JNJoke.filterJokes(
            joke_list=getAllJokes(),
            shown_count=1
        )
        
        return joke_list if len(joke_list) > 0 else None

    def resetJokes():
        """
        Resets the is_seen state for all jokes.
        """
        for joke in getAllJokes():
            joke.is_seen = False
        
        JNJoke.saveAll()

    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_clock_eating",
        display_name="Comer relojes",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_anime_animated",
        display_name="Anime",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_pirate_shower",
        display_name="Higiene pirata",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_cinderella_soccer",
        display_name="Cenicienta",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_blind_fish",
        display_name="Vista de pez",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_skeleton_music",
        display_name="Música esquelética",
        joke_category=JNJokeCategories.corny,
        conditional="persistent.jn_custom_music_unlocked"
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_skeleton_communication",
        display_name="Comunicación esquelética",
        joke_category=JNJokeCategories.corny,
        conditional="jn_jokes.getJoke('joke_skeleton_music').shown_count > 0"
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_ocean_greeting",
        display_name="Saludos del océano",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_tractor_trailer",
        display_name="Tractor-tráiler",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_tentacle_tickles",
        display_name="Tentáculos",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_basic_chemistry",
        display_name="Química básica",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_upset_cat",
        display_name="Molestar a un gato",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_cute_chicks",
        display_name="Pollitas lindas",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_lumberjack_axeception",
        display_name="Leñadores",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_tallest_building",
        display_name="El edificio más alto",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_baking_baseball",
        display_name="Hornear y béisbol",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_soya_tofu",
        display_name="Tofu",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_distrust_atoms",
        display_name="Teoría atómica",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_running_latte",
        display_name="Barista",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_guitar_stringing_along",
        display_name="Guitarrista",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_snek_maths",
        display_name="Matemáticas de serpientes",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_balloonist_hot_air",
        display_name="Aire caliente",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_author_cover_story",
        display_name="Historia de portada",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_wrapped_up_quickly",
        display_name="Embalaje",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_carpentry_nailed_it",
        display_name="Clavado",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_neutrons_no_charge",
        display_name="Neutrones",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_train_sound_track",
        display_name="Pistas de sonido",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_bored_typist",
        display_name="Mecanógrafos",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_regular_moovements",
        display_name="Vacas y escaleras",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_rabbit_lottery",
        display_name="Lotería de conejos",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_trees_logged_out",
        display_name="Cerrar sesión",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_con_crete",
        display_name="Con-creto",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_footless_snakes",
        display_name="Medir serpientes",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_bigger_ball",
        display_name="Deportes de pelota",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_meeting_walls",
        display_name="Paredes encontrandose",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_hour_feeling",
        display_name="Reloj y hora",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_spotless_tigers",
        display_name="Rayas de tigre",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_missing_bell",
        display_name="Sin timbre",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_cheesy_pizza",
        display_name="Pizza",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_veggie_mood",
        display_name="Humor vegetariano",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_scarecrow_award",
        display_name="Espantapájaros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sundae_school",
        display_name="Escuela",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_burned_tongue",
        display_name="Lenguas quemadas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_pointless_pencil",
        display_name="Lápices",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_know_the_drill",
        display_name="El taladro",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_can_do_attitude",
        display_name="Conservera",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_out_of_ctrl",
        display_name="Fuera de control",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_dishwashing",
        display_name="Lavar platos",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_escape_artists",
        display_name="Escapista",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_shoemakers",
        display_name="Zapateros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_lead_times",
        display_name="Paseadores de perros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_shark_literature",
        display_name="Literatura de tiburones",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_developers_committed",
        display_name="Desarrolladores",
        joke_category=JNJokeCategories.funny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_shelved_plans",
        display_name="Planes",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_action_figures",
        display_name="Acción",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_befriending_sharks",
        display_name="Hacerse amigo de tiburones",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_fisherman_broadcast",
        display_name="Videollamadas de pescadores",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_lighthouse_keeper",
        display_name="Farero",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_bakers",
        display_name="Panaderos",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_ravioli_pasta_way",
        display_name="Ravioli",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_spices",
        display_name="Especias",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_movie_theater_concessions",
        display_name="Cine",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_octo_puss",
        display_name="Gato de ocho patas",
        joke_category=JNJokeCategories.bad
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_roller_blade",
        display_name="Afeitarse como patinador",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_psychic_medium",
        display_name="Comidas psíquicas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_ex_press_delivery",
        display_name="Ex-prensa",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_keymakers_lockstep",
        display_name="Cerdejeros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_tube_piping_hot",
        display_name="Cocina de tubo",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_entomology_programming",
        display_name="Entomología",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_booked_it",
        display_name="Autores detenidos",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sheep_flock",
        display_name="Cultos",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_multiple_choice",
        display_name="Opción múltiple",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_horse_hairstyles",
        display_name="Peinados de caballo",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_new_heights",
        display_name="Montañeros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_coffee_grind",
        display_name="Café instantáneo",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_butterfly",
        display_name="Mariposas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_crampons",
        display_name="Escaladores de hielo",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_frog_notes",
        display_name="Notas de rana",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sea_urchins",
        display_name="Erizos",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_airforce_wings",
        display_name="Fuerza aérea",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_time_trial",
        display_name="Contrarreloj",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_wolves_alphabet",
        display_name="Educación de lobos",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sailor_shipshape",
        display_name="Marineros",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_seamstress_thread",
        display_name="Costurera",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sting_operation",
        display_name="Robo de abejas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_sculptors_steak_marbled",
        display_name="Escultores",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_rhetorical",
        display_name="Retórica",
        joke_category=JNJokeCategories.confusing
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_fuzz",
        display_name="Pelusa",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_restroom_comedian",
        display_name="Comediante de baño",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_glasses_framed",
        display_name="Gafas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_surround_sound",
        display_name="Técnico de audio",
        joke_category=JNJokeCategories.corny
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_rose_thorns",
        display_name="Rosas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_acrobats_somersault",
        display_name="Acróbatas",
        joke_category=JNJokeCategories.neutral
    ))
    _m1_script0x2djokes__registerJoke(JNJoke(
        label="joke_frog_seating",
        display_name="Asientos para ranas",
        joke_category=JNJokeCategories.corny
    ))

label joke_clock_eating:
    n 1fcsbg "Oye,{w=0.2} [player]..."
    n 1fsqbg "¿Alguna vez has intentado comerte un reloj?"
    n 1fsqcs "..."
    n 1tsqss "...¿No?"
    n 1ullaj "Bueno,{w=0.2} no puedo culparte."
    n 1fllss "La verdad es que...{w=1.25}{nw}"
    extend 1fsqbg " {i}consume{w=0.3} mucho tiempo{/i}."

    return

label joke_anime_animated:
    n 1ulraj "Dime,{w=0.2} [player]..."
    n 1unmbo "¿Sabes cómo algunas personas se meten mucho en su anime?{w=1}{nw}"
    extend 1nslsssbr " Como que los {i}mencionan{/i} constantemente cada vez que pueden."
    n 1tllsl "Si se emocionan mucho por un episodio..."
    n 1tsqss "¿Eso los haría estar...{w=1.25}{nw}"
    extend 1fsqbg " muy {i}anima{/i}-dos?"

    return

label joke_pirate_shower:
    n 1unmfl "¿Sabías por qué los piratas no se duchan antes de caminar por la tabla?{w=0.75}{nw}"
    extend 1ulraj " ¿Una vez que los capturan?"
    n 1tlrsl "...¿Por qué?"
    n 1fcssm "Jeje.{w=0.75}{nw}"
    extend 1fsqsm " ¿No es obvio?"
    n 1fsrsssbl "...¡Porque prefieren darse un baño de {i}mar{/i}!"

    return

label joke_cinderella_soccer:
    n 1fchbg "¡Hablemos de princesas,{w=0.2} [player]!"
    n 1tnmss "¿Tienes idea de por qué Cenicienta era tan mala jugando al fútbol?"
    n 1tsqsm "..."
    n 1tsqss "...¿No?"
    n 1fchgn "...¡Porque siempre llega tarde al {i}baile{/i}!"

    return

label joke_blind_fish:
    n 1fcsaj "Muy bien,{w=0.2} [player]..."
    n 1tsqsl "¿Qué hace un pez sin ojos?"
    n 1tsqfs "..."
    n 1fcsss "Pues,{w=0.5}{nw}"
    extend 1fsrss " tú dirás..."
    n 1nsqcasbl "...¡{i}Nada{/i}!"

    return

label joke_skeleton_music:
    n 1fcsaj "¡Bien!{w=0.75}{nw}"
    extend 1nslsssbr " Ya que te gusta tanto la música,{w=0.2} [player]..."
    n 1tsqsssbr "¿Cuál es el instrumento favorito de un esqueleto?"
    n 1nsrsssbr "..."
    n 1nsrposbl "...El {i}trom-bón{/i}."

    return

label joke_skeleton_communication:
    n 1nsrsssbl "Aquí tienes otro {i}espeluznante{/i} para ti.{w=0.75}{nw}"
    extend 1tnmsssbl " ¿Cómo se comunican los esqueletos entre sí?"
    n 1fcssssbl "Es obvio.{w=0.75}{nw}"
    extend 1nslsssbr " Usan un tele-{w=0.5}{i}hueso{/i}."

    return

label joke_ocean_greeting:
    n 1fcsbg "¡Muy bien!"
    n 1fcsss "¿Qué le dijo el mar a la arena?"
    n 1fsqsm "..."
    n 1fcsbg "Nada -{w=0.5}{nw}"
    extend 1fchgn " ¡solo le dio una {i}ola{/i}!"

    return

label joke_tractor_trailer:
    n 1fllaj "Se suponía que iba a ver una película sobre tractores,{w=0.75}{nw}"
    extend 1fcspo " ¡pero terminé perdiéndomela!"
    n 1ulraj "Pero está bien,{w=0.2} de verdad."
    n 1fsqss "No vi el tractor..."
    n 1fchbg "...¡Pero al menos vi el {i}tráiler{/i}!"

    return

label joke_tentacle_tickles:
    n 1fcsbg "¡Entonces!{w=0.75}{nw}"
    extend 1fsqbg " ¿Qué animal es dos veces animal?"
    n 1fsqcs "..."
    n 1fllss "¡Pues...{w=0.75}{nw}"
    extend 1fwlbg " el gato,{w=0.5} porque es gato y {i}araña{/i}!"

    return

label joke_basic_chemistry:
    n 1fcsbs "¡Hora de un examen de química,{w=0.2} [player]!"
    n 1fcsbg "¿Qué obtienes cuando mezclas azufre,{w=0.5}{nw}"
    extend 1fllss " wolframio,{w=0.5}{nw}"
    extend 1fnmbg " y plata?"
    n 1usqcs "..."
    n 1fcsbg "{i}SWAG{/i},{w=0.5}{nw}"
    extend 1fchgn " ¡por supuesto!"

    return

label joke_upset_cat:
    n 1ulraj "¿Qué le dice un gato a otro gato cuando se enoja?"
    n 1tnmsm "..."
    n 1fcssm "Ehehe."
    n 1fcsss "Pues...{w=1}{nw}"
    extend 1fsqss " ¡mira que te {i}{w=0.2}araño{/i}!"

    return

label joke_cute_chicks:
    n 1fslem "¿Por qué el granjero solitario estaba emocionado por ir al gallinero?"
    n 1fslsl "..."
    n 1fsrem "...Porque escuchó que estaría lleno de{w=0.75}{nw}"
    extend 1fcsem " '{i}pollitas{/i}{w=0.75}{nw}"
    extend 1fslsl " lindas'."

    return

label joke_lumberjack_axeception:
    n 1unmaj "¿Qué haría un leñador si no pudiera cortar un árbol?"
    n 1flrsm "..."
    n 1flrss "Tendrían un...{w=1}{nw}"
    extend 1fsqbg " {i}hacha{/i}{w=1.25}{nw}"
    extend 1nchgn "-que!"

    return

label joke_tallest_building:
    n 1fcsbg "Ya que te gusta tanto la literatura,{w=0.75}{nw}"
    extend 1fsqsm " esto debería ser fácil."
    n 1fcsaj "¡Entonces!{w=1}{nw}"
    extend 1tnmss "¿Por qué las bibliotecas son los edificios más altos?"
    n 1fsqsm "..."
    n 1fchbg "...¡Porque tienen más {i}historias{/i}!"

    return

label joke_baking_baseball:
    n 1unmbo "Te gusta hornear,{w=0.2} ¿verdad?"
    n 1fsqss "...Entonces, ¿qué tienen en común la repostería y el béisbol?"
    n 1tsqfs "..."
    n 1fcsbg "¡Fácil!{w=0.75}{nw}"
    extend 1fwlbg " ¡Tienes que vigilar la {i}masa{/i}!"

    return

label joke_soya_tofu:
    n 1fsqbg "¿Te consideras un experto culinario,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fcsbg " ¡Entonces adivina esto!"
    n 1fnmss "¿Cómo se defiende la leche de soja?"
    n 1fnmsm "..."
    n 1tsqss "¿Y bien?{w=1}{nw}"
    extend 1fsqbg " ¿No es obvio?"
    n 1nchgn "¡Hace {w=0.3}{i}tó-{w=0.3}fu de artes marciales{/i}!"

    return

label joke_distrust_atoms:
    n 1nlrbo "Ya sabes,{w=0.2} [player]..."
    n 1fnmbo "Nunca me gustó estudiar física.{w=0.75}{nw}"
    extend 1fslfl " {i}Especialmente{/i} la teoría atómica."
    n 1fslsl "..."
    n 1tnmem "¿Qué?{w=1}{nw}"
    extend 1flrfl " ¿Puedes culparme?{w=0.75}{nw}"
    extend 1fcsgs " ¡Es ridículo!"
    n 1fcspo "¿Cómo se supone que voy a tomarlo {i}en serio{/i}..."
    n 1fsqsm "...cuando los átomos {i}forman{/i} todo?"

    return

label joke_running_latte:
    n 1fcsfl "¿Cómo llamas a un barista que no llegó a trabajar a tiempo?"
    n 1nsrsl "..."
    n 1ncsfl "Llegó...{w=1.25}{nw}"
    extend 1fslcasbl " {i}latte{/i}."

    return

label joke_guitar_stringing_along:
    n 1unmpu "¿Te enteraste de la banda que acaba de echar a su guitarrista?"
    n 1fllfl "{i}Aparentemente{/i} prometieron practicar con todos,{w=0.75}{nw}"
    extend 1fnmgs " ¡pero ellos nunca aparecieron!{w=0.75}{nw}"
    extend 1fcswr " ¡Qué imbéciles!"
    n 1fcspo "..."
    n 1fcsaj "Bueno,{w=0.75}{nw}"
    extend 1fllfl " Supongo que se podría decir que sólo estaban...{w=0.75}{nw}"
    extend 1fsqss " ¡dándoles {i}cuerda{/i} a todos!"

    return

label joke_snek_maths:
    n 1ncsfl "...¿En qué tipo de reptil confiarías para hacer sumas largas?"
    n 1nsqsl "..."
    n 1nslpo "..."
    n 1nsqem "...{i}Una víbora{/i}."

    return

label joke_balloonist_hot_air:
    n 1nsqsl "...¿Qué tienen en común un aerostero arrogante y su globo?"
    n 1ncsemesi "..."
    n 1nsrem "Ambos están llenos de...{w=0.75}{nw}"
    extend 1nslajsbr " {i}aire{w=0.3} caliente{/i}."

    return

label joke_author_cover_story:
    n 1fsqsg "Será mejor que no {i}huyas{/i} después de este,{w=0.2} [player]..."
    n 1fcsbg "¿Qué hace un autor cuando necesita una excusa para un día libre?"
    n 1fsqsm "..."
    n 1fcssm "Jeje.{w=0.75}{nw}"
    extend 1fchbg " ¿Qué más?"
    n 1uchgn "...¡Escribirían una {i}historia de portada{/i}!"

    return

label joke_wrapped_up_quickly:
    n 1unmaj "¿Escuchaste sobre la empresa de embalaje que quebró?"
    n 1tnmbo "..."
    n 1tllss "¿No?{w=0.75}{nw}"
    extend 1ncsss " Supongo que no debería sorprenderme demasiado."
    n 1fcsbg "Después de todo."
    n 1fsqbg "Seguro que...{w=1}{nw}"
    extend 1fsqsm " {i}envolvieron todo{/i}{w=0.75}{nw}"
    extend 1fchgn " ¡rápido!"

    return

label joke_carpentry_nailed_it:
    n 1ullbo "Sabes..."
    n 1tnmbo "Realmente nunca me gustó mucho la carpintería."
    n 1tlraj "Pero...{w=1}{nw}"
    extend 1fsqss " ¿si lo hiciera?"
    n 1uchgn "...Me apuesto a que totalmente {w=0.3}{i}lo clavaría{/i}!"

    return

label joke_neutrons_no_charge:
    n 1fsqsm "Espero que estés listo para algo de física,{w=0.2} [player]."
    n 1fcsbg "¡Entonces!{w=1}{nw}"
    extend 1fsqbg "¿Por qué los neutrones no tienen que pagar entrada cuando van a alguna parte?"
    n 1fsqcs "..."
    n 1fcsbg "Porque para los neutrones...{w=1}{nw}"
    extend 1uchgn " ¡nunca hay {i}cargos{/i}!"

    return

label joke_train_sound_track:
    n 1fcsbg "¿Qué es lo que más le gusta escuchar a un conductor de tren mientras trabaja?"
    n 1fnmsm "..."
    n 1tsqss "¿No?{w=0.75}{nw}"
    extend 1fcssm " Jeje."
    n 1fcsbg "Bandas {i}sonoras{/i},{w=1}{nw}"
    extend 1fchbg " ¡por supuesto!"

    return

label joke_bored_typist:
    n 1fcsfl "...¿Por qué el mecanógrafo terminó renunciando a su trabajo?"
    n 1fsrbo "..."
    n 1fcsemesi "..."
    n 1fcsfl "...Porque no era su {i}tipo{/i}."

    return

label joke_regular_moovements:
    n 1nsqem "¿Por qué no se debería obligar a las vacas a subir y bajar escaleras con demasiada frecuencia?"
    n 1fsrsl "..."
    n 1fsrpu "Porque no es parte de sus regulares..."
    n 1fcsflesi "..."
    n 1fslflsbr "...{i}moo{/i}{w=1}-vimeintos."

    return

label joke_rabbit_lottery:
    n 1nlraj "Oye,{w=0.2} [player]...{w=1}{nw}"
    extend 1unmaj " ¿sabías que en realidad hay una {i}lotería{/i} para conejos?"
    n 1fcsbg "Apuesto a que no esperabas escuchar eso."
    n 1fchbg "¡Pero tiene todo el sentido cuando lo piensas!{w=1}{nw}"
    extend 1fsqsm " Después de todo..."
    n 1fsqss "...¿De qué otra forma se unirían a los...{w=0.5}{nw}"
    extend 1fnmbg " {i}millo-nari{/i}{w=0.75}{nw}"
    extend 1uchgn "-ejos?"

    return

label joke_trees_logged_out:
    n 1fcsaj "¡Entonces!{w=1}{nw}"
    extend 1fcsbg " ¿Por qué es tan difícil encontrar árboles en línea,{w=0.2} [player]?"
    n 1fsqsg "..."
    n 1fnmss "Porque siempre tienen...{w=1}{nw}"
    extend 1fsqbg " ¡cerrada la {i}sesión{/i}{w=1}{nw}"
    extend 1fchgn " de tronco!"

    return

label joke_con_crete:
    n 1ullaj "Oye,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " ¿oíste sobre el proyecto de construcción que fue clausurado?"
    n 1flrgs "¡Al parecer todos los materiales fueron cambiados por basura barata!{w=0.75}{nw}"
    extend 1fcsan " ¡Ni siquiera cumplía con el código!{w=1}{nw}"
    extend 1fsran " ¡Una estafa total!"
    n 1fcsaj "Resulta que..."
    n 1fllfl "Se quedaron con puro{w=0.5}{nw}"
    extend 1fsqbg " {i}ce{/i}{w=1}{nw}"
    extend 1nchgn "-miento!"

    return

label joke_footless_snakes:
    n 1ulraj "Oye,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " ¿{i}te{/i} has preguntado alguna vez cómo se miden las serpientes?"
    n 1uwdaj "¡Especialmente con todos esos tamaños diferentes!"
    extend 1fsqcs " ¿Qué tipo de medida funcionaría {i}mejor{/i}?"
    n 1fcsss "Bueno,{w=0.2} supongo que te quedarías con el sistema métrico..."
    n 1fsqbg "...¡Porque definitivamente no vas a usar {i}pies{/i}!"
    extend 1nchgn "!"

    return

label joke_bigger_ball:
    n 1ullbo "Sabes..."
    n 1nslsssbl "Terminé visitando a la enfermera de la escuela la última vez que hice deporte."
    n 1uwdaj "Me preguntaba por qué la pelota se hacía cada vez más grande..."
    n 1unmfl "...¡Pero luego me{w=0.25}{nw}"
    extend 1fchbgsbr " {i}pegó{/i}!"

    return

label joke_meeting_walls:
    n 1fsqfl "...¿Qué le dijo una pared a la otra pared?"
    n 1ftlemesi "..."
    n 1fslbo "Nos vemos en la{w=1}{nw}"
    extend 1fsqbo " {i}esquina{/i}."

    return

label joke_hour_feeling:
    n 1fcsaj "¡Entonces!{w=0.5}{nw}"
    extend 1fsqsm " ¿Cómo saludó el reloj grande al reloj pequeño,{w=0.2} [player]?"
    n 1fsldv "..."
    n 1fchgn "¿{i}Hora{/i}{w=1} qué tal estás?"

    return

label joke_spotless_tigers:
    n 1ulraj "Entonces,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmfl " ¿alguna vez te preguntaste por qué los tigres tienen rayas?"
    n 1fcsss "No es una elección de moda,{w=0.2} eso es seguro..."
    n 1fsqsm "...¡Es porque no quieren que los{w=0.5}{nw}"
    extend 1fchgn " {i}rayen{/i} de la lista!"

    return

label joke_missing_bell:
    n 1fsqsm "¡Toc,{w=0.2} toc,{w=0.2} [player]!"

    show natsuki 1fchsm

    menu:
        "¿Quién es?":
            pass

    n 1ucsaj "Nobel."

    show natsuki 1fsqcs

    menu:
        "¿Nobel quién?":
            pass

    n 1nnmbo "{i}No-bel{/i},{w=1}{nw}"
    extend 1fchgn " ¡así que solo toqué!"

    return

label joke_cheesy_pizza:
    n 1fsqfl "...Encontré un chiste sobre pizza."
    n 1fsrfl "Pero...{w=0.75}{nw}"
    extend 1fcsem " ugh."
    n 1fslsl "Sí.{w=0.3} De ninguna manera voy a compartir algo...{w=1}{nw}"
    extend 1nsqpo " {i}tan cursi{/i}."

    return

label joke_veggie_mood:
    n 1nslsssbl "Je.{w=0.75}{nw}"
    extend 1fcssssbl " A ver a quién te recuerda {i}esto{/i},{w=0.2} [player]."
    n 1ccsajsbl "¡E-{w=0.2}jeem!"
    n 1tnmbo "¿Tienes {i}alguna{/i} idea de cuándo los vegetarianos tienen cambios de humor?"
    n 1nllss "Bueno...{w=0.75}{nw}"
    extend 1fcssmesm " Yo sí."
    n 1fcsbg "...Cuando tienen{w=0.75}{nw}"
    extend 1fchbg " ¡mala {i}uva{/i}!"

    return

label joke_scarecrow_award:
    n 1fsqfl "...¿Por qué el espantapájaros recibió un premio?"
    n 1ncsemesi "..."
    n 1fcsbo "Porque..."
    n 1fsqfl "Fue {i}destacado{/i}{w=0.75}{nw}"
    extend 1nsrca " en su campo."

    return

label joke_sundae_school:
    n 1ullaj "Sabes..."
    n 1tnmbo "He estado pensando mucho en la escuela últimamente."
    n 1ulraj "Quiero decir,{w=0.5}{nw}"
    extend 1unmfl " había {i}tantas{/i} escuelas a las que podría haber ido -{w=0.5}{nw}"
    extend 1fspbg " ¡una incluso daba clases de cocina!"
    n 1fcsan "¡Pero el horario significaba ir en un {i}fin de semana{/i}!{w=0.5}{nw}"
    extend 1fllwr " ¡¿Quién {i}hace{/i} eso?!"
    n 1fcsem "Ugh..."
    n 1flrfl "Hablando de una escuela...{w=1}{nw}"
    extend 1fsqss " {i}domini{/i}{w=0.75}{nw}"
    extend 1uchgn "-cal!"

    return

label joke_burned_tongue:
    n 1ullaj "Sabes,{w=0.75}{nw}"
    extend 1tnmbo " nunca entendí por qué los hipsters pasaban tanto tiempo en cafeterías."
    n 1nsrbo "Como...{w=0.3} ¿qué tiene de divertido estar sentado bebiendo de una taza todo el día?"
    n 1nllfl "De hecho,{w=0.2} ayer mismo vi a uno de ellos en un café..."
    n 1unmaj "¡Y no paraba de quemarse la lengua!{w=0.5} ¡Como si fuera a propósito o algo así!{w=0.75}{nw}"
    extend 1tnmss " ¿Te preguntas por qué,{w=0.2} [player]?"
    n 1flrss "Porque se bebió su café...{w=1}{nw}"
    extend 1fchgn " ¡antes de que se {i}enfriara{/i}!"

    return

label joke_pointless_pencil:
    n 1fllfl "Hombre..."
    n 1fcsem "Estaba {i}intentando{/i} trabajar en mi poesía,{w=0.2} ¡y mi lápiz decidió romperse!{w=0.75}{nw}"
    extend 1fslpo " Genial."
    n 1cllaj "{i}Iba{/i} a contar un chiste sobre ello..."
    n 1tnmbo "¿Pero ahora?{w=0.5}{nw}"
    extend 1fsqsm " No tiene {i}punta{/i}."

    return

label joke_know_the_drill:
    n 1ulraj "Ya sabes,{w=0.2} [player]..."
    n 1nsqsl "Siempre solía molestarme con la gente haciendo trabajos de construcción.{w=0.75}{nw}"
    extend 1fnmem " ¡{i}Especialmente{/i} los fines de semana!"
    n 1fllfl "Es como...{w=1}{nw}"
    extend 1fcsbo " Entiendo que tienen un trabajo que hacer.{w=0.75}{nw}"
    extend 1fsran " ¡¿Pero seriamente tienen que empezar tan {i}temprano{/i}?!{w=0.75}{nw}"
    extend 1fcsan " ¡Yeesh!"
    n 1cslsl "..."
    n 1cslaj "Pero...{w=1}{nw}"
    extend 1cllca " te terminas acostumbrando a todo el ruido después de un rato,{w=0.2} supongo."
    n 1cnmss "Supongo que eventualmente solo...{w=1}{nw}"
    extend 1fsqbg " te sabes el {i}taladro{/i},{w=0.75}{nw}"
    extend 1nchgn " ¿verdad?"

    return

label joke_can_do_attitude:
    n 1fcsbg "Veamos qué tan bien puedes {i}procesar{/i} esto,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fsqsm " Jeje."
    n 1fcsbs "¡Entonces!{w=0.75}{nw}"
    extend 1tsqss " ¿Alguna vez te preguntaste qué se necesita para conseguir un trabajo en una conservera?"
    n 1tsqsm "..."
    n 1fsqsm "¿No?{w=0.75}{nw}"
    extend 1fcsbs " ¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1fcssmesm " ¿No es obvio?"
    n 1fcsbg "...Solo necesitas una actitud de{w=0.5}{nw}"
    extend 1fsqbg " ¡yo {i}puedo{/i}!{w=1}{nw}"
    extend 1uchgn " ...¡hacer latas!"

    return

label joke_out_of_ctrl:
    n 1fllbo "Tengo que decir,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fsqfl " Estoy empezando a hartarme {i}realmente{/i} de todas estas historias sobre escasez."
    n 1fnmem "En serio -{w=0.5}{nw}"
    extend 1fcsgs " ¡es ridículo!{w=0.75}{nw}"
    extend 1flrfl " ¿Por qué es tan difícil pedir cosas,{w=0.2} de repente?"
    n 1fcsgs "Quiero decir,{w=0.5}{nw}"
    extend 1fslpo " ¡incluso el otro día escuché sobre lugares quedándose sin partes para teclados!"
    n 1fcsss "...Je."
    n 1fcstr "Supongo que su gestión realmente debe estar{w=0.5}{nw}"
    extend 1fsqbg " fuera de {i}Control{/i},{w=0.75}{nw}"
    extend 1fchgn " ¿eh?"

    return

label joke_dishwashing:
    n 1csqfl "¿Por qué lavar platos no se considera un deporte competitivo?"
    n 1csrsl "..."
    n 1fcsemesi "..."
    n 1nsqfl "Porque la victoria te la dan...{w=1.25}{nw}"
    extend 1cslcasbr " en {i}bandeja{/i}."

    return

label joke_escape_artists:
    n 1ccsflesi "..."
    n 1cllsl "¿Por qué no deberías confiar en que un escapista aparezca en una invitación?"
    n 1csrbosbr "..."
    n 1ccsemsbr "..."
    n 1nsrtrsbr "...Porque siempre están siendo{w=0.5}{nw}"
    extend 1csqcasbr " {i}atados{/i}."

    return

label joke_shoemakers:
    n 1fllfl "¿Por qué los zapateros no van a ningún lugar soleado de vacaciones?"
    n 1fslca "..."
    n 1ccsemesi "..."
    n 1csrem "...Porque ya están{w=0.5}{nw}"
    extend 1csrsl " {i}curtidos{/i}."

    return

label joke_lead_times:
    n 1ccsfl "...Muy bien.{w=0.75}{nw}"
    extend 1csqem " Tú pediste esto,{w=0.2} [player]."
    n 1csqsl "¿Por qué es tan difícil conseguir un trabajo como paseador de perros hoy en día?"
    n 1cslsl "..."
    n 1ccssl "Je."
    n 1cdlfl "...Porque te traen con la{w=0.5}{nw}"
    extend 1fslfl " {i}correa{/i}."

    return

label joke_shark_literature:
    n 1fcsbs "¡Bien!{w=0.75}{nw}"
    extend 1fdwbg " ¿Qué tal este,{w=0.5}{nw}"
    extend 1fsqsm " [player]?"
    n 1fcsbg "¿Qué tipo de literatura le das a un tiburón?"
    n 1fnmsm "..."
    n 1usqss "¿No?{w=0.75}{nw}"
    extend 1fsqsm " ¿Ni siquiera una conjetura?"
    n 1fcssmesm "Qué decepcionante.{w=0.75}{nw}"
    extend 1fcsbg " ¿No es obvio,{w=0.2} [player]?"
    n 1fnmss "Le das cosas a las que realmente puedan...{w=1}{nw}"
    extend 1fsqbg " {i}hincarles el diente{/i},{w=0.75}{nw}"
    extend 1fchgn " ¡duh!"

    return

label joke_developers_committed:
    n 1ttrpu "Ya sabes,{w=0.2} [player]...{w=1}{nw}"
    extend 1tlraj " Siempre me he preguntado."
    n 1tsqfl "¿Es difícil para los desarrolladores empezar relaciones?{w=0.75}{nw}"
    extend 1tllbo " ¿Los que se meten con código y todas esas cosas?"
    n 1tsqsl "..."
    n 1tsqfl "¿No?{w=0.75}{nw}"
    extend 1clrpu " Huh.{w=1}{nw}"
    extend 1csqss " ¿Seguro,{w=0.2} [player]?"
    n 1fcsss "Porque por lo que estoy leyendo aquí..."
    n 1nchgn "...¡Parece que siempre están bastante {i}comprometidos{/i} ya!"

    return

label joke_shelved_plans:
    n 1ccstr "Tengo que decir,{w=0.2} [player].{w=0.75}{nw}"
    extend 1cslca " Todavía estoy bastante desanimada por estar atrapada aquí y todo eso,{w=0.2} ya sabes."
    n 1cllbo "..."
    n 1tnmfl "¿Qué?{w=0.75}{nw}"
    extend 1tnmbo " ¿No te lo dije?"
    n 1fcsgs "¡De hecho conseguí una entrevista para un trabajo de medio tiempo después de la escuela en una librería!{w=0.75}{nw}"
    extend 1fcspo " ¡Apliqué en línea y todo!"
    n 1knmfl "...¿Pero cómo se supone que voy a llegar allí ahora?"
    n 1ccsemesi "Ugh..."
    n 1nsrpo "..."
    n 1ncsaj "Bueno."
    n 1tllss "Supongo que esos planes van a tener que quedarse{w=0.5}{nw}"
    extend 1fsqbg " en la {i}estantería{/i}{w=0.75}{nw}"
    extend 1nchgn " después de todo,{w=0.2} ¿eh?"

    return

label joke_action_figures:
    n 1fsrem "...En serio no puedo creer que esté contando {i}este{/i}.{w=0.75}{nw}"
    extend 1ccsem " Ugh."
    n 1ccstresi "..."
    n 1nsqsl "¿Qué tipo de regalo aman más los directores de cine?"
    n 1fllbosbr "..."
    n 1fcsflsbr "...Figuras de{w=0.75}{nw}"
    extend 1fsqflsbr " {i}acción{/i}."

    return

label joke_befriending_sharks:
    n 1ccsss "Je.{w=0.75}{nw}"
    extend 1fsqss " ¿Listo,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fnmbg " Vas a estar como pez fuera del agua después de este."
    n 1fcsaj "¡Entonces!{w=0.75}{nw}"
    extend 1fcsbg " ¿Cómo haces para hacerte amigo de un tiburón?"
    n 1fsqsm "..."
    n 1fsqss "¿No?{w=0.75}{nw}"
    extend 1flrss " Wow,{w=0.2} [player]..."
    n 1fsgbg "¿No es obvio?"
    n 1fllss "¡Solo tienes que{w=0.75}{nw}"
    extend 1fsqbg " {i}cebarlo{/i}{w=0.75}{nw}"
    extend 1nchgn " bien primero!"

    return

label joke_fisherman_broadcast:
    n 1csqfl "...¿Por qué es tan difícil hacer una videollamada con un pescador?"
    n 1csrca "..."
    n 1ccspuesi "..."
    n 1clrem "...Porque solo usan{w=0.75}{nw}"
    extend 1csqup " {i}redes{/i}."

    return

label joke_lighthouse_keeper:
    n 1fsrpu "En serio no puedo creer que esté contando {i}este{/i}."
    n 1ccsbo "..."
    n 1cllfl "¿Qué pasa cuando un farero es ascendido?"
    n 1cllslsbr "..."
    n 1ccsemesisbr "..."
    n 1ccsajsbr "Su carrera se vuelve...{w=1}{nw}"
    extend 1csrflsbr " {i}más brillante que nunca{/i}."

    return

label joke_bakers:
    n 1ccsemesi "..."
    n 1clrtr "¿Cómo describes a un panadero a punto de romper su propio récord?"
    n 1csrsl "..."
    n 1ccsflsbl "...Hombre,{w=0.5}{nw}"
    extend 1fslemsbl " esto es tonto."
    n 1cllajsbl "Estaría...{w=1}{nw}"
    extend 1csqemsbl " {i}en racha{/i}."

    return

label joke_ravioli_pasta_way:
    n 1cslflsbr "...No puedo {i}creer{/i} que esté leyendo este.{w=0.75}{nw}"
    extend 1ccsslsbr " Yeesh."
    n 1csrbo "..."
    n 1clrfl "¿Escuchaste sobre el chef que simplemente no podía dejar los raviolis?"
    n 1cnmsl "..."
    n 1ccsemesi "..."
    n 1cllfl "Se pasó de...{w=1}{nw}"
    extend 1csqup " {i}pasta{/i}{w=0.75}{nw}"
    extend 1csrsl "."

    return

label joke_spices:
    n 1csqbg "OKay.{w=0.75}{nw}"
    extend 1fcsbs " ¡Entonces!"
    n 1unmss "¿Cuándo empezaría un chef a añadir pimentón y chile en polvo extra a un plato que pediste?"
    n 1cnmsm "..."
    n 1csqss "¿No?{w=0.75}{nw}"
    extend 1fcsaj " ¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1fnmbg " ¡Incluso {i}tú{/i} deberías haber clavado este!"
    n 1fcsbg "...Cuando quiere{w=0.5}{nw}"
    extend 1fsqss " {i}condimentar{/i}{w=0.75}{nw}"
    extend 1fchbs " tu vida,{w=0.5}{nw}"
    extend 1nchgn " ¡por supuesto!"

    return

label joke_movie_theater_concessions:
    n 1tllfl "Oye,{w=0.5}{nw}"
    extend 1tnmaj " [player] -{w=0.5}{nw}"
    extend 1unmaj " ¿escuchaste sobre el cine que cerró recientemente?"
    n 1csrem "¡Qué fastidio!{w=0.75}{nw}"
    extend 1unmem " En serio -{w=0.5}{nw}"
    extend 1fllem " ¡los dueños tuvieron que vender todo y demás!"
    n 1ccsfl "Aparentemente no pudieron llegar a un acuerdo decente con todos sus costos y licencias."
    n 1csrss "Je."
    n 1ccsss "Supongo que podrías decir...{w=1}{nw}"
    extend 1fchgn " ¡que simplemente no hicieron suficientes {i}concesiones{/i}!"

    return

label joke_octo_puss:
    n 1ccsfl "Ugh...{w=1}{nw}"
    extend 1clrfll " este simplemente suena cruel.{w=0.75}{nw}"
    extend 1fsrsll " Asqueroso."
    n 1ccspuesi "..."
    n 1cllfl "¿Cómo llamas a un gato nacido con el doble de patas?"
    n 1cllsl "..."
    n 1fslsl "..."
    n 1fcsfl "...Un octo-{w=0.75}{nw}"
    extend 1fsrbo "{i}gato{/i}."

    return

label joke_roller_blade:
    n 1fcsbg "Veamos cuánto te {i}china{/i} este,{w=0.5}{nw}"
    extend 1fsqbg " [player]!"
    n 1fcsaj "¡Entonces!{w=0.75}{nw}"
    extend 1unmaj " ¿Qué usa un patinador profesional para un afeitado limpio?"
    n 1tsqsm "..."
    n 1tsqss "¿No?{w=0.75}{nw}"
    extend 1fsqbg " ¿Ni siquiera una conjetura?{w=0.75}{nw}"
    extend 1fsgsm " Ehehe."
    n 1fcsbs "¡Fácil!"
    n 1ullbg "¡Usarían una hoja de...{w=0.75}{nw}"
    extend 1uchbg " {i}patinar{/i}!{w=0.75}{nw}"
    extend 1fchgn " ¡Duh!"

    return

label joke_psychic_medium:
    n 1fcsgs "¡Bien!{w=0.75}{nw}"
    extend 1fsqbg " ¡Aquí tienes una {i}lectura{/i} para ti,{w=0.5}{nw}"
    extend 1fsgsm " [player]!"
    n 1ccsbg "¿Qué tamaño de comida pediría un psíquico?"
    n 1csqcs "..."
    n 1fsgsmeme "Jeje."
    n 1fcsbs "...Pediría un {i}médium{/i},{w=0.75}{nw}"
    extend 1fchbg " ¡obviamente!"

    return

label joke_ex_press_delivery:
    n 1nlraj "Por cierto,{w=0.2} [player] -{w=0.5}{nw}"
    extend 1unmfl " ¿escuchaste sobre el periódico que cerró recientemente?"
    n 1fllfl "Apenas dieron aviso.{w=0.75}{nw}"
    extend 1fsgem " ¡Así que todos tuvieron que empacar y encontrar nuevos trabajos inmediatamente!{w=0.75}{nw}"
    extend 1fcsfl " Qué chiste."
    n 1cnmaj "¡Un par incluso terminó trabajando en mensajería!"
    n 1ncsss "...Je."
    n 1clrsssbl "Supongo que podrías decir que se especializan en...{w=1}{nw}"
    extend 1fsqbg " envíos {i}ex-prensa{/i}!"

    return

label joke_keymakers_lockstep:
    n 1ccsemesi "..."
    n 1ctrfl "...¿Cómo caminan los cerrajeros y sus colegas en el trabajo?"
    n 1csrslsbr "..."
    n 1csqfl "...A paso de...{w=0.75}{nw}"
    extend 1cslup "ce-{i}rradura{/i}."

    return

label joke_tube_piping_hot:
    n 1ccsbg "Veamos si este es de tu gusto,{w=0.5}{nw}"
    extend 1fsgsm " [player]."
    n 1fcsbg "¿Puedes comer comida que alguien preparó dentro de un tubo?"
    n 1fsqsm "..."
    n 1ullbg "Bueno,{w=0.2} ¡sí!{w=0.75}{nw}"
    extend 1fchbg " ¡Seguro que puedes!"
    n 1flrss "Solo tiene que servirse{w=0.5}{nw}"
    extend 1fsgbg " recién salido del...{w=0.75}{nw}"
    extend 1fchbg " {i}tubo{/i},{w=0.5}{nw}"
    extend 1fchsmeme " ¡eso es todo!"

    return

label joke_entomology_programming:
    n 1fnmbg "¡Okay!{w=0.75}{nw}"
    extend 1fcsbg " ¿Por qué el entomólogo pensó en dedicarse a la programación?"
    n 1fnmsm "..."
    n 1tllss "Bueno,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1tsgss " ¿No es obvio?"
    n 1nchgn "¡Porque escuchó que estaría constantemente encontrando {i}bugs{/i}!"

    return

label joke_booked_it:
    n 1fcsbg "¡Bien!{w=0.75}{nw}"
    extend 1fnmbg " Veamos si puedes {i}leer{/i}{w=0.5}{nw}"
    extend 1fcssmesm " este,{w=0.2} [player]."
    n 1fcsaj "¡Entonces!"
    n 1unmfl "¿Escuchaste sobre ese autor famoso que la policía detuvo el otro día?"
    n 1tnmsl "..."
    n 1csqsm "¿No?"
    n 1ccsss "Je.{w=0.75}{nw}"
    extend 1flrbg " No puedo decir que me sorprenda."
    n 1fchbg "...Porque se fue {i}leyendo{/i},{w=0.75}{nw}"
    extend 1fchgnelg " ¡obviamente!"

    return

label joke_sheep_flock:
    n 1fcsfl "Ugh..."
    n 1fsrca "Quienquiera que añadió este {i}definitivamente{/i} tenía lana entre las orejas.{w=0.75}{nw}"
    extend 1fsraj " Eso es todo lo que digo."
    n 1fcsflesi "..."
    n 1cllbo "Lo que sea.{w=0.75}{nw}"
    extend 1cnmfl " ¿Por qué las ovejas son las mejores para iniciar un culto?"
    n 1clrsl "..."
    n 1csrsl "..."
    n 1csqfl "...Porque ya tienen un{w=0.5}{nw}"
    extend 1cslem " {i}rebaño{/i}."

    return

label joke_multiple_choice:
    n 1ccsbg "Déjame{w=0.5}{nw}"
    extend 1csqbg " {i}probarte{/i}{w=0.5}{nw}"
    extend 1fsqsm " con este,{w=0.2} [player]."
    n 1fcsbg "¡Bien!"
    n 1unmaj "Entonces,{w=0.2} ¿por qué los exámenes de opción múltiple son la peor forma de probar a alguien?"
    n 1tsgsm "..."
    n 1csgss "¿En serio?"
    n 1csqbg "¿Ni siquiera una conjetura,{w=0.2} [player]?{w=0.75}{nw}"
    extend 1fsqsm " Jeje."
    n 1fcsbg "Fácil -{w=0.5}{nw}"
    extend 1fchgnelg " ¡porque es solo un {i}ejercicio de marcar casillas{/i}!"

    return

label joke_horse_hairstyles:
    n 1ccsem "En serio no puedo creer que {i}este{/i} sea el que tengo que leer.{w=0.75}{nw}"
    extend 1csrsl " Ugh."
    n 1ccsflesi "..."
    n 1csqfl "¿Qué tipo de peinado nunca deberías hacerle a un caballo?"
    n 1csqsl "..."
    n 1csrbo "..."
    n 1csrem "...Una {i}cola{/i}{w=0.5}{nw}"
    extend 1csqem " de caballo."

    return

label joke_new_heights:
    n 1csqaj "¿Qué pasa cuando un montañero es ascendido?"
    n 1cslsl "..."
    n 1ccsflesi "Ugh..."
    n 1cllpu "...Alcanzan{w=0.75}{nw}"
    extend 1csqem " {i}nuevas alturas{/i}."

    return

label joke_coffee_grind:
    n 1ccsbg "Veamos cómo te{w=0.5}{nw}"
    extend 1csgbg " {i}tomas{/i}{w=0.5}{nw}"
    extend 1fnmbg " este,{w=0.5}{nw}"
    extend 1fsqsm " [player]!"
    n 1fcsgs "¡Entonces!{w=0.75}{nw}"
    extend 1fnmss " ¿Por qué el barista finalmente empezó a ofrecer café instantáneo?"
    n 1fsqsm "..."
    n 1fcsss "Je."
    n 1flrbs "Porque estaban hartos de la {i}molienda{/i},{w=0.75}{nw}"
    extend 1fchgnelg " ¡por supuesto!"

    return

label joke_butterfly:
    n 1ccsss "Je."
    n 1ccsbg "Mejor siéntate,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fnmbg " ¡Porque te garantizo que este te va a {i}encantar{/i}!"
    n 1fdwaj "¿Cuál es el insecto más difícil de atrapar?"
    n 1fsqsm "..."
    n 1fcssm "Ehehe."
    n 1fnmbg "Una {i}mari{/i}{w=0.75}{nw}"
    extend 1fsgbs " -posa,{w=0.5}{nw}"
    extend 1fchgn " ¡Obviamente!"

    return

label joke_crampons:
    n 1fdrfl "Sheesh...{w=1}{nw}"
    extend 1fsrem " ¿Es este en serio lo {i}mejor{/i} que pudieron hacer?{w=0.75}{nw}"
    extend 1fcsem " Dame un respiro."
    n 1fllfl "Ugh.{w=0.75}{nw}"
    extend 1fcsfl " ¿Qué es lo peor que le puedes dar a un escalador de hielo con un esguince?"
    n 1csqsl "..."
    n 1csremsbr "{i}Calam{/i}{w=0.75}{nw}"
    extend 1csrajsbr " -bres."

    return

label joke_frog_notes:
    n 1ccsemesi "..."
    n 1cslflsbl "Supongo que mejor me disculpo por adelantado por este,{w=0.2} [player].{w=0.75}{nw}"
    extend 1ccsemsbl " Ugh."
    n 1ccsaj "Bien.{w=0.75}{nw}"
    extend 1csgsl " ¿Cómo toman notas las ranas para la clase?"
    n 1clrsl "..."
    n 1fsrsl "..."
    n 1fcsfl "Usan sus {i}notas{/i}-{w=0.75}{nw}"
    extend 1csqfl " fures."

    return

label joke_sea_urchins:
    n 1ccsflesi "..."
    n 1csqem "¿En serio tengo que leerte {i}este{/i}?{w=0.75}{nw}"
    extend 1csrfl " Hombre..."
    n 1ccsaj "Bien.{w=0.2} ¿Qué tipo de vida marina causa más problemas en las calles?"
    n 1csgslsbl "..."
    n 1fllemsbl "Ugh.{w=0.75}{nw}"
    extend 1fcsemsbr " Un {i}golfo{/i}{w=0.5}{nw}"
    extend 1fsqflsbr " de mar."

    return

label joke_airforce_wings:
    n 1ulraj "Oye,{w=0.2} [player]...{w=1}{nw}"
    extend 1tsgfl " ¿Oíste sobre la fuerza aérea que empezó a usar pájaros para volar misiones especiales?"
    n 1unmgs "¡Sí!{w=0.75}{nw}"
    extend 1cllflsbl " ¡Hablando de inesperado!{w=0.75}{nw}"
    extend 1cslbosbl " ¡Pensé que alguien me estaba gastando una broma cuando me enteré!"
    n 1ccsajsbl "Bueno,{w=0.2} de todos modos."
    n 1csrss "Nunca dijeron exactamente qué tipo de cosas harían,{w=0.75}{nw}"
    extend 1ccssmesm " pero puedo decirte una cosa,{w=0.2} [player]."
    n 1ccsbg "Al menos ya se han{w=0.5}{nw}"
    extend 1fsqbg " {i}ganado sus alas{/i},{w=0.75}{nw}"
    extend 1fchgn " ¿verdad?"

    return

label joke_time_trial:
    n 1ccsbg "Je.{w=0.75}{nw}"
    extend 1fcsss " Entonces,{w=0.2} [player].{w=0.75}{nw}"
    extend 1csqbg " ¿Qué tipo de deportes de motor ve un relojero los fines de semana?"
    n 1tsqsm "..."
    n 1tsqaj "¿No?{w=0.75}{nw}"
    extend 1tsgfl " ¿En serio?{w=0.75}{nw}"
    extend 1fcssm " {i}Yo{/i} pensé que era bastante fácil,{w=0.2} [player]."
    n 1ccsbg "Estarían viendo{w=0.5}{nw}"
    extend 1csgbg " {i}la contrarreloj{/i},{w=0.75}{nw}"
    extend 1fchbs " ¡duh!"

    return

label joke_wolves_alphabet:
    n 1ccsbg "Je.{w=0.75}{nw}"
    extend 1fllbg " Veremos quién está{w=0.75}{nw}"
    extend 1fsqss " {i}aullando{/i}{w=0.75}{nw}"
    extend 1fcsss " después de este."
    n 1fcsaj "'Kay.{w=0.75}{nw}"
    extend 1fcssm " ¡Entonces!"
    n 1unmaj "¿Qué es lo primero que aprendería un lobo si empezara a ir a la escuela?"
    n 1cnmsm "..."
    n 1csqss "¿Oh?{w=0.75}{nw}"
    extend 1csqbg " ¿No vas a morder el anzuelo,{w=0.2} [player]?"
    n 1ccssm "Ehehe."
    n 1flrbg "Aprenderían el {i}alfa{/i}-{w=0.75}{nw}"
    extend 1fsqbg "beto,{w=0.5}{nw}"
    extend 1fchbs " ¡Duh!"

    return

label joke_sailor_shipshape:
    n 1fupfl "Ugh.{w=0.75}{nw}"
    extend 1fsrem " Como si {i}esta{/i} excusa de chiste tuviera algún sentido.{w=0.75}{nw}"
    extend 1cnmem " ¿Realmente tengo que leerlo,{w=0.2} [player]?"
    n 1ccsemesi "..."
    n 1cslfl "¿Cómo describes a un marinero que entrena todos los días?"
    n 1cllslsbr "..."
    n 1fdlslsbr "..."
    n 1fsqfl "...En forma... de{w=0.75}{nw}"
    extend 1fsrem "{i}barco{/i}."

    return

label joke_seamstress_thread:
    n 1ccsaj "Entonces,{w=0.2} [player] -{w=0.5}{nw}"
    extend 1unmaj " ¿oíste sobre la costurera que siempre dejaba su trabajo hasta el último minuto posible?"
    n 1clrfl "¡Sí!{w=0.75}{nw}"
    extend 1cnmwr " Hablando de implacable.{w=0.75}{nw}"
    extend 1csqemsbr " ¿Te imaginas todo lo que costaría arruinarlo todo,{w=0.2} trabajando así?"
    n 1ccsfl "Hombre...{w=1}{nw}"
    extend 1tnmpu " ¿Si algo pasara?"
    n 1ccsss "...Je."
    n 1fllss "Supongo que realmente estaría{w=0.5}{nw}"
    extend 1fsqbg " {i}pendiendo de un hilo{/i},{w=0.75}{nw}"
    extend 1fchgn " ¿verdad?"

    return

label joke_sting_operation:
    n 1clraj "Oye,{w=0.2} [player]...{w=1}{nw}"
    extend 1tnmsl " ¿oíste sobre todos los robos dirigidos a apicultores recientemente?"
    n 1ccsfl "Quiero decir,{w=0.5}{nw}"
    extend 1fcswr " ¡vamos!{w=0.75}{nw}"
    extend 1fsqem " ¿{i}Abejas{/i}?{w=0.75}{nw}"
    extend 1fllem " ¿Qué tan bajo podrías {i}caer{/i}?"
    n 1fllpu "Aunque...{w=1}{nw}"
    extend 1cllbo " tengo que admitir.{w=0.75}{nw}"
    extend 1unmfl " ¿Cómo los atraparon al final?"
    n 1ccsss "Je."
    n 1ccsbg "¡Eso es lo que yo llamo una{w=0.5}{nw}"
    extend 1fsqbg " operación {i}aguijón{/i}!"

    return

label joke_sculptors_steak_marbled:
    n 1fcsbg "¡'Kay!{w=0.75}{nw}"
    extend 1fsqbg " Entonces,{w=0.2} [player]..."
    n 1fsgss "¿Cómo prefieren los escultores sus filetes?"
    n 1fsgsm "..."
    n 1tsqbg "¿No?{w=0.75}{nw}"
    extend 1fcssmesm " ¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
    extend 1tlrbg " ¿No es obvio?"
    n 1tsgbg "...Con mucho{w=0.5}{nw}"
    extend 1fsqbg " {i}marmolado{/i},{w=0.75}{nw}"
    extend 1fchbs " ¡duh!"

    return

label joke_rhetorical:
    n 1ccsaj "...Entonces."
    n 1cdwpu "...¿Qué obtienes si cruzas un chiste{w=0.5}{nw}"
    extend 1tsqsl " con una pregunta retórica?"

    return

label joke_fuzz:
    n 1ccsflesi "...Hombre,{w=0.2} esto es tonto.{w=0.75}{nw}"
    extend 1csrsl " Bien."
    n 1ccsaj "¿A quién llamas por alguien que solo roba lana,{w=0.2} hilo,{w=0.2} y calcetines esponjosos?"
    n 1cnmbo "..."
    n 1cllbo "..."
    n 1cnmfl "...A la{w=0.5}{nw}"
    extend 1cslfl " {i}pelusa{/i}-icía."

    return

label joke_restroom_comedian:
    n 1ccsemesi "..."
    n 1clrbo "¿Por qué el comediante insistió en calentar su acto en el baño?"
    n 1csqbo "..."
    n 1cslfl "...No puedo creer que esté diciendo esto."
    n 1ccsfl "Para tener chistes...{w=1}{nw}"
    extend 1csqpo " {i}corrientes{/i}."

    return

label joke_glasses_framed:
    n 1fsqbg "Veamos cómo manejas este.{w=0.75}{nw}"
    extend 1fcsaj " ¡Entonces!"
    n 1csqbg "¿Cómo reacciona alguien con gafas ante malas noticias?"
    n 1csqsm "..."
    n 1fsqss "Je.{w=0.75}{nw}"
    extend 1csgbg " ¿No lo sabes,{w=0.2} [player]?"
    n 1flrss "¡Todo depende de cómo{w=0.5}{nw}"
    extend 1fsqbg " {i}enmarquen{/i}{w=0.5}{nw}"
    extend 1fchbs " la situación!"

    return

label joke_surround_sound:
    n 1csqflsbl "No digas que no te advertí,{w=0.2} [player]."
    n 1ccsfl "¿Cómo superan la soledad los técnicos de audio?"
    n 1csrca "..."
    n 1ccsem "Ugh."
    n 1cllem "Usan...{w=1}{nw}"
    extend 1cnmfl " sonido{w=0.5}{nw}"
    extend 1csqfl " {i}envolvente{/i}."

    return

label joke_rose_thorns:
    n 1ccsss "¡Mejor{w=0.5}{nw}"
    extend 1csgbg " {i}agudiza{/i}{w=0.5}{nw}"
    extend 1fnmbg " el oído para esto!"
    n 1fcsaj "¡'Kay!{w=0.75}{nw}"
    extend 1fcssm " Entonces."
    n 1tsqbg "¿Por qué el jardinero renunció a plantar rosas?"
    n 1fnmsm "..."
    n 1ccssmesm "Je."
    n 1clrbg "¡Porque resultaron ser una verdadera{w=0.5}{nw}"
    extend 1csqbg " {i}espina{/i}{w=0.75}{nw}"
    extend 1fchbs " en el costado!"

    return

label joke_acrobats_somersault:
    n 1ccssmesm "Je.{w=0.75}{nw}"
    extend 1fsqbg " ¡Adivina esto,{w=0.2} [player]!"
    n 1fcsbg "¿Qué tipo de movimiento practican más los acróbatas a mitad de año?"
    n 1fnmsm "..."
    n 1fcsbs "¡Duh!"
    n 1fsqbg "Practicarían{w=0.5}{nw}"
    extend 1fsgbg " saltos de{w=0.75}{nw}"
    extend 1fchbg " {i}verano{/i},{w=0.5}{nw}"
    extend 1fchgn " ¡por supuesto!"

    return

label joke_frog_seating:
    n 1cslem "¿A quién molestaron para tener que incluir {i}este{/i}?{w=0.75}{nw}"
    extend 1ccsem " Ugh."
    n 1clrsl "¿Qué tipo de asiento le das a una rana?"
    n 1csrsl "..."
    n 1ccsflesi "..."
    n 1cllfl "Un {i}sapo{/i}-{w=0.75}{nw}"
    extend 1fsqca " rete."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
