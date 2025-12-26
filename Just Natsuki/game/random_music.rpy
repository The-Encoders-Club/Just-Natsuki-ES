default persistent.jn_random_music_enabled = False

init python in jn_random_music:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_custom_music as jn_custom_music
    import store.jn_utils as jn_utils

    def getRandomMusicPlayable():
        """
        Returns whether random music is considered playable, ignoring if any custom music is defined.
        Note that at least two tracks must exist for random music to work properly.

        OUT:
            - True if random music should be playable, otherwise False.
        """
        return (
            store.persistent.jn_custom_music_unlocked
            and store.persistent.jn_random_music_enabled
            and store.Natsuki.isAffectionate(higher=True)
            and store.preferences.get_volume("music") > 0
            and not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY)
        )

label random_music_change:
    if not jn_random_music.getRandomMusicPlayable():
        return

    $ available_custom_music = jn_utils.getAllDirectoryFiles(
        path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
        extension_list=jn_utils.getSupportedMusicFileExtensions()
    )

    if len(available_custom_music) < 2:
        return

    $ track_quip = random.choice([
        "¡Está bien!{w=0.2} ¡Es hora de una melodía diferente!",
        "¡¡¡Está bien!!!{w=0.2} ¡Es hora de otra canción!",
        "Sí,{w=0.2} Creo que ya está bien con esta canción.",
        "'Bueno,{w=0.2}ya es suficiente.",
        "¡Es hora de una nueva canción!",
        "¡Ya es suficiente con ese número!",
        "Quiero escuchar algo más...",
        "¡Es hora de cambiar las cosas!"
    ])
    n 3nchbg "[track_quip]{w=2}{nw}"
    show natsuki 4nchsmeme

    $ jn_custom_music.presentMusicPlayer("playing")
    play audio button_tap_c
    show music_player stopped
    stop music fadeout 2
    $ jnPause(2)

    $ track_followup = random.choice([
        "Ahora,{w=0.2} vamos a ver...",
        "Ahora,{w=0.2} ¿Qué tenemos?",
        "Veamos aquí...",
        "¿Qué más tenemos?",
        "¡Ajá!{w=0.5} ¡Vamos a probar esto!",
        "Déjame ver..."
    ])
    n 2fcssm "[track_followup]{w=2}{nw}"
    show natsuki 4fcssm

    $ music_title = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))[0]

    play audio button_tap_c
    show music_player playing

    $ jnPause(2)
    $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=music_title, is_custom=True), channel="music", fadein=2)
    $ jn_custom_music._now_playing = music_title
    $ renpy.notify("Reproduciendo ahora: {0}".format(jn_custom_music._now_playing.split(".")[0]))
    $ track_complete = random.choice([
        "¡Hecho~!",
        "¡Todo listo!",
        "¡Todo está bien!",
        "¡Allá vamos!",
        "Y...{w=1} ¡estamos bien!",
        "¡Okie-dokie!{w=0.75} Jejeje."
    ])

    n 2uchbgeme "[track_complete]{w=2}{nw}"
    show natsuki 2fcssm

    $ jn_custom_music.hideMusicPlayer()
    $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.random

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_enable",
            unlocked=True,
            prompt="¿Puedes reproducir música personalizada aleatoria para mí?",
            conditional="persistent.jn_custom_music_unlocked and not persistent.jn_random_music_enabled",
            category=["Música"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_enable:
    n 1unmbg "¡Oh!{w=0.5}{nw}"
    extend 3fchbg " Sí,{w=0.1} ¡Puedo hacerlo!"
    n 3unmss "Lo cambiaré cada quince minutos aproximadamente, entonces,{w=0.1} ¿de acuerdo?"
    n 4uwdaj "¡Oh!{w=0.5}{nw}"
    extend 1fllbg " Casi lo olvido {w=0.1}-{w=0.1} déjame verificar si realmente hay música para reproducir primero."
    n 4ncsbo "..."

    if len(jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_utils.getSupportedMusicFileExtensions()
        )) >= 2:

        n 1uchgn "¡Está bien! {w=0.2} ¡Creo que tengo suficiente con qué trabajar aquí!{w=0.5}{nw}"
        extend 4nchsm " Jejeje."
        n 2nsqsm "No te preocupes,{w=0.1} [player].{w=0.5}{nw}"
        extend 2fcsbg " ¡Elegiré los buenos!"

        $ persistent.jn_random_music_enabled = True

    elif preferences.get_volume("music") == 0:

        n 1nsqem "Oh...{w=0.5} eh."
        n 2tsqca "¿Y cómo {i}exactamente{/i} planeas escucharlo con la música apagada?"
        n 2uchbg "Dios mío...{w=0.3} a veces eres un tonto,{w=0.1} [player].{w=0.5}{nw}"
        extend 4nchsm " Jejeje."
        n 3fwlsm "Vuelve a subirlo,{w=0.1} y luego hablaremo,.{w=0.2} ¿de acuerdo?"
    else:


        n 1tllaj "Mmm...{w=0.3} ¿[player]?{w=0.5}{nw}"
        extend 4tnmca " No me has dado exactamente mucho con qué trabajar aquí."
        n 2unmaj "¿Podrías darme al menos un par de pistas?{w=0.5}{nw}"
        extend 2tnmpo " ¿Recuerdas cómo hacer eso, w=0.1} verdad?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 3uchbg "Simplemente agrégalos a la carpeta de música personalizada,{w=0.1} [chosen_tease]!"

    $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.random

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_disable",
            unlocked=True,
            prompt="¿Puedes dejar de reproducir música personalizada aleatoria?",
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_random_music_enabled",
            category=["Música"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_disable:
    n 1unmaj "¿Eh?{w=0.2} Vaya.{w=0.5}{nw}"
    extend 2nsqsf " ¿Son mis elecciones musicales realmente tan malas,{w=0.1} [player]?"
    n 4fsrsm "...Jejeje."
    n 1uchbg "Sólo estoy jugando contigo.{w=0.2} ¡Por supuesto!{w=0.5}{nw}"
    extend 2nchsm " Simplemente lo pondré de nuevo en la música normal."

    $ jn_custom_music.presentMusicPlayer("playing")
    play audio button_tap_c
    show music_player stopped
    stop music fadeout 2
    $ jnPause(2)

    play audio button_tap_c
    show music_player playing
    $ renpy.play(
        filename=jn_custom_music.getMusicFileRelativePath(
            file_name=main_background.location.getCurrentTheme(),
            is_custom=False),
        channel="music",
        fadein=2)
    $ jnPause(2)

    n 2nwlbg "...Y allá vamos!"

    $ jn_custom_music.hideMusicPlayer()
    $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.location
    $ persistent.jn_random_music_enabled = False

    return

#⚠: —Pass