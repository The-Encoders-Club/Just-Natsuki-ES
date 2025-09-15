# by just6889 \|/ President of Traduction Club!
# https://traduction-club.live/

default persistent.language = None

init -999 python:
    def set_language_fonts():
        if persistent.language == "spanish":
            gui.default_font = "mod_assets/fonts/FuzzyBubbles-Regular.ttf"
            gui.text_font = gui.default_font
            gui.name_font = gui.default_font
            gui.interface_font = gui.default_font
        else:
            gui.default_font = "mod_assets/fonts/natsuki.ttf"
            gui.text_font = gui.default_font
            gui.name_font = gui.default_font
            gui.interface_font = gui.default_font

    if persistent.language == "spanish":
        config.language = "spanish"
    elif persistent.language == "english" or persistent.language is None: # Handle None as English
        config.language = None # Ren'Py uses None for the default language (English)
    # else: config.language will remain Ren'Py's default if persistent.language has an unexpected value

    set_language_fonts() # Apply the fonts based on the persistent setting

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label _("Please select a language"):
                style "confirm_prompt"
                xalign 0.5

            vbox:
                style_prefix "radio"
                label _("Language")

                textbutton "English" text_font "DejaVuSans.ttf" action [
                    Language(None),
                    SetField(persistent, "language", "english"),
                    Function(set_language_fonts),
                    SetScreenVariable("chosen_lang", "english"),
                    Show("dialog", message="It is recommended to restart to apply the changes.", ok_action=Quit())
                ]
                textbutton "Español" text_font "mod_assets/fonts/FuzzyBubbles-Regular.ttf" action [
                    Language("spanish"),
                    SetField(persistent, "language", "spanish"),
                    Function(set_language_fonts),
                    SetScreenVariable("chosen_lang", "spanish"),
                    Show("dialog", message="Se recomienda reiniciar el juego\npara aplicar los cambios.", ok_action=Quit())
                ]

style ok_button_custom is button:
    background None
    foreground None
    hover_background None
    hover_foreground None
    insensitive_background None
    insensitive_foreground None

label choose_language:
    call screen choose_language
    return

init python:
    # maybe this wont work
    def set_language_fonts():
        if persistent.language == "spanish":
            gui.default_font = "mod_assets/fonts/FuzzyBubbles-Regular.ttf"
            gui.text_font = gui.default_font
            gui.name_font = gui.default_font
            gui.interface_font = gui.default_font
        else:
            gui.default_font = "mod_assets/fonts/natsuki.ttf"
            gui.text_font = gui.default_font
            gui.name_font = gui.default_font
            gui.interface_font = gui.default_font

label android_menu:
    menu:
        "Gifts":
            jump giftmenu
        "Affect":
            jump affectionmenu
        "Beta Android":
            python:
                request_custom_music_folder()
            jump ch30_loop
        # "Changelog":
        #     jump changelog
        # "Just's Notes (porter)":
        #     jump notas
        # "beta_test":
        #     jump beta_test
        "Nevermind":
            jump ch30_loop

label giftmenu:


    menu:
        "Write a Gift":
            call screen give_custom_gift_screen
        "Predefined Gifts":
            call giftmenu_predefined
        "Return":
            jump ch30_loop
    jump ch30_loop

label affectionmenu:
    n "Your affinity with Nat is [persistent.affinity] points."
    jump ch30_loop

screen give_custom_gift_screen():
    tag menu

    frame:
        style_prefix "gift_"
        xalign 0.5
        yalign 0.5

        vbox:
            text "Enter the name of the gift for Nat (include the '.nats' extension):"
            input value VariableInputValue("gift_input") length 30
            textbutton "Give Gift" action [Function(give_custom_gift, gift_input), Return()]
            textbutton "Close" action Jump("ch30_loop")

default gift_input = ""
init python:
    def give_custom_gift(gift_name):
        """
        to give custom gifts
        """
        if gift_name.endswith(".nats") or gift_name.endswith(".txt"):
            filepath = os.path.join(renpy.config.basedir, 'characters', gift_name)
            with open(filepath, "a") as f:
                pass

label giftmenu_predefined:
    python:
        predefined_gifts = [
            # (Nombre visible, archivo)
            ("Ribbon (Bisexual Pride Themed)", "bisexualpridethemedribbon.gift"),
        ]
        predefined_gifts.append(("Return", None))

    call screen scrollable_choice_menu(predefined_gifts)

    if _return is not None and _return != "Return":
        jump ch30_loop
    else:
        jump giftmenu

init python:
    import os

    # no funciono mi idea
    def request_folder_permission():
        """
        Solicita al usuario acceso a una carpeta usando SAF.
        """
        try:
            from jnius import autoclass, cast
            Intent = autoclass('android.content.Intent')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity

            intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE)
            intent.addCategory(Intent.CATEGORY_DEFAULT)
            activity.startActivityForResult(intent, 42)
            renpy.notify("Selecciona la carpeta para custom_music.")
        except Exception as e:
            renpy.notify("No se pudo solicitar el permiso: {}".format(e))

    def open_file_from_uri(uri_str, filename):
        """
        Abre un archivo dentro de una carpeta SAF usando su URI y nombre de archivo.
        """
        try:
            from jnius import autoclass, cast

            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            Uri = autoclass('android.net.Uri')
            DocumentFile = autoclass('androidx.documentfile.provider.DocumentFile')

            # Convertir el string URI a objeto Uri
            tree_uri = Uri.parse(uri_str)
            # Obtener DocumentFile de la carpeta
            picked_dir = DocumentFile.fromTreeUri(activity, tree_uri)

            # Buscar el archivo por nombre
            target_file = None
            files = picked_dir.listFiles()
            for f in files:
                if f.getName() == filename:
                    target_file = f
                    break

            if not target_file:
                renpy.notify("Archivo no encontrado en la carpeta seleccionada.")
                return None

            # Abrir InputStream para leer el archivo
            input_stream = activity.getContentResolver().openInputStream(target_file.getUri())
            import java.io
            reader = java.io.BufferedReader(java.io.InputStreamReader(input_stream))
            content = ""
            line = reader.readLine()
            while line:
                content += line + "\n"
                line = reader.readLine()
            reader.close()
            input_stream.close()
            return content

        except Exception as e:
            renpy.notify("Error al abrir archivo SAF: {}".format(e))
            return None

    def choose_custom_music_folder():
        from plyer import filechooser
        def on_selection(selection):
            if selection:
                persistent.custom_music_uri = selection[0]
                renpy.notify("Carpeta seleccionada y guardada.")
            else:
                renpy.notify("No se seleccionó carpeta.")
        filechooser.choose_dir(on_selection=on_selection)
    
    def request_custom_music_folder():
        try:
            from jnius import autoclass
            from android import activity

            Intent = autoclass('android.content.Intent')

            def on_activity_result(requestCode, resultCode, data):
                if requestCode == 42 and resultCode == -1:
                    uri = data.getData()
                    if uri:
                        uri_str = str(uri.toString())
                        persistent.custom_music_uri = uri_str
                        renpy.notify("Carpeta seleccionada y guardada.")
                    else:
                        renpy.notify("No se seleccionó carpeta.")
                activity.unbind(on_activity_result=on_activity_result)

            activity.bind(on_activity_result=on_activity_result)

            intent = Intent(Intent.ACTION_OPEN_DOCUMENT_TREE)
            intent.addCategory(Intent.CATEGORY_DEFAULT)
            activity.startActivityForResult(intent, 42)
            renpy.notify("Selecciona la carpeta para custom_music.")

        except Exception as e:
            renpy.notify("No se pudo solicitar el permiso: {}".format(e))