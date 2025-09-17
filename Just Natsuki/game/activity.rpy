default persistent._jn_activity_used_programs = []

init python in jn_activity:
    from Enum import Enum
    from plyer import notification
    import sys
    import random
    import re
    import store
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    ACTIVITY_SYSTEM_ENABLED = False
    LAST_ACTIVITY = None



    if renpy.windows:
        try:
            from plyer import notification
            import pygetwindow
            import win32gui
            ACTIVITY_SYSTEM_ENABLED = True
        except ImportError as e:
            ACTIVITY_SYSTEM_ENABLED = False
            store.jn_utils.log("Sistema de actividad inhabilitado: " + str(e))

    elif renpy.linux:
        try:
            from plyer import notification
            import Xlib
            import Xlib.display
            ACTIVITY_SYSTEM_ENABLED = True
        except ImportError as e:
            ACTIVITY_SYSTEM_ENABLED = False
            store.jn_utils.log("Sistema de actividad inhabilitado: " + str(e))

    elif renpy.macintosh:
        ACTIVITY_SYSTEM_ENABLED = False

    class JNWindowFoundException(Exception):
        """
        Custom exception; used to break out of the win32gui.EnumWindows method while still returning a value,
        as only that and returning False are valid means of termination.
        """
        def __init__(self, hwnd):
            self.hwnd = hwnd
        
        def __str__(self):
            return self.hwnd

    class JNActivities(Enum):
        unknown = 0
        coding = 1
        discord = 2
        music_applications = 3
        gaming  = 4
        youtube = 5
        github_jn = 6
        artwork = 7
        anime_streaming = 8
        work_applications = 9
        twitter = 10
        deviantart = 11
        manga = 12
        ddlc_moe = 13
        takeaway_food = 14
        instagram = 15
        music_creation = 16
        reddit = 17
        fourchan = 18
        monika_after_story = 19
        just_yuri = 20
        forever_and_ever = 21
        video_applications = 22
        e_commerce = 23
        recording_software = 24
        
        def __int__(self):
            return self.value

    class JNPlayerActivity:
        """
        This class represents some activity a player can be doing, outside of JN, to be used in notifications/dialogue.
        """
        def __init__(
            self,
            activity_type,
            window_name_regex=None,
            notify_text=None
        ):
            """
            Initialises a new instance of JNPlayerActivity.

            IN:
                - activity_type - The JNActivities type of this JNPlayerActivity
                - window_name_regex - The window regex that must be matched for this activity to be the current activity
                - notify_text - List of text Natsuki may react with via popup, if this activity is detected
            """
            self.activity_type = activity_type
            self.window_name_regex = window_name_regex
            self.notify_text = notify_text
        
        def getRandomNotifyText(self):
            """
            Returns the substituted reaction text for this activity.
            """
            if self.notify_text and len(self.notify_text) > 0:
                store.happy_emote = jn_utils.getRandomHappyEmoticon()
                store.angry_emote = jn_utils.getRandomAngryEmoticon()
                store.sad_emote = jn_utils.getRandomSadEmoticon()
                store.tease_emote = jn_utils.getRandomTeaseEmoticon()
                store.confused_emote = jn_utils.getRandomConfusedEmoticon()
                return renpy.substitute(random.choice(self.notify_text))
            
            return None

    class JNActivityManager:
        """
        Management class for handling activities.
        """
        def __init__(self):
            self.registered_activities = {}
            self.last_activity = JNPlayerActivity(
                activity_type=JNActivities.unknown
            )
            self._m1_activity__enabled = False
        
        def setIsEnabled(self, state):
            """
            Sets the enabled state, determining if activity detection is active.

            IN:
                - state - bool enabled state to set
            """
            self._m1_activity__enabled = state
        
        def getIsEnabled():
            """
            Gets the enabled state.
            """
            return self._m1_activity__enabled
        
        def registerActivity(self, activity):
            self.registered_activities[activity.activity_type] = activity
        
        def getActivityFromType(self, activity_type):
            """
            Returns the activity corresponding to the given JNActivities activity type, or None if it doesn't exist
            """
            if activity_type in self.registered_activities:
                return self.registered_activities[activity_type]
            
            return None
        
        def getCurrentActivity(self, delay=0):
            """
            Returns the current JNActivities state of the player as determined by the currently active window,
            and if the activity is registered.

            IN:
                - delay - Force RenPy to sleep before running the check. This allows time to swap windows from JN for debugging.
            OUT:
                - JNPlayerActivity type for the active window, or None
            """
            if delay is not 0:
                store.jnPause(delay, hard=True)
            
            if not self._m1_activity__enabled:
                return self.getActivityFromType(JNActivities.unknown)
            
            window_name = getCurrentWindowName()
            if window_name is not None:
                window_name = getCurrentWindowName().lower()
                for activity in self.registered_activities.values():
                    if activity.window_name_regex:
                        if re.search(activity.window_name_regex, window_name) is not None:
                            
                            if not self.hasPlayerDoneActivity(int(activity.activity_type)):
                                store.persistent._jn_activity_used_programs.append(int(activity.activity_type))
                            
                            return activity
            
            return self.getActivityFromType(JNActivities.unknown)
        
        def hasPlayerDoneActivity(self, activity_type):
            """
            Returns True if the player has previously partook in the given activity.

            IN:
                - activity - The JNActivities activity to check
            """
            return int(activity_type) in store.persistent._jn_activity_used_programs

    ACTIVITY_MANAGER = JNActivityManager()

    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.unknown
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.coding,
        window_name_regex="(- visual studio|- notepad/+/+|- atom|- brackets|vim|eclipse|^github desktop$|^sourcetree$|- scratch)",
        notify_text=[
            "Eres realmente un nerd. [player].",
            "¡Se te olvidó el punto y coma! [tease_emote]",
            "¡¿Cómo puedes leer todo eso?!",
            "¿Y bien? ¿Funciona? [tease_emote]",
            "¿Qué es este revoltijo?",
            "Ni siquiera sé por dónde empezar con la codificación...",
            "¿Más cosas de programación?",
            "Ya veo, ya veo. ¡Hoy te toca ser nerd! [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.discord,
        window_name_regex="(discord)",
        notify_text=[
            "Alguien es una mariposa social, ¿eh?",
            "Sí, sí. Charla un rato. [player]~",
            "Hombre... Ojalá tuviera algunos emoticones... [sad_emote]",
            "Quizás debería iniciar un servidor...",
            "¿Eh? ¿Alguien te envió un mensaje?",
            "¿Eh? ¿Alguien te hizo un ping? [confused_emote]",
            "¡No te pases todo el día hablando ahí! [angry_emote]",
            "No soy tan aburrida para hablar, ¿verdad? [sad_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.music_applications,
        window_name_regex="(^spotify$|^spotify premium$|^groove$|^zune$|^itunes$|^musicbee$|^aimp$|^winamp$)",
        notify_text=[
            "¡Será mejor que escuches algo bueno!",
            "¿Nueva playlist, [player]?",
            "¡Escuchando algunas canciones, [player]!",
            "Heeey, ¿cuándo podré elegir algo? [angry_emote]",
            "¡Dale play [tease_emote]!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.gaming,
        window_name_regex="(^steam$|^origin$|^battle.net$|- itch.io)",
        notify_text=[
            "¡Será mejor que no pases todo el día haciendo eso! [angry_emote]",
            "Sólo recuerda tomar descansos, ¿de acuerdo? [sad_emote]",
            "¿Vas a jugar algo?",
            "Podrías haber dicho si estabas aburrido... [sad_emote]",
            "Será mejor que no juegues nada raro...",
            "Es hora de jugar, ¿eh?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.youtube,
        window_name_regex="(youtube)",
        notify_text=[
            "YouTube, ¿eh? Creo que Sayori subió algo alguna vez...",
            "¡Oh! ¡Oh! ¡Déjame ver! [happy_emote]",
            "Qué veremos [player]?",
            "Será mejor que no estés viendo nada raro...",
            "Simplemente... nada de videos de reacciones. Por favor. [angry_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.github_jn,
        window_name_regex="(just-natsuki-team/natsukimoddev)",
        notify_text=[
            "¡Oye! ¡Conozco este lugar!",
            "¡Sabía que me ayudarías! Jejeje.",
            "¡Oh! ¡Oh! ¡Es mi sitio web!",
            "Escuché que aquí sólo vienen nerds... [tease_emote]",
            "Jejeje. ¡Gracias por pasar!",
            "¡Hola! ¡Soy el centro geek! [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.artwork,
        window_name_regex="(clip studio paint|photoshop|krita|gimp|paint.net|paint tool sai|medibang|- paint)",
        notify_text=[
            "¡Dibuja para mí, [player]! Jejeje.",
            "Nunca fui bueno en el arte... [sad_emote]",
            "¿Estas dibujando? [confused_emote]",
            "¡Oh! ¡Oh! ¿Qué estás dibujando?",
            "¿Eh? ¿Qué estás dibujando? [confused_emote]",
            "¡Dibújame! ¡Dibújame!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.anime_streaming,
        window_name_regex="(^crunchyroll$)",
        notify_text=[
            "¿Cuál es el mejor de la temporada?",
            "Tantas opciones...",
            "Todavía no veo Parfait Girls en ningún lado...",
            "¡Infinitas opciones! Jejeje.",
            "Podría perder DÍAS aquí... [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.work_applications,
        window_name_regex="(- word| - excel| - powerpoint|openoffice|libreoffice)",
        notify_text=[
            "¡Qué asco!... trabajo...",
            "Estas seguro de que tienes que hacer esto ahora [player]? [confused_emote]",
            "Ugh... me recuerda a mis tareas escolares...",
            "Genial... ahora estoy teniendo flashbacks de mis proyectos grupales.",
            "¡A-bu-rri-do! Jejeje.",
            "Me recuerda a los trabajos escolares... [angry_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.twitter,
        window_name_regex="(/ twitter)",
        notify_text=[
            "¡Hay tanto arte genial aquí!",
            "Juro que podría perder horas simplemente navegando por aquí...",
            "¡Oh! ¡Oh! ¿Estoy en tendencia?",
            "Probablemente debería revisar mi Twitter, ¿no?",
            "¡Ay, tío! ¡Tengo que revisar mi feed! [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.deviantart,
        window_name_regex="(deviantart - |\| deviantart)",
        notify_text=[
            "Mucho. Arte.",
            "¡Oh! ¿Publicas aquí, [player]?",
            "Simplemente... no busques nada raro...",
            "Yo... conozco este lugar.",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.manga,
        window_name_regex="(- mangadex|- mangasee|- mangakot)",
        notify_text=[
            "¿Cuál es el mejor de la temporada?",
            "No está Parfait Girls aquí... [sad_emote]",
            "¡Oh! ¿Qué estás leyendo? [happy_emote]",
            "¿Buscas la opinión de una EXPERTA? ¡Jaja!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.ddlc_moe,
        window_name_regex="(doki doki literature club! -)",
        notify_text=[
            "...",
            "No me gusta este sitio web.",
            "Uuuuuu... ¿TIENES que visitar este lugar?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.takeaway_food,
        window_name_regex=(
            "((uber eats[a-zA-Z]*| food delivery)|( - uber eats)|(deliveroo - takeaway food delivery)"
            "|(\| domino's pizza)|(\| pizza hut)|(\| grubhub)|(doordash food delivery & takeout -))"
        ),
        notify_text=[
            "¡O-oye! ¡Menos comida chatarra! [angry_emote]",
            "¿Sabes? cocinar no es TAAAN difícil. [angry_emote]",
            "Será mejor que no hagas de eso un hábito...",
            "¡[player]! ¡Piensa en tu billetera! ¡Dios mío! [confused_emote]",
            "[player]... ¿otra vez? [sad_emote]",
            "Simplemente... no hagas de esto un hábito. [angry_emote] ¿Por favor?",
            "¡Qué asco!... comida chatarra...",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.instagram,
        window_name_regex="(• instagram photos and videos)",
        notify_text=[
            "Entonces, ¿a quién estás stalkeando hoy, eh? [tease_emote]",
            "¿Eh? ¿Publicas aquí, [player]?",
            "¿Publicas mucho aquí, [player]?",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.music_creation,
        window_name_regex="(cubase|fl studio|reaper|mixcraft|studio one|logic pro|garageband|cakewalk|pro tools)",
        notify_text=[
            "¡Ooooh! ¿Estás haciendo ritmos?",
            "¿Estás haciendo música? [confused_emote]",
            "¿Debería empezar a tomar NOTAS? Jejeje.",
            "¡Oh! ¡Oh! ¡Tengo que escuchar esto!",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.reddit,
        window_name_regex="(reddit - dive into anything)",
        notify_text=[
            "Espero que no creas todo lo que lees...",
            "¿Eh? ¿Qué hay en las noticias?",
            "¿Hm? ¿Me perdí de algo?",
            "¿Estás haciendo una publicación, [player]? [confused_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.fourchan,
        window_name_regex="(- 4chan|^4chan$)"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.monika_after_story,
        window_name_regex="^monika after story$"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.just_yuri,
        window_name_regex="(^just yuri$|^just yuri \(beta\)$)"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.forever_and_ever,
        window_name_regex="^forever & ever$"
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.video_applications,
        window_name_regex="(- vlc media player)",
        notify_text=[
            "¿Qué estás viendo, [player]? [confused_emote]",
            "¿Estás viendo algo, [player]? [confused_emote]",
            "¡Hola! ¿Hay algún video gracioso? [tease_emote]",
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.e_commerce,
        window_name_regex="(^amazon.[A-Za-z]{2,6}|\| ebay)",
        notify_text=[
            "Simplemente... no te excedas. [angry_emote]",
            "De compras, ¿eh? [tease_emote]",
            "¿Se te acabó algo otra vez? Jejeje.",
            "¿Ah, sí? ¿Tienes que conseguir algo? [confused_emote]",
            "Dinero para quemar, ¿eh?"
        ]
    ))
    ACTIVITY_MANAGER.registerActivity(JNPlayerActivity(
        activity_type=JNActivities.recording_software,
        window_name_regex="(^obs [0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}|^bandicam [0-9]{4}|^fraps|^xsplit broadcaster$|- lightstream studio$)",
        notify_text=[
            "E-espera ... ¿qué tipo de aplicación es esa, [player]? [confused_emote]",
            "Espera un segundo... ¿eso es algún tipo de grabadora?",
            "E-espero que no me estés grabando, [player]. [angry_emote]",
            "¿Eh? ¿Qué clase de programa es ese, [player]? [confused_emote]",
            "¿Qué estás grabando, [player]...? [confused_emote]"
        ]
    ))

    def _getJNWindowHwnd():
        """
        Gets the hwnd of the JN game window (Windows only).

        OUT:
            - int representing the hwnd of the JN game window
        """
        def checkJNWindow(hwnd, ctx):
            """
            Returns JNWindowFoundException containing the hwnd of the JN game window.
            """
            if win32gui.GetWindowText(hwnd) == store.config.window_title:
                raise JNWindowFoundException(hwnd)
        
        try:
            
            win32gui.EnumWindows(checkJNWindow, None)
        
        except JNWindowFoundException as exception:
            return exception.hwnd

    def getJNWindowActive():
        """
        Returns True if the currently active window is the JN game window, otherwise False.
        """
        return getCurrentWindowName() == store.config.window_title

    def getCurrentWindowName(delay=0):
        """
        Gets the title of the currently active window.

        IN: 
            - delay - int amount of seconds to wait before checking window

        OUT:
            - str representing the title of the currently active window
        """
        global ACTIVITY_SYSTEM_ENABLED
        if ACTIVITY_SYSTEM_ENABLED:
            if delay is not 0:
                store.jnPause(delay, hard=True)
            
            try:
                if renpy.windows and pygetwindow.getActiveWindow():
                    return pygetwindow.getActiveWindow().title
                
                elif renpy.linux:
                    
                    focus = Xlib.display.Display().get_input_focus().focus
                    
                    if not isinstance(focus, int):
                        
                        wm_name = focus.get_wm_name()
                        wm_class = focus.get_wm_class()
                        
                        if isinstance(wm_name, basestring) and wm_name != "":
                            
                            return wm_name
                        
                        elif wm_class is None and (wm_name is None or wm_name == ""):
                            
                            focus = focus.query_tree().parent
                            
                            if not isinstance(focus, int):
                                
                                wm_name = focus.get_wm_name()
                                return wm_name if isinstance(wm_name, basestring) else ""
                        
                        elif isinstance(wm_class, tuple):
                            
                            return str(wm_class[0])
            
            
            
            except AttributeError as exception:
                ACTIVITY_SYSTEM_ENABLED = False
                jn_utils.log("Failed to identify activity: {0}; only x11 sessions are supported. Disabling activity system for session.".format(repr(exception)))
                return ""
            
            except Exception as exception:
                ACTIVITY_SYSTEM_ENABLED = False
                jn_utils.log("Failed to identify activity: {0}. Disabling activity system for session.".format(repr(exception)))
                return ""
        
        return ""

    def taskbarFlash(flash_count=2, flash_frequency_milliseconds=750):
        """
        Flashes the JN icon on the taskbar (Windows only).
        By default, the icon will flash twice with a healthy delay between each flash, before remaining lit.

        IN:
            - flash_count - The amount of times to flash the icon before the icon remains in a lit state
            - flash_frequency_milliseconds - The amount of time to wait between each flash, in milliseconds
        """
        pass





    def notifyPopup(message):
        """
        Displays a toast-style popup (Windows and Linux only).

        IN:
            - title - The title to display on the window
            - message - The message to display in the window
        """
        if renpy.windows or renpy.linux:
            notification.notify(
                title="Natsuki",
                message=message,
                app_name=store.config.window_title,
                app_icon=(renpy.config.gamedir + '/mod_assets/jnlogo.ico'),
                timeout=7
            )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
