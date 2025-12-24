default persistent._jn_version = "0.0.1"
default persistent._jn_gs_aff = persistent.affinity
default persistent._jn_pic_aff = 0
default persistent._jn_pic = False

python early in jn_data_migrations:
    from enum import Enum
    import re
    import requests
    import os
    import store
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils







    UPDATE_FUNCS = dict()


    LATE_UPDATES = []



    VER_STR_PARSER = re.compile(r"^(?P<ver>\d+\.\d+\.\d+)(?P<suffix>.*)$")

    migrated_in_session = False
    current_version_latest = False

    class MigrationRuntimes(Enum):
        """
        Enum for the times to run migration scripts.
        """
        INIT = 1
        RUNTIME = 2

    def migration(from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Decorator function to register a data migration function

        IN:
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)

        OUT:
            the wrapper function
        """
        def wrap(_function):
            registerUpdateFunction(
                _callable=_function,
                from_versions=from_versions,
                to_version=to_version,
                runtime=runtime
            )
            return _function
        return wrap

    def registerUpdateFunction(_callable, from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Register a function to be called when the program is updated.

        IN:
            _callable: the function to run (Must take no arguments)
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)
        """
        for from_version in from_versions:
            if from_version not in UPDATE_FUNCS:
                UPDATE_FUNCS[from_version] = dict()
            
            UPDATE_FUNCS[from_version][runtime] = (_callable, to_version)

    def verStrToVerList(ver_str):
        """
        Converts a version string to a list of integers representing the version.
        """
        match = VER_STR_PARSER.match(ver_str)
        if not match:
            raise ValueError("Cadena de versión no válida.")
        
        ver_list = match.group("ver").split(".")
        return [int(x) for x in ver_list]

    def compareVersions(ver_str1, ver_str2):
        """
        Compares two version strings.
        """
        match1 = VER_STR_PARSER.match(ver_str1)
        match2 = VER_STR_PARSER.match(ver_str2)
        
        if not match1 or not match2:
            raise ValueError("Cadena de versión no válida.")
        
        ver1 = verStrToVerList(match1.group("ver"))
        ver2 = verStrToVerList(match2.group("ver"))
        
        
        if len(ver1) > len(ver2):
            ver2 += [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))
        
        
        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
        
        
        return 0

    def checkCurrentVersionIsLatest(notify_if_current=False):
        """
        Checks the latest release and compares the version number against the persisted version number.
        If an update is available, notify the user.
        
        For best results, run threaded as to not block execution.

        IN:
            - notify_if_current: Bool flag on if to notify if Just Natsuki is already up to date. False by default.
        """
        try:
            response = requests.get(jn_globals.LINK_JN_LATEST, verify=os.environ['SSL_CERT_FILE'])
            if response.status_code != 200:
                jn_utils.log("Fallo al buscar actualizaciones: la respuesta de versiones de GitHub fue: {0}".format(response.status_code))
                return False
            
            global current_version_latest
            current_version_latest = compareVersions(store.persistent._jn_version, response.url.split("/")[-1].replace("v", "")) in [0, 1]
            
            if not current_version_latest:
                renpy.notify("¡Hay una actualización disponible para Just Natsuki! Ve a: https://github.com/Just-Natsuki-Team/NatsukiModDev/releases")
            
            elif notify_if_current:
                renpy.notify("¡Just Natsuki ya está actualizado!")
        
        except Exception as exception:
            jn_utils.log("Fallo al buscar actualizaciones: {0}".format(exception))
            return False

    def checkCurrentVersionIsLatestFromMenu():
        """
        Checks the latest release of the mod and notifies regardless of the outcome.
        Hack to bypass Ren'Py's poor menuing code not allowing for nested functions with parameters.
        """
        checkCurrentVersionIsLatest(notify_if_current=True)

    def runInitMigrations():
        """
        Runs init time migration functions. Must be run after init 0
        """
        jn_utils.log("runInitMigrations INICIO")
        
        if store.persistent._jn_version not in UPDATE_FUNCS:
            return
        
        
        from_version = store.persistent._jn_version
        
        
        
        while compareVersions(from_version, renpy.config.version) < 0:
            
            if MigrationRuntimes.RUNTIME in UPDATE_FUNCS[store.persistent._jn_version]:
                LATE_UPDATES.append(UPDATE_FUNCS[store.persistent._jn_version][MigrationRuntimes.RUNTIME])
            
            
            _callable, from_version = UPDATE_FUNCS[from_version][MigrationRuntimes.INIT]
            
            
            _callable()

    def runRuntimeMigrations():
        """
        Runs the runtime migration functions.
        """
        jn_utils.log("runRuntimeMigrations INICIO")
        for _callable in LATE_UPDATES:
            _callable()


init 10 python:
    jn_utils.log("Versión persistente actual pre-verificación de migración: {0}".format(store.persistent._jn_version))
    jn_data_migrations.runInitMigrations()


init python in jn_data_migrations:
    import os
    import shutil
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_desk_items as jn_desk_items
    import store.jn_events as jn_events
    import store.jn_outfits as jn_outfits
    import store.jn_poems as jn_poems
    import store.jn_utils as jn_utils

    @migration(["0.0.0", "0.0.1", "0.0.2"], "1.0.0", runtime=MigrationRuntimes.INIT)
    def to_1_0_0():
        jn_utils.log("Migración a 1.0.0 INICIO")
        
        if (
            store.persistent.jn_player_nicknames_allowed is not None
            and not store.persistent.jn_player_nicknames_allowed
        ):
            store.persistent._jn_nicknames_natsuki_allowed = False
            del store.persistent.jn_player_nicknames_allowed
            jn_utils.log("Migrado: persistent.jn_player_nicknames_allowed")
        
        
        if (
            store.persistent.jn_player_nicknames_current_nickname is not None
            and store.persistent.jn_player_nicknames_current_nickname != "Natsuki"
            and store.persistent._jn_nicknames_natsuki_allowed
        ):
            store.persistent._jn_nicknames_natsuki_current_nickname = store.persistent.jn_player_nicknames_current_nickname
            store.n_name = store.persistent._jn_nicknames_natsuki_current_nickname
            del store.persistent.jn_player_nicknames_current_nickname
            jn_utils.log("Migrado: persistent.jn_player_nicknames_current_nickname")
        
        if (
            store.persistent.jn_player_nicknames_bad_given_total is not None
            and store.persistent.jn_player_nicknames_bad_given_total > 0
        ):
            store.persistent._jn_nicknames_natsuki_bad_given_total = store.persistent.jn_player_nicknames_bad_given_total
            del store.persistent.jn_player_nicknames_bad_given_total
            jn_utils.log("Migrado: persistent.jn_player_nicknames_bad_given_total")
        
        
        if store.Natsuki.isLove(higher=True) and store.persistent.jn_player_love_you_count == 0:
            store.persistent.affinity = jn_affinity.AFF_THRESHOLD_LOVE -1
        
        
        store.persistent._apology_database = dict()
        
        store.persistent._topic_database["talk_i_love_you"]["conditional"] = None
        store.get_topic("talk_i_love_you").conditional = None
        
        store.persistent._topic_database["talk_mod_contributions"]["conditional"] = "not jn_activity.ACTIVITY_SYSTEM_ENABLED or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
        store.get_topic("talk_mod_contributions").conditional = "not jn_activity.ACTIVITY_SYSTEM_ENABLED or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
        
        jn_utils.log("Migrado: store.persistent._apology_database")
        jn_utils.log("""Migrado: store.persistent._topic_database["talk_i_love_you"]["conditional"]""")
        jn_utils.log("""Migrado: store.persistent._topic_database["talk_mod_contributions"]["conditional"]""")
        
        
        if (
            store.persistent.jn_activity_used_programs is not None
            and len(store.persistent.jn_activity_used_programs) > len(store.persistent._jn_activity_used_programs)
        ):
            store.persistent._jn_activity_used_programs = store.persistent.jn_activity_used_programs
            del store.persistent.jn_activity_used_programs
            jn_utils.log("Migrado: persistent.jn_activity_used_programs")
        
        if store.persistent.jn_notify_conversations is not None:
            store.persistent._jn_notify_conversations = store.persistent.jn_notify_conversations
            del store.persistent.jn_notify_conversations
            jn_utils.log("Migrado: persistent.jn_player_nicknames_bad_given_total")
        
        store.persistent._jn_version = "1.0.0"
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.0.0 HECHO")
        return

    @migration(["1.0.0"], "1.0.1", runtime=MigrationRuntimes.INIT)
    def to_1_0_1():
        jn_utils.log("Migración a 1.0.1 INICIO")
        
        
        jn_outfits.getOutfit("jn_nyatsuki_outfit").unlock()
        jn_outfits.getWearable("jn_clothes_qeeb_sweater").unlock()
        jn_outfits.getWearable("jn_clothes_qt_sweater").unlock()
        
        store.persistent._jn_version = "1.0.1"
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.0.1 HECHO")
        return

    @migration(["1.0.1"], "1.0.2", runtime=MigrationRuntimes.INIT)
    def to_1_0_2():
        jn_utils.log("Migración a 1.0.2 INICIO")
        store.persistent._jn_version = "1.0.2"
        jn_utils.log("Migración a 1.0.2 HECHO")
        return

    @migration(["1.0.2"], "1.0.3", runtime=MigrationRuntimes.INIT)
    def to_1_0_3():
        jn_utils.log("Migración a 1.0.3 INICIO")
        store.persistent._jn_version = "1.0.3"
        
        if jn_outfits.getOutfit("jn_skater_outfit").unlocked:
            jn_outfits.getWearable("jn_facewear_plasters").unlock()
        
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.0.3 HECHO")
        return

    @migration(["1.0.3", "1.0.4"], "1.1.0", runtime=MigrationRuntimes.INIT)
    def to_1_1_0():
        jn_utils.log("Migración a 1.1.0 INICIO")
        store.persistent._jn_version = "1.1.0"
        
        store.persistent._event_database["event_not_ready_yet"]["conditional"] = (
            "((jn_is_time_block_early_morning() or jn_is_time_block_mid_morning()) and jn_is_weekday())"
            " or (jn_is_time_block_late_morning and not jn_is_weekday())"
        )
        store.get_topic("event_not_ready_yet").conditional = (
            "((jn_is_time_block_early_morning() or jn_is_time_block_mid_morning()) and jn_is_weekday())"
            " or (jn_is_time_block_late_morning and not jn_is_weekday())"
        )
        jn_utils.log("""Migrado: store.persistent._event_database["event_not_ready_yet"]["conditional"]""")
        
        if "holiday_player_birthday" in store.persistent._seen_ever:
            jn_poems.getPoem("jn_birthday_cakes_candles").unlock()
            jn_utils.log("Migrado: jn_birthday_cakes_candles estado de desbloqueo")
        
        if "holiday_christmas_day" in store.persistent._seen_ever:
            if store.Natsuki.isEnamored(higher=True):
                jn_poems.getPoem("jn_christmas_evergreen").unlock()
                jn_utils.log("Migrado: jn_christmas_evergreen estado de desbloqueo")
            
            elif store.Natsuki.isHappy(higher=True):
                jn_poems.getPoem("jn_christmas_gingerbread_house").unlock()
                jn_utils.log("Migrado: jn_christmas_gingerbread_house estado de desbloqueo")
        
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.1.0 HECHO")
        return

    @migration(["1.1.0"], "1.1.1", runtime=MigrationRuntimes.INIT)
    def to_1_1_1():
        jn_utils.log("Migración a 1.1.1 INICIO")
        store.persistent._jn_version = "1.1.1"
        jn_utils.log("Migración a 1.1.1 HECHO")
        return

    @migration(["1.1.1", "1.1.2"], "1.2.0", runtime=MigrationRuntimes.INIT)
    def to_1_2_0():
        jn_utils.log("Migración a 1.2.0 INICIO")
        store.persistent._jn_version = "1.2.0"
        
        if store.persistent._jn_player_birthday_day_month is not None:
            store.persistent._jn_natsuki_birthday_known = True
        
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.2.0 HECHO")
        return

    @migration(["1.2.0"], "1.2.1", runtime=MigrationRuntimes.INIT)
    def to_1_2_1():
        jn_utils.log("Migración a 1.2.1 INICIO")
        store.persistent._jn_version = "1.2.1"
        jn_utils.log("Migración a 1.2.1 HECHO")
        return

    @migration(["1.2.1"], "1.2.2", runtime=MigrationRuntimes.INIT)
    def to_1_2_2():
        jn_utils.log("Migración a 1.2.2 INICIO")
        store.persistent._jn_version = "1.2.2"
        jn_utils.log("Migración a 1.2.2 HECHO")
        return

    @migration(["1.2.2"], "1.2.3", runtime=MigrationRuntimes.INIT)
    def to_1_2_3():
        jn_utils.log("Migración a 1.2.3 INICIO")
        store.persistent._jn_version = "1.2.3"
        jn_utils.log("Migración a 1.2.3 HECHO")
        return

    @migration(["1.2.3"], "1.2.4", runtime=MigrationRuntimes.INIT)
    def to_1_2_4():
        jn_utils.log("Migración a 1.2.4 INICIO")
        store.persistent._jn_version = "1.2.4"
        
        if "holiday_christmas_day" in store.persistent._seen_ever:
            jn_outfits.getOutfit("jn_christmas_outfit").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_christmas_outfit")
        
        if "talk_are_you_into_cosplay" in store.persistent._seen_ever and store.Natsuki.isAffectionate(higher=True):
            jn_outfits.getOutfit("jn_trainer_cosplay").unlock()
            jn_outfits.getOutfit("jn_sango_cosplay").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendos: jn_trainer_cosplay, jn_sango_cosplay")
        
        if "talk_skateboarding" in store.persistent._seen_ever and store.Natsuki.isAffectionate(higher=True):
            jn_outfits.getOutfit("jn_skater_outfit").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_skater_outfit")
        
        if "event_warm_package" in store.persistent._seen_ever:
            jn_outfits.getOutfit("jn_cosy_cardigan_outfit").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_cosy_cardigan_outfit")
        
        if "talk_fitting_clothing" in store.persistent._seen_ever:
            jn_outfits.getOutfit("jn_pastel_goth_getup").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_pastel_goth_getup")
        
        if "holiday_valentines_day" in store.persistent._seen_ever:
            jn_outfits.getOutfit("jn_ruffle_neck_sweater_outfit").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_ruffle_neck_sweater_outfit")
            
            if store.Natsuki.isLove(higher=True):
                jn_outfits.getOutfit("jn_heart_sweater_outfit").unlock()
                jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_heart_sweater_outfit")
        
        if "talk_chocolate_preference" in store.persistent._seen_ever and store.Natsuki.isAffectionate(higher=True):
            jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendo: jn_chocolate_plaid_collection")
        
        if "holiday_easter" in store.persistent._seen_ever:
            jn_outfits.getOutfit("jn_chick_outfit").unlock()
            jn_outfits.getOutfit("jn_cherry_blossom_outfit").unlock()
            jn_utils.log("Estado de desbloqueo corregido para atuendos: jn_chick_outfit, jn_cherry_blossom_outfit")
        
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.2.4 HECHO")
        return

    @migration(["1.2.4"], "1.3.0", runtime=MigrationRuntimes.INIT)
    def to_1_3_0():
        jn_utils.log("Migración a 1.3.0 INICIO")
        store.persistent._jn_version = "1.3.0"
        
        
        if store.persistent.jn_player_pet is not None:
            store.persistent._jn_player_pet = store.persistent.jn_player_pet
            del store.persistent.jn_player_pet
            jn_utils.log("Migrado: persistent.jn_player_pet")
        
        if store.persistent.jn_player_admission_type_on_quit is not None:
            store.persistent._jn_player_admission_type_on_quit = store.persistent.jn_player_admission_type_on_quit
            del store.persistent.jn_player_admission_type_on_quit
            jn_utils.log("Migrado: persistent.jn_player_admission_type_on_quit")
        
        if jn_outfits.getOutfit("jn_chocolate_plaid_collection").unlocked:
            jn_outfits.getWearable("jn_necklace_tight_golden_necklace").unlock()
            jn_utils.log("Estado de desbloqueo corregido para disponible: jn_necklace_tight_golden_necklace")
        
        if store.get_topic("event_caught_reading_manga").shown_count > 0:
            jn_desk_items.getDeskItem("jn_parfait_manga_held").unlock()
            jn_utils.log("Estado de desbloqueo corregido para objeto de escritorio: jn_parfait_manga_held")
        
        if store.persistent.jn_sunrise_hour is not None:
            del store.persistent.jn_sunrise_hour
            jn_utils.log("Eliminado: persistent.jn_sunrise_hour")
        
        if store.persistent.jn_sunset_hour is not None:
            del store.persistent.jn_sunset_hour
            jn_utils.log("Eliminado: persistent.jn_sunset_hour")
        
        jn_utils.saveGame()
        jn_utils.log("Migración a 1.3.0 HECHO")
        return

    @migration(["1.3.0", "1.3.1", "1.3.2", "1.3.3", "1.3.4"], "1.3.5", runtime=MigrationRuntimes.INIT)
    def to_1_3_5():
        jn_utils.log("Migración a 1.3.5 INICIO")
        
        if renpy.linux or renpy.macintosh:
            
            if jn_utils.deleteDirectory(os.path.join(renpy.config.basedir, "game/mod_assets/natsuki/clothes/jn_clothes_QT_sweater")):
                jn_utils.log("Eliminados activos no utilizados: clothes/jn_clothes_QT_sweater")
            
            if jn_utils.deleteDirectory(os.path.join(renpy.config.basedir, "game/mod_assets/natsuki/sleeves/jn_clothes_QT_sweater")):
                jn_utils.log("Eliminados activos no utilizados: sleeves/jn_clothes_QT_sweater")
        
        
        if jn_utils.deleteFileFromDirectory(os.path.join(renpy.config.basedir, "game/threading.rpy")):
            jn_utils.log("Eliminado archivo fuente no utilizado: game/threading.rpy")
        
        if jn_utils.deleteFileFromDirectory(os.path.join(renpy.config.basedir, "game/threading.rpyc")):
            jn_utils.log("Eliminado archivo compilado no utilizado: game/threading.rpyc")
        
        if store.persistent.jn_total_visit_count > 0 and store.Natsuki.isNormal(higher=True):
            
            store.persistent._jn_player_allow_legacy_music_switch_event = True
        
        
        for holiday in jn_events.getAllHolidays():
            holiday.shown_count = 1 if holiday.label in store.persistent._seen_ever else 0
            jn_utils.log("Establecido conteo de mostrado para {0} a {1}".format(holiday.label, holiday.shown_count))
        
        if store.persistent.affinity >= 12500 and jn_utils.get_total_gameplay_months() < 6:
            store.persistent._jn_pic_aff = store.persistent.affinity
            store.persistent._jn_snpsht_aff = store.persistent.affinity
            store.persistent.affinity = 0
            store.persistent._jn_pic = True
            jn_utils.log("434346".decode("hex"))
        
        jn_utils.saveGame()
        store.persistent._jn_version = "1.3.5"
        jn_utils.log("Migración a 1.3.5 HECHO")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
