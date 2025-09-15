default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

image music_player off = "mod_assets/props/music_player/music_player_off.png"
image music_player playing = "mod_assets/props/music_player/music_player_play.png"
image music_player stopped = "mod_assets/props/music_player/music_player_stop.png"
image music_player paused = "mod_assets/props/music_player/music_player_pause.png"

init python in jn_custom_music:
    from Enum import Enum
    import os
    import store
    import store.jn_events as jn_events
    import store.jn_utils as jn_utils  


    try:
        import mutagen
        import mutagen.mp3 as muta3
        import mutagen.oggopus as mutaopus
        import mutagen.oggvorbis as mutaogg
        MUTAGEN_AVAILABLE = True
    except ImportError:
        MUTAGEN_AVAILABLE = False
        renpy.log("JN Custom Music: Mutagen library not found. Advanced metadata features will be disabled.")


    _MT_TITLE = "title"
    _MT_ARTIST = "artist"
    _MT_MAS_LOOPSTART = "masloopstart"
    _MT_MAS_LOOPEND = "masloopend"
    _MT_RPG_LOOPSTART = "loopstart"
    _MT_RPG_LOOPLENGTH = "looplength"

    _RPY_LOOP_TAG_START = "<"
    _RPY_LOOP_TAG_FROM = "loop"
    _RPY_LOOP_TAG_TO = "to"
    _RPY_LOOP_TAG_END = ">"

    _VALID_EXTENSIONS_FOR_METADATA = ['.mp3', '.ogg', '.opus'] 

    class JNMusicOptionTypes(Enum):
        """
        Identifiers for different music option responses.
        """
        bgm = 1
        custom = 2
        random = 3
        no_music = 4
        location = 5

    class JNCustomMusicSelectionOption:
        """
        Represents a custom music option from the custom music menu.
        """
        def __init__(
            self,
            display_prompt,
            option_type,
            file_name 
        ):
            self.display_prompt = display_prompt
            self.option_type = option_type
            self.file_name = file_name

    CUSTOM_MUSIC_FOLDER = "game/custom_music/"
    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, CUSTOM_MUSIC_FOLDER).replace("\\", "/")

    _NATSUKI_PICK_MUSIC_DONE_QUIPS = [
        _("¡Hecho~!"),
        _("¡Todo listo!"),
        _("¡Todo bien!"),
        _("¡Ahí vamos!"),
        _("Y...{w=0.3} ¡todo en orden"),
        _("¡Oki doki!{w=0.2} Jeje."),
        _("Y... ¡listo!")

    ]

    _now_playing = None
    _last_music_option = None

    def _clean_gui_text(unclean_text):
        """Cleans text for GUI display by removing problematic Ren'Py formatting characters."""
        if not unclean_text:
            return ""
        bad_chars = ("{", "}", "[", "]")
        cleaned = unclean_text
        for char in bad_chars:
            cleaned = cleaned.replace(char, "")
        return cleaned

    def _get_audio_file_object(filepath_abs):
        """Attempts to retrieve the mutagen audio object based on file extension."""
        if not MUTAGEN_AVAILABLE:
            return None, None
        
        _, ext_lower = os.path.splitext(filepath_abs)
        ext_lower = ext_lower.lower()
        
        try:
            if ext_lower == ".mp3":
                return muta3.EasyMP3(filepath_abs), ext_lower
            elif ext_lower == ".ogg":
                return mutaogg.OggVorbis(filepath_abs), ext_lower
            elif ext_lower == ".opus":
                return mutaopus.OggOpus(filepath_abs), ext_lower
        except Exception as e:
            renpy.log("JN Custom Music: Error al cargar metadatos para {0}: {1}".format(filepath_abs, e))
            pass 
        return None, None

    def _get_display_name_from_metadata(audio_obj, ext_lower, default_name_part):
        """Attempts to retrieve song name from metadata tags."""
        if not audio_obj or not hasattr(audio_obj, 'tags') or audio_obj.tags is None:
            return default_name_part
        
        title = None
        artist = None
        
        if ext_lower == ".mp3":
            title_tags = audio_obj.tags.get(_MT_TITLE.lower(), [])
            artist_tags = audio_obj.tags.get(_MT_ARTIST.lower(), [])
        else:
            title_tags = audio_obj.tags.get(_MT_TITLE.upper(), [])
            if not title_tags: title_tags = audio_obj.tags.get(_MT_TITLE, []) 
            
            artist_tags = audio_obj.tags.get(_MT_ARTIST.upper(), [])
            if not artist_tags: artist_tags = audio_obj.tags.get(_MT_ARTIST, [])
        
        if title_tags:
            title = title_tags[0]
        if artist_tags:
            artist = artist_tags[0]
        
        if title and artist:
            return u"{0} - {1}".format(artist, title)
        elif title:
            return title
        return default_name_part

    def _get_loop_string_from_metadata(audio_obj, ext_lower):
        """Attempts to retrieve loop data from tags and generates Ren'Py loop string."""
        if not audio_obj or not hasattr(audio_obj, 'tags') or audio_obj.tags is None:
            return ""
        
        loop_start_sample = None
        loop_length_sample = None
        loop_start_sec = None
        loop_end_sec = None
        
        mas_ls_tags = audio_obj.tags.get(_MT_MAS_LOOPSTART.upper(), audio_obj.tags.get(_MT_MAS_LOOPSTART, []))
        mas_le_tags = audio_obj.tags.get(_MT_MAS_LOOPEND.upper(), audio_obj.tags.get(_MT_MAS_LOOPEND, []))
        
        if mas_ls_tags:
            try: loop_start_sec = float(mas_ls_tags[0])
            except ValueError: pass
        if mas_le_tags:
            try: loop_end_sec = float(mas_le_tags[0])
            except ValueError: pass
        
        if (loop_start_sec is None or loop_start_sec < 0) and ext_lower == ".ogg":
            rpg_ls_tags = audio_obj.tags.get(_MT_RPG_LOOPSTART.upper(), audio_obj.tags.get(_MT_RPG_LOOPSTART, []))
            rpg_ll_tags = audio_obj.tags.get(_MT_RPG_LOOPLENGTH.upper(), audio_obj.tags.get(_MT_RPG_LOOPLENGTH, []))
            if rpg_ls_tags:
                try: loop_start_sample = int(rpg_ls_tags[0])
                except ValueError: pass
            if rpg_ll_tags:
                try: loop_length_sample = int(rpg_ll_tags[0])
                except ValueError: pass
            
            if loop_start_sample is not None and hasattr(audio_obj, 'info') and audio_obj.info.sample_rate > 0:
                sample_rate = float(audio_obj.info.sample_rate)
                loop_start_sec = loop_start_sample / sample_rate
                if loop_length_sample is not None and loop_length_sample > 0:
                    loop_end_sec = loop_start_sec + (loop_length_sample / sample_rate)
                else:
                    loop_end_sec = None
            else:
                loop_start_sec = None
                loop_end_sec = None
        
        
        if loop_start_sec is not None and loop_start_sec >= 0:
            if hasattr(audio_obj, 'info') and loop_start_sec >= audio_obj.info.length:
                return ""
            
            tag_parts = [_RPY_LOOP_TAG_START, _RPY_LOOP_TAG_FROM, str(loop_start_sec)]
            if loop_end_sec is not None and loop_end_sec > loop_start_sec:
                if hasattr(audio_obj, 'info') and loop_end_sec > audio_obj.info.length:
                    pass
                else:
                    tag_parts.extend([_RPY_LOOP_TAG_TO, str(loop_end_sec)])
            tag_parts.append(_RPY_LOOP_TAG_END)
            return "".join(tag_parts)
        
        return ""

    def _scan_custom_music_files_with_metadata():
        """Scans the custom music folder, extracts metadata, and returns a list of JNCustomMusicSelectionOption."""
        scanned_tracks = []
        
        
        
        gamedir_scan_prefix = CUSTOM_MUSIC_FOLDER
        if gamedir_scan_prefix.startswith("game/"):
            gamedir_scan_prefix = gamedir_scan_prefix[len("game/"):] 
        else:
            gamedir_scan_prefix = CUSTOM_MUSIC_FOLDER.replace("\\", "/").split("/")[-2] + "/"
            if not gamedir_scan_prefix: gamedir_scan_prefix = CUSTOM_MUSIC_FOLDER
        
        all_game_files = renpy.list_files()
        
        
        supported_scan_extensions = []
        if hasattr(store, 'jn_utils') and hasattr(store.jn_utils, 'getSupportedMusicFileExtensions'):
            supported_scan_extensions = [ext.lower() for ext in store.jn_utils.getSupportedMusicFileExtensions()]
        elif 'jn_utils' in globals() and hasattr(jn_utils, 'getSupportedMusicFileExtensions'):
            supported_scan_extensions = [ext.lower() for ext in jn_utils.getSupportedMusicFileExtensions()]
        if not supported_scan_extensions:
            supported_scan_extensions = _VALID_EXTENSIONS_FOR_METADATA
        supported_scan_extensions = ['.mp3', '.ogg', '.opus']
        print("DEBUG - Extensiones permitidas:", supported_scan_extensions)
        
        for path_relative_to_gamedir in all_game_files:
            if path_relative_to_gamedir.startswith(gamedir_scan_prefix):
                filename_in_folder = path_relative_to_gamedir[len(gamedir_scan_prefix):]
                base_filename_part, file_ext_lower = os.path.splitext(filename_in_folder)
                file_ext_lower = file_ext_lower.lower()
                if file_ext_lower in supported_scan_extensions:
                    print("DEBUG - Agregando opción custom:", base_filename_part, path_relative_to_gamedir)
                    scanned_tracks.append(
                        JNCustomMusicSelectionOption(
                            display_prompt=base_filename_part,
                            option_type=JNMusicOptionTypes.custom,
                            file_name=filename_in_folder
                        )
                    )
        
        scanned_tracks.sort(key=lambda opt: opt.display_prompt.lower())
        return scanned_tracks

    def presentMusicPlayer(state="stopped"):
        renpy.show(
            name="music_player {0}".format(state),
            at_list=[store.JN_TRANSFORM_FADE_IN],
            zorder=store.JN_PROP_ZORDER
        )
        store.jnPause(0.5)
        renpy.play(filename=store.audio.gift_close, channel="audio")
        store.jnPause(0.5)

    def hideMusicPlayer():
        renpy.show(
            name="music_player",
            at_list=[store.JN_TRANSFORM_FADE_OUT],
            zorder=store.JN_PROP_ZORDER
        )
        store.jnPause(0.5)
        renpy.hide("music_player")
        renpy.play(filename=store.audio.gift_close, channel="audio")
        store.jnPause(0.5)

    def getMusicFileRelativePath(file_name, is_custom):
        if is_custom:
            gamedir_custom_folder = CUSTOM_MUSIC_FOLDER
            if gamedir_custom_folder.startswith("game/"):
                gamedir_custom_folder = gamedir_custom_folder[len("game/"):]
            return "{0}{1}".format(gamedir_custom_folder, file_name)
        else:
            return "mod_assets/bgm/{0}".format(file_name)


    if store.persistent.jn_custom_music_unlocked:
        jn_utils.createDirectoryIfNotExists(CUSTOM_MUSIC_DIRECTORY)

label music_menu:
    $ Natsuki.setInConversation(True)
    $ music_title = _("Pista no identificada")

    python:
        success = False
        final_music_options = []


        scanned_custom_tracks = jn_custom_music._scan_custom_music_files_with_metadata()


        if len(scanned_custom_tracks) > 1:
            final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt=_("You pick!"), 
                option_type=jn_custom_music.JNMusicOptionTypes.random,
                file_name=None
            ))

        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt="Strawberry daydream",
            option_type=jn_custom_music.JNMusicOptionTypes.bgm,
            file_name="mod_assets/bgm/strawberry_daydream.ogg"
        ))
        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt="Stars that shimmer",
            option_type=jn_custom_music.JNMusicOptionTypes.bgm,
            file_name="mod_assets/bgm/stars_that_shimmer.ogg"
        ))
        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt="Just Natsuki",
            option_type=jn_custom_music.JNMusicOptionTypes.bgm,
            file_name="mod_assets/bgm/just_natsuki.ogg"
        ))

        if persistent._jn_event_completed_count > 0 and Natsuki.isNormal(higher=True):
            final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
                display_prompt="Vacation!",
                option_type=jn_custom_music.JNMusicOptionTypes.bgm,
                file_name="mod_assets/bgm/vacation.ogg"
            ))
        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt="Space classroom",
            option_type=jn_custom_music.JNMusicOptionTypes.bgm,
            file_name="mod_assets/bgm/space_classroom.ogg"
        ))

        final_music_options.extend(scanned_custom_tracks)
        print("DEBUG - Opciones finales:", [o.display_prompt for o in final_music_options])

        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt=_("Default"),
            option_type=jn_custom_music.JNMusicOptionTypes.location,
            file_name=None 
        ))
        final_music_options.append(jn_custom_music.JNCustomMusicSelectionOption(
            display_prompt=_("No music"),
            option_type=jn_custom_music.JNMusicOptionTypes.no_music,
            file_name=None
        ))

        custom_music_options = final_music_options 
        success = True

    if not success:
        show natsuki at jn_center

        n 4kllsssbr "Uhmm..."
        n 4klrflsbr "Hey...{w=0.75}{nw}"
        extend 4knmajsbr " [player]?"
        n 4kslslsbr "Something {i}kinda{/i} went wrong when I was trying look for your music...{w=1}{nw}"
        extend 4kslsssbr " can you just check everything out real quick?"
        n 2tlraj "As a reminder -{w=0.5}{nw}"
        extend 2tnmsl " anything you want me to play needs to be in the {i}custom_music{/i} folder."
        n 2fcsbgsbl "Just make sure it's all in {i}.mp3,{w=0.1} .ogg or .wav{/i} format!"

        $ Natsuki.resetLastTopicCall()
        $ Natsuki.resetLastIdleCall()
        jump ch30_loop

    elif preferences.get_volume("music") == 0:
        show natsuki at jn_center
        n 1tsqaj "Uh...{w=1}{nw}"
        extend 1tslaj " huh."
        n 2tsgsg "And {i}how{/i} exactly do you plan to hear any music with the volume at zero?"
        n 2fchbg "Jeez,{w=0.2} [player].{w=0.75}{nw}"
        extend 1uchgn " How do you even get dressed in the morning with memory like that?!"
        n 3ullss "Well,{w=0.2} whatever.{w=0.75}{nw}"
        extend 3unmaj " So..."

        show natsuki option_wait_curious

        menu:
            n "Did you want me to turn the music back up so you can pick something?"
            "Yes.":
                n 1nchsm "Okey-{w=0.1}dokey!{w=0.2} Just a second..."
                $ preferences.set_volume("music", 0.75)
                n 2fcsbg "And there we are!"
                n 2ullss "So...{w=0.5}{nw}"
                extend 2unmaj " what did you wanna listen to?"

                show natsuki option_wait_excited at jn_left
            "No.":

                n 3fcsbg "The sound of silence it is,{w=0.1} then!{w=0.5}{nw}"
                extend 3fchsm " Ehehe."

                $ Natsuki.resetLastTopicCall()
                $ Natsuki.resetLastIdleCall()
                jump ch30_loop
    else:

        $ chosen_quip = renpy.substitute(random.choice([
            "¿Quieres que ponga otra cosa? {w=0.2} ¡Sin problema!",
            "Será mejor que pongas algo bueno, {w=0.2} [player]!",
            "¿Quieres escuchar algo?{w=0.2} ¡segura!",
            "¿Música diferente?{w=0.2} {i}¡AHORA{/i} sí que estamos hablando!",
            "¿Otra canción?{w=0.2} ¡Claro!",
            "¿Quieres escuchar a algo más?{w=0.2} ¡Entendido!",
            "¿Eh?{w=0.2} ¿Qué tienes en mente,{w=0.2} [player]?"
        ]))
        n 3unmbgl "[chosen_quip]"
        show natsuki option_wait_excited at jn_left


    call screen custom_music_menu(custom_music_options)
    show natsuki at jn_center

    if not _return:
        $ Natsuki.resetLastTopicCall()
        $ Natsuki.resetLastIdleCall()
        jump ch30_loop

    if _return.option_type == jn_custom_music.JNMusicOptionTypes.no_music:
        $ music_quip = renpy.substitute(random.choice([
            "Solo en silencio por ahora,{w=0.2} ¿no?",
            "¿No estás de humor,{w=0.2} [player]?{w=0.2} ¡No hay problema!",
            "¡Está bien!{w=0.2} Voy a apagar eso...",
            "¡De acuerdo!{w=0.2} Déjame apagar eso enseguida...",
            "¡Claro que sí!{w=0.2} Déjame quitarlo...",
            "¡No hay problema!{w=0.2} Sólo dame un segundo...",
        ]))
        n 2knmsm "[music_quip]"

        show natsuki 2fchsm
        $ music_title = "No music"

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        n 2uchsm "There you go, [player]!{w=2}{nw}"

        if persistent.jn_random_music_enabled:

            $ persistent.jn_random_music_enabled = False
            n 1unmaj "Oh{w=0.2} -{w=0.50}{nw}"
            extend 3kchbgsbl " and I'll stop switching around the music too.{w=2}{nw}"

        $ jn_custom_music.hideMusicPlayer()

    elif _return.option_type == jn_custom_music.JNMusicOptionTypes.random:

        $ available_custom_music = jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_utils.getSupportedMusicFileExtensions()
        )


        $ chosen_question_quip = renpy.substitute(random.choice([
            "Oh?{w=0.2} ¿Quieres que elija?",
            "¿Eh?{w=0.2} ¿Quieres que elija algo?",
            "¿Hmm?{w=0.2} ¿Quieres que yo elija?",
            "¿Oh?{w=0.2} ¿Quieres que elija algo para escuchar?",
            "¿Eh?{w=0.2} ¿Es mi turno de elegir?"
        ]))
        n 1unmajl "[chosen_question_quip]"

        $ chosen_answer_quip = renpy.substitute(random.choice([
            "¡Seguro!",
            "Claro,{w=0.2} ¡por qué no!",
            "¡Por supuesto!",
            "Jeje.{w=0.2} ¡Déjamelo a mí,{w=0.2} [player]!",
            "Ehehe.{w=0.2} About time too,{w=0.2} [player]!",
            "Okie-dokie,{w=0.2} [player]!",
            "¡Por fin!{w=0.2} ¡Jaja!",
            "¡{i}Ahora{/i} sí estamos hablando!"
        ]))
        n 4uchbgl "[chosen_answer_quip]"
        show natsuki 1fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        $ chosen_search_quip = renpy.substitute(random.choice([
            "Ahora,{w=0.2} veamos...",
            "Déjame echar un vistazo...",
            "¡Muy bien,{w=0.2} a ver qué tenemos...!",
            "¡Oh!{w=0.2} ¿Qué te parece esto?",
            "Veamos..",
            "Vamos a ver..."
        ]))
        n 2ullbgl "[chosen_search_quip]{w=2}{nw}"
        show natsuki 4fcspul


        if len(available_custom_music) > 1:
            $ music_title = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))[0]
            play audio button_tap_c
            show music_player playing
            $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=music_title, is_custom=True), channel="music", fadein=2)
            $ jnPause(2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 1uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 1fcssm

        $ jn_custom_music.hideMusicPlayer()
        $ jn_custom_music._now_playing = music_title
        $ renpy.notify("Estás escuchando: {0}".format(jn_custom_music._now_playing.split(".")[0]))

    elif _return.option_type == jn_custom_music.JNMusicOptionTypes.location:
        $ music_quip = renpy.substitute(random.choice([
            "Lo que funcione, supongo,{w=0.2} ¿eh?",
            "¡Por supuesto!",
            "Bueno, {w=0.2} eres el jefe!",
            "Solo lo habitual, {w=0.2} ¿eh? {w=0.2} ¡Claro!",
            "¡No hay problema!{w=0.2} Sólo dame un segundo...",
        ]))
        n 2knmsm "[music_quip]"

        show natsuki 2fchsm

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

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 2uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 2fcssm

        $ jn_custom_music.hideMusicPlayer()

    elif _return is not None:
        n 2fwlbg "You got it!{w=2}{nw}"
        show natsuki 4fchsmleme

        $ jn_custom_music.presentMusicPlayer("playing")
        play audio button_tap_c
        show music_player stopped
        stop music fadeout 2
        $ jnPause(2)

        play audio button_tap_c
        show music_player playing
        $ renpy.play(
            filename=jn_custom_music.getMusicFileRelativePath(
                file_name=_return.file_name,
                is_custom=_return.option_type == jn_custom_music.JNMusicOptionTypes.custom),
            channel="music",
            fadein=2)

        $ chosen_done_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_DONE_QUIPS))
        n 2uchbgeme "[chosen_done_quip]{w=2}{nw}"
        show natsuki 2fcssm

        $ jn_custom_music.hideMusicPlayer()
        $ jn_custom_music._now_playing = _return.display_prompt
        $ renpy.notify("Estas escuchando: {0}".format(_return.display_prompt))

    $ jn_custom_music._last_music_option = _return.display_prompt
    $ Natsuki.resetLastTopicCall()
    $ Natsuki.resetLastIdleCall()

    jump ch30_loop

screen custom_music_menu(items):
    $ option_width = 400
    if persistent._jn_display_option_icons:
        add "mod_assets/icons/custom_music.png" anchor (0, 0) pos (1280 - (275 + option_width), 20)

    elif not persistent._jn_display_option_icons:
        $ option_width += 175

    fixed:
        area (1280 - (40 + option_width), 40, option_width, 440)
        vbox:
            ypos 0
            yanchor 0

            textbutton "":
                style "categorized_menu_button"
                xsize option_width
                action Return(False)
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound

            null height 20

            viewport:
                id "viewport"
                yfill False
                mousewheel True

                has vbox
                for _value in items:
                    textbutton _value.display_prompt:
                        style "categorized_menu_button"
                        xsize option_width
                        action Return(_value)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound


                        if _value.option_type == jn_custom_music.JNMusicOptionTypes.bgm:
                            idle_background Frame("mod_assets/buttons/choice_hover_blank_note.png", gui.frame_hover_borders, tile=gui.frame_tile)

                        elif _value.option_type == jn_custom_music.JNMusicOptionTypes.custom:
                            idle_background Frame("mod_assets/buttons/choice_hover_blank_folder.png", gui.frame_hover_borders, tile=gui.frame_tile)

                    null height 5

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
