default persistent._event_database = dict()
default persistent._jn_holiday_list = dict()
default persistent._jn_holiday_completed_list = []
default persistent._jn_holiday_deco_list_on_quit = []
default persistent._jn_event_completed_count = 0
default persistent._jn_event_attempt_count = 15

default persistent._jn_player_celebrates_christmas = None
default persistent._jn_player_love_halloween_seen = None
default persistent._jn_player_allow_legacy_music_switch_event = False


transform jn_glasses_pre_slide:
    subpixel True
    ypos 0

transform jn_glasses_slide_down:
    subpixel True
    ypos 0
    easeout 5 ypos 20

transform jn_glasses_slide_down_faster:
    subpixel True
    ypos 0
    easeout 3 ypos 20

transform jn_glasses_readjust:
    subpixel True
    ypos 20
    easein 0.75 ypos 0

transform jn_mistletoe_lift:
    subpixel True
    ypos 0
    easeout 2 ypos -54

transform jn_confetti_fall:
    subpixel True
    ypos 0
    easeout 2.25 alpha 0 ypos 90


image prop poetry_attempt = "mod_assets/props/poetry_attempt.png"
image prop math_attempt = "mod_assets/props/math_attempt.png"
image prop strawberry_milkshake = "mod_assets/props/strawberry_milkshake.png"
image prop glasses_case = "mod_assets/props/glasses_case.png"
image prop hot_chocolate hot = "mod_assets/props/hot_chocolate.png"
image prop hot_chocolate cold = "mod_assets/props/hot_chocolate_cold.png"
image prop cake lit = "mod_assets/props/cake_lit.png"
image prop cake unlit = "mod_assets/props/cake_unlit.png"
image prop watering_can = "mod_assets/props/watering_can.png"
image prop glasses_desk = "mod_assets/props/glasses_desk.png"

image prop f14_heart give = "mod_assets/props/f14/give_heart.png"
image prop f14_heart hold = "mod_assets/props/f14/hold_heart.png"

image prop wintendo_twitch_held free = "mod_assets/props/twitch/held/wintendo_twitch_held_free.png"
image prop wintendo_twitch_held charging = "mod_assets/props/twitch/held/wintendo_twitch_held_charging.png"
image prop wintendo_twitch_playing free:
    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_b.png"
        pause 0.1
    choice:

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/free/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat

image prop wintendo_twitch_playing charging:
    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 2

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
    pause 0.15

    "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
    pause 1.5

    choice:
        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.3

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_b.png"
        pause 0.1
    choice:

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_a.png"
        pause 0.25

        "mod_assets/props/twitch/gaming/charging/wintendo_twitch_playing_c.png"
        pause 0.15

    repeat

image prop wintendo_twitch_battery_low:
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_a.png"
    pause 1
    "mod_assets/props/twitch/low_battery/wintendo_twitch_battery_low_b.png"
    pause 1
    repeat

image prop wintendo_twitch_dead:
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_a.png"
    pause 1
    "mod_assets/props/twitch/dead/wintendo_twitch_dead_b.png"
    pause 1
    repeat

image prop music_notes:
    choice:
        "mod_assets/props/music/music_notes_a.png"
    choice:
        "mod_assets/props/music/music_notes_b.png"
    choice:
        "mod_assets/props/music/music_notes_c.png"
    choice:
        "mod_assets/props/music/music_notes_d.png"
    pause 1
    repeat

image confetti falling:
    "mod_assets/props/confetti/confetti_a.png"
    pause 0.75
    "mod_assets/props/confetti/confetti_b.png"
    pause 0.75
    "mod_assets/props/confetti/confetti_c.png"
    pause 0.75

image confetti desk:
    "mod_assets/props/confetti/confetti_desk.png"


image deco balloons = "mod_assets/deco/balloons.png"
image deco garlands = "mod_assets/deco/garlands.png"
image deco tree day = "mod_assets/deco/tree_day.png"
image deco tree night = "mod_assets/deco/tree_night.png"
image deco hanging_lights lit = "mod_assets/deco/hanging_lights_lit.png"
image deco hanging_lights unlit = "mod_assets/deco/hanging_lights_unlit.png"
image deco wall_stocking day = "mod_assets/deco/wall_stocking_day.png"
image deco wall_stocking night = "mod_assets/deco/wall_stocking_night.png"
image deco d24 = "mod_assets/deco/d24.png"
image deco d25 = "mod_assets/deco/d25.png"
image deco o31 = "mod_assets/deco/o31.png"


image overlay slipping_glasses = "mod_assets/overlays/slipping_glasses.png"
image overlay mistletoe = "mod_assets/overlays/mistletoe.png"
image overlay puddles day = "mod_assets/overlays/puddles_day.png"
image overlay puddles night = "mod_assets/overlays/puddles_night.png"

init python in jn_events:
    import datetime
    from Enum import Enum
    import random
    import store
    import store.audio as audio
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity
    import store.jn_custom_music as jn_custom_music
    import store.jn_globals as jn_globals
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils

    EVENT_MAP = dict()
    EVENT_RETURN_OUTFIT = None

    _m1_script0x2devents__ALL_HOLIDAYS = {}

    def selectEvent():
        """
        Picks and returns a single random event, or None if no events are left.
        """
        kwargs = dict()
        event_list = store.Topic.filter_topics(
            EVENT_MAP.values(),
            unlocked=True,
            affinity=store.Natsuki._getAffinityState(),
            is_seen=False,
            **kwargs
        )
        
        if len(event_list) > 0:
            return random.choice(event_list).label
        
        else:
            return None

    class JNHolidayTypes(Enum):
        new_years_day = 1
        easter = 2
        halloween = 3
        christmas_eve = 4
        christmas_day = 5
        new_years_eve = 6
        natsuki_birthday = 7
        player_birthday = 8
        anniversary = 9
        valentines_day = 10
        
        def __str__(self):
            return self.name
        
        def __int__(self):
            return self.value

    class JNHoliday():
        """
        Describes a holiday event that a user can experience, once per year.
        """
        def __init__(
            self,
            label,
            holiday_type,
            affinity_range,
            natsuki_sprite_code,
            conditional=None,
            bgm=None,
            deco_list=[],
            prop_list=[],
            priority=0
        ):
            """
            Constructor.

            IN:
                - label - The name used to uniquely identify this holiday and refer to it internally
                - holiday_type - The JNHolidayTypes type of this holiday
                - affinity_range - The affinity range that must be satisfied for this holiday to be picked when filtering
                - natsuki_sprite_code - The sprite code to show for Natsuki when the holiday is revealed
                - conditional - Python statement that must evaluate to True for this holiday to be picked when filtering
                - bgm - The optional music to play when the holiday is revealed
                - deco_list - Optional list of deco images to show when setting up
                - prop_list - Optional list of prop images to show when setting up
                - priority - Optional priority value; holidays with lower values are shown first
            """
            self.label = label
            self.is_seen = False
            self.shown_count = 0
            self.holiday_type = holiday_type
            self.conditional = conditional
            self.affinity_range = affinity_range
            self.natsuki_sprite_code = natsuki_sprite_code
            self.bgm = bgm
            self.deco_list = deco_list
            self.prop_list = prop_list
            self.priority = priority
        
        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each holiday from the persistent.
            """
            global _m1_script0x2devents__ALL_HOLIDAYS
            for holiday in _m1_script0x2devents__ALL_HOLIDAYS.itervalues():
                holiday._m1_script0x2devents__load()
        
        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each holiday to the persistent.
            """
            global _m1_script0x2devents__ALL_HOLIDAYS
            for holiday in _m1_script0x2devents__ALL_HOLIDAYS.itervalues():
                holiday._m1_script0x2devents__save()
        
        @staticmethod
        def filterHolidays(
            holiday_list,
            is_seen=None,
            shown_count=None,
            holiday_types=None,
            affinity=None,
            holiday_completion_state=None
        ):
            """
            Returns a filtered list of holidays, given an holiday list and filter criteria.

            IN:
                - holiday_list - the list of JNHoliday objects to query#
                - is_seen - boolean state the seen flag of the holiday must be
                - shown_count - int number of times the holiday must have been seen before
                - holiday_types - list of JNHolidayTypes the holiday must be in
                - affinity - minimum affinity state the holiday must have
                - holiday_completion_state - boolean state the completion state corresponding to each holiday must be

            OUT:
                - list of holidays matching the search criteria
            """
            return [
                _holiday
                for _holiday in holiday_list
                if _holiday._m1_script0x2devents__filterHoliday(
                    is_seen,
                    shown_count,
                    holiday_types,
                    affinity,
                    holiday_completion_state
                )
            ]
        
        def asDict(self):
            """
            Exports a dict representation of this holiday; this is for data we want to persist.

            OUT:
                dictionary representation of the holiday object
            """
            return {
                "is_seen": self.is_seen,
                "shown_count": self.shown_count
            }
        
        def currAffinityInAffinityRange(self, affinity_state=None):
            """
            Checks if the current affinity is within this holidays's affinity_range

            IN:
                affinity_state - Affinity state to test if the holidays can be shown in. If None, the current affinity state is used.
                    (Default: None)
            OUT:
                True if the current affinity is within range. False otherwise
            """
            if not affinity_state:
                affinity_state = jn_affinity._getAffinityState()
            
            return jn_affinity._isAffStateWithinRange(affinity_state, self.affinity_range)
        
        def _m1_script0x2devents__load(self):
            """
            Loads the persisted data for this holiday from the persistent.
            """
            if store.persistent._jn_holiday_list[self.label]:
                self.is_seen = store.persistent._jn_holiday_list[self.label]["is_seen"]
                self.shown_count = store.persistent._jn_holiday_list[self.label]["shown_count"] if "shown_count" in store.persistent._jn_holiday_list[self.label] else 0
        
        def _m1_script0x2devents__save(self):
            """
            Saves the persistable data for this holiday to the persistent.
            """
            store.persistent._jn_holiday_list[self.label] = self.asDict()
        
        def _m1_script0x2devents__filterHoliday(
            self,
            is_seen=None,
            shown_count=None,
            holiday_types=None,
            affinity=None,
            holiday_completion_state=None
        ):
            """
            Returns True, if the holiday meets the filter criteria. Otherwise False.

            IN:
                - holiday_list - the list of JNHoliday objects to query#
                - is_seen - boolean state the seen flag of the holiday must be
                - shown_count - int number of times the holiday must have been seen before
                - holiday_types - list of JNHolidayTypes the holiday must be in
                - affinity - minimum affinity state the holiday must have
                - holiday_completion_state - boolean state the completion state corresponding to each holiday must be

            OUT:
                - True, if the holiday meets the filter criteria. Otherwise False
            """
            if is_seen is not None and self.is_seen != is_seen:
                return False
            
            elif shown_count is not None and self.shown_count < shown_count:
                return False
            
            elif holiday_types is not None and not self.holiday_type in holiday_types:
                return False
            
            elif affinity is not None and not self.currAffinityInAffinityRange(affinity):
                return False
            
            elif (
                holiday_completion_state is not None
                and self.isCompleted()
            ):
                return False
            
            elif self.conditional is not None and not eval(self.conditional, store.__dict__):
                return False
            
            return True
        
        def run(self, suppress_visuals=False):
            """
            Sets up all visuals for this holiday, before revealing everything to the player.
            Any props or decorations left over from the previous holiday are tidied up before presentation.

            IN:
                - suppress_visuals - If True, prevents any props or deco from being displayed automatically
            """
            renpy.hide("prop")
            renpy.hide("deco")
            
            if not suppress_visuals:
                for prop in self.prop_list:
                    renpy.show(name="prop {0}".format(prop), zorder=store.JN_PROP_ZORDER)
            
            if not suppress_visuals:
                for deco in self.deco_list:
                    renpy.show(name="deco {0}".format(deco), zorder=store.JN_DECO_ZORDER)
            
            kwargs = {
                "natsuki_sprite_code": self.natsuki_sprite_code
            }
            if self.bgm:
                kwargs.update({"bgm": self.bgm})
            
            if not suppress_visuals:
                displayVisuals(**kwargs)
            
            else:
                jn_globals.force_quit_enabled = True
        
        def complete(self):
            """
            Marks this holiday as complete, preventing it from being seen again until reset.
            This should be run after a holiday has concluded, so a crash/quit after starting the holiday doesn't lock progression.
            We also mark the holiday type as completed for this year, so we can't cycle through all seasonal events in one year
            Lastly, set the persisted deco list so reloading the game without a day change shows the deco for this event.
            """
            store.persistent._jn_event_completed_count += 1
            self.is_seen = True
            self.shown_count += 1
            self._m1_script0x2devents__save()
            
            if not self.isCompleted():
                store.persistent._jn_holiday_completed_list.append(int(self.holiday_type))
            
            if self.deco_list:
                store.persistent._jn_holiday_deco_list_on_quit = self.deco_list
            
            store.Natsuki.resetLastTopicCall()
            store.Natsuki.resetLastIdleCall()
        
        def isCompleted(self):
            """
            Returns whether this holiday has been completed.

            OUT:
                - True if the holiday has been marked as completed, otherwise False
            """
            return int(self.holiday_type) in store.persistent._jn_holiday_completed_list

    def _m1_script0x2devents__registerHoliday(holiday):
        """
        Registers a new holiday in the list of all holidays, allowing in-game access and persistency.
        """
        if holiday.label in _m1_script0x2devents__ALL_HOLIDAYS:
            jn_utils.log("Cannot register holiday name: {0}, as a holiday with that name already exists.".format(holiday.reference_name))
        
        else:
            _m1_script0x2devents__ALL_HOLIDAYS[holiday.label] = holiday
            if holiday.label not in store.persistent._jn_holiday_list:
                holiday._m1_script0x2devents__save()
            
            else:
                holiday._m1_script0x2devents__load()

    def getHoliday(holiday_name):
        """
        Returns the holiday for the given name, if it exists.

        IN:
            - holiday_name - str outfit name to fetch

        OUT: Corresponding JNHoliday if the holiday exists, otherwise None
        """
        if holiday_name in _m1_script0x2devents__ALL_HOLIDAYS:
            return _m1_script0x2devents__ALL_HOLIDAYS[holiday_name]
        
        return None

    def getHolidaysForDate(input_date=None):
        """
        Gets the holidays - if any - corresponding to the supplied date, or the current date by default.

        IN:
            - input_date - datetime object to test against. Defaults to the current date.

        OUT:
            - JNHoliday representing the holiday for the supplied date.
        """
        
        if input_date is None:
            input_date = datetime.datetime.today()
        
        elif not isinstance(input_date, datetime.date):
            raise TypeError("input_date for holiday check must be of type date; type given was {0}".format(type(input_date)))
        
        holidays = []
        
        if store.jnIsNewYearsDay(input_date):
            holidays.append(JNHolidayTypes.new_years_day)
        
        if store.jnIsValentinesDay(input_date):
            holidays.append(JNHolidayTypes.valentines_day)
        
        if store.jnIsEaster(input_date):
            holidays.append(JNHolidayTypes.easter)
        
        if store.jnIsHalloween(input_date):
            holidays.append(JNHolidayTypes.halloween)
        
        if store.jnIsChristmasEve(input_date):
            holidays.append(JNHolidayTypes.christmas_eve)
        
        if store.jnIsChristmasDay(input_date):
            holidays.append(JNHolidayTypes.christmas_day)
        
        if store.jnIsNewYearsEve(input_date):
            holidays.append(JNHolidayTypes.new_years_eve)
        
        if store.jnIsNatsukiBirthday(input_date):
            holidays.append(JNHolidayTypes.natsuki_birthday)
        
        if store.jnIsPlayerBirthday(input_date):
            holidays.append(JNHolidayTypes.player_birthday)
        
        if store.jnIsAnniversary(input_date):
            holidays.append(JNHolidayTypes.anniversary)
        
        return holidays

    def getAllHolidays():
        """
        Returns a list of all holidays.
        """
        return _m1_script0x2devents__ALL_HOLIDAYS.itervalues()

    def selectHolidays():
        """
        Returns a list of all uncompleted holidays that apply for the current date, or None if no holidays apply.
        Only one holiday of each type may be returned.
        """
        holiday_list = JNHoliday.filterHolidays(
            is_seen=False,
            holiday_list=getAllHolidays(),
            holiday_types=getHolidaysForDate(),
            affinity=store.Natsuki._getAffinityState(),
            holiday_completion_state=False
        )
        
        if len(holiday_list) > 0:
            holiday_types_added = []
            return_list = []
            for holiday in holiday_list:
                if holiday.holiday_type not in holiday_types_added:
                    holiday_types_added.append(holiday.holiday_type)
                    return_list.append(holiday)
            
            return return_list
        
        else:
            return None

    def resetHolidays():
        """
        Resets the is_seen state and corresponding completion state for all holidays.
        Also clears the deco.
        """
        for holiday in getAllHolidays():
            holiday.is_seen = False
        
        JNHoliday.saveAll()
        store.persistent._jn_holiday_completed_list = []
        store.persistent._jn_holiday_deco_list_on_quit = []

    def queueHolidays(holiday_list, is_day_check=False):
        """
        Given a list of holidays, will sort them according to priority and add them to the list of topics to run through.
        Interludes are used to perform pacing, so a holiday will not immediately transition into another.
        """
        store.persistent._event_list = list()
        holiday_list.sort(key = lambda holiday: holiday.priority)
        
        if is_day_check:
            store.queue("holiday_prelude")
        
        while len(holiday_list) > 0:
            store.queue(holiday_list.pop(0).label)
            
            if len(holiday_list) > 0:
                store.queue("holiday_interlude")
            
            else:
                store.queue("ch30_loop")
        
        renpy.jump("call_next_topic")

    def displayVisuals(
        natsuki_sprite_code,
        bgm="mod_assets/bgm/vacation.ogg"
    ):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
            - music_file_path - The str file path of the music to play upon revealing Natsuki; defaults to standard bgm
        """
        renpy.show("natsuki {0}".format(natsuki_sprite_code), at_list=[store.jn_center], zorder=store.JN_NATSUKI_ZORDER)
        store.jnPause(0.1)
        renpy.hide("black")
        renpy.show_screen("hkb_overlay")
        renpy.play(filename=audio.switch_flip, channel="audio")
        renpy.play(filename=bgm, channel="music")
        jn_custom_music._last_music_option = jn_custom_music.JNMusicOptionTypes.location
        renpy.hide("black")




    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_christmas_eve",
        holiday_type=JNHolidayTypes.christmas_eve,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchsm",
        deco_list=["d24"],
        priority=99
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_christmas_day",
        holiday_type=JNHolidayTypes.christmas_day,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fspss",
        deco_list=["d25"],
        priority=99
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_new_years_eve",
        holiday_type=JNHolidayTypes.new_years_eve,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchgneme",
        priority=10
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_new_years_day",
        holiday_type=JNHolidayTypes.new_years_day,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1uchgneme",
        deco_list=["balloons"],
        priority=10
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_valentines_day",
        holiday_type=JNHolidayTypes.valentines_day,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        natsuki_sprite_code="1fsrunlsbr",
        prop_list=["f14_heart hold"],
        priority=10
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_easter",
        holiday_type=JNHolidayTypes.easter,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fsrunlsbr",
        priority=10
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_halloween",
        holiday_type=JNHolidayTypes.halloween,
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1fsrunlsbr",
        deco_list=["o31"],
        priority=10
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_player_birthday",
        holiday_type=JNHolidayTypes.player_birthday,
        affinity_range=(jn_affinity.AFFECTIONATE, None),
        natsuki_sprite_code="1uchgnl",
        bgm=audio.happy_birthday_bgm,
        deco_list=["balloons"],
        prop_list=["cake unlit"],
        priority=50
    ))


    _m1_script0x2devents__registerHoliday(JNHoliday(
        label="holiday_natsuki_birthday",
        holiday_type=JNHolidayTypes.natsuki_birthday,
        conditional="jn_gifts.getGiftFileExists('party_supplies')",
        affinity_range=(jn_affinity.HAPPY, None),
        natsuki_sprite_code="1unmemlsbr",
        bgm=audio.happy_birthday_bgm,
        deco_list=["balloons"],
        prop_list=["cake unlit"],
        priority=50
    ))




init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 2",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_reading_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ jnPause(2)
    n "E-espera...{w=0.3} ¡¿qué?!"
    n "¡M-{w=0.2}Minori!{w=0.5}{nw}"
    extend " ¡Idiota!"
    n "¡En serio no puedo creer...!"
    n "Ugh...{w=0.5}{nw}"
    extend " ¿{i}esto{/i} es por lo que tenía que esperar?"
    n "Vamos...{w=0.5}{nw}"
    extend " dame un respiro..."

    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    $ parfait_manga = jn_desk_items.getDeskItem('jn_parfait_manga_held')
    $ parfait_manga.unlock()
    $ manga_closed = jn_desk_items.getDeskItem("jn_parfait_manga_closed")
    $ manga_closed.unlock()
    $ Natsuki.setDeskItem(parfait_manga)
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "¡...!"
    n 1uskeml "¡[player]!{w=0.5}{nw}"
    extend 1fcsan " ¿P-puedes {i}creer{/i} esto?"
    n 1fllfu "¡Parfait Girls tiene un nuevo editor,{w=0.3}{nw}"
    extend 1fbkwr " y no tiene {i}idea{/i} de lo que está haciendo!"
    n 1flrwr "Digo,{w=0.2} ¡¿has {i}visto{/i} esta basura?!{w=0.5}{nw}"
    extend 1fcsfu " ¡¿Siquiera han {i}leído{/i} la serie antes?!"
    n 1fcsan "¡Como {i}si{/i} Minori alguna vez cayera tan bajo como para-!"
    n 1unmem "¡...!"
    n 1fllpol "..."
    n 1fcspo "De hecho,{w=0.2} ¿sabes qué?{w=0.5} Está bien."
    n 1fsrss "No quería arruinártelo de todos modos."
    n 1flldv "Jejeje..."
    n 1nllpol "Solo...{w=0.5}{nw}"
    extend 1nlrss " guardaré esto."

    show natsuki 1nsrca
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    $ Natsuki.clearDesk()
    show natsuki 4nlrbo
    $ jnPause(4)
    hide black with Dissolve(1)

    n 3ulraj "Entonces..."
    n 3fchbgsbr "¿Qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_writing_poetry",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_writing_poetry:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmmm...{w=0.5}{nw}"
    extend " ¡ugh!"

    play audio paper_crumple
    $ jnPause(7)

    n "..."
    n "¡Nnnnnn-!"
    n "¡Simplemente no puedo {i}concentrarme{/i}!{w=0.5}{nw}"
    extend " ¿Por qué es esto {i}tan{/i} difícil ahora?"

    play audio paper_crumple
    $ jnPause(7)

    n "¡Rrrrr...!"
    n "¡Oh,{w=0.2} {i}olvídalo!{/i}"

    play audio paper_crumple
    $ jnPause(3)
    play audio paper_throw
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    show prop poetry_attempt zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1fsrpo")
    $ jn_globals.force_quit_enabled = True

    n 1uskuplesh "¡...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 4uskgsf "¡¿[player_initial]-[player]?!{w=0.5}{nw}"
    extend 2fbkwrl " ¡¿Cuánto tiempo has estado ahí?!"
    n 2fllpol "..."
    n 4uskeml "¿E-eh? ¿Esto?{w=0.5}{nw}"
    extend 4fcswrl " ¡N-no es nada!{w=0.5}{nw}"
    extend 2flrpol " ¡Nada en absoluto!"

    show natsuki 4fcspol
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    hide prop poetry_attempt
    show natsuki 2nslbol
    $ jnPause(4)
    hide black with Dissolve(1)

    n 2nslpol "..."
    n 2fslsslsbr "E-entonces...{w=0.5}{nw}"
    extend 4fcsbglsbr " ¿qué pasa,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_relationship_doubts",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(None, jn_affinity.DISTRESSED)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_relationship_doubts:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    n "Cuál es siquiera el {i}punto{/i} de esto..."
    n "Solo..."
    n "..."

    if Natsuki.isDistressed(higher=True):
        n "Yo {w=2}{i}odio{/i}{w=2} esto."
    else:

        n "Yo {w=2}{i}ODIO{/i}{w=2} esto."

    n "Lo odio.{w=1} Lo odio.{w=1} Lo odio.{w=1} Lo odio.{w=1} Lo {w=2}{i}odio{/i}{w=2}."
    $ jnPause(5)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder JN_GLITCH_ZORDER with vpunch
        n "¡¡{i}LO ODIO{/i}!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ jnPause(5)

    menu:
        "Entrar.":
            pass

    $ jn_events.displayVisuals(natsuki_sprite_code="1fcsupl", bgm=jn_custom_music.getMusicFileRelativePath(file_name=main_background.location.getCurrentTheme(), is_custom=False))
    $ jn_globals.force_quit_enabled = True

    n 1fsqunltsb "..."
    n 1fsqemtsb "...Oh.{w=1}{nw}"
    extend 2fsrsr " {i}Estás{/i} aquí."
    n 2ncsem "{i}Genial{/i}..."
    n 4fcsantsa "Sí, eso es {i}justo{/i} lo que necesito ahora."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_code_fiddling",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_code_fiddling:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmm..."
    n "¡Ajá!{w=0.5}{nw}"
    extend " Ya veo,{w=0.2} ya veo."
    n "Entonces,{w=0.3} creo...{w=1}{nw}"
    extend " si solo intento...{w=1.5}{nw}"
    extend " muy...{w=2}{nw}"
    extend " cuidadosamente...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_a

    n "¡Ack-!{w=2}{nw}"
    extend " Mierda,{w=0.3} ¡eso {i}dolió{/i}!"
    n "Ugh..."
    n "¿Cómo demonios se las arreglaba Monika con esto todo el tiempo?"
    extend " ¡Este código {i}apesta{/i}!"
    n "..."
    n "..."
    n "Pero...{w=1} ¿qué tal si yo-{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_c

    n "¡Eek!"
    n "..."
    n "...Sí,{w=0.3} no.{w=0.5} Creo que es suficiente por ahora.{w=1}{nw}"
    extend " Cielos..."
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    $ jn_events.displayVisuals("1fslpo")
    $ jn_globals.force_quit_enabled = True

    $ player_initial = jn_utils.getPlayerInitial()
    n 1uskemlesh "¡Ack-!"
    n 4fbkwrl "¡[player_initial]-{w=0.2}[player]!"
    extend 2fcseml " ¿Estás {i}intentando{/i} darme un infarto o algo así?"
    n 2fllpol "Cielos..."
    n 1fsrpo "Hola a ti también,{w=0.2} tonto..."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_not_ready_yet",
            unlocked=True,
            conditional=(
                "((jn_is_time_block_early_morning() or jn_is_time_block_mid_morning()) and jn_is_weekday())"
                " or (jn_is_time_block_late_morning and not jn_is_weekday())"
            ),
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_not_ready_yet:
    python:
        import random
        jn_globals.force_quit_enabled = False


        unlocked_ahoges = [
            jn_outfits.getWearable("jn_headgear_ahoge_curly"),
            jn_outfits.getWearable("jn_headgear_ahoge_small"),
            jn_outfits.getWearable("jn_headgear_ahoge_swoop")
        ]
        for ahoge in unlocked_ahoges:
            ahoge.unlock()


        super_messy_hairstyle = jn_outfits.getWearable("jn_hair_super_messy").unlock()


        outfit_to_restore = Natsuki.getOutfitName()
        ahoge_outfit = jn_outfits.getOutfit("jn_ahoge_unlock")
        ahoge_outfit.headgear = random.choice(unlocked_ahoges)
        jn_outfits.saveTemporaryOutfit(ahoge_outfit)

    $ jnPause(5)
    n "Uuuuuu...{w=2}{nw}"
    extend " viejo..."
    $ jnPause(3)
    n "¡Es muy {i}temprano{/i} para estooo!"
    play audio chair_out_in
    $ jnPause(5)
    n "Ugh...{w=1}{nw}"
    extend " Tengo que irme a la cama más temprano..."
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    $ jn_events.displayVisuals("1uskeml")
    $ jn_globals.force_quit_enabled = True

    n 1uskemlesh "¿E-eh?{w=1}{nw}"
    extend 1uskwrl " ¡¿[player]?!{w=0.75}{nw}"
    extend 4klleml " ¡¿Ya estás aquí?!"
    n 4flrunl "..."
    n 4uskemfeexsbr "¡T-{w=0.3}tengo que arreglarme!"

    show natsuki 1fslunlsbr
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio clothing_ruffle
    $ Natsuki.setOutfit(jn_outfits.getOutfit(outfit_to_restore))
    show natsuki 2fsrpol
    $ jnPause(4)
    hide black with Dissolve(1)

    n 2fcsem "Cielos...{w=1.5}{nw}"
    extend 2nslpo " Realmente tengo que conseguir un despertador o algo.{w=1}{nw}"
    extend 2nsrss " Je."
    n 4flldv "Entonces...{w=1}{nw}"
    extend 3fcsbgl " ¿qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_renpy_for_dummies",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_renpy_for_dummies:
    $ jn_globals.force_quit_enabled = False

    n "..."

    play audio page_turn
    $ jnPause(2)

    n "Labels...{w=1.5}{nw}"
    extend " las labels existen como puntos de programa para ser llamados o saltados,{w=1.5}{nw}"
    extend " ya sea desde el script de Ren'Py,{w=0.3} funciones de Python,{w=0.3} o desde pantallas."
    n "..."
    $ jnPause(1)
    n "...¿Qué?"
    $ jnPause(1)

    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(2)

    n "..."
    n "Las labels pueden ser locales o globales...{w=1.5}{nw}"
    play audio page_turn
    extend " pueden transferir el control a una label usando la declaración de salto (jump)..."
    n "..."
    n "¡Ya veo!{w=1.5}{nw}"
    extend " Ya veo."
    $ jnPause(5)

    n "..."
    n "¡Sep!{w=1.5}{nw}"
    extend " ¡No tengo idea de lo que estoy haciendo!"
    n "No puedo creer que pensé que {i}esto{/i} me ayudaría...{w=1.5}{nw}"
    extend " '{i}galardonado{/i}',{w=0.2} según quién."
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_held"))
    $ jn_events.displayVisuals("1fcspo")
    $ jn_globals.force_quit_enabled = True

    n 1uskemesh "¡O-{w=0.3}oh!"
    extend 1fllbgl " ¡H-{w=0.3}hola,{w=0.2} [player]!"
    n 1ullss "Solo estaba...{w=1.5}{nw}"
    extend 1nslss " haciendo...{w=1.5}{nw}"
    n 1fsrun "..."
    n 1fcswr "¡N-{w=0.2}no importa eso!"
    extend 1fllpo " Este libro es basura de todos modos."

    show natsuki 1fcspo
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 4nslsr
    $ jnPause(4)
    hide black with Dissolve(1)

    n 4nllaj "Entonces...{w=1}{nw}"
    extend 2fchbgsbl " ¿qué hay de nuevo,{w=0.2} [player]?"

    return



init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_reading_a_la_mode",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_reading_a_la_mode:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ jnPause(5)

    n "Oh viejo...{w=1}{nw}"
    extend " este arte..."
    n "¡Es tan {i}{cps=7.5}bonito{/cps}{/i}!"
    n "¡¿Cómo demonios se vuelven tan buenos en esto?!"

    $ jnPause(3)
    play audio page_turn
    $ jnPause(5)

    n "¡Pffffft-!"
    n "¿Qué demonios es {i}eso{/i}?{w=1}{nw}"
    extend " ¡¿En qué estabas {i}pensando{/i}?!"
    n "¡Esto es {i}exactamente{/i} por lo que le dejas el diseño de atuendos a los profesionales!"

    $ jnPause(1)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    python:
        a_la_mode_manga = jn_desk_items.getDeskItem('jn_a_la_mode_manga_held')
        a_la_mode_manga.unlock()
        Natsuki.setDeskItem(a_la_mode_manga)
        jn_events.displayVisuals("1fdwca")
        jn_globals.force_quit_enabled = True

    n 1unmgslesu "¡Oh!{w=1}{nw}"
    extend 1fllbgl " ¡H-{w=0.2}hola,{w=0.2} [player]!"
    n 1nsrss "Solo estaba poniéndome al día con algo de lectura..."
    n 1fspaj "¿Quién hubiera adivinado que el recuentos de la vida y la moda van tan bien juntos?"
    n 1fchbg "¡Tengo que continuar este más tarde!{w=1}{nw}"
    extend 1fchsm " Solo voy a marcar mi lugar muy rápido,{w=0.2} un segundo..."

    show natsuki 1fcssm
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio page_turn
    $ jnPause(1.5)
    play audio drawer
    $ Natsuki.clearDesk()
    $ jnPause(4)
    hide black with Dissolve(1)

    n 3nchbg "¡Yyyyy estamos listos!{w=1}{nw}"
    extend 3fwlsm " ¿Qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_drinking_strawberry_milkshake",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_drinking_strawberry_milkshake:
    $ jn_globals.force_quit_enabled = False
    n "..."

    play audio straw_sip
    $ jnPause(3)

    n "Viejo...{w=1}{nw}"
    extend " ¡{i}qué rico{/i}!"

    play audio straw_sip
    $ jnPause(3)

    n "Wow,{w=0.3} extrañaba estos...{w=1}{nw}"
    extend " ¡¿por qué no pensé en esto antes?!"

    play audio straw_sip
    $ jnPause(2)
    play audio straw_sip
    $ jnPause(7)

    menu:
        "Entrar...":
            pass

    show prop strawberry_milkshake zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1nchdr")
    $ jn_globals.force_quit_enabled = True

    n 4nchdr "..."
    play audio straw_sip
    n 4nsqdr "..."
    n 4uskdrlesh "¡...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 2fbkwrl "¡[player_initial]-{w=0.3}[player]!{w=1}{nw}"
    extend 2flleml " Desearía que dejaras de simplemente {i}aparecer{/i} así..."
    n 1fcseml "Cielos...{w=1}{nw}"
    extend 4fsqpo " ¡casi haces que lo derrame!"
    n 4flrpo "Al menos deja que termine con esto..."

    show natsuki 2fcsdrl
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio glass_move
    hide prop strawberry_milkshake
    show natsuki 4ncssm
    $ jnPause(2)
    hide black with Dissolve(1)

    n 4ncsss "Ah..."
    n 1uchgn "¡Viejo,{w=0.2} eso dio en el clavo!"
    n 4fsqbg "Y ahora me siento más fresca...{w=1}{nw}"
    extend 3tsqsm " ¿qué hay de nuevo, [player]?{w=1}{nw}"
    extend 3fchsm " Jejeje."

    return



init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_step_by_step_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_step_by_step_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ jnPause(2)
    n "Demonios..."
    n "¡¿Quién {i}dibujo{/i} esto?!"
    n "¡Siento que voy a vomitar arcoíris o algo así!"
    $ jnPause(3)
    play audio page_turn
    $ jnPause(2)
    play audio page_turn
    $ jnPause(1)
    n "Vaya..."
    n "B-{w=0.3}bueno,{w=0.2} ¡ya basta de babear por el arte!{w=1.5}{nw}"
    extend " Te lo conseguiste por una razón,{w=0.2} Natsuki..."
    n "Paso a paso..."
    n "Mejorar mi confianza diaria,{w=0.3} ¿eh?{w=1.5}{nw}"
    extend " Bueeeno..."

    $ jnPause(1)
    play audio page_turn
    $ jnPause(5)
    play audio page_turn
    $ jnPause(7)

    menu:
        "Enter...":
            pass

    python:
        step_by_step_manga = jn_desk_items.getDeskItem('jn_step_by_step_manga_held')
        step_by_step_manga.unlock()
        Natsuki.setDeskItem(step_by_step_manga)
        jn_events.displayVisuals("1uskemfesh")
        jn_globals.force_quit_enabled = True

    n 1uskemesh "...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fpawrf "[player_initial]-{w=0.3}[player]!{w=0.2} ¡¿Otra vez?!{w=1}{nw}"
    extend 1fbkwrf " D-{w=0.3}do you really have to barge in like that {i}every{/i} time?"
    n 1flrunfess "Deminios...{w=1}{nw}"
    extend 1fsremfess " Te juro que uno de estos días vas a matarme del susto..."
    n 1fslpol "..."
    n 1tsqsll "...¿Eh?"
    n 1tnmpul "¿Qué?{w=0.2} ¿Tengo algo en la cara?"
    n 1tllpuleqm "..."
    n 1uskajlesu "¡A-{w=0.3}ah!{w=0.75}{nw}"
    extend 1fdwbgl " ¡El libro!"
    n 1fcsbglsbl "Yo solo..."
    n 1fllunl "Yo..."
    n 1fcsunf "Nnnnnn-!"
    n 1fcswrl "¡S-{w=0.2}solo me gusta el arte!{w=1}{nw}"
    extend 1fllemlsbl " ¡Eso es todo!"
    n 1fcswrl "¡Ya tengo {i}mucha{/i} confianza!"
    n 1fllunlsbl "..."
    n 1fcsemlsbr "Y-{w=0.2}y además,{w=1}{nw}"
    extend 1fllpol " Aunque {i}sí{/i} lo estuviera leyendo por lo de auto-{w=0.2}ayuda..."
    n 1kllsll "..."
    n 1kwmpul "...¿Que tendría de malo?"
    n 1fcsbol "Hace falta mucho valor para admitir ante ti misma que puedes hacerlo mejor.{w=1}{nw}"
    extend 1fnmbol " Que {i}puedes{/i} ser mejor."
    n 1fsrbol "...Y solo alguien realmente cruel se burlaría de alguien por intentarlo."
    n 1fcsajl "No lo olvides."

    show natsuki 1ccscal
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio drawer
    $ Natsuki.clearDesk()
    $ jnPause(1.3)
    show natsuki 2ccscal
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    n 4nllcal "..."
    n 4ullajl "Así que..."
    n 3tnmsslsbr "¿Qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_eyewear_problems",
            unlocked=True,
            conditional="persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_eyewear_problems:
    python:
        import copy
        import random

        jn_globals.force_quit_enabled = False


        unlocked_eyewear = [
            jn_outfits.getWearable("jn_eyewear_round_glasses_black"),
            jn_outfits.getWearable("jn_eyewear_round_glasses_red"),
            jn_outfits.getWearable("jn_eyewear_round_glasses_brown"),
            jn_outfits.getWearable("jn_eyewear_round_sunglasses"),
            jn_outfits.getWearable("jn_eyewear_rectangular_glasses_black"),
            jn_outfits.getWearable("jn_eyewear_rectangular_glasses_red"),
        ]
        for eyewear in unlocked_eyewear:
            eyewear.unlock()


        outfit_to_restore = Natsuki.getOutfitName()
        eyewear_outfit = copy.copy(jn_outfits.getOutfit(outfit_to_restore))
        eyewear_outfit.eyewear = jn_outfits.getWearable("jn_none")
        jn_outfits.saveTemporaryOutfit(eyewear_outfit)

    n "..."
    play audio drawer
    $ jnPause(2)

    n "Oh,{w=0.75}{nw}"
    extend " vamos!{w=1}{nw}"
    play audio stationary_rustle_c
    extend " ¡{i}Sé{/i} que los dejé aquí!"
    n "¡Simplemente lo sé!"

    $ jnPause(3)
    play audio drawer
    $ jnPause(2.25)
    play audio drawer
    $ jnPause(1.5)
    play audio stationary_rustle_a
    $ jnPause(0.5)

    n "¡Simplemente no lo entiendo!{w=1}{nw}"
    extend " ¡No es como si alguien {i}estuviera{/i} aquí para meterse con mis cosas!"
    n "Ugh...{w=1.25}{nw}"
    extend " {i}Sabía{/i} que no debí dejar que Sayori tomara prestado mi escritorio para todas las cosas del club..."
    n "Muuuuuy suave,{w=0.5} Natsuki..."

    $ jnPause(2.5)
    play audio paper_crumple
    $ jnPause(1)

    n "¿Y son estos...{w=1} {i}envoltorios de dulces{/i}?!"
    n "Es gracioso..."
    n "No recuerdo haber dicho que mi escritorio era una{w=0.2}{nw}"
    extend " {b}cesta{/b}{w=0.33}{nw}"
    extend " {b}de basura!{/b}"

    play audio gift_rustle
    $ jnPause(3.5)

    n "...Genial.{w=0.75} Y ahora mi cajón está todo pegajoso."
    n "Qué asco..."

    play audio paper_crumple
    $ jnPause(2.5)
    play audio paper_throw
    $ jnPause(3)

    n "Vamos..."

    play audio stationary_rustle_b
    $ jnPause(1.5)
    play audio stationary_rustle_c
    $ jnPause(1.75)
    play audio drawer

    n "¡Puedo...{w=0.5} apenas...{w=0.5} alcanzar la parte de atrás...!"
    play audio chair_in
    $ jnPause(1.5)
    n "¡Nnnnnng-!"

    $ jnPause(2)
    play audio gift_close
    $ jnPause(0.25)

    n "¡...!"
    n "¡¿E-están aquí?!{w=1}{nw}"
    extend " ¡Están aquí!"
    n "Viejo,{w=0.2} qué alivio..."
    n "..."
    play audio glasses_case_open
    n "...Me pregunto si todavía..."
    $ jnPause(3.5)

    menu:
        "Entrar...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_glasses_case"))
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_pre_slide
    $ jn_events.displayVisuals("1fcssmesi")
    $ jn_globals.force_quit_enabled = True

    n 1uskgsesu "¡...!"
    n 1ullajl "¡O-{w=0.2}oh!{w=1}{nw}"
    extend 4fllbglsbl " ¡[player]!"
    n 4fcssslsbl "Je."
    n 1fcsbglsbr "Bueno,{w=0.5}{nw}"
    extend 2fsqsglsbr " ¿no elegiste un buen momento para aparecer?"
    n 2fcssglsbr "..."
    n 2tsqsslsbr "...Entonces,{w=0.3} [player]?{w=1}{nw}"
    extend 4fchgnledzsbr " ¿Notas algo diferente?"
    n 1tsqsmledz "...¿Mmm?"
    n 2usqctleme "¿Ojo?{w=1}{nw}"
    extend 2fcsctl " ¿Qué es eso?"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down
    n 4tllbgl "¿Hice algo con mi cabello?{w=1}{nw}"
    extend 4fcssml " Jejeje."
    n 2nchgnleme "¡Nop!{w=0.5}{nw}"
    extend 2fcsbgl " Y-{w=0.75}{nw}"
    n 2nsqbol "..."

    show natsuki 1fsqbof zorder JN_NATSUKI_ZORDER at jn_center
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_readjust
    $ jnPause(1)

    n 4fcspol "..."
    n 4fcsemfsbl "¡Jum!"
    n 2fcsbglsbl "¡N-{w=0.2}nop!{w=0.75}{nw}"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down
    extend 1fchbglsbr " ¡N-no es mi cabello,{w=0.2} [player]!"
    n 2tsqsmlsbr "¿Qué más hiciste-{w=1}{nw}"
    n 1fsranlsbl "..."
    n 4fcsanf "¡Nnnnn...!"

    show natsuki 1fcsunf zorder JN_NATSUKI_ZORDER at jn_center
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_readjust
    $ jnPause(1.15)

    n 4fcsemlesi "..."
    n 2fcstrlsbr "¡Entonces!"
    show overlay slipping_glasses zorder JN_OVERLAY_ZORDER at jn_glasses_slide_down_faster
    extend 2fsqbglesssbr " ¿Qué más notaste-{w=1}{nw}"
    n 1fslanlsbl "¡Uuuuuuuuu-!"

    menu:
        "Natsuki...":
            pass

    n 1fbkwrlesssbl "¡Está bien!{w=0.75}{nw}"
    extend 4flrwrlesssbl " ¡Está bien!"
    n 2fcsgslsbr "¡Lo sé,{w=0.33} ¿ok?!"
    extend 2fsremlsbr " ¡Los lentes no me quedan bien!"
    n 2fslsrl "{i}Nunca{/i} lo han hecho."
    n 1ksrbol "Y pensar que desperdicié todo ese tiempo tratando de encontrarlos,{w=0.2} también..."
    n 4kcsemlesi "..."

    menu:
        "¡Creo que los lentes te quedan bien, Natsuki!":
            $ Natsuki.calculatedAffinityGain()
            if Natsuki.isEnamored(higher=True):
                n 1knmsll "..."
                n 4kllpul "...Realmente lo crees,{w=0.75}{nw}"
                extend 4knmpul " [player]?"
                n 1ksrunlsbl "..."
                n 1fcssslsbl "Je."
                n 1fsldvlsbr "...Entonces supongo que al menos eso no fue una pérdida de tiempo {i}total{/i}."
                n 2fcsajlsbr "No es que {i}no{/i} crea que me veo bien con ellos también,{w=0.5}{nw}"
                extend 2fcssmfsbl " o-obviamente."

            elif Natsuki.isAffectionate(higher=True):
                n 4uskemfeshsbl "...!{w=0.5}{nw}"
                n 2fcsgsfsbl "B-{w=0.3}bueno,{w=0.2} ¡claro que sí,{w=0.2} [player]!{w=1}{nw}"
                extend 2flrpolsbl " Yo los {i}elegí{/i},{w=0.2} d-después de todo."
                n 4ksrsllsbl "..."
            else:

                n 1fcsgslsbl "B-{w=0.2}bueno,{w=0.5}{nw}"
                extend 4fllgslsbl " ¡pues claro!"
                n 2fcsbglsbr "¡Por supuesto que me quedan bien,{w=0.2} [player]!"
                n 4fcsemlsbr "Digo,{w=0.75}{nw}"
                extend 2fllemlsbr " ¿No pensaste seriamente que elegiría algo que {i}no{/i} mostrara mi sentido del estilo,{w=0.75}{nw}"
                extend 2fnmpolsbr " ¿verdad?"
                n 1fcsemlsbl "Cielos..."
        "Sí, eso fue una pérdida de tiempo.":

            $ Natsuki.percentageAffinityLoss(2)
            if Natsuki.isAffectionate(higher=True):
                n 4fskemlesh "¡H-{w=0.3}hey!{w=1}{nw}"
                extend 1fsqwrl " ¿Y escucharte ser tan grosero {i}no lo es{/i}?"
                n 2flreml "Cielos..."
                n 2fsreml "{i}Alguien{/i} se levantó del lado equivocado de la cama..."
                n 2fsrsll "..."
            else:

                n 4fskwrlesh "¡H-{w=0.2}hey!{w=0.5}{nw}"
                extend 1fnmgsl " ¡¿Por qué fue eso?!"
                n 2fnmwrl "¿Y como si tú actuando como un imbécil {i}no lo fuera{/i}?"
                n 2fsrsllean "..."
        "...":

            n 1fllsll "..."
            n 4knmeml "...¿Qué?"
            extend 2fsqemlsbr " La actuación silenciosa {i}definitivamente{/i} no está ayudando,"
            extend 2fsrpolsbl " idiota..."

    n 1fcsajl "Bueno,{w=0.3} lo que sea.{w=1}{nw}"
    extend 2fllsll " Al menos sé dónde están ahora,"
    extend 2fslbol " supongo."
    n 1fcseml "...Y usarlos tan arriba así era tonto,{w=0.5}{nw}"
    extend 2fcspol " d-de todos modos."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)

    $ Natsuki.clearDesk()
    hide overlay
    $ Natsuki.setOutfit(jn_outfits.getOutfit(outfit_to_restore))
    show natsuki 1fcsbol zorder JN_NATSUKI_ZORDER at jn_center
    play audio glasses_case_close
    $ jnPause(0.75)
    play audio drawer
    $ jnPause(3)
    hide black with Dissolve(2)

    n 4nsrcal "..."
    n 4nsrajl "Yo...{w=0.75}{nw}"
    extend 1nsrsslsbl " supongo que debería disculparme por todo...{w=1.25}{nw}"
    extend 2nslsllsbl " eso."
    n 2nsrpolsbl "No estoy exactamente desplegando la alfombra roja aquí,{w=0.2} ¿verdad?{w=0.75}{nw}"
    extend 1nslsslsbl " Je."
    n 4fcsajlsbr "Y-y además."
    n 3fslsslsbr "Creo que ya es suficiente de ese{w=0.75}{nw}"
    extend 3fsqbglsbr " {i}espectáculo{/i},{w=1}{nw}"
    extend 3nsqbglsbr " ¿eh?"
    n 1nsrsslsbr "Entonces..."
    n 2kchsslesd "¿Q-qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_battery_dead",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_battery_dead:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_a
    n "..."
    n "...¡Ja!"
    play audio button_tap_b
    n "..."

    play audio button_mashing_b
    $ jnPause(3)
    play audio button_mashing_a

    n "¡Oh,{w=0.3} vamos!{w=1.25}{nw}"
    extend " ¡Como {i}si{/i} eso me hubiera golpeado!"
    play audio button_mashing_c

    $ jnPause(2)
    play audio button_mashing_b

    n "¡Nnnng-!"
    n "¡Q-quítate DE ENCIMA!{w=0.5}{nw}"
    extend " ¡Cielos!"
    play audio button_mashing_a
    n "¡ODIO a estos enemigos!"
    n "¡¿Tenían que añadir tantos?!"

    $ jnPause(3)
    play audio button_mashing_b

    n "¡Fuera de mi camino!{w=0.75}{nw}"
    play audio button_tap_b
    extend " ¡Está justo ahí!{w=0.75}{nw}"
    extend " ¡Estoy TAN {i}cerca{/i}!"
    play audio button_tap_ahg
    n "Vamos...{w=1}{nw}"
    play audio button_mashing_c
    extend " ¡{i}vamos{/i}...!"

    menu:
        "Entrar...":
            pass

    show prop wintendo_twitch_playing free zorder JN_PROP_ZORDER
    show natsuki gaming zorder JN_NATSUKI_ZORDER at jn_center
    $ jn_events.displayVisuals("1fdwfol")
    $ jn_globals.force_quit_enabled = True
    $ jnPause(3)

    n 1fdwanl "¡Nnnnnn...!"
    play audio button_mashing_a
    n 1fdwpoless "¡Uuuuuuu-!"
    n 1fdwfo "..."
    play audio button_mashing_c
    n 1fdwfoesssbl "¡Mmmmmm...!"

    show prop wintendo_twitch_held free zorder JN_PROP_ZORDER

    n 1uchbsedz "¡SÍ!{w=1.25}{nw}"
    extend 1uchgnedz " ¡FINALMENTE!"
    n 1kcsbgesisbl "Haah..."
    n 1fcsbgemesbr "¡Trágate {i}esa{/i}!"

    show prop wintendo_twitch_battery_low zorder JN_PROP_ZORDER

    n 1kcsssemesbr "..."
    n 1ksqsmsbl "...{w=0.75}{nw}"
    n 1uskemleshsbl "¡...!"
    n 1fllbglsbl "¡A-{w=0.2}ah!"
    extend 1fchbglsbr " ¡H-{w=0.2}hola,{w=0.2} [player]!"
    extend 1tchbglsbr " ¿Qué pasa?"
    n 1kcssssbl "Viejo..."
    n 1fsldvsbl "Disculpa,"
    extend 1fcsgssbl " ¡pero no tienes {i}IDEA{/i} de cuánto tiempo estuve tratando de superar ese nivel!"
    n 1fnmpol "¡En serio!"
    n 1fcsajl "Digo,{w=1}{nw}"
    extend 1fsrajlsbl " no es como si me estuviera {i}molestando{/i} o algo así..."
    n 1fcsbglsbr "Estoy {i}muy{/i} más allá de enojarme por juegos,{w=0.2} de todas las cosas."
    n 1fslbglsbr "T-tienen suerte de que elegí no ir con todo.{w=1}{nw}"
    extend 1fcsajlsbr " Eso es todo.{w=1}{nw}"
    extend 1nchgnl " Jejeje."
    n 1nchsmleme "..."
    n 1tnmbo "¿Eh?"
    extend 1klrbgesssbl " ¡Oh,{w=0.2} cierto!{w=0.75}{nw}"
    extend 1fchbgesssbr " ¡Lo siento!{w=0.75}{nw}"
    extend 1flrdvlsbr " Ya casi termino de todos modos."
    n 1ucssslsbr "Todo lo que tengo que hacer es guardar,{w=0.5}{nw}"

    show prop wintendo_twitch_dead zorder JN_PROP_ZORDER

    extend " y estaré justo-{w=1.25}{nw}"
    n 1udwssl "..."
    n 1ndwbo "..."
    n 1fdwem "...Pero yo..."
    n 1fdwwr "Y-yo solo...{w=0.5}{nw}"
    extend 1fdwun " cargué..."
    n 1fdwanl "..."
    n 1fcsful "..."
    n 1fcsunl "..."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    play audio chair_out_in
    $ jnPause(5)
    hide black with Dissolve(2)

    n 4ndtbo "..."
    n 4nslbo "..."
    n 4ndtca "..."
    n 2fdteml "Esto queda entre nosotros."
    n 2fsqfrlsbl "¿Entendido?"
    n 1nsrpolsbl "..."
    n 4nsrajlsbl "...Entonces.{w=1}{nw}"
    extend 2tsqsllsbl " ¿Qué hay de nuevo,{w=0.2} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_wintendo_twitch_game_over",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 14",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_wintendo_twitch_game_over:
    $ jn_globals.force_quit_enabled = False
    play audio button_mashing_b
    n "..."
    n "Jejeje..."
    play audio button_mashing_a
    n "Oh sí.{w=0.5} Ajá."

    play audio button_mashing_b
    $ jnPause(2)
    play audio button_mashing_a
    $ jnPause(2)

    n "¡Ugh!{w=0.5}{nw}"
    play audio button_mashing_c
    extend " ¡Levántate!{w=0.75} ¡LEVÁNTATE!"
    n "¡Contraataca,{w=0.2} idiota!"

    play audio button_mashing_b
    $ jnPause(1)

    n "¡Sí!{w=0.75} ¡De ESO estoy hablando!"
    play audio button_mashing_c
    n "¡Tres golpes!{w=0.5}{nw}"
    extend " ¡Cuatro golpes!{w=0.3}{nw}"
    extend " ¡Cinco golpes!"
    n "¡Estás en {i}racha{/i},{w=0.2} Natsuki!"

    play audio button_mashing_b
    $ jnPause(3)
    play audio button_mashing_a

    n "Oh viejo,{w=0.2} ¡estoy ARRASANDO!"
    play audio button_tap_b
    n "¡Sí!{w=0.75}{nw}"
    play audio button_tap_a
    extend " ¡Sí! ¡Vamos!"
    play audio button_mashing_c
    n "¡Solo unos golpes más...!"

    menu:
        "Entrar...":
            pass

    show prop wintendo_twitch_held charging zorder JN_PROP_ZORDER
    show natsuki gaming zorder JN_NATSUKI_ZORDER at jn_center
    $ jn_events.displayVisuals("1unmpu")
    $ jn_globals.force_quit_enabled = True
    $ jnPause(0.5)

    n 1unmemesu "¡...!"
    $ player_initial = jn_utils.getPlayerInitial()
    n 1fnmgs "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 1fllemlsbr " ¡¿C-cuántas veces tengo que decirte q-{w=0.25}{nw}"
    play audio twitch_die
    n 1nskemlsbr "...{w=0.5}{nw}"
    play audio twitch_you_lose
    n 1fdwemsbl "..."
    n 1fcsansbl "..."
    n 1fcsemsbl "Me.{w=0.75}{nw}"
    extend 1fcsfusbr " Estás.{w=0.75}{nw}"
    extend 1fbkwrleansbr " ¡BROMEANDO?!"
    $ player_final = jn_utils.getPlayerFinal(repeat_times=2)
    n 1kbkwrlsbr "[player][player_final]!{w=1}{nw}"
    extend 1fllgslsbr " ¡Vamos!"
    n 1fcswrlsbr "¡T-tú arruinaste totalmente mi ritmo!{w=0.75}{nw}"
    extend 1fsqpolsbl " ¡Gran idiota!"
    n 1kcsemesisbl "..."
    n 1kdwwr "¿...Y ahora tengo que hacer {i}todo eso{/i} de nuevo?{w=1}{nw}"
    extend 1kcspu " Viejo..."
    n 1fslsl "..."
    n 1flrtr "Supongo que haré eso después."
    n 1fsqcal "{b}De nuevo{/b}."
    n 1fcsajlsbl "Tienes suerte de que ya he hecho esa parte tantas veces,{w=0.2} [player].{w=0.75}{nw}"
    extend 1fcscalesm " Créeme."
    n 1ccspol "C-como si seriamente dejara que un contratiempo menor me molestara {i}tanto{/i}."

    show natsuki 1csrpol
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    hide prop
    play audio chair_out_in
    show natsuki 4nsrbol
    $ jnPause(5)
    hide black with Dissolve(2)

    n 4nsrcal "..."
    n 2nnmtrl "... Bueno,{w=0.2} [player].{w=0.75}{nw}"
    extend 2nsqtrl " Espero que estés abrochado."
    n 2nsrpol "...Porque ahora me debes el {i}doble{/i} de diversión hoy para compensar eso."
    n 4nsqbol "..."
    n 4fsqajl "¿... Bien?{w=0.75}{nw}"
    extend 3fcspolesi " ¡Ponte a ello entonces,{w=0.2} [player]!{w=0.75}{nw}"
    extend 3fsqsml " Jejeje."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_warm_package",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7 and persistent.jn_custom_outfits_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_warm_package:
    python:
        jn_globals.force_quit_enabled = False
        teddy_cardigan_outfit = jn_outfits.getOutfit("jn_cosy_cardigan_outfit")
        teddy_cardigan_outfit.unlock()
        Natsuki.setOutfit(teddy_cardigan_outfit)

    if jn_atmosphere.isCurrentWeatherRain() or jn_atmosphere.isCurrentWeatherThunder():
        n "..."
        n "¡Uuuuuuu-!"
        n "Tienes que estar bromeando."
        n "¡¿Lluvia?!{w=0.75} ¡¿Otra vez?!"
        n "¡Siempre se congela aquí cuando hace eso!{w=1} ¡Ni siquiera {i}tengo{/i} un radiador para encender!"
        $ jnPause(3)
        n "Ugh..."
        n "¿Sabes qué?{w=0.75} ¡Al diablo con esto!"
        play audio chair_out
        n "Alguien {i}tenía{/i} que haber dejado un abrigo o...{w=0.75} {i}algo{/i}{w=0.5} tirado por ahí..."
        $ jnPause(3)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "..."
        n "Cielos..."
        n "¿Cómo no es esto suficiente?{w=1} ¡Todavía me estoy congelando el trasero!"

        $ jnPause(3)
        play audio gift_slide
        $ jnPause(1)
        play audio gift_open

        n "Uuuuu..."
        n "Pensarías que la {i}estrella{/i} del club de debate al menos habría {i}intentado{/i} hablar para conseguirnos un club cálido."
        n "Apenas puedo sentir mis dedos de los pies..."

        $ jnPause(3)
        play audio gift_open

        n "¡...!"
        n "¡Oh viejo,{w=0.2} qué contenta estoy de verte {i}aquí{/i}!"
        n "...Espera.{w=1} ¿Cómo sobreviviste {i}tú{/i} estando en un salón con Sayori cerca...?"
        n "..."
        n "...No importa.{w=0.75} Demasiado frío para cuestionarlo.{w=1} Ahora dónde dejaron la tetera la última vez..."
        n "¡Ajá!{w=0.75} ¡Cierto!{w=0.3} Solo tengo que conectarla ahí,{w=0.2} y..."
        $ jnPause(2)

    elif jn_atmosphere.isCurrentWeatherSnow():
        n "..."
        n "¡Uuuuuuu...!"
        n "Como si estar atrapada aquí no fuera suficiente frialdad..."
        n "¡Ahora el {i}clima{/i} me está dando una!{w=1} ¡Literalmente!"
        n "¡Olvida la congelación!{w=0.3} ¡Se me está congelando el-{w=0.5}{i}trasero{/i}!{w=1} He tenido {i}suficiente{/i} de esto..."
        n "..."
        n "¡Oh, al diablo!{w=0.75} ¡Soy una chica de acción!"
        n "¡No tengo que aguantar esto!"

        play audio chair_out
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "Viejo...{w=0.75} {i}Realmente{/i} debí haber ordenado todo esto antes..."
        n "¡Mira toda esta basura!{w=0.75} Caray..."
        n "...Con razón todas mis cosas se seguían perdiendo aquí."
        $ jnPause(3)
        n "..."
        n "¡...!"
        n "¡¿C-cómo terminaste {i}tú{/i} aquí?{w=0.75} ¡Pensé que te habías ido para siempre!"

        play audio clothing_ruffle
        $ jnPause(3)

        n "Vamos...{w=0.75} qué más...{w=0.5} qué más..."
        n "..."
        n "Ugh...{w=1} ahora mis dedos están todos entumecidos..."

        $ jnPause(3)
        play audio gift_slide
        $ jnPause(2)

        n "...¿Eh?{w=0.75} ¿Qué tenemos aquí...?"
        play audio gift_open
        n "¡...!"
        n "¡PUNTUACIÓN!"
        n "Natsuki,{w=0.2} ¡lo has hecho de nuevo!"
        n "Bien...{w=1.25} ahora,{w=0.2} dónde puso ella la tetera..."
        play audio gift_slide
        $ jnPause(2)
        n "¡Ajá!{w=0.75} Ahí vamos.{w=1} Ven con mamá..."
    else:

        n "..."
        n "Ugh...{w=0.75} {i}En serio{/i} no puedo creer mi suerte a veces."
        n "De todos los lugares en los que podría haber estado atrapada {i}literalmente para siempre...{/i}"
        n "¡¿{i}Realmente{/i} tenía que ser el único salón {i}sin{/i} calefacción central?!"
        n "Vamos..."

        $ jnPause(3)

        n "...Espera."
        n "..."
        n "¿No lo hice...?{w=1} Estoy segura que lo hice..."

        play audio chair_out
        $ jnPause(3)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio clothing_ruffle

        n "Viejo,{w=0.2} honestamente olvidé cuánta basura hay aquí atrás..."
        n "No me extraña que el profesor se pusiera ansioso por mis libros."

        $ jnPause(2)
        play audio clothing_ruffle

        n "De Yuri...{w=0.75} De Yuri...{w=0.75} De Yuri..."
        play audio clothing_ruffle
        n "De Monika..."
        $ jnPause(2)
        play audio clothing_ruffle
        $ jnPause(3)
        n "..."
        n "...{b}Definitivamente{/b}{w=0.25} de Yuri."
        n "..."
        n "¡Ajá!{w=0.2} ¡Lo sabía!{w=1} ¡Tomen {i}eso{/i},{w=0.2} pautas del uniforme de la academia!"
        play audio clothing_ruffle
        $ jnPause(3)
        play audio gift_open
        n "...¿Eh?{w=0.2} ¿Y es esto...?"
        n "¡L-lo es!"
        n "Oh viejo...{w=1} ¡JACKPOT!{w=0.75} Jejeje."

    play audio switch_flip
    $ jnPause(2)
    play audio kettle_boil
    $ jnPause(5)
    play audio drink_pour
    $ jnPause(7)
    play audio chair_in
    $ jnPause(3)

    menu:
        "Entrar...":
            pass

    show prop hot_chocolate hot zorder JN_PROP_ZORDER
    $ jn_events.displayVisuals("1fsqbl")
    $ jn_globals.force_quit_enabled = True

    n 1kcsbsesi "Haah...{w=1.5}{nw}"
    extend 1fchsmedz " ¡perfecto!"
    n 2fcsbg "¿Quién {i}necesita{/i} calefacción cuando tienes chocolate caliente?"
    n 2fcssmlesisbl "¡{i}Y{/i} ni siquiera me quemé la lengua esta vez!"

    n 2ndwsm "..."
    n 2uwdgseex "¡...!"
    n 4fllbglsbl "B-{w=0.2}bueno,{w=0.75}{nw}"
    extend 2fcsbglsbl " ¡hola [player]!"
    n 2fllsmlsbl "..."
    n 2tsqsml "¿...?"
    n 2tsqctl "¿Ojo?"
    n 4nchts "¿Es eso una pizca de {i}celos{/i} lo que espío ahí,{w=0.2} [player]?{w=1}{nw}"
    extend 1fsqsmleme " Jejeje."
    n 2uchgn "Bueno,{w=0.2} ¡no puedo culparte!"
    n 2fllbg "Digo...{w=0.5}{nw}"
    extend 4fspgsedz " ¿has {i}visto{/i} esto justo aquí?"
    n 1ncsajsbl "...Y no,{w=0.5}{nw}"
    extend 2fslpo " no me importa cuán poco saludable sea."
    n 1fsqcaesi "{i}Siempre{/i} hago una excepción para el chocolate caliente."
    n 4fcstr "Además,{w=0.2} ya sabes lo que dicen."
    n 2fchgn "...A lo grande o a casa,{w=0.3} ¿verdad?{w=0.75}{nw}"
    extend 2fchsml " Jejeje."
    n 1fllgs "En serio,{w=0.2} ¡el chocolate caliente simplemente no {i}sería{/i} chocolate caliente sin {i}todos{/i} los extras!"
    n 2fcsgs "¿Crema?{w=0.3} ¡Listo!{w=0.3} ¿Malvaviscos?{w=0.3} ¡Listo!"
    n 2fsqcal "...¿Mi taza especial de panda?{w=1.25}{nw}"
    extend 4fcssml " ¡Listo de nuevo!"
    n 1fchbgl "¡Perfección!{w=0.75}{nw}"
    extend 2fcstsl " Si yo lo digo~."

    n 2ullss "Bueno,{w=0.5}{nw}"
    extend 4fsqss " por mucho que esté segura de que te {i}encantaría{/i} compartir esto conmigo,{w=0.2} [player]..."
    n 1fcscaesi "Hay algunas cosas que simplemente no puedo permitir.{w=0.75}{nw}"
    extend 1fsqsm " Jejeje."
    n 2fsqbg "¡Así que!{w=0.5} Prepárate."
    n 2fchbg "...¡Porque voy a compartir algunos consejos bastante {i}calientes{/i} de mi parte en su lugar!"
    n 4fsqbg "Así es,{w=0.2} [player].{w=1}{nw}"
    extend 2fchbledz " ¡Tienes asientos de primera fila para otra lección de tu servidora~!"
    n 1fcsaj "Como puedes ver,{w=0.75}{nw}"
    extend 2fcstr " no es exactamente difícil mantenerse agradable y tostado si sabes lo que estás haciendo..."
    n 2fchsm "...¡Y todo comienza con lo que usas!"
    n 4fllpu "Piénsalo como una pelea:{w=0.75}{nw}"
    extend 1flrem " el frío es tu oponente,{w=1}{nw}"
    extend 2fcspoesi " ¡y tu ropa es tu armadura!"

    n 2ullaj "Ahora -{w=0.2} obviamente,{w=0.2} querrás empezar con capas.{w=0.75}{nw}"
    extend 2nsrss " Probablemente ya sabías eso."
    n 1fnmgs "¡Pero eso no significa que debas ponerte {i}cualquier cosa{/i} que encuentres!"
    n 4fcspo "Realmente tienes que {i}pensar{/i} en qué es exactamente lo que te estás poniendo -{w=1}{nw}"
    extend 4unmaj " ¡como el material!"
    n 2fslaj "Si tu ropa no es transpirable,{w=0.75}{nw}"
    extend 2fsqpu " entonces terminarás todo pegajoso y sudoroso debajo de toda esa tela..."
    n 1fcsan "...¡Y la ropa mojada es inútil para mantener el calor adentro!"
    n 4ksqup "Lo último que quieres es estar congelado {i}y{/i} apestoso..."
    n 2fcsaj "Así que elige tus capas{w=0.75}{nw}"
    extend 2fslpu " -{w=0.5} y cuántas de ellas -{w=0.5}{nw}"
    extend 2fchsm " ¡sabiamente!"

    n 2fcsgs "Siguiente: ¡hazte de la ropa ajustada!"
    n 1nsqem "Realmente quieres cosas que te den al menos algún tipo de espacio entre tu piel y la tela."
    n 1ullaj "De esa manera,{w=0.2} todo el calor de tu cuerpo se queda atrapado a tu alrededor -{w=0.75}{nw}"
    extend 4fchgn " ¡como un pequeño escudo tostado!"
    n 4flrsl "Si solo usas algo como leggings,{w=0.5}{nw}"
    extend 1fsqsl " entonces todo ese calor va directo de tu cuerpo,{w=0.2} a la tela..."
    n 2fllem "...Y luego el aire simplemente lo arrebata,{w=0.2} ¡como un gorrón profesional!{w=0.75}{nw}"
    extend 2fcswr " ¡Qué desperdicio!"
    n 4fslss "Además,{w=0.2} a menos que seas un ciclista profesional o algo así,{w=1}{nw}"
    extend 2fsqss " dudo {i}mucho{/i} que necesites la aerodinámica..."
    n 2fchbg "Así que mantenla linda y holgada,{w=0.2} [player]!{w=0.75}{nw}"
    extend 4nchgn " ¡Pan comido!"

    n 4uwdaj "Oh -{w=0.5}{nw}"
    extend 1nllaj " cierto,{w=0.2} ¿y sobre todo?"
    n 1ncssr "..."
    n 2nsqaj "...Solo no seas tonto al salir,{w=0.2} ¿de acuerdo?"
    n 4nslss "Digo,{w=0.2} lo entiendo -{w=0.5}{nw}"
    extend 1ksqss " a veces simplemente tienes cosas que {i}necesitan{/i} hacerse allá afuera.{w=0.75}{nw}"
    extend 1ksrsm " Pasa.{w=1}{nw}"
    extend 4ksrsl " Pero..."
    n 4ksqbo "...Solo conoce tus límites.{w=0.5}{nw}"
    extend 1ksqpo " Caliéntate {i}adecuadamente{/i} si has pasado años en un clima de porquería,{w=0.5}{nw}"
    extend 1fslpo " o edificios viejos y desagradables..."
    n 2fcsaj "Refugio decente,{w=0.2} bebidas calientes,{w=0.5}{nw}"


    if Natsuki.isLove(higher=True):
        extend 2tslss " comida caliente..."
        n 1nsldvleafsbl "Un poco de tiempo de calidad con tu chica favorita..."
        n 4fchsmlsbl "¡T-todo cuenta!"

    elif Natsuki.isAffectionate(higher=True):
        extend 2tslss " comida caliente..."
        n 1fsrdvl "U-un poco de tiempo de calidad con cierto alguien..."
        n 4fcssslsbr "¡T-todo cuenta!"
    else:

        extend 2tslss " comida caliente...{w=0.5}{nw}"
        extend 4unmaj " ¡te sorprendería cuánto un poco de horneado puede subir el calor!"
        n 1fslslsbr "...Hablando por experiencia."
        n 1kslsl "..."
        n 2fcsbgsbr "¡P-pero sí!"

    show prop hot_chocolate cold

    n 2nchsm "¡Y eso más o menos {i}envuelve{/i} las cosas!{w=0.75}"
    extend 2nllss " Y-"
    n 1unmsf "..."
    n 4udwemeshsbl "¡...!"
    n 4uskemsbl "¡M-mi bebida!{w=1}{nw}"
    extend 4kbkwresssbr " ¡S-se está enfriando!{w=0.75}{nw}"

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1)
    hide prop hot_chocolate
    play audio straw_sip
    $ jnPause(2)
    play audio glass_move
    show natsuki 1kcsss zorder JN_NATSUKI_ZORDER at jn_center
    $ jnPause(3)
    hide black with Dissolve(2)

    n 1kcsbgesi "Haaah...{w=1.25}{nw}"
    extend 4nchtseme " ¡mucho mejor!"
    n 3fsqsm "Ahora que eso está fuera del camino,{w=0.2} [player]..."
    n 3usqbg "...¿Qué tal si calientas ese músculo conversacional tuyo?{w=1}{nw}"
    extend 1fsqsmeme " Jejeje."
    n 2tsqss "¿Bien?{w=0.75}{nw}"
    extend 2fchbl " ¡Estoy esperando!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_sanjo",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_sanjo:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Viejo...{w=1} ¿en serio no hay {i}nada más{/i} que hacer en este basurero?{w=0.75} ¡Estoy tan {b}aburrida{/b}!"
    n "¿Realmente les hubiera {i}matado{/i} mantener algunos juegos de mesa aquí o qué?"
    n "Ugh..."

    $ jnPause(5)

    n "..."
    n "¡Oh,{w=0.2} al diablo con esto!{w=0.75} Terminé de estar sentada.{w=0.75} {i}Otra vez{/i}."
    n "Tiene que haber algo que me perdí en el escritorio del profesor o...{w=1} algo..."

    play audio chair_out
    $ jnPause(3)

    n "..."

    play audio drawer
    $ jnPause(3)
    n "Huh.{w=0.75} ¿Desde cuándo los profesores guardan tanta papelería?{w=0.75} Genial."
    n "Estoy bastante segura de que a nadie le importaría si yo...{w=1} solo..."
    play audio stationary_rustle_c
    $ jnPause(0.75)
    n "Yoink."
    $ jnPause(3)

    n "Bien...{w=1} ahora qué tenemos aquí..."
    $ jnPause(2)

    n "Basura..."
    play audio stationary_rustle_a
    extend " más basura..."
    play audio stationary_rustle_b
    n "..."
    play audio paper_crumple
    n "¿Huh?{w=0.75} ¿Qué es...?"
    n "..."
    n "...¡Oh,{w=0.75} {i}iu{/i}!{w=0.75} ¡Q-{w=0.2}qué asco!"
    play audio paper_throw
    $ jnPause(2)
    n "N-{w=0.2}ni siquiera {i}quiero{/i} saber qué había en {i}eso{/i}..."
    n "Casi me hace vomitar."

    play audio drawer
    $ jnPause(4)

    n "..."
    n "...¿Huh?"
    n "Espera.{w=0.75} ¿Es eso...?"
    n "..."
    n "¡L-{w=0.2}lo es!{w=0.75} ¿Qué estás haciendo {i}tú{/i} todavía aquí?"
    n "...¿Y qué clase de idiota desconsiderado simplemente te dejó {i}ahí{/i}?"

    play audio gift_slide
    $ jnPause(1)
    play audio necklace_clip
    n "¡Ack!{w=0.5} ¡Mi dedo!{w=0.75} M-{w=0.2}me pinché..."
    $ jnPause(3)

    n "Viejo...{w=1} y estás todo asqueroso y crujiente ahora también."
    n "..."
    n "Está bien.{w=0.75} Supongo que mejor te arreglo todo..."

    $ jnPause(2)
    play audio drink_pour
    $ jnPause(2)
    play audio glasses_case_close
    $ jnPause(2)
    play audio chair_in
    $ jnPause(2)

    menu:
        "Entrar...":
            pass

    $ sanjo = jn_desk_items.getDeskItem("jn_sanjo")
    $ Natsuki.setDeskItem(sanjo)
    $ jn_events.displayVisuals("2fcssm")
    $ jn_globals.force_quit_enabled = True

    n 2fcssmeme "...{w=0.75}{nw}"
    n 2ccssm "...{w=0.75}{nw}"
    n 2tsqbo "...?{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 2unmgslesh "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fbkwrl " ¡Cielos!{w=0.75}{nw}"
    extend 4flrwrlsbl " ¿Desde cuándo llegaste {i}tú{/i} aquí?"
    n 4fsqemlsbl "¡¿Seriamente esperaste afuera del salón por todo ese tiempo?!{w=0.75}{nw}"
    extend 4csqfllsbl " ¿Cuánto tiempo estuviste siquiera {i}ahí{/i}?"
    n 4ccsemsbl "Ugh..."
    n 2flrflsbr "Realmente desearía que dejaras de hacer eso.{w=0.75}{nw}"
    extend 2fsqposbr " Gran tonto.{w=0.75}{nw}"
    extend 2ccsposbr " Ya deberías saber que odio que me asusten."
    n 4ccsemsbl "Y-{w=0.2}y de todos modos,{w=0.2} [player].{w=0.75}{nw}"
    extend 4cllaj " ¿No puedes ver que ya estoy {i}ocupada{/i} aquí?{w=0.75}{nw}"
    extend 3cslbo " Caray."

    if Natsuki.isEnamored(higher=True):
        n 4ccsfl "Digo,{w=0.75}{nw}"
        extend 5cllfll " no es que me importe {i}tanto{/i}.{w=0.75}{nw}"
        extend 3ccspolsbr " P-{w=0.2}pero aún así."
        n 3ccsajlsbr "Un poco de aviso hubiera sido lindo.{w=1}{nw}"
        extend 3nsrbolsbr " Eso es todo lo que digo."
    else:

        n 3ccstr "Hablando de desconsiderado.{w=0.75}{nw}"
        extend 3csrca " Al menos podrías darme algún tipo de aviso o algo la próxima vez."

    n 4csrbo "..."
    n 4tsqbo "..."
    n 2tnmfl "...¿Qué?{w=0.75}{nw}"
    extend 2cnmflsbl " ¿Cuál es el problema con {i}esa{/i} mirada,{w=0.5}{nw}"
    extend 2clrflsbl " tan de repente?"

    show natsuki option_wait_sulky
    menu:
        n "Si tienes algo que preguntar entonces solo dilo ya,{w=0.2} [player]."
        "¿Qué pasa con la planta, [n_name]?":

            n 1csqfl "...¿En serio,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2fsqem " '¿Qué pasa con la planta'?"
            n 4fllem "¿Y qué se supone exactamente que significa {i}eso{/i}?{w=0.75}{nw}"
            extend 4fnmaj " ¿Huh?"
            n 3fcsgs "¿Estás tratando de decir que necesita una {i}excusa{/i} para estar aquí o algo así?{w=0.75}{nw}"
            extend 3fcspo " Caray."
            n 1csrbo "Hablando de desplegar la alfombra roja."
            n 4ccsaj "Además."
            n 2fslfl "{i}'La planta'{/i} tiene un nombre,{w=0.5}{nw}"
            extend 2ccsaj " sabes."
            n 2cllbo "..."
            n 2cslbolsbl "..."
            n 5csqcalsbl "...Es Sanjo."
        "Parece que tú y la planta tienen algo en común...":

            n 4fsqfl "...Y-{w=0.2}y qué es exactamente {i}eso{/i},{w=0.5}{nw}"
            extend 4fsqem " [player]?"
            n 2fsqca "..."
            n 2fcsgs "No,{w=0.2} no.{w=0.75}{nw}"
            extend 4fnmaj " Continúa.{w=1}{nw}"
            extend 3fsqca " {i}Insisto{/i}."
            n 3fsqbo "..."
            n 3tsqfl "¿Bien?"
            n 3ccsss "No empieces a acobardarte ahora,{w=0.2} [player].{w=0.75}{nw}"
            extend 3ccsfl " ¡Escúpelo!"
            n 4csqfs "..."
            n 4fcsfs "Je.{w=0.75}{nw}"
            extend 2fcsfl " Sí."
            n 2fcspoesm "Eso es más o menos lo que Sanjo aquí y yo pensamos."
        "...":

            n 5csrunsbr "..."
            n 5csqemsbr "¿Q-{w=0.2}qué?{w=0.75}{nw}"
            extend 4ccsajsbr " No me mires así,{w=0.2} [player]."
            n 3ccsflsbr "Además."
            n 3ccsposbr "...Molestarás a Sanjo aquí."

    n 1ccsajlsbr "Y-{w=0.2}y no,{w=0.5}{nw}"
    extend 5cdlbosbr " no lo nombré yo misma."
    n 4tllpu "De hecho...{w=0.75}{nw}"
    extend 7tllbo " ahora que lo pienso.{w=1}{nw}"
    extend 7tnmfl " En realidad no sé {i}quién{/i} lo hizo."
    n 3unmaj "Uno de los profesores simplemente lo trajo un día y le dijo a la clase que lo cuidara.{w=0.75}{nw}"
    extend 3clrpu " Luego simplemente nunca se molestó en llevárselo de vuelta."
    n 3tlraj "Así que...{w=1}{nw}"
    extend 7tnmbo " Supongo que simplemente nos acostumbramos a tenerlo cerca,{w=0.2} supongo."
    n 4cslfl "...Aún así no explica por qué alguien simplemente decidió empujarlo debajo del escritorio del profesor.{w=0.75}{nw}"
    extend 4fslem " Idiotas."
    n 2ccsfl "Bueno,{w=0.2} lo que sea.{w=0.75}{nw}"
    extend 2ulrfl " Ha sido dejado por ahí el tiempo suficiente,{w=0.5}{nw}"
    extend 1fcstr " así que claramente {i}alguien{/i} va a tener que cuidar de Sanjo aquí."
    n 3fchgn "...¡Y quién mejor para asumir el reto que su servidora!"
    n 3fsqsm "Jejeje.{w=0.75}{nw}"
    extend 6fcsbg " ¡Sep!"
    n 3fcssmesm "¡Creo que ya es hora de que [n_name] finalmente ponga en marcha su pulgar verde!"
    n 4clrbgsbl "No me malinterpretes -{w=0.5}{nw}"
    extend 4csrsssbl " No estoy diciendo que vaya a ser una jardinera profesional o algo así.{w=0.75}{nw}"
    extend 7fcsss " Pero seamos realistas."
    n 7ullaj "Si vas a dedicarte un poco a la horticultura..."
    n 6fchbg "¿Dónde mejor para empezar que un cactus,{w=0.2} verdad?"
    n 4tlrss "Piénsalo,{w=0.2} [player] -{w=0.5}{nw}"
    extend 3fdlsm " este pequeñín estaba prácticamente {i}hecho{/i} para un principiante.{w=0.75}{nw}"
    extend 6fcsbg " ¡Básicamente ya se vale por sí mismo!"
    n 7ulraj "Además digo...{w=0.75}{nw}"
    extend 7unmbo " no es como si realmente tuviera que desviarme de mi camino para cuidarlo tampoco.{w=1}{nw}"
    extend 3cdlss " Creo que puedes adivinar por qué."
    n 1ullss "Un poco de luz solar aquí,{w=0.2} un par de chorritos de agua allá...{w=1}{nw}"
    extend 2fcsbg " ¿qué tan {i}difícil{/i} podría ser?"
    n 2fcssmesm "Jejeje."
    n 4fcsaj "¡Entonces!"
    n 2flrss "Mejor mantén tus ojos y oídos{w=0.5}{nw}"
    extend 2fsqss " {i}atentos{/i},{w=0.75}{nw}"
    extend 4fsqbg " [player]..."
    n 3nchgnl "¡Porque voy a hacer que Sanjo florezca antes de que te des cuenta!"

    $ sanjo.unlock()
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_house_of_cards",
            unlocked=True,
            conditional="persistent.jn_snap_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_house_of_cards:
    $ jn_globals.force_quit_enabled = False
    play audio card_place
    $ jnPause(5)
    n "Y...{w=1}{nw}"
    play audio card_place
    extend " ¡esa es otra!{w=1} ¡Sí!"
    n "Cielos...{w=1} ¿por qué no pensé en esto antes?{w=0.75} ¡Esto es en realidad {i}mucho{/i} más divertido de lo que pensé!"
    n "Jejeje."

    $ jnPause(1)
    play audio card_place
    $ jnPause(2)

    n "..."
    n "..."
    n "Nnnnnnnn..."
    n "..."
    play audio card_place
    $ jnPause(1.5)
    n "¡Sí!{w=0.75} Okey...{w=1.25} otra más..."
    n "Lo juro,{w=0.2} si este escritorio de porquería se tambalea de nuevo ahora..."

    $ jnPause(2)

    n "¡Mmmmm...!"
    n "..."
    play audio card_place
    $ jnPause(1.5)
    n "¡Bien!{w=0.75} Viejo...{w=1} ¡[n_name], estás en {i}racha{/i}!{w=0.75} ¡Esto es lo más lejos que he llegado!"
    $ jnPause(1)
    n "...C-{w=0.2}cierto.{w=0.75} Siguiente carta..."

    $ jnPause(1.5)
    play audio card_place
    $ jnPause(3)

    n "F-{w=0.2}fácil...{w=1} vamos...{w=1} no tires esta ahora..."
    n "..."
    n "Tan...{w=1.5} cerca..."
    play audio chair_in
    n "Solo tengo que...{w=1} equilibrarla...{w=1} bien...!"
    $ jnPause(1)

    menu:
        "Entrar...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_house_of_cards"))
    $ jn_events.displayVisuals("4fdwpusbr")
    $ jn_globals.force_quit_enabled = True

    n 4fdwfosbr "..."
    n 4tsqpueqmsbr "...?{w=0.75}{nw}"
    n 4uskemleshsbl "...!{w=0.75}{nw}"
    $ player_initial = jn_utils.getPlayerInitial()
    n 4fbkwrlsbr "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
    extend 4fllwrlsbr " ¡Cielos!{w=0.75}{nw}"
    extend 4fcsgslsbr " ¡¿C-{w=0.2}cuántas veces tengo que recordártelo?!"
    n 4ftlemlsbr "¡Juro que es como si realmente estuvieras {i}tratando{/i} de darme un ataque al corazón!{w=0.75}{nw}"
    extend 4fcsgssbr " ¡Vamos!\n{w=0.75}{nw}"
    extend 4csqemsbl "¿Es tocar {i}seriamente{/i} tan difícil?"
    n 2fcswrsbl "¡Y-{w=0.2}y además!{w=0.75}{nw}"
    extend 2fdwwrsbr " ¡Mira!{w=0.75}{nw}"
    extend 4fcsgssbr " ¿No puedes {i}ver{/i} que estoy claramente ocupada justo-{nw}"

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pile"))
    show natsuki 1uskemeexsbl
    play audio card_shuffle
    $ jnPause(1)
    show natsuki 1ndwflsbl
    $ jnPause(4)

    n 4ndwpusbl "...Ahora."
    show natsuki 1fdwbolsbl
    $ jnPause(2)
    show natsuki 1fdwunlsbl
    $ jnPause(3)
    n 1fsrunl "..."
    n 1fcsunl "..."
    n 1fcsfll "Me."
    n 1fcseml "Estás."
    n 4fcsanl "Jodidamente{w=1}{nw}"
    extend 4fbkwrl " ¡¿{i}BROMEANDO{/i}?!{w=0.75}{nw}"
    $ player_final = jn_utils.getPlayerFinal(3)
    extend 4knmwrl " ¡[player_initial]-[player][player_final]!"
    n 4fcsanl "¡Uuuuuu-!"
    n 4cbkwrless "¡T-{w=0.2}tú me desconcentraste completamente!{w=0.75}{nw}"
    extend 2fcsful " ¡No tienes {i}idea{/i} de cuánto me tomó llegar tan lejos!{w=0.75}{nw}"
    extend 4knmeml " ¡Y-{w=0.2}yo totalmente {i}tenía{/i}{w=0.5}{nw}"
    extend 4knmwrl " eeese!"
    n 1kdweml "¡...Y ahora tengo que hacerlo todo de nuevo!"
    n 1kcsflesi "..."
    n 1csrem "Viejo...{w=1.25}{nw}"
    extend 2csrsl " y ni siquiera pude tomar una foto ni nada."
    n 2fsrbo "..."
    n 2csqbo "..."
    n 2ccsfl "..."
    n 1ccsaj "...Olvídalo.{w=0.75}{nw}"
    extend 1fcswrlsbl " ¡Olvídalo!{w=1}{nw}"
    extend 4ftlfllsbl " Ni siquiera me importa ya."
    n 4ccsfllsbl "Esto fue una pérdida total de tiempo en primer lugar,{w=0.5}{nw}"
    extend 4cslsllsbl " d-{w=0.2}de todos modos."

    show natsuki 1ccscasbl
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(1)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    show natsuki 2cslsl
    $ jnPause(1)
    hide black with Dissolve(1.25)

    n 2cslbo "..."
    n 2csqbo "..."
    n 2ccspo "Hmph."
    n 2fcsfl "Bueno,{w=0.5}{nw}"
    extend 4cnmaj " Espero que sepas en lo que estás metido ahora,{w=0.2} [player]."
    n 5cllaj "Viendo cómo me debes a lo grande por arruinar mi ritmo y todo eso."
    n 3cllsl "..."
    n 3cnmem "¿Qué?{w=0.75}{nw}"
    extend 3ccsgs " ¡Hablo en serio!{w=1}{nw}"
    extend 4ccsposbl " No hay {i}manera{/i} de que te deje salir de esto {i}tan{/i} fácilmente."

    if Natsuki.isEnamored(higher=True):
        n 1ccssssbl "...Je.{w=0.75}{nw}"
        extend 2fcsflsbl " Y-{w=0.2}y además,{w=0.2} [player]."
        extend 2ccsaj " Ya has visto suficientes cartas por ahora."
        n 7ccsbgl "...A-{w=0.2}así que ¿no reconoces a una {i}reina{/i} cuando ves una?{w=0.75}{nw}"
        extend 5fsrdvl " Jejeje."
        n 3fsrfslsbl "..."
        n 3ccsajlsbr "¿Bien?{w=0.75}{nw}"
        extend 3cllbglsbr " Empieza ya,{w=0.2} [player].{w=0.75}{nw}"
        extend 4fsqsslsbr " ¿Después de {i}semejante{/i} metida de pata?"
        $ time_of_day = "today" if jn_is_day() else "tonight"
        n 3fcsbglsbr "¡M-{w=0.2}más te vale {i}creer{/i} que me vas a dar el tratamiento real [time_of_day]!"
        n 3fsqsmlsbr "Jejeje."
    else:

        n 1ccsss "...Je.{w=0.75}{nw}"
        extend 2ccsaj " Lo siento,{w=0.2} [player]."
        n 2flltr "Ya terminé con las cartas."
        extend 6fsqbg " ¡Pero compensarme por esto es solo la mano que te ha tocado!"
        n 3fcssm "Jejeje."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_blackjack_unlock",
            unlocked=True,
            conditional="persistent.jn_snap_unlocked",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_blackjack_unlock:
    $ jn_globals.force_quit_enabled = False
    $ jnPause(3)
    play audio laptop_close
    $ jnPause(2)
    n "...Muy bien.{w=0.75} Probemos esto.{w=0.75} {i}Otra vez{/i}."
    n "Tiene {i}que{/i} haber algunos resultados decentes esta vez..."
    $ jnPause(2)

    play audio keyboard
    n "Juegos de cartas...{w=1.75}{nw}"
    play audio keyboard
    extend " dos jugadores..."
    n "..."
    play audio button_tap_c
    extend "Buscar."
    $ jnPause(3)

    n "..."
    play audio keyboard
    n "...Juegos de cartas...{w=1} dos jugadores...{w=1.75}{nw}"
    play audio keyboard
    extend " {i}fácil{/i}."

    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(2)

    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(2)

    n "¡Oh,{w=0.2} por-!{w=0.5}{nw}"
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    $ jnPause(0.15)
    play audio button_tap_c
    extend " ¡Buscar!{w=0.75} Cielos..."
    n "¿Por qué esta cosa es tan {i}lenta{/i}?{w=0.75} ¿Cuál es siquiera el {i}punto{/i} de las actualizaciones si siempre empeoran las cosas?"
    n "Ugh...{w=1} con razón la escuela estaba literalmente regalando estos montones de chatarra."
    n "Estúpidos recortes presupuestarios."
    $ jnPause(3)
    n "...Finalmente.{w=0.75} {i}Ahora{/i} decides cargar."
    n "Por supuesto que tenían {i}que{/i} instalar el peor navegador que pudieron encontrar también."
    n "Dame un respiro."

    $ jnPause(1)
    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    $ jnPause(0.75)
    n "¡Uuuuuuuuu-!"
    n "Y-y por última vez,{w=0.2} ¡{b}no{/b} estoy buscando giros gratis!{w=0.75} ¡¿Por qué los resultados de búsqueda {i}apestan{/i} tanto ahora?!"
    n "¡Si {i}quisiera{/i} apostar todos mis ahorros,{w=0.2} ya lo habría {i}hecho{/i}!"
    n "Caray..."

    $ jnPause(2)
    play audio button_tap_c
    $ jnPause(2)
    play audio keyboard
    $ jnPause(3)
    play audio button_tap_c
    $ jnPause(1)

    n "¡Nnnnnn-!"
    n "¡Vamos!{w=0.75} ¡¿Por qué esto tiene que ser tan {i}difícil{/i}?!"
    n "¡Solo dame un juego que realmente pueda {i}jugar{/i} o lo juro,{w=0.2} voy a-!"
    n "..."
    n "...Huh."
    play audio button_tap_c
    $ jnPause(3)
    play audio button_tap_c
    $ jnPause(5)

    menu:
        "Entrar...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_laptop"))
    $ jn_events.displayVisuals("1ndwpu")
    $ jn_globals.force_quit_enabled = True


    n 1ndwpu "..."
    n 1fdwpu "..."
    n 1fdwbo "..."
    n 1tnmboeqm "...?{w=0.75}{nw}"
    n 1unmfllesh "¡A-{w=0.2}ah!{w=0.75}{nw}"
    extend 2ullemlsbr " ¡[player]!{w=0.75}{nw}"
    extend 2fcsgslsbr " ¡B-{w=0.2}bueno,{w=0.2} finalmente!"
    n 2fcsajlsbr "Seguro que te tomaste tu dulce tiempo para llegar aquí.{w=0.75}{nw}"
    extend 1csqcasbl " {i}Otra vez{/i}.{w=0.75}{nw}"
    extend 1tsqflsbl " ¿Estás {i}tratando{/i} de establecer algún tipo de récord de tardanza o qué?"
    n 1tllflsbl "En serio...{w=1}{nw}"
    extend 1nsqem " vas a dejar en vergüenza la tardanza de Sayori a este ritmo."
    n 1ncsflesi "..."
    n 1nlraj "Bueno,{w=0.2} de todos modos.{w=0.75}{nw}"
    extend 7fcsaj " Suerte para ti,{w=0.2} [player]."
    n 7fnmsl "Hay al menos {i}una{/i} cosa para la que llegaste a tiempo."
    n 3fsqsm "Jejeje."
    n 6fnmbg "...¡Porque finalmente encontré un nuevo juego que quiero probar!{w=0.75}{nw}"
    extend 3fchgn " ¡Incluso memoricé todas las reglas y todo!"
    n 1tsqbg "¿Y lo mejor de todo?"
    n 6fnmbg "¡Ni siquiera {i}necesitamos{/i} nada nuevo para jugarlo!"
    n 7fcscs "¡Sep!{w=0.75}{nw}"
    extend 7flrbg " No rebuscaré en ese viejo y apestoso armario hoy.\n{w=0.75}{nw}"
    extend 3fcssmesm " ¡Tengo todo lo que necesito justo aquí!"
    n 1fcsss "Je.{w=0.75}{nw}"
    extend 1tsqsm " ¿Y gracias a ti?{w=0.75}{nw}"
    extend 1fsqbg " ¡Eso incluye a un segundo jugador!"
    n 1fchsm "..."
    n 1tsqpu "¿Qué?"
    n 7unmaj "Oh,{w=0.2} cierto.{w=0.75}{nw}"
    extend 7nnmss " Probablemente te estés preguntando a qué viene todo este alboroto de repente,{w=0.5}{nw}"
    extend 7nlrss " huh."
    n 7ulraj "Entonces...{w=1}{nw}"

    if persistent._jn_snap_player_wins > 0 or persistent._jn_snap_natsuki_wins > 0:
        extend 7nllaj " Sé que hemos jugado un montón de Snap antes,{w=0.2} obviamente.{w=0.75}{nw}"
        extend 3unmfl " Y no me malinterpretes -{w=0.5}{nw}"
        extend 3clrflsbl " no estoy diciendo que me estuviera {i}aburriendo{/i} de él,{w=0.2} exactamente."
        n 1nsraj "Pero...{w=1}{nw}"
        extend 1clrfl " siempre sentí que le faltaba algo.{w=0.75}{nw}"
        extend 7tnmbo " ¿Sabes?"
    else:

        extend 7tlrbo " Estoy bastante segura de que mencioné Snap antes.{w=0.75}{nw}"
        extend 7tnmfl " ¿Ese juego de cartas donde tienes que gritar las cartas coincidentes para ganar?"
        n 3nllfl "...Incluso si nunca terminamos {i}jugándolo{/i} realmente,{w=0.5}{nw}"
        extend 3nslsl " por la razón que sea."
        n 3nllpu "Pero como...{w=1}{nw}"
        extend 7nsqcasbr " Supongo que está bien si lo único que realmente te importa en un juego son los tiempos de reacción."

    n 1fllaj "No diría exactamente que es un juego de {i}habilidad{/i} o algo así."
    n 1ccsss "Así que no es como si se necesitara algún tipo de cerebro maestro para descubrir qué falta aquí."
    n 3fsqsm "..."
    n 3tsqss "¿Qué?{w=0.75}{nw}"
    extend 3fnmsm " ¿No era obvio ya,{w=0.5}{nw}"
    extend 3fsqsm " [player]?"
    n 6fcsbg "...¡Algo de estrategia real!{w=0.75}{nw}"
    extend 6fchgn " ¡Duh!"
    n 1fnmbg "¿Y qué mejor manera de asegurarse de que realmente estás usando el cerebro que en un juego donde tienes que pensar por una vez en tus movimientos?"
    n 7fcsbg "¡Lo adivinaste!{w=0.75}{nw}"
    extend 1fsqbg " Estoy hablando de..."

    show natsuki 1fcssm
    $ jnPause(1)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_card_pack"))
    play audio smack
    $ jnPause(1.25)

    n 3fchbs "¡...Blackjack!"
    n 3fchsm "..."
    n 3fcssmeme "Jejeje."
    n 7ullss "Lo sé,{w=0.2} lo sé.{w=0.75}{nw}"
    extend 7ccsbgedz " Soy una genio,{w=0.2} ¿verdad?{w=0.75}{nw}"
    extend 6ccssm " Apuesto a que desearías haberlo pensado {i}tú{/i} antes,{w=0.2} ¿eh?"
    n 7ulraj "De hecho había escuchado sobre él hace un tiempo,{w=0.5}{nw}"
    extend 7clrsssbl " pero nunca pensé que fuera algo que realmente pudiera ser divertido de jugar.{w=0.75}{nw}"
    extend 3cslsssbl " Especialmente con solo dos jugadores."
    n 3tnmbo "Así que cuando estaba buscando algo más que hacer con el paquete de cartas,{w=0.2} supongo que simplemente se me vino a la mente."
    n 3tllss "Además.{w=0.75}{nw}"
    extend 1cslsssbr " {i}Dije{/i} que no sabía muchos juegos de cartas antes.{w=0.75}{nw}"
    extend 1ccsposbr " Estudiar sobre otro estaba claramente fuera de mis planes."
    n 7unmaj "En serio aunque -{w=0.5}{nw}"
    extend 3fchbg " ¡es perfecto!{w=0.75}{nw}"
    extend 3fspbg " ¡Y es {i}súper{/i} fácil de aprender también!"
    n 3ccsss "Confía en mí,{w=0.2} [player].{w=0.75}{nw}"
    extend 7tsqss " ¿Sale un par de rondas?"
    n 7tsrss "Bueno.{w=0.75}{nw}"
    extend 6ccssmesm " Seguirás perdiendo,{w=0.2} por supuesto.{w=0.75}{nw}"
    extend 3fchgnelg " ¡Pero al menos te divertirás mucho mientras lo haces!"
    n 1csqsm "..."
    n 1csqbg " ¿...Bien?{w=0.75}{nw}"
    extend 1unmbg " ¿Qué piensas al respecto,{w=0.2} [player]?{w=0.75}{nw}"
    extend 3fcsbg " ¡No mientas!"

    $ persistent._jn_blackjack_unlocked = True
    show natsuki option_wait_smug
    menu:
        n "Puedo decir que te estás {i}muriendo{/i} por empezar,{w=0.2} ¿verdad?"
        "¡Puedes apostar que sí!":

            n 1fcssm "Je.{w=0.75}{nw}"
            extend 7fcsbg " Justo como pensaba.{w=0.75}{nw}"
            extend 3fchgn " ¡Puedo leerte como un libro!"
            n 3unmaj "Oh -{w=0.5}{nw}"
            extend 3cdwss " déjame guardar esto muy rápido primero."

            show natsuki 1ccssmeme
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(1)
            play audio laptop_close
            $ jnPause(2)
            play audio drawer
            $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
            show natsuki 1cllsmeme
            $ jnPause(1)
            hide black with Dissolve(1)

            jump blackjack_explanation
        "Ahora no,{w=0.2} [n_name].":

            n 1ccssl "Je.{w=0.75}{nw}"
            extend 3clrfl " No digas más,{w=0.2} [player].{w=0.75}{nw}"
            extend 3clrsl " No digas más."
            n 3ccstr "{i}Totalmente{/i} lo entiendo."
            n 1csqbo "..."
            n 3fcsbg "...Totalmente entiendo que vendrás arrastrándote más tarde cuando finalmente te aburras,{w=0.2} eso es."
            n 3fsqsm "Jejeje."
            n 7ulrfl "Nah,{w=0.2} supongo que está bien.{w=0.75}{nw}"
            extend 3cnmbo " Como si fuera a obligarte a jugar o algo así.{w=0.75}{nw}"
            extend 3csrfll " No soy {i}tan{/i} exigente."
            n 1ullsl "Pero oye."
            extend 6nchgn " No es como si hubiera falta de tiempo para que empieces a aprender y perder más tarde,{w=0.2} ¿verdad?"

            show natsuki 1ccssmeme
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(2)
            play audio laptop_close
            $ jnPause(2)
            play audio drawer
            $ Natsuki.clearDesk()
            show natsuki 1cllsmeme
            $ jnPause(2)
            hide black with Dissolve(1)

            n 2cllss "Bueno,{w=0.2} ahora que eso finalmente está fuera del camino..."
            $ chosen_descriptor = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else player
            n 7fchbgl "¿Qué hay de nuevo,{w=0.2} [chosen_descriptor]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_internet_connection",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_internet_connection:
    $ jn_globals.force_quit_enabled = False
    $ jnPause(3)
    n "¡...Finalmente!{w=0.75} ¡Ya era hora de que cargara!"
    n "Cielos...{w=1} Juro que el sitio web tarda mucho más en cargar ahora..."
    n "Estúpidas políticas de red escolar."
    $ jnPause(2)
    n "Okey...{w=1} ¿Ahora dónde lo pausé la última vez...?"
    play audio button_tap_c
    n "..."
    play audio button_tap_c
    n "..."
    play audio button_tap_c
    n "¡Ajá!{w=0.75} ¡Aquí vamos!"
    play music anime_generic_theme loop
    $ jnPause(3)

    n "..."
    n "..."
    play audio anime_slash
    n "¡Ack!{w=0.75} ¡¿Qué demonios fue eso?!{w=0.75} ¡V-{w=0.2}vamos,{w=0.2} Minori!"
    n "¡A-{w=0.2}al diablo con las reglas!{w=0.75} ¡Defiéndete!"
    $ jnPause(3)

    play audio anime_punch
    $ jnPause(0.5)
    play audio anime_punch
    n "¡Oh,{w=0.2} por-!"
    n "¿Qué estás {i}haciendo{/i}?{w=0.75} ¡Deja de abrazarte con el suelo y levántate ya!"
    n "¡Como {i}si{/i} un aspirante sin nombre los tuviera a ambos en el suelo tan fácilmente!"
    n "Por favor..."
    $ jnPause(3)

    n "Caray...{w=1} ¡Suficiente con los monólogos internos!{w=0.75} ¡Tuviste un {i}episodio{/i} entero para dudar de ti misma!"
    n "Ugh..."
    n "Odio cuando lo alargan así.{w=0.75} Como si no {i}hubiera{/i} ya suficiente relleno en este episodio..."
    n "Dame un respiro."
    $ jnPause(3)

    play audio anime_punch
    $ jnPause(0.75)
    play audio anime_punch
    $ jnPause(0.25)
    play audio anime_punch
    n "¡Sí!{w=0.5} ¡Sí!{w=0.5} ¡Ahora de {i}eso{/i} es de lo que estoy hablando!{w=0.75}{nw}"
    play audio anime_punch
    extend " ¡Vamos!"
    $ jnPause(2)

    n "...!"
    play audio chair_out_fast
    $ jnPause(0.2)
    n "¡M-{w=0.2}Minori!{w=0.5}{nw}"
    play audio anime_slash
    extend " ¡MUEVETE!"
    n "Viejo..."
    n "¿Seriamente puedes esquivar {i}algo{/i} más lento?"
    $ jnPause(2)

    play audio anime_punch
    n "¡SÍ!"
    play audio anime_punch
    $ jnPause(0.25)
    play audio anime_punch
    n "¡Muéstrale,{w=0.2} Alice!{w=0.75}{nw}"
    play audio anime_punch 
    extend " ¡Patea su lamentable trasero-!"
    play audio chair_in
    $ jnPause(1)
    stop music
    $ jnPause(2)
    n "..."
    play audio button_tap_c
    n "...¿Huh?"

    play audio button_tap_c

    python:
        jnPause(1)
        for i in range(0, 7):
            renpy.play(filename=audio.button_tap_c, channel="audio")
            jnPause(0.2)

    n "...Oh,{w=0.5} tienes {w=0.3}{b}que{/b}{w=0.3} estar bromeando.{w=0.75}{nw}"
    play audio button_tap_c
    extend " ¡¿P-{w=0.2}por qué ahora?!"
    play audio button_tap_c
    $ jnPause(1)

    play audio button_tap_c
    $ jnPause(0.5)
    play audio button_tap_c
    $ jnPause(2)

    n "¡Nnnnn-!"
    n "¡¿Qué {i}pasa{/i} con el internet en este basurero?!{w=0.75} ¡En serio!"

    if jn_outfits.getOutfit("jn_cosy_cardigan_outfit").unlocked:
        n "Como si la calefacción rota no fuera suficiente dolor en el trasero.{w=0.75} ¿Ahora la conexión a internet también está fallando?"
    else:

        n "No me digas que la conexión a internet {i}ahora{/i} me está fallando..."

    n "¡Vamos,{w=0.2} pedazo de chatarra!{w=0.75} ¡Carga!{w=0.75}{nw}"
    play audio button_tap_c
    extend " ¡Carga!"

    play audio button_tap_c
    $ jnPause(0.5)
    play audio button_tap_c
    $ jnPause(1)

    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c
    $ jnPause(0.25)
    play audio button_tap_c

    n "¡Uuuuuuuu-!"
    n "¿N-{w=0.2}nada en este {w=0.2}{i}ESTÚPIDO{/i}{w=0.2} salón de clases funciona además de mí?"

    play audio button_tap_c
    $ jnPause(1)
    play audio button_tap_c
    $ jnPause(0.35)
    play audio button_tap_c

    menu:
        "Entrar...":
            pass

    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_laptop"))
    $ jn_events.displayVisuals("4fcsan")
    $ jn_globals.force_quit_enabled = True

    n 4fdwan "..."
    n 4fcsup "..."
    n 4csqemeqm "...?{w=0.75}{nw}"
    n 4unmflleshsbl "¡A-{w=0.2}ah!{w=0.75}{nw}"
    extend 3flrgslsbl " ¡[player]!{w=0.75}{nw}"
    extend 3fcswrlsbl " ¡¿P-{w=0.2}puedes {i}creer{/i}{w=0.2} esta basura?!"
    n 1fslanl "No sé si es esta laptop antigua o qué,{w=0.5}{nw}"
    extend 4fcsanl " ¡pero la conexión aquí absolutamente {b}apesta{/b}!"
    n 4flreml "En serio -{w=0.5}{nw}"
    extend 4fbkwrl " ¡me está volviendo loca!"
    extend 2fcsanl " ¡Esta es como la tercera vez esta semana que muere totalmente conmigo!"
    n 2fcsgs "¿Por qué es la única vez que realmente estoy de humor para sentarme y ver algo,{w=0.5}{nw}"
    extend 2fsrem " decide que quiere tartamudear más que Yuri intentando hacer stand-up?"
    n 1fcsflesi "Ugh..."
    n 2fslfl "Qué chiste.{w=0.75}{nw}"
    extend 2fslbo " Juro que nunca fue tan malo antes también."

    if Natsuki.isEnamored(higher=True):
        n 2csraj "No has estado jugando con la conexión a internet o algo así,{w=0.5}{nw}"
        extend 2csqpo " ¿verdad [player]?"
    else:

        n 2fsqfl "Más te vale no haber estado jugando con la conexión a internet o algo así a propósito,{w=0.5}{nw}"
        extend 2fsrca " [player]."

    n 2ccsemesi "..."
    n 4ccsaj "L-{w=0.2}lo que sea.{w=0.75}{nw}"
    extend 3cllfl " No es como si no pudiera intentar transmitirlo de nuevo más tarde.{w=0.75}{nw}"
    extend 3fslfl " {i}Supongo{/i}."
    n 7fcsfl "Además.{w=0.75}{nw}"
    extend 7fcstrsbr " Todo el mundo sabe que los finales de temporada siempre están sobrevalorados,{w=0.2} d-{w=0.2}de todos modos."

    show natsuki 4fcscasbr
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    play audio laptop_close
    $ jnPause(0.75)
    play audio drawer
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    $ jnPause(1.3)
    show natsuki 3ccsbo
    hide black with Dissolve(0.5)
    $ jnPause(0.5)

    n 3clrbo "..."
    n 3csraj "...Tengo que admitirlo.{w=0.75}{nw}"
    extend 3csrsl " Estaría mintiendo si dijera que no estaba al menos un poco molesta por eso.{w=0.75}{nw}"
    n 4cdrem "Hablando de una decepción."
    n 4csqfl "Especialmente con el tiempo que estuve esperando a que saliera el episodio también."
    n 2cllbo "..."
    n 2cllaj "Pero...{w=1}{nw}"
    extend 2ccstr " Te diré una cosa sin embargo,{w=0.2} [player]."
    n 4ccsss "Te estás engañando a ti mismo si piensas seriamente que voy a dejar que {w=0.2}{i}eso{/i}{w=0.2} de todas las cosas me deprima."

    if Natsuki.isEnamored(higher=True):
        n 4ccsbg "Después de todo..."
        n 7ccsbgl "A-{w=0.2}al menos hay {i}una{/i} conexión aquí en la que siempre puedo confiar,{w=0.2} ¿verdad?{w=0.75}{nw}"
        extend 3fsqsml " Jejeje."
        n 5fchbgl "B-{w=0.2}bienvenido de nuevo,{w=0.5}{nw}"
        $ chosen_tease = jn_utils.getRandomTease()
        extend 5fchgnl " ¡[chosen_tease]!"

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 2fchbll "¡Siéntete como en casa ya,{w=0.2} [chosen_endearment]!"
        else:

            n 2nchgnl "¡Ponte cómodo ya!"
    else:

        n 7ccsbgl "D-{w=0.2}después de todo..."
        n 7fsqbgl "Parece que todavía hay {i}una{/i} conexión aquí que no me va a fallar.{w=0.75}{nw}"
        extend 3fcsbgsbr " Como si siquiera tuvieras opción."
        n 3fcssmsbr "Jejeje."
        n 3fchbg "¡Bienvenido de nuevo,{w=0.2} [player]!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_change_of_atmosphere",
            unlocked=True,
            conditional="persistent._jn_player_allow_legacy_music_switch_event",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_change_of_atmosphere:
    $ jn_globals.force_quit_enabled = False
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_RAIN)
    $ jn_atmosphere.SOUND_EFFECTS_RAIN.start()

    if jn_is_day():
        show overlay puddles day zorder JN_OVERLAY_ZORDER
    else:

        show overlay puddles night zorder JN_OVERLAY_ZORDER

    $ jn_outfits.getWearable("jn_clothes_raincoat").unlock()
    $ jn_outfits.getWearable("jn_headgear_raincoat_hood").unlock()
    $ jn_outfits.saveTemporaryOutfit(jn_outfits.getOutfit("jn_raincoat_unlock"))

    n "..."
    n "Mmmmmmnnn..."
    n "...¿Uh?"
    $ jnPause(3)

    n "Uuuuuu...{w=2} mi cabeza..."
    n "¿Qué hora es,{w=0.2} siquiera...?{w=2} ¿C-{w=0.2}cuánto tiempo estuve {i}fuera{/i}?"
    $ jnPause(2)
    n "Viejo...{w=2}{nw}"

    if jn_utils.getMinutesSinceLastVisit() > 60:
        extend " {i}Sabía{/i} que tratar de dormir un poco en mi escritorio no iba a funcionar..."
    else:

        extend " {i}Sabía{/i} que tratar de tomar una siesta en mi escritorio era una idea {i}estúpida{/i}..."

    n "Ugh."
    $ jnPause(3)

    n "Y estas sillas de madera rotas...{w=1} ¿En serio les hubiera matado conseguir muebles que fueran realmente cómodos o qué?"
    n "Caray...{w=1} No es como si no {i}fuéramos{/i} a estar sentados aquí sobre nuestros traseros por horas."
    n "Mi espalda me está {w=0.5}{i}matando{/i}..."

    $ jnPause(3)
    play audio chair_out_slow
    n "Tengo que despertar...{w=1} Tengo que despertar..."
    n "Ugh...{w=1} ¡Piensa,{w=0.2} [n_name]!{w=0.75} Tiene que haber algo de café o algo por aquí en algún luga-{nw}"
    play audio puddle_step_a
    $ jnPause(1)

    n "¡A-{w=0.2}ack!{w=0.2} ¡Está todo mojado!{w=0.75} ¡¿Qué demonios...?! "
    $ jnPause(1)
    play audio drip_a
    $ jnPause(0.25)
    play audio drip_b

    n "..."
    n "¿Es eso...{w=1} {i}agua de lluvia{/i}...?{w=0.75} Oh,{w=0.2} tienes {w=0.2}{b}que{/b}{w=0.2} estar bromeando.{w=0.75} ¡¿En serio?!{w=0.75} ¡¿Por qué ahora?!"
    n "¿Quién construyó siquiera esta escuela de porquería?{w=0.75} ¡¿El {i}club de carpintería{/i}?!"
    $ jnPause(2)

    n "No...{w=1} No me digas."
    n "..."
    play audio puddle_step_a
    $ jnPause(0.5)
    play audio puddle_step_b
    $ jnPause(0.25)
    n "¡Uuuuuuu-!"
    n "¡Está por {i}todas partes{/i}!{w=0.75} ¡Incluso el escritorio del profesor está goteando ahora!"
    n "...Qué asco.{w=1} {i}Y{/i} mis pantuflas están todas empapadas ahora,{w=0.2} también..."
    n "Grandioso.{w=1} Simplemente {i}perfecto{/i}."
    play audio drip_b
    n "Totalmente necesitaba todo esto en mi vida ahora mismo."
    n "...{i}No{/i}."
    $ jnPause(2)

    n "..."
    n "Vamos..."
    $ time_of_day = "day" if jn_is_day() else "night"
    n "¿Dónde dejaron esa estúpida cubeta?{w=0.75} ¡{i}Sé{/i} que tenían una aquí!\n{w=0.75}Tuve que pararme afuera con ella suficientes veces..."
    play audio drip_a
    n "¿Podría este [time_of_day] {i}posiblemente{/i} ponerse peor-{nw}"

    play audio metal_clang
    n "¡A-{w=0.2}auch!{w=0.2} ¡¿Quién demonios-?!{nw}"
    $ jnPause(0.25)
    play audio water_splash
    $ jnPause(1)
    play audio drip_a
    $ jnPause(2)
    play audio drip_b

    n "..."
    play audio drip_a
    n "..."
    n "..."
    play audio chair_in
    $ jnPause(2)
    play audio drip_a
    $ jnPause(1)

    menu:
        "Entrar...":
            pass

    if preferences.get_volume("music") == 0:
        $ preferences.set_volume("music", 0.75)

    $ jn_events.displayVisuals(natsuki_sprite_code="2fslsr", bgm="mod_assets/bgm/just_natsuki.ogg")
    show screen weather_raindrops
    $ jn_globals.force_quit_enabled = True
    $ jnPause(1)
    show natsuki 2fcssr
    $ jnPause(0.1)
    show natsuki 2fslsr
    $ jnPause(2)
    show natsuki 2fcssr
    $ jnPause(0.3)
    show natsuki 2fslsr
    $ jnPause(0.1)
    show natsuki 2fcssr
    $ jnPause(0.1)
    show natsuki 2fslsr
    $ jnPause(2)

    if Natsuki.isEnamored(higher=True):
        n 2fsrsl "..."
        n 2csqpueqm "...¿Huh?{w=0.75}{nw}"
        extend 2cllpul " Oh."
        n 4cslssl "...Je.{w=0.75}{nw}"
        extend 4ccsfllsbr " [player].{w=0.75}{nw}"
        extend 3csqfllsbr " Realmente tienes un don para elegir los peores momentos para aparecer a veces."
        n 3clrsllsbr "{i}Sabes{/i} eso...{w=1}{nw}"
        extend 5csgcalsbr " ¿Verdad?"

    elif Natsuki.isHappy(higher=True):
        n 2fsrsl "..."
        n 2tsgpueqm "...¿Huh?{w=0.75}{nw}"
        $ player_initial = jn_utils.getPlayerInitial()
        extend 4unmemlesh " ¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 4cllemlsbl " ¡¿Cuándo llegaste aquí,{w=0.2} tan de repente?!"
        n 3ccsgslsbl "...¿Y seriamente tenías que elegir {i}ahora{/i} de todos los momentos para aparecer?{w=0.75}{nw}"
        extend 3csrfllsbl " Cielos..."
    else:

        n 2fsrsl "..."
        n 2tsqpueqm "...¿Huh?{w=0.75}{nw}"
        extend 1cllfllsbr " Oh.{w=0.2} [player]."
        n 1fcsflesisbr "..."
        n 4ftlem "Por supuesto que elegirías ahora de todos los momentos para decidir aparecer,{w=0.2} también.{w=0.75}{nw}"
        extend 4fslfl " Asombroso."

    n 4fslsl "..."
    n 4csqfl "...Sí.{w=0.75}{nw}"
    extend 2flrem " Como probablemente puedes notar.{w=0.75}{nw}"
    extend 2fcsan " No me he estado exactamente {i}divirtiendo{/i} aquí."
    n 2ftrem "{i}'¡Salones de clase nuevos!'{/i},{w=0.5}{nw}"
    extend 4fsran " si como no."
    n 7fcsem "Como...{w=0.3} Siempre fueron bastante pésimos.{w=0.75}{nw}"
    extend 3fslsl " Pero juro que nunca fue {i}tan{/i} malo antes."
    n 4cnmwrl "¡No,{w=0.2} de verdad!{w=0.75}{nw}"
    extend 3fcswrsbr " ¡Hablo en serio aquí,{w=0.2} [player]!"

    if get_topic("event_warm_package").shown_count > 0:
        n 3fcsflsbr "Y-{w=0.2}yo sé que dije que la calefacción estaba totalmente rota aquí ya.{w=0.75}{nw}"
        extend 1clrwrsbr " ¡Pero nunca estuvo realmente {i}goteando{/i} por todas partes ni nada!{w=0.75}{nw}"
        extend 2csrunsbr " Al menos no tanto."
    else:

        n 3fcsgssbr "Cosas como la calefacción o los gabinetes aquí siempre estuvieron bastante rotos.{w=0.75}{nw}"
        extend 1clrwrsbl " ¡N-{w=0.2}nunca fue como si estuviéramos sentados empapados ni nada!"
        n 2cslemsbr "...O al menos no tan mal como {i}esto{/i}."

    n 2cupemsbr "Nunca pensé que necesitaría usar esta cosa estúpida en {i}interiores{/i} de todos los lugares.{w=0.75}{nw}"
    extend 2fcsemsbr " Qué chiste."
    n 2cslsl "..."
    n 4cslaj "Y en realidad.{w=0.75}{nw}"
    extend 4cllflsbr " A-{w=0.2}ahora que lo pienso."
    n 7clrfllsbr "Si este lugar ni siquiera puede mantener el {i}clima{/i} fuera ya,{w=0.2} entonces..."
    n 7csrunlsbr "..."
    n 3ccsemlsbr "Sí,{w=0.2} no.{w=0.75}{nw}"
    extend 3cllemlsbr " Realmente no quiero pensar en eso ahora."
    n 1kcsflesi "..."
    n 1ksrfl "Viejo..."
    n 2csrsl "Y como si no hubiera tenidog suficiente..{w=0.75}{nw}"
    extend 2csrfl " Ahora tengo que recordar secar este basurero más tarde también.{w=0.75}{nw}"
    extend 2ftrem " Genial."
    n 4knmwr "¡Ni siquiera sé si hay un trapeador por aquí ya!{w=0.75}{nw}"
    extend 4fllem " Apuesto a que pensaron que esos eran {i}demasiado caros{/i} también..."
    n 2fllsl "..."
    n 2fslan "..."
    n 4fcsan "¡Uuuuuuu...!"
    n 4fllem "¿Y mataría a este lugar poner algo de música diferente por una vez?{w=0.75}{nw}"
    extend 4fsqan " Ni siquiera sé cuánto tiempo he estado escuchando la misma canción ahora."
    n 3fcsup "Bueno,{w=0.2} noticia de última hora:{w=0.5}{nw}"
    extend 3fbkwr " ¡Estoy harta de ella!{w=0.75}{nw}"
    extend 4flrfu " ¡Es como si todo se estuviera juntando solo para colmar mi paciencia!"
    n 1fcsfu "Me siento como basura,{w=0.5}{nw}"
    extend 2fsran " se está {i}congelando{/i} siempre..."
    n 2fllan "Todas mis cosas están totalmente empapadas..."
    n 1fsqan "Y esa {i}música{/i}..."

    show natsuki 1fsqun
    $ jnPause(2)
    show natsuki 2fcsun
    $ jnPause(2)
    show natsuki 4fcsup

    n 1fcsan "¡Nnnnnnnn-!"
    n 1fcsupl "Solo...."
    n 2fsrupl "En serio..."
    n 1fcsupl "¿Por qué este basurero no puede simplemente{w=0.75}{nw}"
    extend 4fcsanl " ¡YA!{w=0.75}{nw}"
    extend 4fcsful " ¡PARAR!{w=0.75}{nw}"
    extend 4fbkwrlean " ¡CON ESTO!"

    show natsuki 4fcsunl
    stop music fadeout 1
    hide screen weather_raindrops
    $ jn_atmosphere.SOUND_EFFECTS_RAIN.stop()
    show overlay puddles zorder JN_OVERLAY_ZORDER at JN_TRANSFORM_FADE_OUT(4)
    $ jnPause(0.5)
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_SUNNY)
    $ jnPause(1)
    show natsuki 4ulrbol

    n 1nlrbol "..."
    n 1clrbol "..."
    n 2clrflsbl "Yo...{w=1}{nw}"
    extend 2csrflsbl " todavía no tengo idea de cómo hice eso la primera vez.{w=1.5}{nw}"
    extend 1csrslsbl " Huh."
    n 3ccsfllsbr "B-{w=0.2}bueno,{w=0.2} al menos eso es la lluvia resuelta."
    n 3ccssslsbr "Je.{w=0.75}{nw}"
    extend 3nchgn " ¡Supongo que no tengo que trapear después de todo!"
    n 7ccsbg "Ahora,{w=0.2} si la música pudiera darse prisa y captar el mensaje también..."

    show natsuki 7ccssm
    $ jnPause(3)
    show natsuki 3csqsr
    $ jnPause(2)
    hide overlay

    n 1ccsemesi "..."
    n 4ccsem "Dije,{w=0.5}{nw}"
    extend 4fsrfl " ¡ahora si la música pudiera simplemente {i}cambiar{/i} ya!"

    show natsuki 2fsrsr
    $ jnPause(2)
    show natsuki 2fsrun
    $ jnPause(2)
    show natsuki 2fcsun
    $ jnPause(2)

    n 1fllem "¡Oh,{w=0.2} por-!{w=0.75}{nw}"
    extend 2fcswr " ¡¿Es esto una broma?!{w=0.75}{nw}"
    extend 2fllem " ¡¿Fue eso una cosa de una sola vez?!"
    n 4fbkwr "¡Qué tengo que hacer para tener un poco de atmósfera por aqu-!{nw}"
    $ renpy.play(filename=jn_custom_music.getMusicFileRelativePath(file_name=main_background.location.getCurrentTheme(), is_custom=False), channel="music")
    $ jnPause(0.2)
    show natsuki 4unmpul
    $ jnPause(1.5)
    n 4nlrpulsbl "...Toma."
    $ jnPause(2)
    show natsuki 1nlrsllsbl

    n 3ccssslsbr "Je.{w=0.75}{nw}"
    extend 3ccsbglsbr " ¡S-{w=0.2}sí!{w=0.75}{nw}"
    extend 7fchbg " ¡Ahora de {i}eso{/i} es de lo que estoy hablando!{w=0.75}{nw}"
    extend 4fnmgsedz " ¡Algo de maldita música real por una vez!"
    n 3fcsbgsbl "Y-{w=0.2}y hablando de cambiar melodías..."
    $ time_of_day = "today" if jn_is_day() else "tonight"

    if Natsuki.isAffectionate(higher=True):
        n 7fsqbgl "¿Qué tal si {i}finalmente{/i} empezamos [time_of_day] por el buen camino también ahora,{w=0.2} eh?\n{w=0.75}{nw}"
        extend 3fcssml " E-{w=0.2}ehehe."
        n 4fllssl "Solo déjame deshacerme del impermeable muy rápido..."
        show natsuki 4fcssml
    else:

        n 3fsqbg "¡Ya era hora de que finalmente volviéramos al buen camino!{w=0.75}{nw}"
        extend 3fcssm " Jejeje."
        n 1unmbo "Oh, cierto."
        extend 4clrsssbl " Solo voy a tirar esta cosa muy rápido..."
        show natsuki 4ccssm

    $ jnPause(0.1)
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(0.5)
    show natsuki 2fcssmeme
    $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
    play audio zipper
    $ jnPause(1)
    play audio clothing_ruffle

    if persistent.jn_natsuki_auto_outfit_change_enabled or persistent.jn_natsuki_outfit_on_quit == "jn_temporary_outfit":
        $ Natsuki.setOutfit(jn_outfits.getRealtimeOutfit())

    elif jn_outfits.outfitExists(persistent.jn_natsuki_outfit_on_quit):
        $ Natsuki.setOutfit(jn_outfits.getOutfit(persistent.jn_natsuki_outfit_on_quit))
    else:

        $ Natsuki.setOutfit(jn_outfits.getOutfit("jn_school_uniform"))

    $ jnPause(1.5)
    hide black with Dissolve(0.5)
    $ jnPause(1)

    n 7fcsbg "Sep.{w=0.75}{nw}"
    extend 3fchgn " ¡Mucho mejor!"
    n 3fchsm "..."
    n 4fsqsm "¿Y bien?{w=0.75}{nw}"
    extend 4fcsbg " ¿Qué estás esperando?"

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 3fchgnl "¡S-{w=0.2}siéntete como en casa ya,{w=0.2} [chosen_endearment]!"

    elif Natsuki.isEnamored(higher=True):
        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 3fchbgl "¡P-{w=0.2}ponte cómodo ya,{w=0.5}{nw}"
        extend 3fchgnl " gran [chosen_tease]!"
    else:

        n 2fchbg "¡Empieza a hablar ya,{w=0.2} [player]!"

    return




label holiday_prelude:
    n 1tllbo "..."
    n 1ullpu "...Sabes,{w=0.75}{nw}"
    extend 3fsrcaesp " casi se siente como si me estuviera perdiendo de algo."
    n 3fsrpu "...{w=1}{nw}"
    n 1uskemlesh "...!{w=0.5}{nw}"
    n 1fbkwrl "¡S-{w=0.3}sólo un segundo!{w=1}{nw}"
    extend 2flrpol " ¡Y-{w=0.2}ya vuelvo!{w=1}{nw}"

    hide screen hkb_overlay
    show black zorder JN_BLACK_ZORDER
    stop music
    hide prop
    hide deco
    play audio switch_flip
    $ jnPause(5)

    return


label holiday_interlude:
    n 1fllbo "..."
    n 1tllpu "Sabes..."
    n 4tnmpueqm "Siento que estoy olvidando algo más."
    n 2fsrpu "...{w=1}{nw}"
    n 1uskemlesh "...!{w=0.5}{nw}"
    n 1fbkwrl "¡S-{w=0.3}sólo un segundo!{w=1}{nw}"
    extend 2flrpol " ¡No vayas a ningún lado!{w=1}{nw}"

    hide screen hkb_overlay
    show black zorder JN_BLACK_ZORDER
    stop music
    hide prop
    hide deco
    play audio switch_flip
    $ jnPause(5)

    return

label holiday_new_years_day:
    python:
        import copy


        jn_outfits.getWearable("jn_headgear_new_year_headband").unlock()
        new_years_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        new_years_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_new_year_headband")
        new_years_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(new_years_hat_outfit)

        jn_events.getHoliday("holiday_new_years_day").run()

    n 1uchbs "¡CINCO!"
    n 1uchbg "¡CUATRO!"
    n 1uchbs "¡TRES!"
    n 1uchbg "¡DOS!"
    n 1unmajesu "U-"
    n 1fskemesh "...!"
    n 3fcsanless "¡Uuuuuuuu-!"
    n 3fcsemless "¿Es una{w=0.5}{nw}"
    extend 3fcswrl " {cps=10}maldita{/cps}{w=0.5}{nw}"
    extend 1fbkwrlean " {i}broma{/i}?"
    n 1kskem "¡¿Me lo perdí?!{w=0.5}{nw}"
    extend 1kskwr " ¡¿OTRA VEZ?!"
    n 3fcsfu "¡Ugh!{w=0.5}{nw}"
    n 1fbkwrlean "¡¿Cómo {i}siempre{/i} me pierdo algo que solo pasa una vez al año?!{w=1.25}{nw}"
    extend 4kslfreso " ¡No puedo {i}creer{/i} que estaba tan perdida con el tiempo!"

    if jn_is_day():
        n 4tnmpu "...Muy perdida,{w=0.2} en realidad.{w=0.5} Ahora que miro la hora.{w=1}{nw}"
        extend 4nsrpo " Estuve muy cerca."
        n 1kcsemedr "Cielos..."
        n 3fslajl "Podrías haberme despertado antes,{w=0.5}{nw}"
        extend 3fsqpol " idiota."
        n 1nslpu "Pero...{w=1}{nw}"
        extend 1tsqsl " Supongo que no puedo darte demasiados problemas por ello,{w=0.2} [player]."
        n 1fcsbg " Tu resaca puede hacer eso por mí.{w=0.5}{nw}"
        extend 1fcsajsbr " ¡De todos modos!"
    else:

        n 1kcsemedr "Viejo..."
        n 2fsrpu "Ahora eso me va a molestar por el resto del día..."
        n 2fslsrl "Vaya forma de empezar el año nuevo,{w=0.2} ¿eh?"
        n 1fcspoesi "..."
        n 1fcsajsbr "Bueno,{w=0.2} ¡lo que sea!"

    n 1fcsemlsbr "¿Perderse el año nuevo?{w=0.5}{nw}"
    extend 2flrbgsbl " ¡M-{w=0.3}meramente un contratiempo menor!"
    n 1fcsajsbr "Además,{w=0.5}{nw}"
    extend 3fllbgsbr " ¡no es como si se nos fueran a acabar los años para contar!{w=1}{nw}"
    extend 3nsrsssbr " Probablemente."
    n 1nllpusbr "Es...{w=1}{nw}"
    extend 1nsqsssbl " medio difícil de decir en estos días, ¿eh?"
    n 1kllbosbl "..."

    n 1unmsl "Pero ya en serio,{w=0.2} [player]?"
    n 3nslss "Sé que ya medio arruiné mi nuevo comienzo..."
    n 4fnmbol "Pero eso no significa que te salvaste."
    n 1fcsss "Sí,{w=0.2} sí.{w=0.5} Lo sé."
    n 1fslss "No voy a darte todo un sermón sobre nuevos comienzos,{w=1}{nw}"
    extend 1tlrbo " ir al gimnasio{w=0.5}{nw}"
    extend 4tnmss " o algo así."

    if jn_is_day():
        n 1fchgn "¡{i}Algo{/i} me dice que no apreciarías el dolor de cabeza extra!"

    n 1tllaj "Pero...{w=1}{nw}"
    extend 1tnmsl " de hecho hay una cosa que quiero decir."
    n 1ncssl "..."
    n 1ucspu "Solo..."

    if Natsuki.isAffectionate(higher=True):
        extend 4fnmpul " prométeme algo,{w=0.2} [player].{w=0.5}{nw}"
        extend 4knmbol " ¿Por favor?"
    else:

        extend 1fnmpu " haz una cosa por mí.{w=0.5}{nw}"
        extend 4knmbol " ¿Por favor?"

    n 2kslbol "..."
    n 2kplpulsbl "Contacta a alguien hoy.{w=0.5}{nw}"

    if Natsuki.isEnamored(higher=True):
        extend 1fcsajfesssbl " Y-{w=0.2}y no me refiero a mí.{w=0.5}{nw}"
        extend 1fslssfesssbl " Esta vez."
    else:

        extend 1fcsajfesssbl " Y-{w=0.2}y no me refiero a mí.{w=0.5}{nw}"

    n 1fcsun "Por favor...{w=1}{nw}"
    extend 1fcspul " escúchame,{w=0.2} ¿está bien?"
    n 2kllun "No todos tienen el lujo de amigos o familia.{w=1}{nw}"
    extend 4ksqpu " Y confía en mí cuando digo que no todos esperan con ansias un año nuevo..."
    n 1knmsl "Pero el mensaje correcto realmente {i}puede{/i} hacer toda la diferencia."
    n 2klrsl "...Y nunca sabes si siempre tendrás la oportunidad de enviarlo."
    n 1ncspu "Algún familiar con el que no te llevas bien,{w=1}{nw}"
    extend 1nllsr " un amigo del que te has distanciado..."
    n 4knmpu "No van a...{w=0.5}{nw}"
    extend 4kllpu " estar ahí{w=0.5}{nw}"
    extend 4fslunl " para siempre."
    n 2kslunltsb "...Justo como mis amigas,{w=0.3} [player]."
    n 1fcsajftsa "Y-{w=0.2}y recordar a las personas a tu alrededor es igual de importante que cualquier propósito estúpido."
    n 1fnmsrl "Así que no me importa {i}cómo{/i} lo hagas.{w=1}{nw}"
    extend 1fllpul " Mensaje de texto,{w=0.35} llamada telefónica,{w=0.35} lo que sea."
    n 1fcspul "Pero por favor...{w=0.5}{nw}"
    extend 1kllsrl " haz algo,{w=0.2} ¿entendido?{w=1}{nw}"
    extend 4fnmbol " Por ti mismo tanto como por ellos."

    n 4nlrunl "..."
    n 1ncsajl "Oh,{w=0.5}{nw}"
    extend 2nsleml " cielos."
    $ current_year = datetime.date.today().year
    n 3fllunlsbr "Apenas estamos en [current_year] y ya estoy poniendo las cosas todas serias..."
    n 1fslsslsbr "Je.{w=0.5}{nw}"
    extend 1tsqpu " Tanto para una celebración alegre,{w=0.2} ¿no?"
    n 4tnmpu "¿Pero [player]?"
    n 2kllsl "..."

    if Natsuki.isEnamored(higher=True):
        n 4knmsll "...Gracias."
        n 1kllssl "Por este año,{w=0.2} quiero decir."
        n 2fcsemlesssbl "¡S-{w=0.2}sé que no lo demuestro mucho!{w=0.5}{nw}"
        extend 2klrpul " Pero...{w=0.5}{nw}"
        extend 2knmpul " solo tomarte tiempo de tu día para visitarme,{w=0.75}{nw}"
        extend 2kllssl " escuchar todas mis tonterías,{w=0.75}{nw}"
        extend 2fsldvl " lidiar con mi basura a veces..."
        n 1knmbol "...Importa."
        n 1kllssl "Realmente lo hace,{w=0.2} je.{w=1.25}{nw}"
        extend 4kllbofsbr " Mucho."
        n 1kllajf "Y...{w=1}{nw}"
        extend 4knmpufsbr " ¿una última cosa?"
        n 1fcsunfsbr "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5)

        if Natsuki.isLove(higher=True):
            show natsuki 1fsldvlsbl zorder JN_NATSUKI_ZORDER at jn_center
            play audio kiss
            $ jnPause(1.5)
            hide black with Dissolve(1.25)
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 4kwmsmf "...Feliz año nuevo,{w=0.2} [chosen_endearment].{w=1.25}{nw}"
            extend 4kllssfess " Jejeje."
        else:

            show natsuki 1nsldvlsbl zorder JN_NATSUKI_ZORDER at jn_center
            $ jnPause(1.5)
            hide black with Dissolve(1.25)
            $ chosen_tease = jn_utils.getRandomTease()
            n 4klrssf "Je."
            n 1fchsmfess "...Feliz año nuevo,{w=0.2} [chosen_tease]."
    else:

        n 1knmsll "...Gracias.{w=0.75}{nw}"
        extend 3fcsemlsbl " P-{w=0.2}por este año,{w=0.2} quiero decir."
        n 1fslbolesssbl "Yo...{w=0.5}{nw}"
        extend 4knmboless " realmente aprecio que hayas pasado tanto tiempo conmigo ya."
        n 1kllssless "Incluso si {i}soy{/i} solo una chica gruñona atrapada en algún{w=0.5}{nw}"
        extend 2fsrssl " salón de clases espacial mágico."
        n 1nlrunl "..."
        n 1kbkwrl "¡En serio!{w=0.2} ¡Lo aprecio!"
        n 3fllanlsbl "Es..."
        n 1kcsemlesisbl "..."
        n 2ksrpol "S-{w=0.3}significa mucho para mí,{w=0.2} ¿está bien?"
        n 1ksrpul "Y...{w=0.75}{nw}"
        extend 1knmssl " ¿una última cosa?"
        n 1ncsajl "..."
        n 1fcsunl "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        show natsuki 1fsldvlsbl zorder JN_NATSUKI_ZORDER at jn_center
        play audio clothing_ruffle
        $ jnPause(3.5)
        hide black with Dissolve(1.25)

        n 4fsqdvlesssbr "...F-{w=0.2}feliz año nuevo,{w=0.2} tonto."
        n 4nslsslesssbl "Y-{w=0.2}y si alguien pregunta,{w=0.3} eso nunca pasó.{w=1}{nw}"
        extend 4fsldvlesssbl " Jejeje..."

    $ jn_events.getHoliday("holiday_new_years_day").complete()

    return

label holiday_valentines_day:
    $ valentine_outfit = jn_outfits.getOutfit("jn_ruffle_neck_sweater_outfit")
    $ valentine_outfit.unlock()
    $ jn_outfits.saveTemporaryOutfit(valentine_outfit)
    $ player_has_gifted_clothes = len(jn_outfits.JNWearable.filterWearables(jn_outfits.getAllWearables(), True, False)) > 0
    $ jn_events.getHoliday("holiday_valentines_day").run()

    n 1uskfllsbr "...!{w=0.75}{nw}"
    n 1uskwrlsbr "¡A-{w=0.2}ah!{w=0.75}{nw}"
    extend 1flrbglsbr " ¡[player]!"
    n 1fcsajlsbl "Bueno,{w=1}{nw}"
    extend 1fcsgslsbl " ¿no te tomaste tu dulce tiempo en aparecer?{w=0.75}{nw}"
    extend 1fllemlsbl " ¡Cielos!"
    n 1fcsemlsbl "Digo,{w=0.75}{nw}"
    extend 1fcsgsl " ¡vamos!{w=1}{nw}"
    extend 1fnmpol " ¿Olvidaste totalmente qué día era o algo así?{w=1}{nw}"
    extend 1fsqpol " ¿{i}Seriamente{/i} tengo que recordártelo?"
    n 1fcswrl "¡No soy tu asistente personal,{w=0.2} sabes!"
    n 1fsqpol "..."
    n 1fsqpul "...¿Huh?{w=0.75}{nw}"
    extend 1tsqfll " ¿Qué?"
    n 1nlrfllsbl "¿Para qué es esa mirada,{w=0.5}{nw}"
    extend 1knmfllsbl " tan de repente?"

    if Natsuki.isLove(higher=True):
        n 1knmbolsbl "..."
        n 1udweml "¡O-{w=0.2}oh!{w=0.75}{nw}"
        extend 1fcseml " Cierto.{w=1}{nw}"
        extend 1nsrbolsbl " L-{w=0.2}los chocolates."
        n 1ksrbolsbl "..."
        n 1ksqfllsbl "...Vamos,{w=0.2} [player].{w=1}{nw}"
        extend 1knmfllsbl " ¿No es obvio?{w=1}{nw}"
        extend 1klrfllsbl " ¿Por qué más crees que {i}mágicamente{/i} tendría una caja de ellos lista?"
        n 1ksrslfsbl "...S-{w=0.2}son tuyos."
        n 1fcsajlsbl "S-{w=0.2}sé que no puedo dártelos exactamente..."
        n 1nslpulsbl "Bueno.{w=1}{nw}"
        extend 1nslsslsbr " A menos que cuentes untarlos por toda la pantalla o algo.{w=1}{nw}"
        extend 1kslbolsbr " Pero..."
        n 1kslunlsbr "..."
        n 1fcsunlsbr "¡Tenía que hacer algo!{w=0.75}{nw}"
        extend 1flrfllsbr " Y-{w=0.2}y no solo porque estamos...{w=1.25}{nw}"
        extend 1ksrbof " ya sabes."
        n 1kcsfll "Es solo que..."
        n 1kslsll "..."
        n 1kslpul "Has...{w=0.75}{nw}"
        extend 1kllbol " realmente hecho tanto por mí ya.{w=1}{nw}"
        extend 1knmbol " ¿Sabes?"
        n 1knmfll "...Y por un tiempo súper largo ya también."
        n 1ncsajl "Sí,{w=0.2} me trajiste de vuelta.{w=1.25}{nw}"
        extend 1nsrfsl " Obviamente.{w=1}{nw}"
        extend 1knmbol " Pero son todas las cosas pequeñas las que {i}realmente{/i} me importan,{w=0.2} [player]."
        n 1kllbol "Es cuántas veces has venido a visitarme."
        n 1kllsslsbr "Es cómo siempre me dejas taladrarte los oídos con cosas al azar."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1klrajlsbr "Es todas las cosas nuevas que solo...{w=1}{nw}"
            extend 1klrsllsbr " me has dado.{w=1.25}{nw}"
            extend 1ksrpol " Incluso si nunca las pedí."

        n 1kcspulesi "..."
        n 1ksqsll "...Mira.{w=1}{nw}"
        extend 1klrsll " Nunca he sido buena en este tipo de cosas.{w=1.25}{nw}"
        extend 1fcsunlsbl " S-{w=0.2}siempre tengo problemas con ello."
        n 1fcspulsbl "Especialmente cuando es todo tan...{w=0.75}{nw}"
        extend 1ksrsllsbl " tan nuevo para mí.{w=0.75}{nw}"
        extend 1kllsllsbl " Tener a alguien que..."
        n 1kllsrlsbl "..."
        n 1kllfllsbl "...A quien realmente le importo."
        n 1knmpulsbl "A-{w=0.2}alguien que{w=0.75}{nw}"
        extend 1ksrpufsbr " me{w=0.75}{nw}"
        extend 1ksrbofsbr " ama."
        n 1kcsajlsbr "Pero lo que intento decir es..."
        n 1ksrbolsbr "..."
        n 1knmbolsbr "...Se aprecia,{w=0.2} [player].{w=0.75}{nw}"
        extend 1knmfllsbr " De verdad.{w=1}{nw}"
        extend 1kllbolsbl " Mucho más de lo que crees."
        n 1knmbofsbl "Y...{w=0.5} realmente quería que supieras eso."
        n 1fcsemfsbl "Incluso si significa que tengo que sentirme toda incómoda en el proceso."
        extend 1ksrbof " Eso es lo que {i}realmente{/i} importa."
        n 1ksrajf "Así que...{w=1.25}{nw}"
        extend 1ksrssf " sí."
        n 1ksrfsf "..."
        n 1knmfsf "...¿Y [player]?"
        n 1kslcafsbr "..."

        show natsuki 1fcscafsbr
        play audio chair_out
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(3)

        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle

        $ valentine_special_outfit = jn_outfits.getOutfit("jn_heart_sweater_outfit")
        $ valentine_special_outfit.unlock()
        $ jn_outfits.saveTemporaryOutfit(valentine_special_outfit)
        show natsuki 1nsrdvfess at jn_center

        $ jnPause(5)
        play audio chair_in
        $ jnPause(2)
        hide black with Dissolve(2)
        $ jnPause(1)

        n 1fsrssf "S-{w=0.2}sorpresa."
        show prop f14_heart give
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1fchbgfesssbl "F-{w=0.2}feliz día de San Valentín,{w=0.2} [chosen_endearment].{w=1.25}{nw}"
        extend 1fchsmfesssbl " Jejeje."

    elif Natsuki.isEnamored(higher=True):
        n 1uskwrlesh "¡A-{w=0.2}ah!{w=0.5}{nw}"
        extend 1udwfll " ¿E-{w=0.2}esta cosa?"
        n 1fcsgslsbr "Digo,{w=0.2} es obviamente..."
        n 1fslunlsbr "..."
        n 1fcsemlsbr "¡E-{w=0.2}es...!"
        n 1fcsanlsbr "¡Nnnnnnnn...!"
        n 1fbkwrlsbr "¡¿P-{w=0.2}para qué {i}crees{/i} que es?!{w=0.75}{nw}"
        extend 1flrwrlsbr " No tengo que deletrearlo todo realmente,{w=0.2} ¿o sí?{w=0.75}{nw}"
        extend 1fcsemlsbr " ¡Cielos!"
        n 1fllemlsbr "¡E-{w=0.2}Es solo que...!"
        extend 1ksremlsbr " como si esto no fuera ya bastante incómodo..."
        n 1fcsunlsbl "..."
        n 1ncspulesi "..."
        n 1flrbol "...Los hice para ti,{w=0.75}{nw}"
        extend 1fnmbol " ¿okey?{w=1}{nw}"
        extend 1fslcalsbl " No creerías lo difícil que fue encontrar todo esto."
        n 1fcsemfsbl "¡S-{w=0.2}sé que no somos {i}así{/i}!{w=0.75}{nw}"
        extend 1flrslf " Y sé que no puedo simplemente dártelos.{w=1}{nw}"
        extend 1klrbof " Pero ese no es el punto en absoluto."
        n 1klrfll "Es solo que..."
        n 1ksrsll "..."
        n 1ksrfll "No hacer {i}algo{/i}...{w=0.75}{nw}"
        extend 1fllbol " simplemente no se hubiera sentido bien.{w=1}{nw}"
        extend 1kllbol " N-{w=0.2}no después de todo lo que has hecho por mí."
        n 1fcscal "...Y-{w=0.2}y no me refiero solo a traerme de vuelta,{w=0.2} [player]."
        n 1nlrsll "Escuchar todos mis pensamientos tontos.{w=1}{nw}"
        extend 1ksrbol " Molestarte en venir a visitarme todo el tiempo."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1fsrsslsbl "I-{w=0.2}incluso los regalos sorpresa tontos que {i}insistes{/i} en darme."

        n 1kllajl "Es todo..."
        n 1kslunl "..."
        n 1ksqbolsbr "...Se aprecia.{w=1}{nw}"
        extend 1knmbolsbr " ¿Okey?{w=1.25}{nw}"
        extend 1klrbolsbr " De verdad."
        n 1ksrflf "...Y quería asegurarme de que supieras eso también."
        n 1ksrslf "..."
        n 1ksrajl "Así que...{w=1}{nw}"
        extend 1nsrssl " sí.{w=1.25}{nw}"
        extend 1nsrcal " Ten."
        show prop f14_heart give
        $ jnPause(3)
        n 1ksrcal "..."
        n 1nnmajl "...¿Y [player]?"
        n 1fslunlsbl "..."

        show prop f14_heart hold
        show natsuki 1fcsunfsbl
        play audio chair_out
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)

        play audio clothing_ruffle
        $ jnPause(3)
        show natsuki 1nsrbofsbr at jn_center

        $ jnPause(3)
        play audio chair_in
        $ jnPause(1)
        hide black with Dissolve(2)
        $ jnPause(2)

        show prop f14_heart give
        n 1fsrfsfsbr "F-{w=0.2}feliz día de San Valentín."
    else:

        n 1uskflleshsbr "...!{w=0.5}{nw}"
        n 1fcsgslsbr "¡¿E-{w=0.2}esto?!{w=0.75}{nw}"
        extend 1flrgslsbr " Es..."
        n 1fcsgslsbr "¡E-{w=0.2}es...!"
        n 1fcsanlsbr "¡Nnnnnnnn...!"
        n 1fbkwrlsbr "¡¿P-{w=0.2}para qué {i}crees{/i} que es?!{w=0.75}{nw}"
        extend 1flrwrlsbr " No tengo que {i}realmente{/i} deletrearlo todo,{w=0.2} ¿o sí?{w=0.75}{nw}"
        extend 1fcsemlsbr " ¡Cielos!"
        n 1fllemlsbr "¡E-{w=0.2}Es solo que...!"
        n 1fslemlsbr "..."
        n 1kslsllsbr "..."
        n 1fcsemlsbr "...Okey,{w=0.75}{nw}"
        extend 1flrbolsbl " mira.{w=1}{nw}"
        extend 1fsrsrlsbl " No soy tonta."
        n 1fcsgslsbl "Sé que no somos como...{w=0.75}{nw}"
        extend 1fslunfsbl " eso.{w=1.5}{nw}"
        extend 1kslbolsbl " Pero..."
        n 1kllbolsbl "..."
        n 1fcsbolsbr "Simplemente no se sentía bien no hacer {i}algo{/i}.{w=1}{nw}"
        extend 1fnmbolsbl " Piénsalo,{w=0.2} [player]."
        n 1fcsemfsbl "¡N-{w=0.2}no tienes que ser todo acaramelado con alguien para demostrarle que te importa!{w=0.75}{nw}"
        extend 1fsrcalsbl " A pesar de lo que insisten todos los anuncios cursis."
        n 1fsqcalsbl "...Y sí [player],{w=0.2} antes de que digas nada.{w=0.75}{nw}"
        extend 1fcscalsbl " T-{w=0.2}tú sí me importas."
        n 1flrcalsbl "T-{w=0.2}traerme de vuelta,{w=0.75}{nw}"
        extend 1nllbol " escuchar todos mis pensamientos tontos..."

        if persistent.jn_custom_outfits_unlocked and player_has_gifted_clothes:
            n 1kslbolsbr "Todas las cosas nuevas que me has dado."

        n 1ncsemlsbr "I-{w=0.2}incluso solo...{w=1}{nw}"
        extend 1kslsllsbr " aparecerte."
        n 1ncsajlsbr "Es todo..."
        n 1klrbolsbr "..."
        n 1kcsemlesisbr "..."
        n 1ksqcal "...Se aprecia,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fcseml " Y-{w=0.2}y tenía que asegurarme de que supieras eso."
        n 1fcscal "Q-{w=0.2}quisieras hacerlo o no."
        n 1nslajl "Así que..."
        n 1fslslf "..."
        show prop f14_heart give
        n 1fcsslfsbr "...Ten."
        n 1fcsajfsbr "Solo finge que lo estás tomando o algo,{w=0.75}{nw}"
        extend 1flrcafsbr " supongo.{w=1.25}{nw}"
        extend 1fsrpolsbr " Antes de que cambie de opinión."
        n 1nsrpolsbr "..."
        n 1nsrpulsbr "Y..."
        n 1fcssslsbl "F...{w=0.75}{nw}"
        extend 1fcspolsbl "feliz día de San Valentín,{w=0.2} [player]."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio gift_close
    $ jnPause(3)
    play audio drawer
    hide prop f14_heart
    $ jnPause(3)

    if Natsuki.isLove(higher=True):
        play audio kiss
        $ jnPause(2.5)

    hide black with Dissolve(2)
    $ jnPause(2)

    $ jn_events.getHoliday("holiday_valentines_day").complete()

    return

label holiday_easter:
    python:
        persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)
        jn_atmosphere.showSky(jn_atmosphere.WEATHER_CHERRY_BLOSSOM)

        chick_outfit = jn_outfits.getOutfit("jn_chick_outfit")
        chick_outfit.unlock()
        jn_outfits.saveTemporaryOutfit(chick_outfit)

        jn_events.getHoliday("holiday_easter").run()

    n 1unmflleex "...!{w=1.25}{nw}"
    n 4unmbgl "¡[player]!{w=0.5}{nw}"
    extend 4uchbgl " ¡[player]!{w=0.3} ¡[player]!"
    n 2fcsfll "D-{w=0.2}digo,{w=0.5}{nw}"
    extend 2fcsgslsbr " ¡ya era hora de que trajeras tu trasero aquí!{w=1}{nw}"

    if jn_is_day():
        extend 4fcsgssbl " ¿Siquiera {i}sabes{/i} qué día es hoy?{w=0.75}{nw}"
        extend 2fcsposbl " ¡Cielos!"
    else:

        extend 4fsqgssbl " ¿Siquiera {i}sabes{/i} qué día es hoy?"
        n 2fsrslsbl "Supongo que no,{w=0.75}{nw}"
        extend 2fcspoesisbl " considerando la hora a la que llegaste."

    n 2fsqca "No tengo que recordártelo {i}seriamente{/i},{w=0.2} ¿verdad?"
    n 1fcstresi "..."
    n 4fcsaj "Es..."
    n 3fchbg "Pascua,{w=0.75}{nw}"
    extend 3uchgn " ¡obvio!{w=1}{nw}"
    extend 4fsqbg " ¿Qué más iba a ser,{w=0.2} [player]?"
    n 1fcsbg "Después de todo.{w=0.75}{nw}"
    extend 3fsqsm " {i}Sabes{/i} lo que significa la Pascua,{w=0.2} ¿verdad?"
    n 3tsqsm "..."
    n 1fcssm "Je."
    n 4fcsbg "Sí,{w=0.2} lo sabes.{w=0.75}{nw}"
    extend 1fcssmesm " Básicamente tengo un sexto sentido para este tipo de cosas,{w=0.2} después de todo."
    n 1fcsss "Significa..."
    n 3fchbs "Temporada de flores de cerezo,{w=0.75}{nw}"
    extend 3uchgn " ¡obviamente!"
    n 4tnmbo "..."
    n 4tnmfl "¿Qué?{w=0.75}{nw}"
    extend 2fsrpo " ¡Hablo en serio,{w=0.2} [player]!{w=1}{nw}"
    extend 2fcsaj " ¿Por qué no lo haría?"
    n 1fcsfl "Es...{w=1.25}{nw}"
    extend 3uchgnledz " ¡{b}ASOMBROSO{/b}!"
    n 4ullbg "Ver todos los árboles de cerezo simplemente {i}explotar{/i} en vida así. ¿{w=0.75}{nw}"
    extend 4fspgs " ¡Es {i}súper{/i} bonito!"
    n 2fcsbs "¿Qué más se te ocurre que inunde el lugar de color así de bien,{w=0.2} eh?"
    n 1ulrss "Además con cómo las flores viajan todo el camino desde el sur hacia el norte..."
    n 3uchgn "¡Es prácticamente un anuncio rodante para el verano!{w=0.2} ¡Me encanta!"

    $ cherry_blossom_outfit = jn_outfits.getOutfit("jn_cherry_blossom_outfit")
    if not cherry_blossom_outfit.unlocked:
        $ cherry_blossom_outfit.unlock()
        n 4fslpu "Estoy segura de que tenía un vestido súper elegante con ese tema en algún lugar..."

    n 3unmaj "¿Pero personalmente?{w=0.75}{nw}"
    extend 3fcsca " Me gusta pensar que es mi recompensa por sobrevivir a todos los asquerosos meses de invierno también."
    n 1fslem "Soportar todo el clima de porquería,{w=0.2} levantarse cuando está oscuro -{w=0.5}{nw}"
    extend 1fsqsl " volver cuando está oscuro."
    n 2fcswr "¡Sin mencionar estar básicamente atrapada en interiores todo el tiempo!"
    n 4ulrfl "Así que después de todo eso,{w=0.75}{nw}"
    extend 4nsrss " ver todo empezar a parecerse a algo salido de un cuento de hadas,{w=0.5}{nw}"
    extend 2tnmbo " incluso si es solo por un par de semanas.{w=0.75}{nw}"
    extend 2tllss " Bueno..."
    n 1fchsm "¡{i}Casi{/i} hace que valga la pena lidiar con el invierno!"
    n 4fsqss "...{i}Casi{/i}.{w=1}{nw}"
    extend 4fcssm " Jejeje."

    $ easter_poem = jn_poems.getPoem("jn_easter_sakura_in_bloom")
    if not easter_poem.unlocked:
        $ easter_poem.unlock()
        n 1fcsbg "De hecho..."

        show natsuki 1fcssmeme
        play audio page_turn
        show prop poetry_attempt zorder JN_PROP_ZORDER at JN_TRANSFORM_FADE_IN
        $ jnPause(2)

        n 1fchbgeme "Ta-{w=0.2}da!{w=0.75}{nw}"
        extend 4uchgn " ¡Incluso escribí un poema sobre ello!{w=0.75}{nw}"
        extend 4fcsbg " ¿Cómo podría {i}no{/i} hacerlo?"
        n 2flrfl "¿Qué clase de poeta simplemente desperdiciaría una inspiración tan fácil?"
        n 2fcsaj "Digo...{w=1}{nw}"
        extend 2fcssm " ¡prácticamente se escribió solo!"
        n 1fsqsm "..."
        n 4fsqss "¿Oh?{w=0.75}{nw}"
        extend 4fnmss " ¿Qué es eso,{w=0.2} [player]?"
        n 2fcsbgsbl "¿Te estás {i}muriendo{/i} por verlo?{w=0.75}{nw}"
        extend 2fnmbgsbl " ¿Es eso?"
        n 2fsqcssbl "..."
        n 2fcsbglsbl "B-{w=0.2}bueno,{w=0.75}{nw}"
        extend 2fcssmlsbl " no veo por qué no.{w=1.25}{nw}"
        extend 4fcsajlsbr " Después de todo..."
        n 4fcssmlsbr "¡{i}Alguien{/i} tiene que recordarte cómo se ve la literatura {i}real{/i} de vez en cuando!"
        show natsuki 1fsrsmlsbr

        call show_poem (easter_poem)
        show natsuki 1fsrbolsbr

        n 2fllsssbr "¿Y bien?{w=0.75}{nw}"
        extend 2fcssmsbr " ¡Te dije que básicamente se escribió solo!"
        n 4fsqsm "No quiero presumir,{w=0.2} [player].{w=1}{nw}"
        extend 4tnmaj " ¿Pero a diferencia de los árboles?"
        n 2fcssmesm "Mi escritura está {i}siempre{/i} en plena floración.{w=0.75}{nw}"
        extend 2fchsm " Jajaja."

        show natsuki 4fcssm
        play audio page_turn
        hide prop at JN_TRANSFORM_FADE_OUT
        $ jnPause(2)

    n 4tslbo "..."
    n 4unmaj "Oh,{w=0.2} cierto.{w=1}{nw}"
    extend 2ulraj " Y todas las cosas de chocolate son geniales también,{w=0.75}{nw}"
    extend 2tlrbo " supongo."
    n 1fsqsm "Jejeje."
    n 3fcsbs "No me digas que {i}esa{/i} es la parte de la Pascua en la que estabas {i}realmente{/i} interesado,{w=0.2} [player]."
    n 3fcsbg "¡Puedo leerte como un libro!"
    n 3nlraj "Aunque...{w=1.25}{nw}"
    extend 1tnmbo " en toda seriedad,{w=0.2} [player]?{w=0.75}{nw}"
    n 2ullfl "Realmente nunca cubrimos mucho eso en la escuela,{w=0.2} para ser honesta.{w=0.5}{nw}"
    extend 2tnmsl " La Pascua."
    n 4fsran "No es como si eso detuviera a todos los estúpidos anuncios de {i}intentar{/i} cubrirlo por nosotros."
    n 1unmca "Pero al menos entiendo lo que se supone que representa.{w=1}{nw}"
    extend 2ullaj " Renacimiento,{w=0.2} empezar de nuevo -{w=0.75}{nw}"
    extend 2fcssm " ese tipo de cosas."
    n 4fcsbg "¿Sorprendido,{w=0.2} [player]?{w=0.75}{nw}"
    extend 3fsqss " ¿De dónde {i}más{/i} creías que saqué la idea para el vestido?"
    n 3fsrss "No sé mucho sobre la Pascua..."
    n 3fchgnl "¡Pero no se necesita ser un genio para saber que los pollitos son liiindos!{w=0.75}{nw}"
    extend 4uchgnl " ¡Amo esas pequeñas bolitas amarillas!"
    n 1ncsssl "Viejo..."
    n 4fcstrl "Tengo {w=0.2}{b}que{/b}{w=0.2} conseguir algunos peluches o algo..."
    n 4nslcalsbr "..."
    n 2fcstrlsbr "Bueno,{w=0.2} d-{w=0.2}de todos modos."

    if Natsuki.isEnamored(higher=True):
        n 2ulraj "La Pascua puede tratarse de nuevos comienzos,{w=0.75}{nw}"
        extend 2nlrpu " pero...{w=1}{nw}"
        extend 4tnmbo " ¿honestamente?"
        n 4nllssl "...¿Gracias a ti?"
        n 1kllbol "..."
        n 1ncsssl "Je."

        if Natsuki.isLove(higher=True):
            n 1ksrssl "Creo que ya he {i}tenido{/i} lo mejor que podría haber obtenido."
            n 4ksrbolsbl "..."

            show natsuki 4fcsbolsbl
            play audio chair_out
            show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
            $ jnPause(3)
            play audio kiss
            show natsuki 4nslfsl at jn_center
            $ jnPause(3)
            play audio chair_in
            $ jnPause(2)
            hide black with Dissolve(2)

            n 4nsldvl "...Y supongo que terminamos {i}floreciendo{/i} también,{w=0.2} ¿eh?{w=1.25}{nw}"
            extend 4fchsslsbl " E-{w=0.2}ehehe..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbll "F-{w=0.2}feliz Pascua,{w=0.2} [chosen_tease]!"
        else:

            n 3ksrssl "Creo que ya he tenido lo mejor que podría haber obtenido.{w=0.75}{nw}"
            extend 3nsrsmlsbl " Jejeje."
            $ chosen_tease = jn_utils.getRandomTease()
            n 3fchbgl "F-{w=0.2}feliz Pascua,{w=0.2} [chosen_tease]!"

    elif Natsuki.isAffectionate(higher=True):
        n 2ullaj "La Pascua puede tratarse de nuevos comienzos,{w=0.75}{nw}"
        extend 2tnmbo " pero ¿honestamente?"
        n 4kslslsbr "..."
        n 4fllsslsbr "Yo...{w=1}{nw}"
        extend 1nsrsslsbr " creo que puedo conformarme con el que me diste también.{w=1}{nw}"
        extend 1fcssslsbr " Jejeje."
        n 2fcsbglsbl "F-{w=0.2}feliz Pascua,{w=0.2} [player]!"
    else:

        n 2ulrbo "Dicen que la Pascua se trata de nuevos comienzos,{w=0.75}{nw}"
        extend 2tlrpu " pero...{w=1}{nw}"
        extend 2fnmsm " ¿honestamente?"
        n 3fcsbg "...Me gusta pensar que este apeeenas está comenzando.{w=1}{nw}"
        extend 3fsqsm " Jejeje."
        n 4nchgn "¡Feliz Pascua,{w=0.2} [player]!"

    $ jn_events.getHoliday("holiday_easter").complete()

    return

label holiday_halloween:
    if preferences.get_volume("music") < 0.25:
        $ preferences.set_volume("music", 0.75)

    if preferences.get_volume("sfx") < 0.25:
        $ preferences.set_volume("sfx", 0.75)

    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_GLITCH)
    hide natsuki
    show chair zorder JN_NATSUKI_ZORDER
    show desk zorder JN_NATSUKI_ZORDER
    $ jn_events.getHoliday("holiday_halloween").run(suppress_visuals=True)
    hide black

    $ jnPause(3)
    show tense zorder JN_GLITCH_ZORDER at JN_PULSE
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)
    show tense zorder JN_GLITCH_ZORDER at JN_PULSE
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)
    show tense zorder JN_GLITCH_ZORDER at JN_PULSE
    play audio thump
    $ jnPause(1.5)
    hide tense
    $ jnPause(1)

    python:
        for i in range(1, 7):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(1.5)

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_b
    $ jnPause(1)

    python:
        for i in range(1, 5):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(1)
            
            if (random.randint(1,5) == 1):
                renpy.play(filename=audio.glitch_d, channel="audio")
                jnPause(0.25)

    play audio static
    show glitch_garbled_a zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_a
    $ jnPause(0.5)
    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    $ jnPause(0.3)

    python:
        for i in range(1, 3):
            renpy.show(
                name="tense",
                at_list=[JN_PULSE],
                zorder=JN_GLITCH_ZORDER)
            renpy.play(filename=audio.thump, channel="audio")
            jnPause(0.75)
            
            if (random.randint(1,4) == 1):
                renpy.play(filename=audio.glitch_d, channel="audio")
                jnPause(0.25)
                renpy.show(
                    name="glitch_garbled_red",
                    at_list=[JN_PULSE],
                    zorder=JN_GLITCH_ZORDER)
                jnPause(0.15)
                renpy.hide("glitch_garbled_red")

    play audio static
    show glitch_garbled_b zorder JN_GLITCH_ZORDER with hpunch
    hide glitch_garbled_b
    $ jnPause(0.25)

    play audio static
    show glitch_garbled_c zorder JN_GLITCH_ZORDER with vpunch
    hide glitch_garbled_c
    $ jnPause(0.15)
    play audio glitch_d

    show black zorder JN_BLACK_ZORDER
    $ jnPause(0.25)
    play audio ooo_creep
    $ jnPause(6)
    hide desk
    hide chair
    $ jn_atmosphere.showSky(jn_atmosphere.WEATHER_SUNNY)
    $ magical_girl_cosplay = jn_outfits.getOutfit("jn_magical_girl_cosplay")
    $ magical_girl_cosplay.unlock()
    $ Natsuki.setOutfit(outfit=magical_girl_cosplay, persist=False)
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_renpy_for_dummies_closed"))
    $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_pumpkins"))
    show deco o31 zorder JN_DECO_ZORDER
    show natsuki 4fchgn zorder JN_NATSUKI_ZORDER at jn_center
    $ jnPause(0.15)
    play audio switch_flip
    hide black
    $ jnPause(1)


    $ renpy.play(filename="mod_assets/bgm/vacation.ogg", channel="music")
    $ renpy.show_screen("hkb_overlay")
    $ jn_globals.force_quit_enabled = True

    $ player_upper = player.upper()
    n 4fchbg "FELIZ HALLOWEEN,{w=0.75}{nw}"
    extend 4fchbs " ¡[player_upper]!"
    n 4fchsm "..."
    n 4fsqsm "..."
    n 2fsqss "¿Y bien?{w=0.75}{nw}"
    extend 2fcsgs " ¡No te quedes ahí sentado!{w=0.75}{nw}"
    extend 4fchgn " ¡Di algo ya!"
    n 3fnmbs "¿Te asusté?{w=0.2} ¿Te asusté?{w=0.75}{nw}"
    extend 3fcsbs " ¡No mientas!{w=1}{nw}"
    extend 7fsqbg " ¡{i}Totalmente{/i} te atrapé esta vez!"
    n 3ccsbg "Cielos...{w=1}{nw}"
    extend 7fcsbs " ¡{i}Sabía{/i} que este viejo libro tonto sería útil algún día!\n{w=0.75}{nw}"
    extend 7fsqss "Nada mal para un montón de scripts reutilizados,{w=0.2} ¿eh?"
    n 3unmbg "Y hey -{w=0.5}{nw}"
    extend 3tlrbg " ni siquiera exploté el salón de clases ni nada.{w=0.75}{nw}"
    extend 4fchbg " ¡Yo llamaría a eso un éxito total!"
    n 2fchsm "Ajaja."
    n 2cllss "Bueno,{w=0.2} de todos modos.{w=0.75}{nw}"
    extend 2ccsbg " Creo que ya he terminado de tontear por ahora."
    n 4ullaj "Entonces -{w=0.5}{nw}"
    extend 4csqbg " ¿te gusta lo que he hecho con el lugar?{w=0.75}{nw}"
    extend 3ccspo " Será mejor que aprecies todo el esfuerzo que puse en todo esto,{w=0.2} [player]."
    n 3fnmbg "¡Sip!{w=0.75}{nw}"
    extend 7fcsbg " Como puedes ver {i}claramente{/i} -{w=0.5}{nw}"
    extend 6fchbg " ¡fui a por {i}todas{/i} esta vez!"
    n 7clrbg "¿Decoraciones asombrosas hechas a mano?{w=0.75}{nw}"
    extend 7ccsbg " ¡Listo!{w=1}{nw}"
    extend 6ckrsm " ¿Cosplay fabulosamente hecho?{w=0.75}{nw}"
    extend 6fcsbs " ¡Listo otra vez!"
    n 3fnmbg "¿Conseguir fácilmente el mejor susto del año en [player]?"
    n 7fsgsm "..."
    n 7fcssm "Jejeje.{w=0.75}{nw}"
    extend 3fchgnelg " ¡Puedes apostarlo!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 1cllbg "Viejo..."
        n 2unmaj "Sabes,{w=0.2} estoy bastante segura de haberlo mencionado antes en algún momento.{w=0.75}{nw}"
        extend 5csrbosbl " Sobre cómo realmente no me gusta el horror y todo eso."
        n 4ccsfl "Pero seamos realistas aquí,{w=0.2} [player]."
    else:

        n 1cllbg "Viejo...{w=1}{nw}"
        extend 2tlraj " Sé que te dije que no era la mayor fanática del horror ya,{w=0.75}{nw}"
        extend 4ccsfl " pero seamos realistas."

    n 4tnmaj "¿Cuando realmente se trata de lo que vale la pena?{w=0.75}{nw}"
    extend 7ccssmesm " Simplemente no puedes vencer a un buen y viejo Halloween."
    n 3unmfl "¡No,{w=0.2} en serio!{w=0.75}{nw}"
    extend 3fcsbg " ¡Piénsalo!"
    n 4fsqss "No {i}solo{/i} es una excusa para sacar mi kit de costura y dejar a {i}todos{/i} boquiabiertos con mi costura..."
    n 1ccsss "Pero vamos.{w=0.75}{nw}"
    extend 2fchgn " ¿Qué {i}otras{/i} festividades te dan la excusa para atiborrarte de tantos dulces gratis como puedas agarrar,{w=0.2} eh?"
    n 2fsqsm "..."
    n 1fcssm "Jejeje.{w=0.75}{nw}"
    extend 4fcsbg " Eso es lo que pensé,{w=0.2} [player].{w=1.25}{nw}"
    extend 3fchbg " ¡Halloween es lo mejor!"

    if Natsuki.isLove(higher=True) and jn_events.getHoliday("holiday_halloween").shown_count == 0:
        n 3clrbo "..."
        n 4clrpu "O...{w=1}{nw}"
        extend 4klrsl " Supongo que lo sería."
        n 5csrslsbl "No es como si fuera del tipo de saberlo,{w=0.2} d-{w=0.2}después de todo."

        if jn_events.getHoliday("holiday_christmas_day").shown_count > 0:
            n 5cnmsl "..."
            n 2knmfl "¿Qué?{w=0.75}{nw}"
            extend 2kllfll " ¿No recuerdas,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1cllbol " Es como lo que te dije la última Navidad."
        else:

            n 4fcsem "Es solo que..."
            n 2kslsl "..."
            n 2kslfl "S-{w=0.2}simplemente apesta.{w=0.75}{nw}"
            extend 4knmbol " ¿Sabes?{w=1}{nw}"
            extend 1klrsll " Con mi familia y todo."

        n 1ksrsll "..."
        n 4ccspu "Nosotros...{w=1}{nw}"
        extend 4ccsfl " nunca...{w=1}{nw}"
        extend 4cllfl " realmente celebramos mucho.{w=1.25}{nw}"
        extend 2cdlsl " En absoluto."
        n 2clrfl "...Y Halloween no fue la excepción.{w=0.75}{nw}"
        extend 2clrsl " Obviamente.{w=0.75}{nw}"
        extend 4knmfl " ¿Por qué lo sería?"
        n 4cslfl "Y las excusas.{w=0.75}{nw}"
        extend 1fcsan " Cada año sin falta."
        n 3flrwr "'¡No es lo que hacemos aquí,{w=0.2} Natsuki!'{w=0.75}{nw}"
        extend 3fllem " '¡Simplemente no está bien,{w=0.2} Natsuki!{w=0.2} ¿Qué pensarían nuestros vecinos?'"
        n 3fslan "¡Como si casi todos en nuestra calle {i}no{/i} tuvieran hijos,{w=0.2} o pusieran decoraciones!"
        n 4fcsan "Dame un respiro."
        n 4fsrsl "Je.{w=0.75}{nw}"
        extend 2fnmsl " Todos sabíamos cuáles eran las {i}verdaderas{/i} razones,{w=0.2} [player]."
        n 2flrbol "Y no eran solo porque no era lo suficientemente japonés,{w=0.2} te diré eso."
        n 1ksrbol "..."
        n 1ccsfllesi "..."
        n 4cnmfll "...Mira.{w=0.75}{nw}"
        extend 4ccsajl " No estoy solo molesta por perderme de literalmente todo cada año."
        n 2cllsll "No me importan unos disfraces de mal gusto o un montón de porquerías de la tienda de conveniencia."
        n 2cslsll "No es como si esas cosas simplemente desaparecieran o algo el resto del año."
        n 2cnmpul "No me importa nada de eso."
        n 1clrgsl "Yo..."
        n 5clrunl "..."
        n 5fcsajl "Yo...{w=1}{nw}"
        extend 1fcsfll " solo...{w=1}{nw}"
        extend 1fllfll " quería unirme a lo que todos los demás estaban haciendo.{w=1}{nw}"
        extend 4knmwrl " ¡C-{w=0.2}con lo que mis {i}amigas{/i} me invitaron a hacer!{w=0.75}{nw}"
        extend 4clrunl " ¿Es eso {i}realmente{/i} semejante crimen?"
        n 4fcswrl "Y-{w=0.2}y además,{w=0.2} ¡qué derecho tenían {i}ellos{/i} de...!"
        n 4fllunltsc "D-{w=0.2}de..."
        n 1fcsunltsa "..."
        n 1fcsanltsa "..."
        n 2fcsflltsa "..."
        n 2csrslltsb "...Olvídalo.{w=1.25}{nw}"
        extend 2ccsgsl " ¡Olvídalo!{w=1}{nw}"
        extend 4cslunl " Ni siquiera sé {i}por qué{/i} todavía me molesta tanto."
        n 4fcseml "Era todo simplemente..."
        n 4cslbol "..."
        n 1kslbol "...Tan estúpido."
        n 3ccseml "Y-{w=0.2}y sé que no hay nada que me detenga de hacer lo que quiera ahora.\n{w=0.75}{nw}"
        extend 3clrbol "Como puedes ver."
        n 4klrfll "Pero eso no cambia todo el tiempo perdido.{w=1.25}{nw}"
        extend 5kdlbol " Toda la decepción."
        n 1kslbol "Y no creo que nunca lo haga."
        n 2kslsslsbr "...I-{w=0.2}incluso si pasar Halloween contigo en su lugar {i}es{/i} bastante asombroso."
        n 2kslsllsbr "..."
        n 4knmpulsbr "...Te escribí algo también,{w=0.5}{nw}"
        extend 5klrbolsbr " sabes."
        n 5clrcalsbr "..."

        $ halloween_poem = jn_poems.getPoem("jn_natsuki_hallows_end")
        $ halloween_poem.unlock()
        play audio page_turn
        $ Natsuki.setDeskItem(jn_desk_items.getDeskItem("jn_poem_on_desk"))
        $ jnPause(2)

        n 5csqcalsbr "..."
        n 4fnmfllsbl "¡H-{w=0.2}hey!{w=0.75}{nw}"
        extend 4fllfllsbl " Vamos."
        n 2cdlbolsbl "No me des esa mirada,{w=0.2} [player].{w=0.75}{nw}"
        extend 2ccsemlsbl " Solo..."
        n 1ksrpulsbl "..."
        n 1ccsfll "...Solo tómalo ya.{w=1}{nw}"
        extend 4cnmcal " Antes de que cambie de opinión sobre todo el asunto."
        n 4cdrcal "..."

        show natsuki 4kdrcal
        $ jnPause(0.5)
        call show_poem (halloween_poem)
        show natsuki 1cnmcal

        n 1cnmajl "Tú..."
        n 4cllajl "Realmente leíste todo eso..."
        n 5csgsll "¿Verdad?"
        n 2ccseml "Porque no tienes {i}idea{/i} de qué dolor fue eso con tan poco aviso.{w=0.75}{nw}"
        extend 2clleml " Especialmente contigo merodeando todo el tiempo.{w=1}{nw}"
        extend 2ccspol " Tonto."
        n 1clrbolsbl "..."
        n 4ksrpulsbl "Pero..."
        n 4ksgpulsbl "¿En serio,{w=0.2} [player]?"
        n 1kslsllsbl "..."

        show natsuki 4ccsunlsbl zorder JN_NATSUKI_ZORDER at jn_center
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(2)
        play audio clothing_ruffle
        $ jnPause(3.5)
        show natsuki 5cslbolsbr zorder JN_NATSUKI_ZORDER at jn_center
        hide black with Dissolve(1.25)

        n 5kslpul "...G-{w=0.2}gracias.{w=0.75}{nw}"
        extend 2knmbol " Por estar conmigo en Halloween,{w=0.2} quiero decir."
        n 4ccsfll "Sé que realmente nunca conseguí disfrazarme,{w=0.75}{nw}"
        extend 4cdrfll " o hacer toneladas de decoraciones elegantes,{w=0.75}{nw}"
        extend 1ksrsll " o ir de fiesta ni nada emocionante como eso."
        n 1nlrpul "Pero...{w=1.25}{nw}"
        extend 5nsrssfsbl " S-{w=0.2}supongo que puedo conformarme con invitarme a ti en su lugar."
        n 5nsrajlsbl "Así que..."
        n 1csrfslsbl "...Sí."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4cchsmlsbl "F-{w=0.2}feliz Halloween,{w=0.2} [chosen_endearment]."
        n 4cslsmlsbl "..."
        n 2ccsfllsbr "A-{w=0.2}ahora,{w=0.2} suficiente de todas las cosas acarameladas.{w=0.75}{nw}"
        extend 2cllfllsbr " Cielos,{w=0.2} [player]."
        n 2csqpo "¿Has olvidado {i}totalmente{/i} para qué se supone que es hoy ya o qué?"
        n 4fsqsm "..."
        n 4fsqss "¿No?"
        n 2fcsss "Je.{w=0.75}{nw}"
        extend 2ccsbg " Entonces será mejor que empieces a prepararte,{w=0.2} [player]."
        n 4cslbgsbr "Estar aquí contigo puede ser un dulce..."
        $ jn_stickers.stickerWindowPeekUp(at_right=True)
        n 4fsqbs "...¡Pero puedes apostar que todavía tengo una tonelada de {i}trucos{/i} bajo la manga!{w=0.75}{nw}"
        extend 2nchgn " Jejeje."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(1)
        play audio drawer
        $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.centre)
        $ jnPause(2)
        hide black with Dissolve(0.5)

        $ chosen_tease = jn_utils.getRandomTeaseName()
        n 2uchgnl "¡Ahora pongámonos espeluznantes ya,{w=0.2} tú [chosen_tease]!"
        $ persistent._jn_player_love_halloween_seen = True
    else:

        n 3cslss "..."
        n 4cslfl "O...{w=1}{nw}"
        extend 4cslsl " al menos lo sería.{w=0.75}{nw}"
        extend 2fsrem " Si {i}algunas personas{/i} no insistieran en ser completos idiotas al respecto."
        n 2fcsfl "Ugh."
        n 2clrfl "Como,{w=0.2} no me malinterpretes -{w=0.5}{nw}"
        extend 4fcsaj " ¡siempre estoy lista para una buena broma!{w=0.75}{nw}"
        extend 4ccspo " No soy susceptible,{w=0.2} obviamente."
        n 2fslan "¡Pero lo que no puedo {i}soportar{/i} es cuando algunas personas lo llevan {i}demasiado{/i} lejos!{w=0.75}{nw}"
        extend 1fsqem " O simplemente son verdaderos idiotas sobre todo el asunto."
        n 4fcsfl "Sí.{w=0.75}{nw}"
        extend 4fsgfl " Conoces el tipo,{w=0.2} [player]."
        n 3ftrfl "{i}Bromistas{/i},{w=0.5}{nw}"
        extend 3fsran " una mierda."
        n 4fnmgs "¡En serio!"
        n 4fllem "Entiendo que la noche de travesuras es una cosa también."
        n 2fcswr "¡¿Pero qué clase de 'travesura' implica solo cabrear a la gente?!{w=0.75}{nw}"
        extend 2fnmfu " ¿O ir por todas partes y quedar como un completo idiota?"
        n 2fcsan "Dame un respiro."
        n 4csqan "Y ni siquiera me {i}hagas{/i} empezar sobre mantener a todos despiertos toda la noche con música de porquería..."
        n 3fsrem "...O destrozando un montón de cosas de otras personas a propósito."
        n 3fcsemesi "Ugh..."
        n 4cllsl "Olvida los huevos y el papel higiénico."
        n 5fslsl "Solo me hace querer darles un bofetón justo en sus estúpidas caras.{w=0.75}{nw}"
        extend 2fcsgs " ¿Quién dice que eso no es solo {i}mi{/i} versión de una 'broma'?"
        n 2fsrsl "Idiotas."
        n 1fcsflesi "..."
        n 4ccsfl "L-{w=0.2}lo que sea.{w=0.75}{nw}"
        extend 4cnmaj " ¿Sabes qué,{w=0.2} [player]?"
        n 2flrfl "¿Quién tiene el tiempo para preocuparse por un montón de idiotas arruinando las cosas para ellos mismos?{w=0.75}{nw}"
        extend 2fcspo " Yo seguro que no."
        n 1ccsaj "Y-{w=0.2}y además."

        if Natsuki.isLove(higher=True):
            n 3cllssl "Ambos sabemos que {i}tú{/i} no eres así.{w=0.75}{nw}"
            extend 5ccssslsbr " E-{w=0.2}eso es todo lo que importa."

        elif Natsuki.isAffectionate(higher=True):
            n 7cllsslsbr "Estoy bastante segura de que {i}tú{/i} no eres así.{w=0.75}{nw}"
            extend 3ccssslsbr " Incluso si eres un tonto."
        else:

            n 7csqss "Dudo un poco que {i}tú{/i} seas una de esas personas."

        n 3clrss "Y no es como si tuviéramos que preocuparnos por nada de eso aquí tampoco,{w=0.2} de todos modos."
        n 4fcsaw "¡Así que!"
        n 4fsqbg "Espero que te hayas preparado,{w=0.2} [player]."
        n 2ccsbg "Porque si no has preparado suficientes dulces hoy para tu servidora..."
        $ jn_stickers.stickerWindowPeekUp(at_right=True)
        n 2fchgn "...¡Entonces será mejor que te prepares para algunos trucos más de primera en su lugar!{w=0.75}{nw}"
        extend 1nchgn " Jejeje."

        if Natsuki.isLove(higher=True):
            $ chosen_tease = jn_utils.getRandomTeaseName()
            n 2fwlbgl "Te amo también,{w=0.5}{nw}"
            extend 2fchblleaf " ¡gran [chosen_tease]!"

        elif Natsuki.isAffectionate(higher=True):
            $ random_tease = random.choice(["tonto", "bobo"])
            n 3fchbgl "¡Ahora pongámonos espeluznantes ya,{w=0.2} tú [random_tease]!"
        else:

            n 3fnmbg "¡Ahora pongámonos espeluznantes ya!"

    $ jn_events.getHoliday("holiday_halloween").complete()
    return

label holiday_christmas_eve:
    python:
        import copy


        jn_atmosphere.showSky(jn_atmosphere.WEATHER_SNOW)


        jn_outfits.getWearable("jn_headgear_santa_hat").unlock()
        santa_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        santa_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_santa_hat")
        santa_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(santa_hat_outfit)


        jn_events.getHoliday("holiday_christmas_eve").run()

    n 1uchbg "¡Heeeey!{w=0.75}{nw}"
    extend 4uchbs " ¡[player]!{w=0.5} ¡[player]!"
    n 1uchgnedz "¿Adivina qué día es?"
    n 1tsqsm "..."
    n 1fsqsm "Jejeje.{w=0.5}{nw}"
    extend 1fchbl " ¡Como {i}si{/i} necesitara recordártelo!"
    n 3ulraj "Cielos..."
    n 3tnmsssbr "Es difícil creer que ya sea Nochebuena,{w=0.2} ¿eh?"
    n 3nsrsssbr "Es casi espeluznante lo rápido que llega en realidad.{w=1}{nw}"
    extend 1uwdajsbr " ¡En serio!"
    n 1fllem "Digo...{w=1}{nw}"
    extend 1nsqbo " la última parte del año se siente principalmente como un gran festival del aburrimiento."
    n 2nsrem "La escuela empieza de nuevo,{w=0.75}{nw}"
    extend 2fslem " se pone todo frío y desagradable afuera,{w=0.75}{nw}"
    extend 2nsqpo " todos se quedan atrapados adentro..."
    n 1fnmem "¿Pero luego antes de que te des cuenta?{w=1}{nw}"
    extend 1fcsgs " Diciembre llega,{w=0.75}{nw}"
    extend 1fbkwr " ¡y es como si se desatara el infierno!"
    n 3fslan "¡Cada vez!{w=0.5} ¡Como un reloj!"
    n 3fcsemsbr "Cielos,{w=0.5}{nw}"
    extend 1tsqemsbr " pensarías que con un {i}año{/i} entero para prepararse,{w=1}{nw}"
    extend 1fslcasbr " la gente no dejaría {i}siempre{/i} las cosas para el último mes."
    n 3flrem "Como...{w=0.75}{nw}"
    extend 3fcswr " ¿quién se {i}hace{/i} eso a sí mismo?"
    n 1fcsajeansbr "Oh,{w=0.75}{nw}"
    extend 1fcsgs " y ni siquiera me {i}hagas{/i} empezar con la música que {i}cada{w=0.3} maldita{w=0.3} tienda{/i}{w=0.3} siente la necesidad de poner..."
    n 1fslsl "Ugh..."
    n 1fcspoesi "Lo juro,{w=0.2} es como algún tipo de dolor de oído coordinado."
    n 1fllca "..."
    n 1unmgslsbl "¡N-{w=0.3}no me malinterpretes!{w=0.75}{nw}"
    extend 3fcsgslsbl " ¡No soy ningún Scrooge{nw}"
    extend 3fcspolsbr "!"
    n 1fcsbglsbr "...S-{w=0.2}solo no estoy atrapada en las {i}Navidades pasadas{/i},{w=0.2} ¡eso es todo!{w=0.75}{nw}"
    extend 4fchsml " Jejeje."
    n 1ullss "Bueno,{w=0.75}{nw}"
    extend 1nllbg " lo que sea.{w=1}{nw}"
    extend 1fchgn " Al menos {i}aquí{/i} podemos cambiar el disco,{w=0.2} ¿verdad?"
    n 1fsqbg "Y hablando de eso..."
    n 4uchsmedz "¿Qué opinas de mis habilidades de decoración,{w=0.2} [player]?{w=0.75}{nw}"
    extend 4fwlbgeme " Nada mal para {i}solo{/i} útiles escolares,{w=0.2} si lo digo yo misma."
    n 1fchbl "¡Solo no me preguntes de dónde saqué el árbol!"
    n 1usqsm "...{w=1}{nw}"
    n 4uwdajeex "¡Ah!{w=1}{nw}"
    n 3fnmbg "¿Pero qué hay de ti,{w=0.2} [player]?{w=1}{nw}"
    extend 3fsqsg " ¿Eh?"
    n 1fcsbg "No pensaste {i}seriamente{/i} que te habías salvado de decorar,{w=0.2} ¿o sí?"
    n 1fchbg "¡Lo siento!{w=0.75}{nw}"
    extend 1uchgnelg " ¡Ni lo sueñes!"
    n 4fcsbg "Así que...{w=1}{nw}"

    show natsuki 1tsqsm at jn_center

    menu:
        extend " ¿Ya {i}estas{/i} listo,{w=0.2} [player]?"
        "¡Puedes apostar que sí!":

            n 1usqct "¿Ojo?"
            n 1fchbg "¡Bueno,{w=0.2} no es broma!{w=1}{nw}"
            extend 2fcsbs " Ahora eso es {i}exactamente{/i} lo que me gusta escuchar."
            n 1fchbs "¡Este año va a ser {b}asombroso{/b}!{w=0.75}{nw}"
            extend 1uchgnedz " ¡Simplemente lo sé!"

            $ persistent._jn_player_celebrates_christmas = True
        "Aún no he decorado.":

            n 1uskemlesh "¡¿H-{w=0.2}eh?!"
            n 1fbkwrl "E-{w=0.2}entonces qué estás haciendo sentando por aquí,{w=0.2} ¡¿tontito?!{w=0.75}{nw}"
            extend 3fcsajlsbl " Cielos..."
            n 3fcspolsbl "No voy a hacer {i}tu{/i} lugar también,{w=0.2} sabes."
            n 1fchbl "...No {i}gratis{/i},{w=0.2} de todos modos."

            $ persistent._jn_player_celebrates_christmas = True
        "Realmente no celebro la Navidad.":

            n 4kslpu "...Aww.{w=0.75}{nw}"
            extend 4knmbo " ¿En serio?"
            n 1kllsl "..."
            n 1fcstrlsbr "D-{w=0.2}digo,{w=0.75}{nw}"
            extend 1fchsmlsbl " eso está totalmente bien."
            n 2fsqsslsbl "...¡Solo significa que tengo que celebrar por los dos!{w=0.75}{nw}"
            extend 2fchsmleme " Jajaja."

            $ persistent._jn_player_celebrates_christmas = False

    n 1kslsm "..."
    n 1kslpu "Pero...{w=1}{nw}"
    extend 4knmpu " ya en serio,{w=0.2} [player]?"
    n 2ksrbosbl "..."

    if Natsuki.isEnamored(higher=True):
        n 1kcscalsbl "...Gracias."
        n 2ksrajlsbl "Por venir a verme hoy,{w=0.2} quiero decir."
        n 4knmajl "Es..."
        n 4kslpul "..."
        n 1kcsbolesi "En serio significa mucho.{w=1}{nw}"
        extend 4kwmbol " Que estés aquí ahora mismo."
        n 2ksrbol "...Probablemente más de lo que sabrías."
        n 1klrbol "..."
        n 1kwmpuf "...Realmente debería haber estado pasando el día de hoy con mis amigos,{w=0.2} [player].{w=1}{nw}"
        extend 1kllbol " Pero..."

        if Natsuki.isLove(higher=True):
            n 4kwmfsfsbr "C-{w=0.3}creo que puedo conformarme solo contigo."
        else:

            n 2nslfsfsbr "Probablemente puedo conformarme contigo este año."

        n 1kslbol "..."
        n 1kslpul "Y...{w=0.75}{nw}"
        extend 4ksqbol " ¿[player]?"
        n 2ksrfsfsbr "..."
        show natsuki 1fcscafsbr

    elif Natsuki.isAffectionate(higher=True):
        n 1kcscalsbl "...G-{w=0.2}gracias."
        n 1fcsemlsbl "P-{w=0.3}por estar aquí hoy,{w=0.75}{nw}"
        extend 2kslbolsbl " quiero decir."
        n 1fcsbolsbr "S-{w=0.3}sé que no tenías que venir a visitarme en absoluto.{w=0.75}{nw}"
        extend 2ksrpulsbl " Y sería una verdadera idiota al exigirlo..."
        n 1knmpulsbl "Así que solo..."
        n 1kslunlsbl "..."
        n 1fcsunf "Solo...{w=0.75} que sepas que lo aprecio.{w=1.25}{nw}"
        extend 4kwmunl " ¿Va?"
        n 2kslbol "De verdad.{w=1.25}{nw}"
        extend 4ksqbol " Gracias."
        n 1ksrcal "..."
        n 1ksrajlsbr "Y...{w=1}{nw}"
        extend 4knmajlsbr " ¿[player]?"
        n 1kcsunfsbr "..."
        show natsuki 2fcssrfsbr
    else:

        n 1kcscalsbl "...Gracias.{w=0.75}{nw}"
        extend 1fcsemlsbl " P-{w=0.3}por aparecer hoy,{w=0.2} quiero decir."
        n 3fcsgslesssbr "¡S-{w=0.2}sabía que lo harías,{w=0.2} por supuesto!"
        n 3fcscal "Y-{w=0.2}y además."
        extend 3fsrcal " Solo un verdadero idiota dejaría a alguien completamente solo aquí,{w=1}{nw}"
        extend 1klrcafsbr " de todas las noches."
        n 1fcsajlsbr "Así que yo..."
        n 1fllajlsbr "Yo..."
        n 4kslsllsbr "..."
        n 1fcsunlsbr "Yo...{w=1.25}{nw}"
        extend 1kcspufesisbr " realmente lo aprecio.{w=0.75}{nw}"
        extend 4kwmbolsbr " De verdad."
        n 4kslbolsbr "..."
        n 4kwmpulsbr "...Y-{w=0.2}y [player]?"
        n 2fslunfsbl "..."
        show natsuki 1fcsunfesssbl

    play audio chair_out
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)

    if Natsuki.isEnamored(higher=True):
        play audio clothing_ruffle

        if Natsuki.isLove(higher=True):
            $ jnPause(2.5)
            play audio kiss

        show natsuki 1kcsfsf at jn_center
    else:

        play audio clothing_ruffle
        show natsuki 4kcsbol at jn_center

    $ jnPause(3)
    play audio chair_in
    $ jnPause(2)

    if Natsuki.isLove(higher=True):
        show overlay mistletoe zorder JN_OVERLAY_ZORDER at jn_mistletoe_lift

    hide black with Dissolve(1.25)

    if Natsuki.isLove(higher=True):
        n 4fchsmf "¡C-{w=0.2}cuidado con el muérdago!"
        n 4fchtsfeaf "Jejeje."
        hide overlay

    elif Natsuki.isEnamored(higher=True):
        n 2kslsmlsbl "E-{w=0.2}entonces..."
        n 4kwmsml "¿De qué querías hablar,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fchsmlsbr " Jejeje."
    else:

        n 2kslfsl "..."
        n 1ncsajlsbl "A-{w=0.3}ahora,{w=1}{nw}"
        extend 4tsqsslsbl " ¿dónde estábamos?"
        n 3fsrdvlsbr "Jejeje..."

    $ Natsuki.calculatedAffinityGain(5, bypass=True)
    $ jn_events.getHoliday("holiday_christmas_eve").complete()

    return

label holiday_christmas_day:
    python:

        jn_atmosphere.showSky(jn_atmosphere.WEATHER_SNOW)


        christmas_outfit = jn_outfits.getOutfit("jn_christmas_outfit")
        christmas_outfit.unlock()
        jn_outfits.saveTemporaryOutfit(christmas_outfit)


        jn_events.getHoliday("holiday_christmas_day").run()

    n 1uwdgsesu "¡Ay dios mío!{w=0.5}{nw}"
    extend 4uchbsl " ¡Ay dios mío ay dios mío ay dios mío ay dios mío ay dios míooo!"
    n 1unmbgleex "!{w=0.5}{nw}"
    n 4uwdbgl "¡[player]!{w=0.75}{nw}"
    extend 4uwdbsl " ¡[player]!{w=0.2} ¡[player]!"
    n 1uchbsl "¡Está aquí!{w=0.75}{nw}"
    extend 1uchbgl " ¡Maldita sea,{w=0.5}{nw}"
    extend 1fchbsl " finalmente,{w=0.5}{nw}"
    extend 4uchgnleme " por fin {i}ESTA AQUÍ{/i}!"

    if jn_get_current_time_block in [JNTimeBlocks.early_morning, JNTimeBlocks.mid_morning, JNTimeBlocks.late_morning]:
        n 3fspgs "¡Vamos!{w=0.75}{nw}"
        extend 1knmgs " ¡Quítate el sueño de los ojos ya,{w=0.2} [player]!"
        n 1fcsss "¡Arriba y a ello!{w=0.5}{nw}"
        extend 4fchbg " ¡Vamos,{w=0.2} [player]!"
    else:

        n 3fspgs "¿Qué te {i}tomó{/i} tanto tiempo siquiera?{w=0.75}{nw}"
        extend 3fsqpoesi " ¿Olvidaste qué día era o algo así?{w=0.5}{nw}"
        extend 3fcsgs " ¡Es hora de celebrar!"
        n 1fcsbg "Porque..."

    n 4uchbsleme "¡ES NAVIIIDAAAD!{w=1}{nw}"
    extend 1uchsmleme " ¡Jejeje!"
    n 1kcssslesi "..."
    n 1kcsss "Viejo,{w=0.75}{nw}"
    extend 3fchsm " se siente tan bien decir eso {i}finalmente{/i}..."
    n 1ullss "Digo...{w=0.75}{nw}"
    extend 2tllss " no es como si tuviera toneladas planeadas o algo.{w=1}{nw}"
    extend 2nsrss " ...No es como si hubiera mucho {i}que{/i} planear aquí."
    n 1ncsss "Pero simplemente hay algo sobre la Navidad que trae esa sensación de alivio,{w=0.5}{nw}"
    extend 4ksqsm " ¿sabes?"
    n 1fcssm "Los estudios pueden irse a pasear,{w=0.75}{nw}"
    extend 1ullaj " todo está arreglado y listo para ir para todos..."
    n 1tnmss "E incluso si es solo por un par de días..."
    n 4fchbg "¡Solo tener todo ese peso y estrés removido {i}es lo máximo{/i}!{w=1}{nw}"
    extend 4uchgn " ¡Es genial!"
    n 1kcsssesi "Como si pudiera sentir el estrés del año lavándose de mí..."
    n 4fwlbl "¡Y ni siquiera tengo que cocinar nada aquí!{w=0.75}{nw}"
    extend 1fchsm " Jejeje..."
    n 2kslsm "..."
    n 1kslsr "..."
    n 1kcssr "..."
    n 1ncspu "Es...{w=0.75}{nw}"
    extend 2kslpu " duro a veces,{w=1}{nw}"
    extend 2kslsl " ya sabes."
    n 2ksqsl "La Navidad,{w=0.2} quiero decir."
    n 2klrbo "..."
    n 1kcspuesi "..."
    n 4ksrslsbl "...Cómo {i}siquiera{/i} digo esto..."
    n 1fcsunsbl "..."
    n 1fcsaj "Nosotros..."
    n 2ksrsl "N-{w=0.2}nosotros siempre fuimos 'tradicionales',{w=0.2} mi familia.{w=1}{nw}"
    extend 1ksqsl " S-{w=0.2}si nos preguntaban."
    n 2ncsss "...Je.{w=1}{nw}"
    extend 4tsqbo " ¿Por qué,{w=0.2} te preguntas?"
    n 2kslbo "...Piénsalo,{w=0.2} [player]."
    n 1ksqsr "..."
    n 1fcssr "...No necesitas comprar regalos,{w=0.2} si eres {i}tradicional{/i}.{w=1.25}{nw}"
    extend 2fsrsl " No necesitas invitar huéspedes,{w=0.2} si eres {i}tradicional{/i}."
    n 1ksqsl "..."
    n 1kllpu "Ves a dónde voy con esto...{w=1}{nw}"
    extend 4ksqbo " ¿verdad?"
    n 2fcsunl "N-{w=0.2}no celebrarla no era una {i}elección{/i} en mi casa,{w=0.2} [player]."
    n 1fcsbol "..."
    n 1ncspul "Así que..."
    n 1nnmbo "...Hice la mía propia.{w=0.75}{nw}"
    extend 2kllbo " Me escapaba."
    n 2ncsss "Je.{w=0.75}{nw}"
    extend 4nslss " Ya me había vuelto {i}realmente{/i} buena en averiguar dónde estaban las tablas del piso que crujían,{w=0.5}{nw}"
    extend 1nslfs " te diré eso."
    n 2kslsll "Solo me iba por un par de horas."
    n 1nsrssl "Seguro,{w=0.3} hacía frío,{w=0.75}{nw}"
    extend 1ksrsrl " pero..."
    n 1fsrunl "Al menos ver todas las decoraciones en las casas de la gente me daba {i}algo{/i} de alegría."
    n 1fslsll "Además.{w=0.3} No es como si a {i}ellos{/i} particularmente les importara dónde estaba..."
    n 1kslsll "..."
    n 4ksqbol "Pero a mis amigas siempre sí."
    n 4knmpul "...Ya habíamos arreglado algo,{w=1}{nw}"
    extend 4knmbolsbr " sabes."
    n 1kllbolsbr "Para Navidad.{w=1}{nw}"
    extend 2tnmbolsbr " ¿No te dije,{w=0.2} [player]?"
    n 1nllss "Estaba {i}destinada{/i} a reunirme con todas,{w=0.75}{nw}"
    extend 4nslfs " y se suponía que iríamos a lo de Yuri juntas."
    n 2kslss "...Je.{w=0.75}{nw}"
    extend 4knmbo " Había tanta charla sobre a dónde iríamos todas."
    n 1klrsssbl "Sayori se emocionó tanto por ser anfitriona...{w=0.75}{nw}"
    extend 2nsrsssbl " pero habría estado {i}demasiado{/i} apretado para todas nosotras."
    n 1nlraj "Aunque...{w=1}{nw}"
    extend 1tnmbo " ¿en serio?"
    n 1kslbo "..."
    n 1kcsaj "Yo...{w=0.75}{nw}"
    extend 2kslfs " nunca le presté mucha atención realmente."
    n 1ucsaj "La casa de Sayori,{w=0.75}{nw}"
    extend 1nlraj " la de Monika...{w=1}{nw}"
    extend 4ksrfs " Honestamente ni siquiera importaba."
    n 1knmbo "...¿A dónde fuera que iba?{w=1}{nw}"
    extend 4tnmpu " ¿Mientras estuviéramos todas juntas?"
    n 1kllbol "..."
    n 2fcsunl "E-{w=0.3}es ahí donde estaba {i}mi{/i} hogar."
    n 2fcsunltsa "..."
    n 2fllunltsc "Ni siquiera me importaba lo que recibía."
    n 2fcsunl "No importaba.{w=1}{nw}"
    extend 4ksrsll " N-{w=0.2}no realmente."
    n 1kcsajl "Solo...{w=1}{nw}"
    extend 2fcsunl " calidez.{w=0.5} P-{w=0.2}personas a las que realmente les {i}importaba{/i}."
    n 2fcsemltsa "N-{w=0.2}no el dinero.{w=1}{nw}"
    extend 2ksrboltsb " Yo.{w=1}{nw}"
    extend 1ksrpultsb " Inlcuso si nunca pude conseguirles {i}nada{/i}..."
    n 1fcsunlsbl "...Ese era regalo suficiente para mí."
    n 1fcsajlsbl "Así que es por eso..."
    n 2flrajltscsbl "A-{w=0.3}así que es..."
    n 2klremltscsbl "...e-{w=0.3}es...{w=1}{nw}"
    extend 2fcsemltsd " p-{w=0.3}por qué..."
    n 2kcsupltsd "..."
    n 2kcsanltsd "..."

    $ prompt = "Natsuki..." if Natsuki.isEnamored(higher=True) else "¿Natsuki?"
    menu:
        "[prompt]":
            pass

    n 2fcsunltsd "E-{w=0.3}estoy bien.{w=1}{nw}"
    extend 2fcsemltsa " ¡Estoy bien!"
    n 1kcsboltsa "..."
    n 1kcspultsa "E-{w=0.2}es solo que..."
    n 4kslpultsb "..."
    n 1kcspultsb "..."
    n 1kcsboltsb "..."
    n 4ksqboltsb "...Ellas ya no están aquí,{w=0.2} [player].{w=1.25}{nw}"
    extend 1kslpultsb " No han estado aquí por mucho tiempo ya."
    n 2kllboltdr "...S-se han ido."
    n 1kwmboltdr "Pero nunca dejaron de ser mis amigas.{w=1.25}{nw}"
    extend 1kcsbol " Y-{w=0.2}y supongo que es por eso que sigo celebrando."
    n 3kslfsl "...Por ellas."

    if Natsuki.isEnamored(higher=True):
        n 1ksqbol "..."
        n 3ksrfslsbl "...Y-{w=0.3}y por ti."

    n 4kslpul "Así que..."
    n 1knmpul "..."
    n 1kcspul "...Gracias,{w=0.2} [player].{w=1}{nw}"
    extend 2ksrpolsbl " De verdad."
    n 1kcssllsbl "No tengo a {i}todas{/i} mis amigas ahora mismo,{w=0.75}{nw}"
    extend 2ksrbol " pero..."

    if Natsuki.isLove(higher=True):
        n 2ksqbol "...¿Solo tenerte aquí,{w=0.2} [player]?"
        n 1kslfsl "Je."
        n 1kllssl "...Sí.{w=1}{nw}"
        extend 4kcssmfsbl " {i}Sé{/i} que puedo arreglármelas."

    elif Natsuki.isEnamored():
        n 2kslsmlsbl "...Creo que puedo arreglármelas solo contigo."

    elif Natsuki.isAffectionate():
        n 4nslsslsbl "...A-{w=0.2}al menos tengo al mejor."
    else:

        n 1ncsbol "Creo..."
        n 1ncspulesi "..."
        n 1ncscal "C-{w=0.2}Creo que incluso solo uno aquí es suficiente por ahora."

    if persistent._jn_player_celebrates_christmas == False:
        n 2nslsslsbr "Incluso si {i}no{/i} celebras realmente la Navidad."

    $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
        poem_list=jn_poems.getAllPoems(),
        unlocked=False,
        holiday_types=[jn_events.JNHolidayTypes.christmas_day],
        affinity=Natsuki._getAffinityState()
    )
    $ unlocked_poem_pool.sort(key = lambda poem: poem.affinity_range[0])
    $ christmas_poem = unlocked_poem_pool.pop() if len(unlocked_poem_pool) > 0 else None

    if christmas_poem:
        $ christmas_poem.unlock()


        n 1nllsllsbl "..."
        n 4knmcalsbl "...Te conseguí algo,{w=0.2} sabes."
        n 1fsrunlsbl "..."
        n 3fnmajlsbl "¡H-{w=0.3}hey!{w=0.75}{nw}"
        extend 3fcspolsbr " No me des esa mirada."
        n 1fcstrlsbr "No pensaste {i}seriamente{/i} que todo lo que tenía para darte era una {i}historia{/i},{w=0.2} ¿o sí?"
        n 1fcsemlsbr "Tenía que al menos {i}intentarlo{/i},{w=0.75}{nw}"
        extend 4kllbolsbr " a-{w=0.2}así que..."

        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1knmbofsbr "..."
            n 2fcscalsbr "...S-{w=0.2}solo míralo ya,{w=0.2} [chosen_tease]."
            show natsuki 1kcscalsbr at jn_center
        else:

            n 1nslunlsbr "..."
            n 2fcsunlsbl "¡Nnnnnnn-!"
            n 2fcsemlsbl "...S-{w=0.2}solo...{w=1}{nw}"
            extend 2ksrsllsbl " léelo ya,{w=0.2} [player].{w=1.25}{nw}"
            extend 2fcssllsbl " {i}A-antes{/i} de que cambie de opinión."
            show natsuki 1ksrsllsbl at jn_center

        call show_poem (christmas_poem)

        if Natsuki.isEnamored(higher=True):
            n 4ksqcalsbr "...¿Terminaste,{w=0.2} [player]?"
            n 1kslcalsbr "..."
            n 1kcsbolsbl "...Mira.{w=1}{nw}"
            extend 1fcseml " Estoy..."
            n 1kslbol "..."
            n 3ksqbol "No voy a engañarme y decir que este fue un regalo {i}asombroso{/i}."
            n 3nsrsssbl "...No es como si fuera la {i}primera{/i} en darte un poema."
            n 1ncsajsbl "Solo..."
            n 1kslsllsbl "..."
            n 1kcssllsbl "S-{w=0.2}solo quería mostrar algo de aprecio.{w=1}{nw}"
            extend 4ksqcal " P-{w=0.2}por todo."
            n 1kcsajl "Esto...{w=0.75}{nw}"
            extend 1kcssll " en serio...{w=0.75}{nw}"
            extend 4kwmsll " s-{w=0.2}significa mucho para mí,{w=0.2} [player]."
            n 1kslbol "D-{w=0.2}de verdad."
            n 4kwmfsl "...Gracias."
        else:

            n 2nsqsllsbl "..."
            n 2tsqcalsbl "¿Todo listo,{w=0.2} [player]?{w=1}{nw}"
            extend 2nslssl " Viejo..."
            n 1fcsajlsbl "Y-{w=0.2}ya era hora,{w=0.2} ¿eh?{w=1}{nw}"
            extend 3flrajlsbl " Lo juro,{w=0.5}{nw}"
            extend 3fcspolsbl " a veces es como si {i}necesitaras{/i} que te lean las cosas o algo así.{w=0.75}{nw}"
            extend 1fsrfslsbl " Je."
            n 1ksrbol "..."
            n 1kcsbolesi "..."
            n 4fslbol "...Sé que no fue mucho.{w=0.75}{nw}"
            extend 1kslsll " No voy a engañarme."
            n 3fsrunlsbr "S-{w=0.2}sé que no puedo conseguirte algún {i}regalo elegante{/i}.{w=0.75}{nw}"
            extend 3fsrajlsbr " Es solo que..."
            n 1ksrbolsbr "..."
            n 1fcsbofsbr "...Quiero que sepas que aprecio lo que has hecho.{w=1}{nw}"
            extend 4fsldvlsbl " Incluso si es solo escucharme divagar a veces."
            n 1nllpulsbl "Realmente..."
            n 1fcsunlsbl "..."
            n 1kcscalsbl "..."
            n 1ksqcalsbl "S-{w=0.2}Significa mucho para mí,{w=0.2} [player]."
            n 2ksrcafsbl "...G-gracias."
    else:

        n 2kllbol "..."

        if Natsuki.isEnamored(higher=True):
            n 4kwmfsl "...¿Y [player]?"
            show natsuki 1fcscalsbl at jn_center
        else:

            n 1kllpul "...Y...{w=1}"
            extend 4knmsll " ¿[player]?"
            n 1ksrsllsbl "..."
            show natsuki 1fcsunlsbl at jn_center

    play audio chair_out
    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)

    if Natsuki.isEnamored(higher=True):
        play audio clothing_ruffle
        $ jnPause(2.5)
        play audio kiss
        show natsuki 1kcsfsf at jn_center
    else:

        play audio clothing_ruffle
        show natsuki 1kcsbol at jn_center

    $ jnPause(3)
    play audio chair_in
    $ jnPause(1)
    hide black with Dissolve(2)
    $ jnPause(2)

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 4kchfsfeaf "...Feliz Navidad,{w=0.2} [chosen_endearment]."
    else:

        n 1fchsmfsbl "F-{w=0.3}feliz Navidad."

    $ jn_events.getHoliday("holiday_christmas_day").complete()

    return

label holiday_new_years_eve:
    $ jn_events.getHoliday("holiday_new_years_eve").run()

    n 4nchbselg "¡[player]!{w=1}{nw}"
    n 4uchlgelg "¡[player]!{w=0.5} ¡[player]!"
    n 1fspaj "¡Mira la fecha!{w=0.5}{nw}"
    extend 1unmbg " ¡¿Siquiera sabes qué día es?!{w=1}{nw}"
    extend 1fspgsedz " ¡Es casi año nuevo!"
    n 3kcsss "Vaya...{w=1}{nw}"
    extend 3fchgn " y ya era hora,{w=0.2} ¿eh?"
    n 4ullaj "No sé tú,{w=0.2} [player]...{w=1}{nw}"
    $ current_year = datetime.date.today().year
    extend 1fchbleme " ¡pero no puedo {i}ESPERAR{/i} para decirle al [current_year] dónde metérselo!"
    n 1fsqsm "Y qué mejor manera de hacer eso...{w=0.75}{nw}"
    extend 1fchgnedz " ¿que un montón de explosiones y bocadillos?"
    n 3fchsml "Jejeje.{w=0.5}{nw}"
    extend 3fchbglelg " ¡Va a ser genial!"

    if Natsuki.isEnamored(higher=True):
        n 1kllsml "..."
        n 1kllpul "Pero...{w=0.75}{nw}"
        extend 4knmbol " ya en serio,{w=0.2} [player]?"
        n 1klrbol "..."
        n 1fcspul "Me...{w=1}{nw}"
        extend 2knmpol " gustaría mucho pasarlo contigo."
        n 1kllpof "..."
        n 2kslunf "...Me gustaría mucho."
        n 2fcsemf "S-{w=0.3}si no tenías nada planeado,{w=0.2} de todos modos.{w=1}{nw}"
        extend 2nwmpol " No voy a ser una idiota al respecto si ya tenías cosas que hacer."
        n 1nlrpul "Aunque...{w=1}{nw}"
        extend 1tnmpul " ¿si no?{w=0.75}{nw}"
        extend 1nslssl " Bueno..."
        n 4nsqsmfsbl "Sabes dónde encontrarme.{w=0.5}{nw}"
        extend 4flldvfsbl " Jejeje."

        if Natsuki.isLove(higher=True):
            n 1uchsmfeaf "¡Te amo,{w=0.2} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1kllsll "..."
        n 4knmsll "...No voy a esperar que dejes todos tus planes para venir a verme,{w=0.5}{nw}"
        extend 1klrbol " ya sabes."
        n 2fcsemlesssbl "S-{w=0.3}sé que ya tienes...{w=1}{nw}"
        extend 2fllsllsbl " una vida.{w=0.75}{nw}"
        extend 1kslsllsbl " Allá afuera."
        n 2fcspol "No voy a ser una completa idiota al respecto.{w=0.75}{nw}"
        extend 1fcsajlsbl " Soy {i}mucho{/i} mejor que eso,{w=0.5}{nw}"
        extend 2fslpolsbr " d-{w=0.3}después de todo."
        n 1kslpulsbr "Pero...{w=1.25}{nw}"
        extend 4knmpulsbl " ¿[player]?"
        n 1ksrunlsbl "..."
        n 3fcspolsbl "...No es como si le dijera {i}no{/i} a tu compañía,{w=0.2} sabes.{w=1}{nw}"
        extend 3fllpofesssbl " M-{w=0.3}mientras no lo pongas todo asqueroso,{w=0.2} de todos modos."
        n 1fsldvfesdsbr "Jejeje."
    else:

        n 1fnmssl "Solo una advertencia sin embargo,{w=0.2} [player]..."
        n 1fsqbgl "{i}Totalmente{/i} espero verte aquí para ello.{w=1}{nw}"
        extend 1fcslgl " ¡Sin excusas!"
        n 1fcsajl "Y-{w=0.3}y además,{w=0.5}{nw}"
        extend 2fsrpofsbl " tú me {i}trajiste{/i} de vuelta para experimentar cosas como esta."
        n 2fsqpolsbr "Es lo menos que puedes hacer...{w=1}{nw}"
        extend 4kwmpolsbr " ¿verdad?"

    $ jn_events.getHoliday("holiday_new_years_eve").complete()

    return

label holiday_natsuki_birthday:
    python:
        import copy


        party_hat = jn_outfits.getWearable("jn_headgear_classic_party_hat")

        if not party_hat.unlocked:
            party_hat.unlock()

        birthday_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        birthday_outfit.headgear = party_hat
        birthday_outfit.hairstyle = jn_outfits.getWearable("jn_hair_ponytail")
        jn_outfits.saveTemporaryOutfit(birthday_outfit)


        jn_utils.deleteFileFromDirectory(os.path.join(renpy.config.basedir, "characters/party_supplies.nats").replace("\\", "/"))

        player_initial = jn_utils.getPlayerInitial()
        player_final = jn_utils.getPlayerFinal(3)
        already_celebrated_player_birthday = jn_events.getHoliday("holiday_player_birthday").is_seen
        jn_atmosphere.showSky(weather=jn_atmosphere.WEATHER_CHERRY_BLOSSOM, with_transition=False)

        jn_events.getHoliday("holiday_natsuki_birthday").run()

    $ jnPause(0.25)
    play audio smack
    show natsuki 1cchanlsbr
    show confetti falling zorder JN_PROP_ZORDER at jn_confetti_fall
    $ jnPause(2.25)
    hide confetti
    show confetti desk zorder JN_PROP_ZORDER

    if persistent._jn_natsuki_birthday_known:
        n 1uskgsleshsbr "¡...!{w=0.75}{nw}"
        n 4ccsemlsbr "E-{w=0.2}espera,{w=0.5}{nw}"
        extend 4cnmemlsbr " ¿qué?{w=0.75}{nw}"
        extend 4cllemlsbl " Esto es..."
        n 4clrwrlsbl "¡Esto es todo...!{w=0.75}{nw}"
        extend 1unmemlsbl " ¿C-{w=0.2}cómo...?!"

        show natsuki idle fluster
        menu:
            "¡Feliz Cumpleaños, [n_name]!":
                pass

        n 4fcsanlsbl "¡Nnnnnnn-!"
        n 4fbkwrf "¡[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 2kbkwrl " ¡¿Qué {i}es{/i} todo estooo?!"
        n 2fcsgslsbl "¡S-{w=0.2}se suponía que {i}olvidarías{/i} todo sobre mi cumpleaños!{w=0.75}{nw}"
        extend 2fllgslsbl " ¡¿Y qué vas y haces?!"
        n 4fbkwrleansbl "¡Vas y me haces el centro de atención de {i}todo{/i}!"
        n 1fcsgsl "Luego solo para colmo,{w=0.5}{nw}"
        extend 4flrgslsbr " ¡es {i}fácilmente{/i} el tipo de atención más vergonzosa también!"
        extend 4ksrfllsbr " Cielos..."
    else:

        n 1uskgsleshsbr "¡...!{w=0.75}{nw}"
        n 4kllfllsbr "¿H-{w=0.2}eh?{w=0.75}{nw}"
        extend 4klrpulsbl " Qué demonios..."
        n 1clrfllsbl "¿Q-{w=0.2}qué es siquiera...?"
        n 1cllunlsbr "Esto...{w=1}{nw}"
        extend 4fsluplsbl " esto es todo..."
        n 4fcsuplsbl "..."
        n 4fcsanlsbl "¡Uuuuuuuu...!"
        n 2fbkwrf "¡[player_initial]-{w=0.2}[player][player_final]!{w=1}{nw}"
        extend 2knmwrl " ¡¿Qué {b}demonios{/b} es todo esto?!{w=0.75}{nw}"
        extend 2fllwrl " ¡¿Me estás {i}bromeando{/i}?!"
        n 4fbkwrl "¡Ni siquiera te {i}dije{/i} mi cumpleaños!{w=0.75}{nw}"
        extend 1clreml " ¡Cómo siquiera tú...!"

        show natsuki idle fluster
        menu:
            "¡Feliz Cumpleaños, [n_name]!":
                pass

        if Natsuki.isEnamored(higher=True):
            n 2ccsgslsbl "¡B-{w=0.2}bueno sí!{w=0.75}{nw}"
            extend 2flremlsbl " ¡No es broma!{w=0.75}{nw}"
            extend 2csrfllsbl " Caray..."
            n 4ksrbolsbl "Deberías saber que odio ser puesta en evidencia así para ahora..."
            n 1ccsbolesisbl "..."
            n 2ccsfll "Lo juro,{w=0.2} [player].{w=0.75}{nw}"
            extend 2csrfll " Eres {i}tan{/i} idiota a veces."
            extend 2csqpol " ¿Sabes eso?"
        else:

            n 1uskeml "¡...!{w=0.5}{nw}"
            n 4fcsanl "¡Uuuuuuu-!"
            n 2fcseml "[player],{w=0.2} lo juro..."
            n 2cslsll "Eres {i}tan{/i} idiota a veces.{w=0.75}{nw}"
            extend 2csqsll " De verdad.{w=1}{nw}"
            extend 1csrcal " Odio ser puesta en evidencia así..."

    if already_celebrated_player_birthday:
        show natsuki 1csrbol
        menu:
            "Solo devolviendo el favor.":
                pass

        n 1unmemlesh "¡...!{w=0.5}{nw}"
        n 4csrbol "..."
        n 2ccseml "...Sí,{w=0.2} sí.{w=0.75}{nw}"
        extend 2nslpol " Sabelotodo."
        n 2ccsfll "Pero va{w=0.5}{nw}"
        extend 2ccsgsl " ¡mos!{w=0.75}{nw}"
    else:

        n 2ccsfllsbl "...Y vamos ya.{w=0.75}{nw}"

    extend 2cdwfllsbr " ¿En serio?{w=0.75}{nw}"
    extend 2cupajlsbr " ¿Simplemente {i}tenías{/i} que conseguir el pastel y todo lo demás también?"
    n 2csrsllsbr "..."
    n 2csrpulsbr "...Y ahora que lo pienso..."
    n 4csqtrl "¿Dónde siquiera {i}encontraste{/i} todo esto?"

    if already_celebrated_player_birthday:
        n 2fsqcal "...¿Y por qué el pastel se ve {i}exactamente{/i} como el que te hice?"
        n 2csrcal "..."
        n 4csrajl "Voy a...{w=0.75}{nw}"
        extend 4csrbolsbl " solo pretender que nunca lo he visto antes."
    else:

        n 4unmemlsbr "¡N-{w=0.2}no es que no me guste ni nada!{w=0.75}{nw}"
        extend 2fcsemlsbr " ¡Está perfectamente bien!{w=1}{nw}"
        extend 2clrsll " Pero..."
        n 1csrbol "..."

    n 1cdwbol "..."
    n 2cslfll "...Vas a hacerme hacer toda la cosa del deseo.{w=0.75}{nw}"
    extend 2ksqsll " ¿No es así?"

    $ jnPause(2)
    show prop cake lit zorder JN_PROP_ZORDER
    play audio necklace_clip
    show natsuki 2cslcal
    $ jnPause(3)

    menu:
        "¡Pide un deseo, [n_name]!":
            pass

    show natsuki 2csqcal
    $ jnPause(3)

    n 2clrsll "..."
    n 2ccspulesi "..."
    n 2cslpol "...Bien.{w=1}{nw}"

    if Natsuki.isLove(higher=True):
        extend 1ccscaf " P-{w=0.2}pero solo porque eres tú.{w=0.75}{nw}"
        extend 4csqcaf " ¿Entendido?"

    elif Natsuki.isEnamored(higher=True):
        extend 1ccsajl " P-{w=0.2}pero solo porque hiciste todo...{w=1}{nw}"
        extend 4ksrcal " esto."

    elif Natsuki.isAffectionate(higher=True):
        extend 1ccsajl " P-{w=0.2}pero solo porque pusiste el esfuerzo.{w=0.75}{nw}"
        extend 4csqcal " ¿Entendido?"
    else:

        extend 1ccsajl " Pero {i}solo{/i} porque me vería como una total idiota de lo contrario.{w=0.75}{nw}"
        extend 4fsqcal " ¿Capiche?"

    show natsuki 1ncsca
    $ jnPause(5)
    show natsuki 1ccsaj
    show prop cake unlit zorder JN_PROP_ZORDER
    play audio blow
    $ jnPause(0.5)
    show natsuki 1ccsbo
    $ jnPause(4)

    if Natsuki.isEnamored(higher=True):
        n 1ncsss "...Je.{w=1.25}{nw}"
        extend 2clrsm " Ni siquiera puedo {i}recordar{/i} la última vez que pude hacer eso."
        n 2clrsl "..."
        n 2clrpu "Pero...{w=1}{nw}"
        extend 2cnmpu " ¿[player]?"
        n 1kslsll "..."
        n 1klrsll "...Gracias.{w=1}{nw}"
        extend 1kcsfll " P-{w=0.2}por todo esto..."
        extend 4cslfll " esto."
        n 4ccsfll "Esto..."
        n 4ksrcalsbl "..."
        n 2ksrajlsbl "...Realmente significa mucho."
        n 2ccsajlsbl "Y-{w=0.2}y no solo debido a las decoraciones llamativas,{w=0.2} o el tonto pastel.{w=0.75}{nw}"
        extend 2cllsllsbl " Puedo vivir sin esas cosas.{w=1.25}{nw}"
        extend 2cslbol " He {i}vivido{/i} sin esas cosas."
        n 1ksrcal "...Probablemente más veces de las que pensarías."
        n 4ccspu "Es solo que..."
        n 4clrun "..."
        n 1clrpul "Nadie...{w=1}{nw}"
        extend 1csrpul " nunca...{w=1}{nw}"
        extend 1ccsunl " realmente...{w=1}{nw}"
        extend 2cslunl " se había esforzado tanto antes."
        n 2kslsllsbr "...Por mí."
        n 4kslbolsbr "Y solo estaría mintiendo si dijera que no estaba intentando aún acostumbrarme a ello."
        n 1cnmemlsbr "¡N-{w=0.2}no es como si a {i}nadie{/i} le hubiera importado lo suficiente!{w=0.75}{nw}"
        extend 1clrfll " Sé que las otras habrían hecho {i}algo parecido{/i}.{w=0.75}{nw}"
        extend 4clrajl " Sayori,{w=0.2} Monika..."
        n 4csrfsl "Je.{w=0.75}{nw}"
        extend 4ksrsll " Incluso Yuri.{w=1}{nw}"
        extend 2ksrpul " Pero..."
        n 2kcssllesi "..."
        n 2cllsl "...No están aquí.{w=0.75}{nw}"
        extend 4kslsl " N-{w=0.2}no más."
        n 4knmsl "...Y nunca lo estarán de nuevo."
        n 1klrpu "Así que es por eso..."
        n 1klrbol "..."
        n 1ccsunl "Así que...{w=0.75}{nw}"
        extend 4cslemltsb " e-{w=0.2}eso es..."
        n 4cslunltsb "..."
        n 4fcsunltsa "..."
        n 4fcsupltsa "A-{w=0.4}así que es por eso que yo..."
        n 1ccsunltsa "..."
        n 2ksrslltsb "..."
        n 2ncspulesi "..."
        $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 2kslsll "...Gracias,{w=0.2} [chosen_endearment].{w=0.75}{nw}"
        extend 2knmsll " De verdad.{w=0.75}{nw}"
        extend 2klrssl " ¿Incluso {i}si{/i} todo esto es solo a través de una pantalla?"
        n 4klrfsl "..."
        n 4ncsssl "...Je."
        n 2kslfsl "Es aún así...{w=0.3} mucho más de lo que podría haber esperado."

        $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
            poem_list=jn_poems.getAllPoems(),
            unlocked=False,
            holiday_types=[jn_events.JNHolidayTypes.natsuki_birthday],
            affinity=Natsuki._getAffinityState()
        )
        $ unlocked_poem_pool.sort(key = lambda poem: poem.affinity_range[0])
        $ birthday_poem = unlocked_poem_pool.pop() if len(unlocked_poem_pool) > 0 else None

        if birthday_poem:
            $ birthday_poem.unlock()

            n 1kslsll "..."
            n 4knmbol "...Terminé escribiendo algo,{w=0.2} sabes."
            n 4klrbolsbr "..."
            n 2knmfllsbr "¿Qué?{w=0.75}{nw}"
            extend 2ccscalsbr " No me des esa mirada.{w=1}{nw}"
            extend 2ccsfllsbr " Y-{w=0.2}yo {i}sé{/i} que se supone no le das cosas a otra gente en tu cumpleaños.{w=1}{nw}"
            extend 2cslcalsbr " {i}Obviamente{/i}."
            n 2cllsllsbr "Pero..."
            n 1kllbol "..."
            n 4ccsajl "No importa."
            n 4cslcal "S-{w=0.2}solo tómalo.{w=0.5}{nw}"
            extend 2ccscalsbl " Antes de que cambie de opinión."

            show natsuki 2cllsrlsbl
            call show_poem (birthday_poem)
            $ jnPause(3)

            n 2cllbol "..."
            n 2cllajl "Oye..."
            n 2kllsll "...Leíste eso,{w=0.75}{nw}"
            extend 4knmbol " ¿verdad?"
            n 4klrbol "Porque...{w=1}{nw}"
            extend 2ksrfll " Realmente {b}decía{/b} en serio todo eso,{w=0.2} [player].{w=0.75}{nw}"
            extend 2knmbol " Realmente deberías saber que lo hago para ahora."
            n 2ccsfllsbr "P-{w=0.2}puede que no sea más alta."
            n 4kllbolsbr "Pero...{w=0.3} ¿estando aquí contigo?"
            n 4ncsssl "Je."
            n 1nsrfsf "...Me gusta pensar que crecí de todos modos.{w=0.75}{nw}"
            extend 2ccssml " S-{w=0.2}solo un poco."

        n 4kslbol "..."
        n 4knmbol "...¿Y [player]?"
        n 4klrbolsbl "..."
        show natsuki 1ccsbol
    else:

        if Natsuki.isAffectionate(higher=True):
            n 1nslss "...Je.{w=0.75}{nw}"
            extend 2tsqbol " ¿Feliz ahora,{w=0.2} [player]?{w=0.75}{nw}"
            extend 2clrfll " Caray..."
            n 2clrsl "..."
            n 2nlraj "Pero..."
            n 4ksrslsbl "..."
        else:

            n 2csqfll "...¿Feliz ahora?{w=0.75}{nw}"
            extend 2cllfllsbr " Cielos..."
            n 2ccsposbr "Si {i}quisiera{/i} estar avergonzada solo habría preguntado,{w=0.2} sabes."
            n 2csrpo "..."
            n 2nsrbo "Pero..."
            n 4ksrslsbl "..."

        n 1ksrbolsbr "...Gracias.{w=1}{nw}"
        extend 4ccspulsbr " P-{w=0.2}por todo esto,{w=0.2} quiero decir."
        n 4cllpul "Es solo que..."
        n 1kllsll "..."
        n 1fcssll "Es...{w=0.75}{nw}"
        extend 4fcsunl " mucho{w=0.75}{nw}"
        extend 4ksrsll " a lo que acostumbrarse.{w=1}{nw}"
        extend 4knmbol " Realmente celebrarlo con cualquiera."
        n 2kslcal "...Mucho menos con cualquiera a quien realmente le {i}importe{/i}."
        n 2fcsgslsbl "¡N-{w=0.2}no como si las otras {i}no{/i} hubieran hecho nada!"
        extend 2ccsflsbl " ¡Por supuesto que lo harían!{w=0.75}{nw}"
        extend 4clrss " Sayori,{w=0.2} Monika..."
        n 4ccsss "Je."
        extend 2cslfs " Incluso Yuri.{w=1}{nw}"
        extend 2kslbo " Es solo que..."
        n 4ccsunl "..."
        n 4ccsfll "No es...{w=0.75}{nw}"
        extend 4clrbol " como si fueran a aparecer pronto.{w=0.75}{nw}"
        extend 2ksrbol " E-{w=0.2}especialmente no ahora."
        n 2ksrsll "..."
        n 2fcsfllsbl "¡A-{w=0.2}así que!{w=0.75}{nw}"
        extend 2fcsajlsbl " Es por eso..."
        n 2fcsunlsbl "E-{w=0.2}eso es..."
        n 2kslunl "..."
        n 4ccsunl "Es..."
        n 4ccsflf "¡E-{w=0.2}es simplemente algo bueno que aparecieras hoy!{w=1}{nw}"
        extend 2fcsfll " Eso es todo lo que digo.{w=1}{nw}"
        extend 2nsrbol " Así que..."
        n 1ksrsll "...Sí."
        n 1ksrbol "..."
        n 4ksqbol "...¿Y [player]?"
        n 4cslunl "..."
        show natsuki 4ccsunf

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ jnPause(2)
    play audio glass_move
    hide prop
    hide confetti
    $ jnPause(2)
    play audio chair_out
    $ jnPause(3)
    play audio clothing_ruffle

    if Natsuki.isLove(higher=True):
        $ jnPause(1)
        n "...T-{w=0.2}te amo."
        $ jnPause(3)
        play audio kiss
        $ jnPause(3)
        show natsuki 1nsrfsf
        $ jnPause(5)

    elif Natsuki.isEnamored(higher=True):
        show natsuki 1nsrbof
        $ jnPause(4)

    elif Natsuki.isAffectionate(higher=True):
        show natsuki 1csrbof
        $ jnPause(3)
    else:

        show natsuki 1csrunfsbr
        $ jnPause(3)

    $ jnPause(1.25)
    hide black with Dissolve(1.25)
    $ jnPause(3)

    $ gold_star_hairpin = jn_outfits.getWearable("jn_accessory_gold_star_hairpin")
    $ pink_star_hairpin = jn_outfits.getWearable("jn_accessory_pink_star_hairpin")

    if (
        persistent.jn_custom_outfits_unlocked 
        and (not gold_star_hairpin.unlocked or not pink_star_hairpin.unlocked)
    ):
        $ hairpin_to_gift = gold_star_hairpin if not gold_star_hairpin.unlocked else pink_star_hairpin
        $ hairpin_to_gift.unlock()
        n 2ksrbol "..."
        n 2nsrajl "Así que...{w=1}{nw}"
        extend 4tnmbol " qué es...{w=0.5}{nw}"

        show natsuki 1tnmboltsbeqm
        $ jn_gifts.GIFT_BLUE.present()
        $ jnPause(0.5)
        show natsuki 4udwfll

        if Natsuki.isEnamored(higher=True):
            $ jnPause(3)
            n 4knmpul "...[player]...{w=1.25}{nw}"
            extend 2ksrpul " vamos..."
            n 2knmsll "¿No me has avergonzado lo suficiente ya?{w=0.75}{nw}"
            extend 2ksrpol " Cielos..."
            n 2cllsll "..."
            n 2kcspulesi "..."
            n 4kslbol "...Bien.{w=1}{nw}"
            extend 4nslsslsbr " Supongo que es lo menos que podría hacer,{w=0.2} ¿eh?"
        else:

            $ jnPause(1.5)
            n 4unmfll "¡...!{w=0.5}{nw}"
            n 2fslunlsbr "..."
            n 2fsqunlsbr "M-{w=0.2}más vale que esto no sea algún tipo de broma,{w=0.2} [player]."
            n 2nsrsllsbl "..."
            n 2ccsemlsbl "B-{w=0.2}bien."
            extend 4ksrbolsbr " Supongo que es lo menos que debería hacer."

        show natsuki 4cdwbolsbr
        $ jn_gifts.GIFT_BLUE.open()
        $ jnPause(3)
        show natsuki 1udwfllsbr
        play audio gift_rustle
        $ jn_gifts.GIFT_BLUE.empty()
        $ jnPause(3)

        if Natsuki.isEnamored(higher=True):
            show natsuki 4ksrfsltsb
        else:

            show natsuki 4csrboltsb

        $ jnPause(3)
        play audio necklace_clip
        $ birthday_outfit.accessory = hairpin_to_gift
        $ jn_outfits.saveTemporaryOutfit(birthday_outfit)

        if Natsuki.isEnamored(higher=True):
            show natsuki 2ksrsml
        else:

            show natsuki 2nsrbol

        $ jnPause(3)

        if Natsuki.isEnamored(higher=True):
            n 2nsrssl "...Je."
            n 4nsrfsl "Realmente...{w=1}{nw}"
            extend 1ksrfsl " {i}se{/i} siente como mi cumpleaños ahora."
            $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove() else jn_utils.getRandomTease()
            n 1ksqbol "...Gracias,{w=0.2} [player].{w=0.75}{nw}"
            extend 1kllssl " Es..."
            n 2kslfslsbr "..."
            n 2kslssfsbr "...Lo amo.{w=1}{nw}"
            extend 4kslfslsbr " G-{w=0.2}gracias.{w=1}{nw}"
            extend 4cslsslsbr " Gran bobo."
            show natsuki 4cslsml
        else:

            n 2nsrbol "..."
            n 2nsrajlsbl "...S-{w=0.2}supongo que esa es una forma de hacerlo sentir como un cumpleaños.{w=0.75}{nw}"
            extend 2nsrsslsbl " Je."
            n 4ksrbolsbl "..."
            n 4knmbolsbr "...Gracias,{w=0.2} [player].{w=1}{nw}"
            extend 4klrbolsbr " Es..."
            n 1ksrsllsbr "..."
            n 2ncssslsbr "...Es asombroso.{w=1}{nw}"
            extend 2cslsslsbl " I-{w=0.2}incluso si {i}vino{/i} de un tonto."
            show natsuki 2nslfsl

        $ jn_gifts.GIFT_BLUE.close()
        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        $ jn_gifts.GIFT_BLUE.hide()
        hide black with Dissolve(1.5)
        $ jnPause(3)

    if Natsuki.isEnamored(higher=True):
        n 1nsrbol "..."
        n 1nsrssl "Así que..."
        $ chosen_endearment = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        n 3tnmssl "¿Qué querías hacer hoy,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3csldvlsbr " Jejeje..."

    elif Natsuki.isAffectionate(higher=True):
        n 2nsrbol "..."
        n 2nsrajl "Así que..."
        n 2ccssslsbr "¿Q-{w=0.2}qué está pasando,{w=0.2} [player]?{w=0.75}{nw}"
        extend 2cslsslsbr " Jejeje..."
    else:

        n 2nsrbol "..."
        n 2nsrajl "A-{w=0.2}así que..."
        n 2ccssssbl "¿Qué mas hay de nuevo,{w=0.2} [player]?"

    $ persistent._jn_natsuki_birthday_known = True
    $ Natsuki.calculatedAffinityGain(base=2.5, bypass=True)
    $ jn_events.getHoliday("holiday_natsuki_birthday").complete()

    return

label holiday_player_birthday:
    python:
        import copy
        import datetime

        today_day_month = (datetime.date.today().day, datetime.date.today().month)


        jn_outfits.getWearable("jn_headgear_classic_party_hat").unlock()
        birthday_hat_outfit = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        birthday_hat_outfit.headgear = jn_outfits.getWearable("jn_headgear_classic_party_hat")
        birthday_hat_outfit.hairstyle = jn_outfits.getWearable("jn_hair_down")
        jn_outfits.saveTemporaryOutfit(birthday_hat_outfit)

        jn_events.getHoliday("holiday_player_birthday").run()
        player_name_capitalized = player.upper()

    n 1uchlgl "¡FELIZ CUMPLEAÑOS,{w=0.2} [player_name_capitalized]!"

    if (
        persistent._jn_player_birthday_is_leap_day
        and today_day_month == (28, 2)
    ):

        n 4nsldvlsbr "...O lo suficientemente cerca de todos modos este año,{w=0.2} ¿verdad?"

    n 1fcsbg "Apuesto a que no pensaste que tenía algo planeado todo el tiempo,{w=0.2} ¿o sí?{w=0.5}{nw}"
    extend 1nchsml " Jejeje."
    n 1fnmaj "¡No mientas!{w=1}{nw}"
    extend 4fchbl " Sé que te atrapé {i}muy{/i} bien esta vez."
    n 1ullss "Bueno,{w=0.2} lo que sea.{w=1}{nw}"
    extend 1tsqsm " Ambos sabemos lo que {i}tú{/i} estás esperando,{w=0.2} ¿eh?"
    n 2fcsss "Sí,{w=0.2} sí.{w=0.5}{nw}"
    extend 2fchsm " Te tengo cubierto,{w=0.2} [player]."

    show prop cake lit zorder JN_PROP_ZORDER
    play audio necklace_clip

    n 1uchgn "¡Ta-{w=0.3}da!"
    $ jnPause(3)
    n 1fnmpu "..."
    n 1fbkwr "¡¿Qué?!{w=1}{nw}"
    extend 2fllpol " ¿No esperarás {i}seriamente{/i} que cante yo solita?{w=1}{nw}"
    extend 2fcseml " ¡De ninguna manera!"
    n 2nlrpol "..."
    n 1nlrpu "Pero..."
    n 1nchbs "¡Sí!{w=0.2} ¡Aquí tienes!{w=0.5}{nw}"
    extend 1nchsml " Jejeje."
    n 1tsqsm "Así que,{w=0.2} ¿[player]?{w=1}{nw}"
    extend 1tsqss " ¿No vas a pedir un deseo?"
    n 4tlrpu "...Mejor piensa en uno pronto,{w=0.2} en realidad.{w=1}{nw}"
    extend 4uskemlesh " ¡Tengo que apagar esto antes de que la cera arruine todo el glaseado!"
    n 2nllpo "..."
    n 1tsqpu "¿Todo listo?{w=0.5}{nw}"
    extend 2fsrpo " Ya era hora.{w=1}{nw}"
    extend 1fchbg " ¡Apaguemos estas ya!"

    n 1ncsaj "...{w=0.5}{nw}"
    show prop cake unlit zorder JN_PROP_ZORDER
    play audio blow

    n 1nchsm "..."
    n 2tsgss "¿Y bien?{w=0.75}{nw}"
    extend 2tnmaj " ¿Qué estás esperando,{w=0.2} [player]?{w=1}{nw}"
    extend 2flrcal " ¡Ataca ya!"
    n 2nsqsll "No me digas que me esforcé tanto en esto para nada."
    n 2fsqsr "..."
    n 1uskajesu "...Oh.{w=0.5}{nw}"
    extend 1fllssl " Jejeje.{w=1}{nw}"
    extend 1fslssl " Cierto."
    n 4flrssl "Yo...{w=1.5}{nw}"
    extend 4fsrdvl " medio olvidé sobre {i}ese{/i} aspecto."
    n 2fslpol "Y realmente no tengo ganas de embarrar pastel por toda tu pantalla.{w=1}{nw}"
    extend 2ullaj " Así que..."
    n 1nsrss "Solo guardaré esto para después."
    n 4fnmajl "¡Oye!{w=0.5}{nw}"
    extend 4fllbgl " Es la intención lo que cuenta,{w=0.2} ¿verdad?"
    show natsuki 4fsldvl

    play audio glass_move
    hide prop cake unlit
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    $ unlocked_poem_pool = jn_poems.JNPoem.filterPoems(
        poem_list=jn_poems.getAllPoems(),
        unlocked=False,
        holiday_types=[jn_events.JNHolidayTypes.player_birthday],
        affinity=Natsuki._getAffinityState()
    )
    $ birthday_poem = random.choice(unlocked_poem_pool) if len(unlocked_poem_pool) > 0 else None

    if birthday_poem:
        if Natsuki.isEnamored(higher=True):
            n 1kllcal "..."
            n 1knmpul "...Te escribí algo también,{w=0.2} sabes."
            n 2fcseml "S-{w=0.2}sé que no es algún {i}gran{/i} regalo,{w=1}{nw}"
            extend 2klrsrl " pero..."
            n 4fsrsrl "..."
            n 4fcsunl "Uuuuu..."
            n 1fcspul "Solo...{w=1}{nw}"
            $ chosen_tease = jn_utils.getRandomTease()
            extend 2klrpol " léelo ya,{w=0.2} [chosen_tease]."
        else:

            n 1fllunl "..."
            n 3fnmcal "E-{w=0.2}espero que no pensaras que simplemente te dejaría con nada."
            n 3nsrpol "No soy {i}tan{/i} idiota."
            n 1nsrajl "Así que...{w=1}{nw}"
            extend 4fnmcal " aquí tienes."
            n 1fcsemf "S-{w=0.2}solo apresúrate y léelo.{w=1}{nw}"
            extend 2fslbof " No voy a leértelo."

        call show_poem (birthday_poem)

        if Natsuki.isEnamored(higher=True):
            n 1knmbol "Oye...{w=1}{nw}"
            extend 1knmpul " {i}sí{/i} lo leíste,{w=0.2} ¿verdad?"
            n 2fslbol "Trabajé mucho en eso,{w=0.2} sabes."
            n 1fcseml "Y-{w=0.2}y dije en serio cada palabra,{w=1}{nw}"
            extend 4kllbof " así que..."
            n 1klrssf "...Sí."
            n 4flldvl "Yo..."
            extend 4fslssl " solo pondré ese poema de vuelta en mi escritorio por ahora."
        else:

            n 1nsqpul "¿Todo listo?{w=1}{nw}"
            extend 2fcseml " {i}Finalmente{/i}.{w=1}{nw}"
            extend 2fslcal " Cielos..."
            n 1fslunl "..."
            n 1fcsajl "Supongo que solo lo guardaré en mi escritorio por ahora.{w=1}{nw}"
            extend 4fsrssl " P-{w=0.2}por si acaso querías referenciar mis habilidades de escritura luego,{w=0.2} {i}obviamente{/i}."

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    if Natsuki.isLove(higher=True):
        n 1klrssl "Y...{w=1.5}{nw}"
        extend 4knmsml " ¿[player]?"

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        $ jnPause(0.5)
        play audio kiss
        $ jnPause(0.25)
        hide black with Dissolve(1.25)

        n 4kwmssf "F-{w=0.2}feliz cumpleaños.{w=1}{nw}"
        extend 1kchsmf " Jejeje."

    elif Natsuki.isEnamored(higher=True):
        n 4kwmssf "F-{w=0.2}feliz cumpleaños."
    else:

        n 1fcsbgf "¡De nada!"

    if birthday_poem:
        $ birthday_poem.unlock()

    $ jn_events.getHoliday("holiday_player_birthday").complete()

    return

label holiday_anniversary:

    $ jn_events.getHoliday("holiday_anniversary").run()
    $ jn_events.getHoliday("holiday_anniversary").complete()

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
