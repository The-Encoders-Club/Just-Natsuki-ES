label ch30_autoload:

    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        config.skipping = False
        config.allow_skipping = False
        config.keymap['skip'] = []
        config.keymap['toggle_skip'] = []
        config.keymap['fast_skip'] = []
        config.predict_statements = 5
        config.image_cache_size = 128
        n.display_args["callback"] = jnNoDismissDialogue
        n.what_args["slow_abortable"] = False





label ch30_visual_setup:

    show black zorder JN_BLACK_ZORDER


    $ main_background.show()


    $ jn_atmosphere.updateSky()



label ch30_init:
    python:
        import codecs
        import random  




        jn_data_migrations.runRuntimeMigrations()


        persistent._jn_version = config.version
        jn_utils.log("Current persisted version post-mig check: {0}".format(store.persistent._jn_version))

        if store.persistent._jn_pic:
            renpy.jump("greeting_pic")

        if (
            jn_utils.getAllDirectoryFiles(path=renpy.config.gamedir, extension_list=["rpy"]) 
            and persistent._jn_scw
        ):
            renpy.show_screen("warn", "596f75206172652072756e6e696e6720736f7572636520282e727079292066696c65732120556e6c65737320796f75206b6e6f77207768617420796f752061726520646f696e672c20706c656173652073776974636820746f2072656c656173652066696c65732e".decode("hex"))




        if Natsuki.isEnamored(higher=True) and persistent._jn_nicknames_natsuki_allowed and persistent._jn_nicknames_natsuki_current_nickname:
            n_name = persistent._jn_nicknames_natsuki_current_nickname

        if Natsuki.isEnamored(higher=True) and persistent._jn_nicknames_player_allowed and persistent._jn_nicknames_player_current_nickname:
            player = persistent._jn_nicknames_player_current_nickname


        Natsuki.checkResetDailies()
        Natsuki.setInConversation(True)
        persistent.jn_total_visit_count += 1



        tt_in_session = False
        if ((persistent.jn_last_visited_date - datetime.datetime.now()).total_seconds() / 3600) >= 30:
            jn_utils.log("545421".decode("hex"))
            persistent._jn_player_tt_state += 1
            tt_in_session = True

        elif ((persistent.jn_last_visited_date - datetime.datetime.now()).total_seconds() / 3600) >= 10:
            persistent._jn_player_tt_instances += 1
            
            if persistent._jn_player_tt_instances == 3 or persistent._jn_player_tt_instances == 6:
                jn_utils.log("545421".decode("hex"))
                tt_in_session = True
                persistent._jn_player_tt_state += 1


        elif (
            not persistent._jn_player_extended_leave_response
            and (datetime.datetime.now() - persistent.jn_last_visited_date).total_seconds() / 604800 >= 2
        ):
            Natsuki.setQuitApology(jn_apologies.ApologyTypes.prolonged_leave)


        elif not Natsuki.getQuitApology() and datetime.date.today().day != persistent.jn_last_visited_date.day:
            Natsuki.calculatedAffinityGain()


        if (
            len(persistent._jn_holiday_deco_list_on_quit) > 0 
            and datetime.date.today().day == persistent.jn_last_visited_date.day
            and not tt_in_session
        ):
            for deco in persistent._jn_holiday_deco_list_on_quit:
                renpy.show(name="deco {0}".format(deco), zorder=store.JN_DECO_ZORDER)

        else:
            persistent._jn_holiday_deco_list_on_quit = []


        if (datetime.datetime.now().year > persistent.jn_last_visited_date.year):
            jn_events.resetHolidays()
            jn_utils.log("Holiday completion states reset.")

        persistent.jn_last_visited_date = datetime.datetime.now()




        if Natsuki.isHappy(higher=True) and persistent.jn_custom_outfits_unlocked:
            jn_outfits.loadCustomWearables()
            jn_outfits.loadCustomOutfits()

        jn_outfits.JNWearable.loadAll()
        jn_outfits.JNOutfit.loadAll()
        jn_utils.log("Outfit data loaded.")


        if persistent.jn_natsuki_auto_outfit_change_enabled or persistent.jn_natsuki_outfit_on_quit == "jn_temporary_outfit":
            
            Natsuki.setOutfit(jn_outfits.getRealtimeOutfit())

        elif jn_outfits.outfitExists(persistent.jn_natsuki_outfit_on_quit):
            
            Natsuki.setOutfit(jn_outfits.getOutfit(persistent.jn_natsuki_outfit_on_quit))

        else:
            
            Natsuki.setOutfit(jn_outfits.getOutfit("jn_school_uniform"))

        jn_utils.log("Outfit set.")



        jn_desk_items.JNDeskItem.loadAll()
        jn_utils.log("Desk item data loaded.")




        jn_poems.JNPoem.loadAll()
        jn_utils.log("Poem data loaded.")


        jn_events.JNHoliday.loadAll()
        jn_utils.log("Holiday data loaded.")

        jn_jokes.JNJoke.loadAll()
        jn_utils.log("Joke data loaded.")




        if tt_in_session:
            if persistent._jn_player_tt_state == 1:
                push("greeting_tt_warning")
                renpy.jump("call_next_topic")
            
            elif persistent._jn_player_tt_state == 2:
                renpy.jump("greeting_tt_fatal")
            
            else:
                renpy.jump("greeting_tt_game_over")

        elif persistent._jn_player_tt_state >= 2:
            renpy.jump("greeting_tt_game_over")


        jn_utils.fireAndForgetFunction(jn_data_migrations.checkCurrentVersionIsLatest)


        available_holidays = jn_events.selectHolidays()
        if available_holidays:
            renpy.hide("deco")
            jn_events.queueHolidays(available_holidays)


        elif not jn_topic_in_event_list_pattern("^greeting_"):
            if (
                (random.randint(1, 10) == 1 or persistent._jn_event_attempt_count == 20)
                and (not persistent._jn_player_admission_type_on_quit and not Natsuki.getQuitApology())
                and jn_events.selectEvent()
            ):
                persistent._jn_event_attempt_count = 0
                push(jn_events.selectEvent())
                renpy.call("call_next_topic", False)
            
            elif persistent._jn_player_allow_legacy_music_switch_event and get_topic("event_change_of_atmosphere").shown_count == 0:
                
                push("event_change_of_atmosphere")
                renpy.call("call_next_topic", False)
            
            else:
                persistent._jn_event_attempt_count += 1
                greeting_topic = jn_greetings.selectGreeting()
                push(greeting_topic.label)
                
                
                if "prop" in greeting_topic.additional_properties:
                    renpy.show(name="prop {0}".format(greeting_topic.additional_properties["prop"]), zorder=JN_PROP_ZORDER)
                
                
                if "overlay" in greeting_topic.additional_properties:
                    renpy.show(name="overlay {0}".format(greeting_topic.additional_properties["overlay"]), zorder=JN_OVERLAY_ZORDER)
                
                
                if "desk_item" in greeting_topic.additional_properties:
                    desk_item = jn_desk_items.getDeskItem(greeting_topic.additional_properties["desk_item"])
                    Natsuki.setDeskItem(desk_item)
                
                
                if "expression" in greeting_topic.additional_properties:
                    renpy.show("natsuki {0}".format(greeting_topic.additional_properties["expression"]), at_list=[jn_center], zorder=JN_NATSUKI_ZORDER)
                
                else:
                    renpy.show("natsuki idle", at_list=[jn_center], zorder=JN_NATSUKI_ZORDER)
                
                persistent._jn_player_admission_type_on_quit = None
                Natsuki.clearQuitApology()


    $ jnPause(0.1)
    hide black with Dissolve(1)
    $ jnPause(0.5)
    show screen hkb_overlay


    if jn_random_music.getRandomMusicPlayable():
        $ available_custom_music = jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_utils.getSupportedMusicFileExtensions()
        )
        if len(available_custom_music) >= 2:

            $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=random.choice(available_custom_music)[0], is_custom=True), channel="music")
            $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.random
        else:

            $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=main_background.location.getCurrentTheme(), is_custom=False), channel="music")
            $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.random
    else:

        $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=main_background.location.getCurrentTheme(), is_custom=False), channel="music")
        $ jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.location


    if (
        Natsuki.isAffectionate(higher=True)
        and (not persistent._jn_natsuki_chibi_seen and persistent.jn_total_visit_count > 50) or (random.randint(1, 1000) == 1)
    ):
        $ jn_stickers.stickerWindowPeekUp(at_right=random.choice([True, False]))




label ch30_loop:
    $ jn_activity.ACTIVITY_MANAGER.setIsEnabled(True)
    $ jnShowNatsukiIdle(jn_center)


    python:
        _now = datetime.datetime.now()

        if LAST_MINUTE_CHECK.minute is not _now.minute:
            minute_check()
            LAST_MINUTE_CHECK = _now
            
            if LAST_MINUTE_CHECK.minute in (0, 15, 30, 45):
                quarter_hour_check()
            
            if LAST_MINUTE_CHECK.minute in (0, 30):
                half_hour_check()

        if LAST_HOUR_CHECK is not _now.hour:
            hour_check()
            LAST_HOUR_CHECK = _now.hour

        if LAST_DAY_CHECK is not _now.day:
            
            LAST_DAY_CHECK = _now.day
            day_check()

        Natsuki.setForceQuitAttempt(False)
        Natsuki.setInConversation(False)


    while persistent._event_list:
        call call_next_topic



label ch30_wait:
    window hide
    python:
        import random

        if not jn_topic_in_event_list("weather_change") and jn_locations.checkUpdateLocationSunriseSunset(main_background):
            queue("weather_change")

        jnShowNatsukiIdle(jn_center)  
        jnPause(delay=5.0, hard=True)

    jump ch30_loop


label call_next_topic(show_natsuki=True):
    $ _topic = None

    if show_natsuki:
        $ jnShowNatsukiIdle(jn_center)

    if persistent._event_list:
        $ _topic = persistent._event_list.pop(0)

        if renpy.has_label(_topic):

            if (persistent._jn_notify_conversations
                and jn_utils.get_current_session_length().total_seconds() > 60
                and not jn_activity.getJNWindowActive()
                and not _topic in ["random_music_change", "weather_change"]
                and not "idle_" in _topic):

                play audio notification
                python:
                    jn_activity.taskbarFlash()
                    store.happy_emote = jn_utils.getRandomHappyEmoticon()
                    store.angry_emote = jn_utils.getRandomAngryEmoticon()
                    store.sad_emote = jn_utils.getRandomSadEmoticon()
                    store.tease_emote = jn_utils.getRandomTeaseEmoticon()
                    store.confused_emote = jn_utils.getRandomConfusedEmoticon()

                    ENAMORED_NOTIFY_MESSAGES = [
                            "[player]! [player]! Wanna talk? [happy_emote]",
                            "Hey! You got a sec? [happy_emote]",
                            "Wanna talk? [happy_emote]",
                            "[player]! I got something! [happy_emote]",
                            "Heeey! Wanna talk?",
                            "Talk to meeee! [angry_emote]",
                            "I'm talking to you, dummy! [tease_emote]"
                        ]
                    AFFECTIONATE_NOTIFY_MESSAGES = [
                            "Wanna talk?",
                            "[player]! You wanna talk?",
                            "Hey! Hey! Talk to me! [angry_emote]",
                            "Hey dummy! I'm talking to you!",
                            "[player]! I just thought of something! [confused_emote]",
                            "[player]! I wanna talk to you!",
                            "I just thought of something, [player]!"
                        ]
                    HAPPY_NOTIFY_MESSAGES = [
                            "[player]! Did you have a sec?",
                            "[player]? Can I borrow you?",
                            "Hey! Come here a sec?",
                            "Hey! I wanna talk!",
                            "You there, [player]?"
                        ]
                    NORMAL_NOTIFY_MESSAGES = [
                            "You wanna talk?",
                            "Hey... are you busy?",
                            "[player]? Did you have a sec?",
                            "Can I borrow you for a sec?",
                            "You there, [player]?",
                            "Hey... you still there?",
                            "[player]? Are you there?"
                        ]

                    if Natsuki.isNormal(higher=True):
                        if Natsuki.isEnamored(higher=True):
                            notify_message = random.choice(ENAMORED_NOTIFY_MESSAGES)
                        
                        elif Natsuki.isAffectionate(higher=True):
                            notify_message = random.choice(AFFECTIONATE_NOTIFY_MESSAGES)
                        
                        elif Natsuki.isHappy(higher=True):
                            notify_message = random.choice(HAPPY_NOTIFY_MESSAGES)
                        
                        else:
                            notify_message = random.choice(NORMAL_NOTIFY_MESSAGES)
                        
                        jn_activity.notifyPopup(renpy.substitute(notify_message))


            $ Natsuki.setInConversation(True)
            call expression _topic


            $ Natsuki.resetLastIdleCall()

    python:


        return_keys = _return if isinstance(_return, dict) else dict()

        topic_obj = get_topic(_topic)


        if topic_obj is not None:
            
            topic_obj.shown_count += 1
            topic_obj.last_seen = datetime.datetime.now()
            
            
            if "derandom" in return_keys:
                topic_obj.random = False


    if "quit" in return_keys:
        jump quit


    python:
        import re

        if isinstance(_topic, basestring): 
            
            if re.search("(^talk_)", _topic) or not re.search("(_change$)|(^idle_)", _topic):
                Natsuki.resetLastTopicCall()

        Natsuki.setInConversation(False)

    jump ch30_loop

init python:
    LAST_MINUTE_CHECK = datetime.datetime.now()
    LAST_HOUR_CHECK = LAST_MINUTE_CHECK.hour
    LAST_DAY_CHECK = LAST_MINUTE_CHECK.day

    def minute_check():
        """
        Runs every minute during breaks between topics
        """
        jn_utils.saveGame()
        
        
        Natsuki.checkResetDailies()
        
        
        if len(jn_plugins.minute_check_calls) > 0:
            for action in jn_plugins.minute_check_calls:
                eval(action.statement)
        
        
        current_activity = jn_activity.ACTIVITY_MANAGER.getCurrentActivity()
        
        if (
            Natsuki.isHappy(higher=True)
            and persistent.jn_custom_outfits_unlocked
            and jn_outfits.getSafePendingUnlocks()
            and not jn_events.selectHolidays()
        ):
            queue("new_wearables_outfits_unlocked")
        
        
        if (
            persistent.jn_natsuki_random_topic_frequency != jn_preferences.random_topic_frequency.NEVER
            and datetime.datetime.now() > Natsuki.getLastTopicCall() + datetime.timedelta(minutes=jn_preferences.random_topic_frequency.getRandomTopicCooldown())
            and datetime.datetime.now() >= Natsuki.getLastMenuCall() + datetime.timedelta(seconds=5)
            and not persistent._event_list
        ):
            if not persistent.jn_natsuki_repeat_topics:
                topic_pool = Topic.filter_topics(
                    topics.TOPIC_MAP.values(),
                    unlocked=True,
                    nat_says=True,
                    location=main_background.location.id,
                    affinity=Natsuki._getAffinityState(),
                    is_seen=False
                )
                if persistent._jn_daily_jokes_unlocked and persistent._jn_daily_jokes_enabled and not persistent._jn_daily_joke_given:
                    topic_pool.append(get_topic("talk_daily_joke")) 
            else:
                topic_pool = Topic.filter_topics(
                    topics.TOPIC_MAP.values(),
                    unlocked=True,
                    nat_says=True,
                    location=main_background.location.id,
                    affinity=Natsuki._getAffinityState(),
                    excludes_categories=["Setup"]
                )
            
            if topic_pool:
                if (not persistent.jn_natsuki_repeat_topics):
                    
                    store.persistent._jn_out_of_topics_warning_given = False
                
                Natsuki.calculatedAffinityGain()
                queue(random.choice(topic_pool).label)
            
            elif (
                not store.persistent.jn_natsuki_repeat_topics 
                and not store.persistent._jn_out_of_topics_warning_given
                and persistent._jn_natsuki_out_of_topics_remind
            ):
                
                queue("talk_out_of_topics")
        
        
        if (
            persistent._jn_natsuki_idles_enabled
            and datetime.datetime.now() >= Natsuki.getLastTopicCall() + datetime.timedelta(minutes=2)
            and datetime.datetime.now() >= Natsuki.getLastIdleCall() + datetime.timedelta(minutes=10)
            and datetime.datetime.now() >= Natsuki.getLastMenuCall() + datetime.timedelta(seconds=5)
            and not persistent._event_list
        ):
            idle_topic = jn_idles.selectIdle()
            if idle_topic:
                queue(idle_topic)
                Natsuki.resetLastIdleCall()
        
        
        if (
            persistent._jn_notify_activity
            and Natsuki.isAffectionate(higher=True)
            and current_activity.activity_type != jn_activity.ACTIVITY_MANAGER.last_activity.activity_type
            and random.randint(1, 20) == 1
        ):
            jn_activity.ACTIVITY_MANAGER.last_activity = current_activity
            if jn_activity.ACTIVITY_MANAGER.last_activity.getRandomNotifyText():
                jn_activity.notifyPopup(jn_activity.ACTIVITY_MANAGER.last_activity.getRandomNotifyText())
        
        if (random.randint(1, 10000) == 1):
            jn_stickers.stickerWindowPeekUp(at_right=random.choice([True, False]))
        
        return

    def quarter_hour_check():
        """
        Runs every fifteen minutes during breaks between topics
        """
        
        
        if len(jn_plugins.quarter_hour_check_calls) > 0:
            for action in jn_plugins.quarter_hour_check_calls:
                eval(action.statement)
        
        if not jn_topic_in_event_list("weather_change"):
            queue("weather_change")
        
        if not jn_topic_in_event_list("random_music_change"):
            queue("random_music_change")
        
        return

    def half_hour_check():
        """
        Runs every thirty minutes during breaks between topics
        """
        
        
        if len(jn_plugins.half_hour_check_calls) > 0:
            for action in jn_plugins.half_hour_check_calls:
                eval(action.statement)
        
        return

    def hour_check():
        """
        Runs every hour during breaks between topics
        """
        
        
        if len(jn_plugins.hour_check_calls) > 0:
            for action in jn_plugins.hour_check_calls:
                eval(action.statement)
        
        if not jn_topic_in_event_list("weather_change"):
            queue("weather_change")
        
        if (
            persistent.jn_natsuki_auto_outfit_change_enabled
            and not Natsuki.isWearingOutfit(jn_outfits.getRealtimeOutfit().reference_name)
        ):
            
            renpy.call("outfits_auto_change")
        
        jn_utils.fireAndForgetFunction(jn_data_migrations.checkCurrentVersionIsLatest)
        
        return

    def day_check():
        """
        Runs every day during breaks between topics
        """
        
        if len(jn_plugins.day_check_calls) > 0:
            for action in jn_plugins.day_check_calls:
                eval(action.statement)
        
        if not jn_topic_in_event_list("weather_change"):
            queue("weather_change")
        
        
        if (datetime.datetime.now().year > persistent.jn_last_visited_date.year):
            jn_events.resetHolidays()
            jn_utils.log("Holiday completion states reset.")
        
        persistent.jn_last_visited_date = datetime.datetime.now()
        
        
        persistent._jn_holiday_prop_list_on_quit = []
        available_holidays = jn_events.selectHolidays()
        if available_holidays:
            jn_events.queueHolidays(available_holidays, is_day_check=True)
        
        return

label talk_menu:
    python:

        if Natsuki.isEnamored(higher=True):
            _talk_flavor_text = renpy.substitute(random.choice([
                "What's up,{w=0.1} [player]?",
                "What's on your mind,{w=0.1} [player]?",
                "Something up,{w=0.1} [player]?",
                "You wanna talk?{w=0.2} Ehehe.",
                "I'd love to talk!",
                "I always love talking to you,{w=0.1} [player]!",
                "[player]!{w=0.2} What's up?",
                "[player]!{w=0.2} What's on your mind?",
                "Ooh!{w=0.2} What did you wanna talk about?",
                "I'm all ears,{w=0.1} [player]!",
                "I've always got time for you,{w=0.1} [player]!",
                "Hey!{w=0.2} What's up,{w=0.2} [player]?",
                "What have you got for me?{w=0.2} Ehehe.",
                "[player]!{w=0.2} What's new?",
                "[player]!{w=0.2} You wanna talk?",
                "Shoot,{w=0.2} [player]!{w=0.3} Ehehe.",
                "Shoot,{w=0.2} [player]!",
                "Oh!{w=0.2} Oh!{w=0.2} You got something for me?",
                "Talk to me,{w=0.2} [player]!{w=0.3} Ehehe."
            ]))

        elif Natsuki.isNormal(higher=True):
            _talk_flavor_text = renpy.substitute(random.choice([
                "What's up?",
                "What's on your mind?",
                "What's happening?",
                "Something on your mind?",
                "Oh?{w=0.2} You wanna talk?",
                "Huh?{w=0.2} What's up?",
                "You wanna share something?",
                "What's new,{w=0.1} [player]?",
                "'Sup,{w=0.1} [player]?",
                "You wanna talk?",
                "Hey,{w=0.2} [player]!"
            ]))

        elif Natsuki.isDistressed(higher=True):
            _talk_flavor_text = renpy.substitute(random.choice([
                "What do you want?",
                "What is it?",
                "Make it quick.",
                "What now?",
                "What do you want now?",
                "What is it this time?",
                "Yeah?{w=0.2} What?",
                "What now?",
                "This better be good."
            ]))

        else:
            _talk_flavor_text = renpy.substitute(random.choice([
                "...",
                "...?",
                "What?",
                "Just talk already.",
                "Spit it out.",
                "Start talking.",
                "Get it over with.",
                "What do {i}you{/i} want?",
                "Get on with it.",
                "Talk."
            ]))

        jnShowNatsukiTalkMenu()
        Natsuki.setInConversation(True)

    menu:
        n "[_talk_flavor_text]"
        "Let's talk about...":

            call player_select_topic
        "Tell me again about...":

            call player_select_topic (is_repeat_topics=True)

        "I love you, [n_name]!" if Natsuki.isLove(higher=True) and persistent.jn_player_love_you_count > 0:
            $ push("talk_i_love_you")
            jump call_next_topic

        "I feel..." if Natsuki.isHappy(higher=True):
            jump player_admissions_start

        "I want to tell you..." if Natsuki.isHappy(higher=True):
            jump player_compliments_start
        "I want to say sorry...":

            jump player_apologies_start

        "About your outfit..." if Natsuki.isHappy(higher=True) and persistent.jn_custom_outfits_unlocked:
            jump outfits_menu

        "Goodbye..." if Natsuki.isAffectionate(higher=True):
            jump farewell_menu

        "Goodbye." if Natsuki.isHappy(lower=True):
            jump farewell_start
        "Nevermind.":

            $ Natsuki.resetLastIdleCall()
            $ Natsuki.resetLastMenuCall()
            jump ch30_loop

    $ Natsuki.resetLastIdleCall()
    $ Natsuki.resetLastMenuCall()

    return

label player_select_topic(is_repeat_topics=False):
    python:
        if (is_repeat_topics):
            _topics = Topic.filter_topics(
                topics.TOPIC_MAP.values(),
                nat_says=True,
                unlocked=True,
                location=main_background.location.id,
                affinity=Natsuki._getAffinityState(),
                is_seen=True
            )

        else:
            _topics = Topic.filter_topics(
                topics.TOPIC_MAP.values(),
                player_says=True,
                unlocked=True,
                location=main_background.location.id,
                affinity=Natsuki._getAffinityState()
            )


        _topics.sort(key=lambda topic: topic.prompt)


        menu_items = menu_dict(_topics)

    call screen categorized_menu(
        menu_items=menu_items,
        category_pane_space=(990, 40, 250, 572),
        option_list_space=(710, 40, 250, 572), 
        category_length=len(_topics))

    $ _choice = _return


    if isinstance(_choice, basestring):
        $ push(_choice)
        $ Natsuki.calculatedAffinityGain()
        jump call_next_topic


    elif _choice == -1:
        jump talk_menu


    $ _return = None

    jump ch30_loop

label farewell_menu:
    python:

        available_farewell_options = jn_farewells.getFarewellOptions()
        available_farewell_options.sort(key = lambda option: option[0])
        available_farewell_options.append(("Goodbye.", "farewell_start"))

    call screen scrollable_choice_menu(available_farewell_options, ("Go back", None))
    $ Natsuki.setForceQuitAttempt(False)

    if isinstance(_return, basestring):
        $ jnShowNatsukiIdle(jn_center)
        $ push(_return)
        jump call_next_topic

    jump talk_menu

label outfits_menu:
    call screen scrollable_choice_menu([
        ("Can you wear an outfit for me?", "outfits_wear_outfit"),
        ("Can I suggest a new outfit?", "outfits_suggest_outfit"),
        ("Can you forget about an outfit I suggested?", "outfits_remove_outfit"),
        ("Can you search again for new items?", "outfits_reload")],
        ("Go back", None),
        400,
        "mod_assets/icons/outfits.png")

    if isinstance(_return, basestring):
        $ jnShowNatsukiIdle(jn_center)
        $ push(_return)
        jump call_next_topic

    jump talk_menu

label extras_menu:
    python:
        Natsuki.setInConversation(True)
        avaliable_extras_options = []


        for extras_option in jn_plugins.extras_options:
            if eval(extras_option.visible_if):
                avaliable_extras_options.append((extras_option.option_name, extras_option.jump_label))


        avaliable_extras_options.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(avaliable_extras_options, ("Nevermind.", None))

    if isinstance(_return, basestring):
        $ renpy.jump(_return)

    jump ch30_loop

label try_force_quit:
    $ Natsuki.setInConversation(True)


    if persistent._jn_player_tt_state >= 2 or persistent._jn_pic:
        $ renpy.jump("quit")


    elif (
        jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete
        and jn_farewells.JNForceQuitStates(persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.not_force_quit
    ):

        $ Natsuki.setForceQuitAttempt(False)
        $ push("farewell_force_quit")
        $ renpy.jump("call_next_topic")

    elif not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete:

        $ Natsuki.setForceQuitAttempt(False)
        $ renpy.jump("quit")
    else:

        $ Natsuki.setForceQuitAttempt(True)
        $ Natsuki.addApology(jn_apologies.ApologyTypes.sudden_leave)
        $ Natsuki.setQuitApology(jn_apologies.ApologyTypes.sudden_leave)


        if Natsuki.isAffectionate(higher=True):
            n 2ccsem "W-{w=0.2}wait,{w=0.5}{nw}"
            extend 2knmflsbl " what?{w=0.75}{nw}"
            extend 5clrunlsbl " Can you at {i}least{/i} say goodbye first,{w=0.2} [player]?"

        elif Natsuki.isNormal(higher=True):
            n 4kskem "H-{w=0.2}hey!{w=0.75}{nw}"
            extend 4kllflsbl " Y-{w=0.2}you aren't just going to leave like that,{w=0.5}{nw}"
            extend 4ksqunsbl " are you?"

        elif Natsuki.isDistressed(higher=True):
            n 2fsqpu "...Really?{w=0.75}{nw}"
            extend 2fcsupsbr " I don't even get a 'goodbye' now?"
        else:

            n 2fsqsftsb "..."

        menu:
            "Nevermind.":

                if Natsuki.isAffectionate(higher=True):
                    n 4kllssl "T-{w=0.2}thanks,{w=0.2} [player].{w=1}{nw}"
                    n 1tllss "Now,{w=0.2} where was I...?{w=1}{nw}"
                    extend 1unmbo " Oh,{w=0.2} right.{w=1}{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 2flleml "G-{w=0.2}good!{w=1}{nw}"
                    extend 2kllpol " Good...{w=1}{nw}"
                    n 1tslpu "Now...{w=0.3} what was I saying again?{w=0.5}{nw}"
                    extend 1nnmbo " Oh,{w=0.2} right.{w=1}{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 1fsqfr "...Thank you.{w=1}{nw}"
                    n 1fslpu "As I was {i}saying{/i}...{w=1}{nw}"
                else:

                    n 1fcsfr "Whatever.{w=1}{nw}"
                    n 2fsqsl "{cps=7.5}As I was saying.{/cps}{w=1}{nw}"

                $ Natsuki.setForceQuitAttempt(False)
                $ Natsuki.removeApology(jn_apologies.ApologyTypes.sudden_leave)
                $ Natsuki.clearQuitApology()

                return
            "...":


                hide screen hkb_overlay
                if Natsuki.isAffectionate(higher=True):
                    n 4kwmem "Come on,{w=0.2} [player]...{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 2kcsup "...!{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 4fwmun "...Really,{w=0.2} [player]?{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 2kcsfu "Hnnng-!{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 2fslun "Don't let the door hit you on the way out.{w=1}{nw}"
                    extend 2fsqem " Jerk.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 2fcsan "Nnngg-!{nw}"
                else:

                    n 1fslun "Heh.{w=1}{nw}"
                    extend 1fsqfr "...Maybe you {i}shouldn't{/i} come back.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1fcsfr "...{nw}"

                    if (random.randint(0, 10) == 1):
                        play sound glitch_d loop
                        show glitch_garbled_red zorder JN_GLITCH_ZORDER with vpunch
                        $ jnPause(random.randint(4,13), hard=True)
                        stop sound
                        play audio glitch_e
                        show glitch_garbled_n zorder JN_GLITCH_ZORDER with hpunch
                        $ jnPause(0.025, hard=True)
                        hide glitch_garbled_n
                        hide glitch_garbled_red

                play audio static
                show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
                hide glitch_garbled_b
                $ renpy.jump("quit")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
