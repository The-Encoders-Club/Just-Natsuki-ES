













define config.version = "1.3.5"
define config.name = "Just Natsuki"
define config.window_title = _("Just Natsuki - {0}".format(config.version))




define gui.show_name = False




define gui.about = _("")






define build.name = "JustNatsuki"


define build.executable_name = "DDLC"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75















define config.save_directory = "JustNatsuki"







define config.window_icon = "mod_assets/jnlogo.png"



define config.developer = False
define config.console = False
define config.allow_skipping = False
define config.skipping = False
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.include_update = True




    build.classify("game/mod_assets/**", "all")


    build.classify("game/*.rpyc", "all")


    build.classify("game/python-packages/**", "all")


    build.classify("README.html", "all")
    build.classify("README.md", "all")



    build.documentation('**.html')
    build.documentation('COPYRIGHT.txt')
    build.documentation('README.txt')
    build.documentation('**.md')




    build.classify("game/*.rpy", None)
    build.classify("game/dev/**", None)
    build.classify("game/saves/**", None)
    build.classify("game/cache/**", None)


    build.classify("log/**", None)
    build.classify("*.log", None)
    build.classify("errors.txt", None)
    build.classify("log.txt", None)


    build.classify("screenshots/**", None)
    build.classify("renpy/**", None)
    build.classify("characters/**", None)
    build.classify("custom_outfits/**", None)
    build.classify("custom_wearables/**", None)
    build.classify("custom_music/**", None)
    build.classify("**.exe", None)
    build.classify("DDLC.py", None)
    build.classify("DDLC.sh", None)

    build.include_old_themes = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
