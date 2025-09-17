init -100 python:
    if not hasattr(store, "submods"):
        store.submods = []

    class SubmodInfo(object):
        def __init__(self, name, version, author, coauthors, description):
            self.name = name
            self.version = version
            self.author = author
            self.coauthors = coauthors
            self.description = description

    def register_submod(name, version, author, coauthors, description):
        info = SubmodInfo(name, version, author, coauthors, description)
        store.submods.append(info)

screen submods_list_screen():
    tag menu

    use game_menu(_("Submods")):

        default tooltip = Tooltip("")

        viewport id "submods_scroll":
            scrollbars "vertical"
            mousewheel True
            draggable True

            has vbox
            style_prefix "check"
            xfill True
            xmaximum 1000

            if submods:
                for s in sorted(submods, key=lambda x: x.name):
                    vbox:
                        xfill True
                        xmaximum 1000

                        label s.name:
                            yanchor 0
                            xalign 0
                            text_text_align 0.0

                        if hasattr(s, "coautores") and s.coauthors:
                            $ authors = "v{0}{{space=20}}por {1}, {2}".format(s.version, s.author, ", ".join(s.coauthors))
                        else:
                            $ authors = "v{0}{{space=20}}por {1}".format(s.version, s.author)

                        text "[authors]":
                            yanchor 0
                            xalign 0
                            text_align 0.0
                            layout "greedy"
                            style "main_menu_version"

                        if s.description:
                            text s.description text_align 0.0

                        null height 20
            else:
                text _("No hay submods instalados.")

        text tooltip.value:
            xalign 0 yalign 1.0
            xoffset 300 yoffset -10
            style "main_menu_version"

init -1 python:
    if not hasattr(store, "LATE_TOPIC_REGISTRY"):
        store.LATE_TOPIC_REGISTRY = []

init 999 python:
    for topic, topic_group in getattr(store, "LATE_TOPIC_REGISTRY", []):
        registerTopic(topic, topic_group=topic_group)
        if topic_group == TOPIC_TYPE_NORMAL:
            store.topics.TOPIC_MAP[topic.label] = topic
            store.topic_handler.ALL_TOPIC_MAP[topic.label] = topic
    store.LATE_TOPIC_REGISTRY = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
