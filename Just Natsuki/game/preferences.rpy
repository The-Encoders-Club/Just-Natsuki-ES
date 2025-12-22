default persistent.jn_ui_style = "default"

init python in jn_preferences.weather:
    from Enum import Enum
    import store

    class JNWeatherSettings(Enum):
        disabled = 1
        random = 2
        real_time = 3
        
        def __int__(self):
            return self.value

init python in jn_preferences.random_topic_frequency:
    from Enum import Enum
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4

    def getRandomTopicFrequencyDescription():
        """
        Gets the descriptor for the random topic frequency, as given by the current frequency.
        """
        return {
            0: "Never",
            1: "Rarely",
            2: "Sometimes",
            3: "Frequent",
            4: "Often",
        }.get(store.persistent.jn_natsuki_random_topic_frequency)

    def getRandomTopicCooldown():
        """
        Gets the cooldown (in minutes) between topics prompted by Natsuki, as given by the current frequency.
        """
        return {
            0: 10000,
            1: 30,
            2: 15,
            3: 5,
            4: 2,
        }.get(store.persistent.jn_natsuki_random_topic_frequency)


default persistent.jn_natsuki_random_topic_frequency = jn_preferences.random_topic_frequency.SOMETIMES


default persistent.jn_natsuki_repeat_topics = True


default persistent._jn_natsuki_idles_enabled = True


default persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)


default persistent._jn_notify_conversations = True


default persistent._jn_notify_activity = True


default persistent._jn_scw = True


default persistent._jn_natsuki_out_of_topics_remind = True


default persistent._jn_display_option_icons = True


default persistent._jn_blackjack_show_hand_value = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
