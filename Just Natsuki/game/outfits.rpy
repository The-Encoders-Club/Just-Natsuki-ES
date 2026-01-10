
init -2:
    default persistent.jn_natsuki_auto_outfit_change_enabled = True
    default persistent.jn_custom_outfits_unlocked = False
    default persistent.jn_natsuki_outfit_on_quit = "jn_school_uniform"
    default persistent.jn_outfit_list = {}
    default persistent.jn_wearable_list = {}
    default persistent._jn_pending_outfit_unlocks = []

init -1 python in jn_outfits:
    from Enum import Enum
    import json
    import os
    import random
    import re
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_utils as jn_utils
    import time


    _m1_outfits__CUSTOM_WEARABLES_DIRECTORY = os.path.join(renpy.config.basedir, "custom_wearables/").replace("\\", "/")
    _m1_outfits__CUSTOM_OUTFITS_DIRECTORY = os.path.join(renpy.config.basedir, "custom_outfits/").replace("\\", "/")
    _m1_outfits__WEARABLE_BASE_PATH = os.path.join(renpy.config.basedir, "game/mod_assets/natsuki/")


    _m1_outfits__RESTRICTED_CHARACTERS_REGEX = "((\.)|(\[)|(\])|(\})|(\{)|(,)|(\!))"


    _m1_outfits__ALL_WEARABLES = {}
    _m1_outfits__ALL_OUTFITS = {}

    _PREVIEW_OUTFIT = None
    _LAST_OUTFIT = None

    _changes_made = False


    WEARABLE_CATEGORIES = [
        "hairstyle",
        "eyewear",
        "accessory",
        "clothes",
        "headgear",
        "necklace",
        "facewear",
        "back"
    ]

    class JNWearable():
        """
        Describes a standalone object that Natsuki can wear.
        """
        def __init__(
            self,
            reference_name,
            display_name,
            unlocked,
            is_jn_wearable
        ):
            """
            Constructor.

            IN:
                - reference_name - The name used to uniquely identify this wearable and refer to it internally
                - display_name - The name displayed to the user
                - unlocked - Whether or not this wearable is selectable to the player on menus
                - is_jn_wearable - Whether or not this wearable is an official JN wearable. Official wearables cannot be deleted/modified.
            """
            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = unlocked
            self.is_jn_wearable = is_jn_wearable
        
        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each wearable from the persistent.
            """
            global _m1_outfits__ALL_WEARABLES
            for wearable in _m1_outfits__ALL_WEARABLES.values():
                wearable._m1_outfits__load()
        
        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each wearable to the persistent.
            """
            global _m1_outfits__ALL_WEARABLES
            for wearable in _m1_outfits__ALL_WEARABLES.values():
                wearable._m1_outfits__save()
        
        @staticmethod
        def filterWearables(
            wearable_list,
            unlocked=None,
            is_jn_wearable=None,
            reference_name=None,
            not_reference_name=None,
            wearable_type=None
        ):
            """
            Returns a filtered list of wearables, given an wearable list and filter criteria.

            IN:
                - wearable_list - the list of JNWearable child wearables to query
                - unlocked - the boolean unlocked state to filter for
                - is_jn_wearable - the boolean is_jn_wearable state to filter for
                - reference_name - list of reference_names the wearable must have
                - not_reference_name - list of reference_names the wearable must not have
                - wearable_type the wearable type to filter for

            OUT:
                - list of JNWearable child wearables matching the search criteria
            """
            return [
                _wearable
                for _wearable in wearable_list
                if _wearable._m1_outfits__filterWearable(
                    unlocked,
                    is_jn_wearable,
                    reference_name,
                    not_reference_name,
                    wearable_type
                )
            ]
        
        def asDict(self):
            """
            Exports a dict representation of this wearable; this is for data we want to persist.

            OUT:
                dictionary representation of the wearable object
            """
            return {
                "unlocked": self.unlocked
            }
        
        def unlock(self):
            """
            Unlocks this wearable, making it available to the player.
            """
            
            self.unlocked = True
            self._m1_outfits__save()
        
        def lock(self):
            """
            Locks this wearable, making it unavailable to the player.
            """
            
            self.unlocked = False
            self._m1_outfits__save()
        
        def _m1_outfits__load(self):
            """
            Loads the persisted data for this wearable from the persistent.
            """
            if store.persistent.jn_wearable_list[self.reference_name]:
                self.unlocked = store.persistent.jn_wearable_list[self.reference_name]["unlocked"]
        
        def _m1_outfits__save(self):
            """
            Saves the persistable data for this wearable to the persistent.
            """
            store.persistent.jn_wearable_list[self.reference_name] = self.asDict()
        
        def _m1_outfits__filterWearable(
            self,
            unlocked=None,
            is_jn_wearable=None,
            reference_name=None,
            not_reference_name=None,
            wearable_type=None
        ):
            """
            Returns True, if the wearable meets the filter criteria. Otherwise False.

            IN:
                - wearable_list - the list of JNWearable child wearables to query
                - unlocked - the boolean unlocked state to filter for
                - is_jn_wearable - the boolean is_jn_wearable state to filter for
                - reference_name - list of reference_names the wearable must have
                - not_reference_name - list of reference_names the wearable must not have
                - wearable_type the wearable type to filter for

            OUT:
                - True, if the wearable meets the filter criteria. Otherwise False
            """
            if unlocked is not None and self.unlocked != unlocked:
                return False
            
            elif is_jn_wearable is not None and self.is_jn_wearable != is_jn_wearable:
                return False
            
            elif reference_name is not None and not self.reference_name in reference_name:
                return False
            
            elif not_reference_name is not None and self.reference_name in not_reference_name:
                return False
            
            elif wearable_type is not None and not isinstance(self, wearable_type):
                return False
            
            return True

    class JNHairstyle(JNWearable):
        """
        Describes a hairstyle for Natsuki; a wearable with additional functionality specific to hairstyles.
        """
        def getFolderName(self):
            return "hair"

    class JNEyewear(JNWearable):
        """
        Describes eyewear for Natsuki; a wearable with additional functionality specific to eyewear.
        """
        def getFolderName(self):
            return "eyewear"

    class JNAccessory(JNWearable):
        """
        Describes an accessory for Natsuki; a wearable with additional functionality specific to accessories.
        """
        def getFolderName(self):
            return "accessory"

    class JNClothes(JNWearable):
        """
        Describes a set of clothes for Natsuki; a wearable with additional functionality specific to clothes.
        """
        def getFolderName(self):
            return "clothes"

    class JNHeadgear(JNWearable):
        """
        Describes some headgear for Natsuki; a wearable with additional functionality specific to headgear.
        """
        def getFolderName(self):
            return "headgear"

    class JNNecklace(JNWearable):
        """
        Describes some headgear for Natsuki; a wearable with additional functionality specific to necklaces.
        """
        def getFolderName(self):
            return "necklace"

    class JNFacewear(JNWearable):
        """
        Describes some facewear for Natsuki; a wearable with additional functionality specific to facewear.
        """
        def getFolderName(self):
            return "facewear"

    class JNBack(JNWearable):
        """
        Describes some back item for Natsuki; a wearable with additional functionality specific to back items.
        """
        def getFolderName(self):
            return "back"

    class JNOutfit():
        """
        Describes a complete outfit for Natsuki to wear; including clothing, hairstyle, etc.
        At minimum, an outfit must consist of clothes and a hairstyle.
        """
        def __init__(
            self,
            reference_name,
            display_name,
            unlocked,
            is_jn_outfit,
            clothes,
            hairstyle,
            accessory=None,
            eyewear=None,
            headgear=None,
            necklace=None,
            facewear=None,
            back=None
        ):
            """
            Constructor.

            IN:
                - reference_name - The name used to uniquely identify this outfit and refer to it internally
                - display_name - The name displayed to the user
                - unlocked - Whether or not this outfit is selectable to the player on menus
                - is_jn_outfit - Whether or not this outfit is an official JN outfit. Official outfits cannot be deleted/modified.
                - clothes - JNClothes associated with this outfit.
                - hairstyle - JNHairstyle associated with this outfit.
                - accessory - JNAccessory associated with this outfit. Optional.
                - eyewear - JNEyewear associated with this outfit. Optional.
                - headgear - JNHeadgear associated with this outfit. Optional.
                - necklace - JNNecklace associated with this outfit. Optional.
                - facewear - JNFacewear associated with this outfit. Optional.
                - back - JNBack associated with this outfit. Optional.
            """
            
            if clothes is None:
                raise TypeError("Outfit clothing cannot be None")
                return
            
            
            if hairstyle is None:
                raise TypeError("Outfit hairstyle cannot be None")
                return
            
            self.reference_name = reference_name
            self.display_name = display_name
            self.unlocked = unlocked
            self.is_jn_outfit = is_jn_outfit
            self.clothes = clothes
            self.hairstyle = hairstyle
            self.accessory = accessory
            self.eyewear = eyewear
            self.headgear = headgear
            self.necklace = necklace
            self.facewear = facewear
            self.back = back
        
        @staticmethod
        def loadAll():
            """
            Loads all persisted data for each outfit from the persistent.
            """
            global _m1_outfits__ALL_OUTFITS
            for outfit in _m1_outfits__ALL_OUTFITS.values():
                outfit._m1_outfits__load()
        
        @staticmethod
        def saveAll():
            """
            Saves all persistable data for each outfit to the persistent.
            """
            global _m1_outfits__ALL_OUTFITS
            for outfit in _m1_outfits__ALL_OUTFITS.values():
                outfit._m1_outfits__save()
        
        @staticmethod
        def filterOutfits(
            outfit_list,
            unlocked=None,
            is_jn_outfit=None,
            display_name=None,
            not_reference_name=None,
            has_accessory=None,
            has_eyewear=None,
            has_headgear=None,
            has_necklace=None,
            has_facewear=None,
            has_back=None
        ):
            """
            Returns a filtered list of outfits, given an outfit list and filter criteria.

            IN:
                - outfit_list - the list of JNOutfit outfits to query
                - unlocked - the boolean unlocked state to filter for
                - is_jn_outfit - the boolean is_jn_outfit state to filter for
                - display_name - list of display names any outfits must have
                - not_reference_name - list of reference names outfits must not have
                - has_accessory - the boolean has_accessory state to filter for
                - has_eyewear - the boolean has_eyewear state to filter for
                - has_headgear - the boolean has_headgear state to filter for
                - has_necklace - the boolean has_necklace state to filter for
                - has_facewear - the boolean has_facewear state to filter for
                - has_back - the boolean has_back state to filter for

            OUT:
                - list of JNOutfit outfits matching the search criteria
            """
            return [
                _outfit
                for _outfit in outfit_list
                if _outfit._m1_outfits__filterOutfit(
                    unlocked,
                    is_jn_outfit,
                    display_name,
                    not_reference_name,
                    has_accessory,
                    has_eyewear,
                    has_headgear,
                    has_necklace,
                    has_facewear,
                    has_back
                )
            ]
        
        def asDict(self):
            """
            Exports a dict representation of this outfit; this is for data we want to persist.

            OUT:
                dictionary representation of the outfit object
            """
            return {
                "unlocked": self.unlocked
            }
        
        def unlock(self):
            """
            Unlocks this outfit, making it (and all constituent wearables) available to the player.
            """
            
            self.unlocked = True
            self._m1_outfits__save()
            
            
            if not self.clothes.unlocked:
                self.clothes.unlock()
            
            if not self.hairstyle.unlocked:
                self.hairstyle.unlock()
            
            if self.accessory and not self.accessory.unlocked:
                self.accessory.unlock()
            
            if self.eyewear and not self.eyewear.unlocked:
                self.eyewear.unlock()
            
            if self.headgear and not self.headgear.unlocked:
                self.headgear.unlock()
            
            if self.necklace and not self.necklace.unlocked:
                self.necklace.unlock()
            
            if self.facewear and not self.facewear.unlocked:
                self.facewear.unlock()
            
            if self.back and not self.back.unlocked:
                self.back.unlock()
        
        def lock(self):
            """
            Locks this outfit, making it unavailable to the player.
            Any constituent wearables remain unlocked however, as these can be used in custom outfits/other JN outfits.
            """
            self.unlocked = False
            self._m1_outfits__save()
        
        def toJsonString(self):
            """
            Returns this outfit as a JSON string for export use.
            """
            
            outfit_dict = {
                "reference_name": self.reference_name,
                "display_name": self.display_name,
                "unlocked": True, 
                "clothes": self.clothes.reference_name,
                "hairstyle": self.hairstyle.reference_name
            }
            
            
            if self.headgear and isinstance(self.headgear, JNHeadgear):
                outfit_dict["headgear"] = self.headgear.reference_name
            
            if self.eyewear and isinstance(self.eyewear, JNEyewear):
                outfit_dict["eyewear"] = self.eyewear.reference_name
            
            if self.accessory and isinstance(self.accessory, JNAccessory):
                outfit_dict["accessory"] = self.accessory.reference_name
            
            if self.necklace and isinstance(self.necklace, JNNecklace):
                outfit_dict["necklace"] = self.necklace.reference_name
            
            if self.facewear and isinstance(self.facewear, JNFacewear):
                outfit_dict["facewear"] = self.facewear.reference_name
            
            if self.back and isinstance(self.back, JNBack):
                outfit_dict["back"] = self.back.reference_name
            
            return json.dumps(outfit_dict)
        
        def _m1_outfits__load(self):
            """
            Loads the persisted data for this outfit from the persistent, if it exists.
            """
            if store.persistent.jn_outfit_list[self.reference_name]:
                self.unlocked = store.persistent.jn_outfit_list[self.reference_name]["unlocked"]
        
        def _m1_outfits__save(self):
            """
            Saves the persistable data for this outfit to the persistent.
            """
            store.persistent.jn_outfit_list[self.reference_name] = self.asDict()
        
        def _m1_outfits__deleteSave(self):
            """
            Deletes the persistable data for this outfit from the persistent, if it exists.
            """
            if store.persistent.jn_outfit_list[self.reference_name]:
                del store.persistent.jn_outfit_list[self.reference_name]
        
        def _m1_outfits__filterOutfit(
            self,
            unlocked=None,
            is_jn_outfit=None,
            display_name=None,
            not_reference_name=None,
            has_accessory=None,
            has_eyewear=None,
            has_headgear=None,
            has_necklace=None,
            has_facewear=None,
            has_back=None
        ):
            """
            Returns True, if the outfit meets the filter criteria. Otherwise False.

            IN:
                - unlocked - the boolean unlocked state to filter for
                - is_jn_outfit - the boolean is_jn_outfit state to filter for
                - display_name - list of display names any outfits must have
                - not_reference_name - list of reference_names the outfit must not have
                - has_accessory - the boolean has_accessory state to filter for
                - has_eyewear - the boolean has_eyewear state to filter for
                - has_headgear - the boolean has_headgear state to filter for
                - has_necklace - the boolean has_necklace state to filter for
                - has_facewear - the boolean has_facewear state to filter for
                - has_back - the boolean has_back state to filter for

            OUT:
                - True, if the outfit meets the filter criteria. Otherwise False
            """
            if unlocked is not None and self.unlocked != unlocked:
                return False
            
            elif is_jn_outfit is not None and self.is_jn_outfit != is_jn_outfit:
                return False
            
            elif display_name is not None and self.reference_name not in display_name:
                return False
            
            elif not_reference_name is not None and self.reference_name in not_reference_name:
                return False
            
            elif has_accessory is not None and bool(self.has_accessory) != has_accessory:
                return False
            
            elif has_eyewear is not None and bool(self.has_eyewear) != has_eyewear:
                return False
            
            elif has_headgear is not None and bool(self.has_headgear) != has_headgear:
                return False
            
            elif has_necklace is not None and bool(self.has_necklace) != has_necklace:
                return False
            
            elif has_facewear is not None and bool(self.has_facewear) != has_facewear:
                return False
            
            elif has_back is not None and bool(self.has_back) != has_back:
                return False
            
            return True

    def _m1_outfits__registerOutfit(outfit, player_created=False):
        """
        Registers a new outfit in the list of all outfits, allowing in-game access and persistency.
        If the outfit has no existing corresponding persistent entry, it is saved.

        IN:
            - outfit - the JNOutfit to register.
            - player_created - Boolean flag describing whether this outfit was defined by the current player via the new outfit creation flow
        """
        if outfit.reference_name in _m1_outfits__ALL_OUTFITS:
            jn_utils.log("No se puede registrar el nombre del atuendo: {0}, ya que un atuendo con ese nombre ya existe.".format(outfit.reference_name))
        
        else:
            if not outfit.accessory:
                outfit.accessory = getWearable("jn_none")
            
            if not outfit.eyewear:
                outfit.eyewear = getWearable("jn_none")
            
            if not outfit.headgear:
                outfit.headgear = getWearable("jn_none")
            
            if not outfit.necklace:
                outfit.necklace = getWearable("jn_none")
            
            if not outfit.facewear:
                outfit.facewear = getWearable("jn_none")
            
            if not outfit.back:
                outfit.back = getWearable("jn_none")
            
            _m1_outfits__ALL_OUTFITS[outfit.reference_name] = outfit
            if outfit.reference_name not in store.persistent.jn_outfit_list:
                outfit._m1_outfits__save()
                
                
                if not "jn_" in outfit.reference_name and not player_created:
                    store.persistent._jn_pending_outfit_unlocks.append(outfit.reference_name)
            
            else:
                outfit._m1_outfits__load()

    def _m1_outfits__registerWearable(wearable):
        """
        Registers a new wearable in the list of all wearables, allowing in-game access and persistency.
        """
        if wearable.reference_name in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede registrar el nombre del vestible: {0}, ya que un vestible con ese nombre ya existe.".format(wearable.reference_name))
        
        else:
            _m1_outfits__ALL_WEARABLES[wearable.reference_name] = wearable
            if wearable.reference_name not in store.persistent.jn_wearable_list:
                wearable._m1_outfits__save()
                
                
                if not "jn_" in wearable.reference_name:
                    store.persistent._jn_pending_outfit_unlocks.append(wearable.reference_name)
            
            else:
                wearable._m1_outfits__load()

    def _m1_outfits__deleteOutfit(outfit):
        """
        Deletes an outfit from the list of all outfits.
        If the outfit has a corresponding persistent entry, it is deleted.
        """
        outfit._m1_outfits__deleteSave()
        del _m1_outfits__ALL_OUTFITS[outfit.reference_name]

    def _checkWearableSprites(wearable):
        """
        Checks sprite paths based on wearable type to ensure all required assets exist.

        IN:
            - wearable - the JNWearable wearable to test

        OUT:
            - True if all required assets for the wearable exist, otherwise False
        """
        WEARABLE_COMMON_PATH = os.path.join(_m1_outfits__WEARABLE_BASE_PATH, wearable.getFolderName())
        
        for pose in store.JNPose:
            
            
            
            if isinstance(wearable, JNClothes):
                
                sleeves_path = os.path.join(_m1_outfits__WEARABLE_BASE_PATH, "sleeves", wearable.reference_name, "{0}.png".format(pose.name))
                clothes_path = os.path.join(_m1_outfits__WEARABLE_BASE_PATH, "clothes", wearable.reference_name, "{0}.png".format(pose.name))
                
                if not jn_utils.getFileExists(sleeves_path) or not jn_utils.getFileExists(clothes_path):
                    jn_utils.log("Faltan sprites de ropa/mangas para {0}".format(wearable.reference_name))
                    return False
            
            elif isinstance(wearable, JNHairstyle):
                
                back_path = os.path.join(WEARABLE_COMMON_PATH, wearable.reference_name, "sitting", "back.png")
                bangs_path = os.path.join(WEARABLE_COMMON_PATH, wearable.reference_name, "sitting", "bangs.png")
                
                if not jn_utils.getFileExists(back_path) or not jn_utils.getFileExists(bangs_path):
                    jn_utils.log("Faltan sprites de espalda/flequillo para {0}".format(wearable.reference_name))
                    return False
            
            else:
                
                resource_path = os.path.join(WEARABLE_COMMON_PATH, wearable.reference_name, "sitting.png")
                
                if not jn_utils.getFileExists(resource_path):
                    jn_utils.log("Faltan sprite(s) para {0}: verificar {1}".format(wearable.reference_name, resource_path))
                    return False
        
        return True

    def _loadWearableFromJson(json):
        """
        Attempts to load a wearable from a JSON object and register it.

        IN:
            - json - JSON object describing the wearable
        """
        
        if (
            "reference_name" not in json
            or "display_name" not in json
            or "unlocked" not in json
            or "category" not in json
        ):
            jn_utils.log("No se puede cargar el vestible ya que uno o más atributos clave no existen.")
            return False
        
        
        elif (
            not isinstance(json["reference_name"], basestring)
            or not isinstance(json["display_name"], basestring)
            or not isinstance(json["unlocked"], bool)
            or not isinstance(json["category"], basestring)
            or not json["category"] in WEARABLE_CATEGORIES
        ):
            jn_utils.log("No se puede cargar el vestible {0} ya que uno o más atributos tienen el tipo de datos incorrecto.".format(json["reference_name"]))
            return False
        
        
        elif re.search("^jn_.", json["reference_name"].lower()):
            jn_utils.log("No se puede cargar el vestible {0} ya que el nombre de referencia contiene un espacio de nombres reservado.".format(json["reference_name"]))
            return False
        
        
        elif re.search(_m1_outfits__RESTRICTED_CHARACTERS_REGEX, json["reference_name"]):
            jn_utils.log("No se puede cargar el vestible {0} ya que el nombre de referencia contiene uno o más caracteres restringidos.".format(json["reference_name"]))
            return False
        
        else:
            
            kwargs = {
                "reference_name": json["reference_name"],
                "display_name": json["display_name"],
                "unlocked": json["unlocked"],
                "is_jn_wearable": False
            }
            
            if json["category"] == "hairstyle":
                wearable = JNHairstyle(**kwargs)
            
            elif json["category"] == "eyewear":
                wearable = JNEyewear(**kwargs)
            
            elif json["category"] == "accessory":
                wearable = JNAccessory(**kwargs)
            
            elif json["category"] == "clothes":
                wearable = JNClothes(**kwargs)
            
            elif json["category"] == "headgear":
                wearable = JNHeadgear(**kwargs)
            
            elif json["category"] == "necklace":
                wearable = JNNecklace(**kwargs)
            
            elif json["category"] == "facewear":
                wearable = JNFacewear(**kwargs)
            
            elif json["category"] == "back":
                wearable = JNBack(**kwargs)
            
            
            if not _checkWearableSprites(wearable):
                jn_utils.log("No se puede cargar el vestible {0} ya que faltan uno o más sprites: ¿este ítem soporta {1}?".format(wearable.reference_name, store.config.version))
                return False
            
            _m1_outfits__registerWearable(wearable)
            return True

    def _loadOutfitFromJson(json):
        """
        Attempts to load an outfit from a JSON object and register it.

        IN:
            - json - JSON object describing the outfit

        OUT: True if load was successful, otherwise False
        """
        
        if (
            "reference_name" not in json
            or "display_name" not in json
            or "unlocked" not in json
            or "clothes" not in json
            or "hairstyle" not in json
        ):
            jn_utils.log("No se puede cargar el atuendo ya que uno o más atributos clave no existen.")
            return False
        
        
        elif (
            not isinstance(json["reference_name"], basestring)
            or not isinstance(json["display_name"], basestring)
            or not isinstance(json["unlocked"], bool)
            or not isinstance(json["clothes"], basestring)
            or not isinstance(json["hairstyle"], basestring)
            or "eyewear" in json and not isinstance(json["eyewear"], basestring)
            or "headgear" in json and not isinstance(json["headgear"], basestring)
            or "necklace" in json and not isinstance(json["necklace"], basestring)
            or "facewear" in json and not isinstance(json["facewear"], basestring)
            or "back" in json and not isinstance(json["back"], basestring)
        ):
            jn_utils.log("No se puede cargar el atuendo como uno o más atributos tienen el tipo de datos incorrecto.")
            return False
        
        
        elif re.search("^jn_.", json["reference_name"].lower()):
            jn_utils.log("No se puede cargar el atuendo {0} ya que el nombre de referencia contiene un espacio de nombres reservado.".format(json["reference_name"]))
            return False
        
        
        elif re.search(_m1_outfits__RESTRICTED_CHARACTERS_REGEX, json["reference_name"]):
            jn_utils.log("No se puede cargar el atuendo {0} ya que el nombre de referencia contiene uno o más caracteres restringidos.".format(json["reference_name"]))
            return False
        
        
        if not json["clothes"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que la ropa especificada no existe.".format(json["reference_name"]))
            return False
        
        elif not json["hairstyle"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el peinado especificado no existe.".format(json["reference_name"]))
            return False
        
        elif "accessory" in json and not json["accessory"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio especificado no existe.".format(json["reference_name"]))
            return False
        
        elif "eyewear" in json and not json["eyewear"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que las gafas especificadas no existen.".format(json["reference_name"]))
            return False
        
        elif "headgear" in json and not json["headgear"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el sombrero especificado no existe.".format(json["reference_name"]))
            return False
        
        elif "necklace" in json and not json["necklace"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el collar especificado no existe.".format(json["reference_name"]))
            return False
        
        elif "facewear" in json and not json["facewear"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio facial especificado no existe.".format(json["reference_name"]))
            return False
        
        elif "back" in json and not json["back"] in _m1_outfits__ALL_WEARABLES:
            jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio trasero especificado no existe.".format(json["reference_name"]))
            return False
        
        else:
            outfit = JNOutfit(
                reference_name=json["reference_name"],
                display_name=json["display_name"],
                unlocked=json["unlocked"],
                is_jn_outfit=False,
                clothes=_m1_outfits__ALL_WEARABLES[json["clothes"]],
                hairstyle=_m1_outfits__ALL_WEARABLES[json["hairstyle"]],
                accessory=_m1_outfits__ALL_WEARABLES[json["accessory"]] if "accessory" in json else None,
                eyewear=_m1_outfits__ALL_WEARABLES[json["eyewear"]] if "eyewear" in json else None,
                headgear=_m1_outfits__ALL_WEARABLES[json["headgear"]] if "headgear" in json else None,
                necklace=_m1_outfits__ALL_WEARABLES[json["necklace"]]  if "necklace" in json else None,
                facewear=_m1_outfits__ALL_WEARABLES[json["facewear"]]  if "facewear" in json else None,
                back=_m1_outfits__ALL_WEARABLES[json["back"]]  if "back" in json else None
            )
            
            
            if not isinstance(outfit.clothes, JNClothes):
                jn_utils.log("No se puede cargar el atuendo {0} ya que la ropa especificada no es válida.".format(outfit.reference_name))
                return False
            
            elif not isinstance(outfit.hairstyle, JNHairstyle):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el peinado especificado no es válido.".format(outfit.reference_name))
                return False
            
            elif outfit.accessory and not isinstance(outfit.accessory, JNAccessory):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio especificado no es válido.".format(outfit.reference_name))
                return False
            
            elif outfit.eyewear and not isinstance(outfit.eyewear, JNEyewear):
                jn_utils.log("No se puede cargar el atuendo {0} ya que las gafas especificadas no son válidas.".format(outfit.reference_name))
                return False
            
            elif outfit.headgear and not isinstance(outfit.headgear, JNHeadgear):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el sombrero especificado no es válido.".format(outfit.reference_name))
                return False
            
            elif outfit.necklace and not isinstance(outfit.necklace, JNNecklace):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el collar especificado no es válido.".format(outfit.reference_name))
                return False
            
            elif outfit.facewear and not isinstance(outfit.facewear, JNFacewear):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio facial especificado no es válido.".format(outfit.reference_name))
                return False
            
            elif outfit.back and not isinstance(outfit.back, JNBack):
                jn_utils.log("No se puede cargar el atuendo {0} ya que el accesorio trasero especificado no es válido.".format(outfit.reference_name))
                return False
            
            
            if outfit.unlocked:
                if (
                    not outfit.clothes.unlocked
                    or not outfit.hairstyle.unlocked
                    or outfit.accessory and not outfit.accessory.unlocked
                    or outfit.eyewear and not outfit.eyewear.unlocked
                    or outfit.headgear and not outfit.headgear.unlocked
                    or outfit.necklace and not outfit.necklace.unlocked
                    or outfit.facewear and not outfit.facewear.unlocked
                    or outfit.back and not outfit.back.unlocked
                ):
                    jn_utils.log("El atuendo {0} contiene uno o más componentes bloqueados; bloqueando el atuendo.".format(outfit.reference_name))
                    outfit.unlocked = False
            
            _m1_outfits__registerOutfit(outfit)
            return True

    def loadCustomOutfits():
        """
        Loads the custom wearables from the game/outfits directory.
        """
        if jn_utils.createDirectoryIfNotExists(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY):
            jn_utils.log("No se pueden cargar los atuendos personalizados ya que el directorio no existe y tuvo que ser creado.")
            return
        
        outfit_files = jn_utils.getAllDirectoryFiles(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY, ["json"])
        success_count = 0
        
        for file_name, file_path in outfit_files:
            try:
                with open(file_path) as outfit_data:
                    if _loadOutfitFromJson(json.loads(outfit_data.read())):
                        success_count += 1
            
            except OSError:
                jn_utils.log("No se puede leer el archivo {0}; no se pudo encontrar el archivo.".format(file_name))
            
            except TypeError:
                jn_utils.log("No se puede leer el archivo {0}; archivo corrupto o JSON inválido.".format(file_name))
            
            except ValueError:
                jn_utils.log("No se puede leer el archivo {0}; archivo corrupto o JSON inválido.".format(file_name))
            
            except:
                raise
        
        if success_count != len(outfit_files):
            renpy.notify("Uno o más atuendos fallaron al cargar; por favor revisa el registro para más información.")

    def loadCustomWearables():
        """
        Loads the custom wearables from the game/wearables directory.
        """
        if jn_utils.createDirectoryIfNotExists(_m1_outfits__CUSTOM_WEARABLES_DIRECTORY):
            jn_utils.log("No se pueden cargar los vestibles personalizados ya que el directorio no existe y tuvo que ser creado.")
            return
        
        wearable_files = jn_utils.getAllDirectoryFiles(_m1_outfits__CUSTOM_WEARABLES_DIRECTORY, ["json"])
        success_count = 0
        
        for file_name, file_path in wearable_files:
            try:
                with open(file_path) as wearable_data:
                    if _loadWearableFromJson(json.loads(wearable_data.read())):
                        success_count += 1
            
            except OSError:
                jn_utils.log("No se puede leer el archivo {0}; no se pudo encontrar el archivo.".format(file_name))
            
            except TypeError:
                jn_utils.log("No se puede leer el archivo {0}; archivo corrupto o JSON inválido.".format(file_name))
            
            except ValueError:
                jn_utils.log("No se puede leer el archivo {0}; archivo corrupto o JSON inválido.".format(file_name))
            
            except:
                raise
        
        if success_count != len(wearable_files):
            renpy.notify("Uno o más vestibles fallaron al cargar; por favor revisa el registro para más información.")

    def unloadCustomOutfits():
        """
        Unloads all custom outfits from active memory.
        """
        _m1_outfits__ALL_OUTFITS = JNOutfit.filterOutfits(
            outfit_list=getAllOutfits(),
            is_jn_outfit=True)

    def unloadCustomWearables():
        """
        Unloads all custom wearables from active memory.
        """
        _m1_outfits__ALL_WEARABLES = JNWearable.filterWearables(
            wearable_list=getAllWearables(),
            is_jn_wearable=True)
        
        return

    def outfitExists(outfit_name):
        """
        Returns whether the given outfit exists in the list of registered outfits.

        IN:
            - outfit_name - str outfit name to search for

        OUT: True if it exists, otherwise False
        """
        return outfit_name in _m1_outfits__ALL_OUTFITS

    def wearableExists(wearable_name):
        """
        Returns whether the given outfit exists in the list of registered outfits.

        IN:
            - wearable_name - str wearable name to search for

        OUT: True if it exists, otherwise False
        """
        return wearable_name in _m1_outfits__ALL_WEARABLES

    def getOutfit(outfit_name):
        """
        Returns the outfit for the given name, if it exists.

        IN:
            - outfit_name - str outfit name to fetch

        OUT: Corresponding JNOutfit if the outfit exists, otherwise None
        """
        if outfitExists(outfit_name):
            return _m1_outfits__ALL_OUTFITS[outfit_name]
        
        return None

    def getWearable(wearable_name):
        """
        Returns the outfit for the given name, if it exists.

        IN:
            - wearable_name - str wearable name to fetch

        OUT: Corresponding JNWearable child if the wearable exists, otherwise None
        """
        if wearableExists(wearable_name):
            return _m1_outfits__ALL_WEARABLES[wearable_name]
        
        return None

    def getAllOutfits():
        """
        Returns a list of all outfits.
        """
        return _m1_outfits__ALL_OUTFITS.values()

    def getAllWearables():
        """
        Returns a list of all outfits.
        """
        return _m1_outfits__ALL_WEARABLES.values()

    def saveTemporaryOutfit(outfit):
        """
        Saves the given outfit as the designated temporary outfit.
        The temporary outfit is not persisted between game exit/reload.

        IN:
            - outfit - the JNOutfit to use as the base for the temporary outfit
        """
        temporary_outfit = getOutfit("jn_temporary_outfit")
        temporary_outfit.clothes = outfit.clothes
        temporary_outfit.hairstyle = outfit.hairstyle
        temporary_outfit.accessory = getWearable("jn_none") if not outfit.accessory else outfit.accessory
        temporary_outfit.eyewear = getWearable("jn_none") if not outfit.eyewear else outfit.eyewear
        temporary_outfit.headgear = getWearable("jn_none") if not outfit.headgear else outfit.headgear
        temporary_outfit.necklace = getWearable("jn_none") if not outfit.necklace else outfit.necklace
        temporary_outfit.facewear = getWearable("jn_none") if not outfit.facewear else outfit.facewear
        temporary_outfit.back = getWearable("jn_none") if not outfit.back else outfit.back
        
        store.Natsuki.setOutfit(temporary_outfit, persist=False)
        
        return True

    def saveCustomOutfit(outfit):
        """
        Saves the given outfit as a JSON custom outfit file.

        IN:
            - outfit - the JNOutfit to save
        """
        
        new_custom_outfit = JNOutfit(
            reference_name="{0}_{1}_{2}".format(
                store.persistent.playername,
                outfit.display_name.replace(" ", "_"),
                int(time.time())
            ).lower(),
            display_name=outfit.display_name,
            unlocked=True,
            is_jn_outfit=False,
            clothes=outfit.clothes,
            hairstyle=outfit.hairstyle,
            accessory=outfit.accessory,
            eyewear=outfit.eyewear,
            headgear=outfit.headgear,
            necklace=outfit.necklace,
            facewear=outfit.facewear,
            back=outfit.back
        )
        
        
        if jn_utils.createDirectoryIfNotExists(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY):
            jn_utils.log("El directorio custom_outfits no fue encontrado y tuvo que ser creado.")
        
        try:
            
            with open(os.path.join(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY, "{0}.json".format(new_custom_outfit.reference_name)), "w") as file:
                file.write(new_custom_outfit.toJsonString())
            
            
            _m1_outfits__registerOutfit(outfit=new_custom_outfit, player_created=True)
            store.Natsuki.setOutfit(new_custom_outfit)
            renpy.notify("¡Atuendo guardado!")
            return True
        
        except Exception as exception:
            renpy.notify("Fallo al guardar atuendo; chequea el registro para mas información.")
            jn_utils.log("Fallo al guardar atuendo {0}, ya que una operación de escritura no fue posible.".format(new_custom_outfit.display_name))
            return False

    def deleteCustomOutfit(outfit):
        """
        Removes the given outfit from the list of all outfits, and removes its persistent data.
        You should check to make sure Natsuki isn't wearing the outfit first.

        IN:
            - outfit - the JNOutfit to delete
        """
        if outfit.is_jn_outfit:
            renpy.notify("Fallo al borrar atuendo; chequea el registro para mas información.")
            jn_utils.log("Fallo al borrar atuendo {0}, ya que es un objeto oficial y no puede ser removido.".format(outfit.display_name))
            return False
        
        
        if jn_utils.createDirectoryIfNotExists(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY):
            jn_utils.log("El directorio custom_outfits no fue encontrado y tuvo que ser creado.")
        
        
        elif not jn_utils.deleteFileFromDirectory(
            path=os.path.join(_m1_outfits__CUSTOM_OUTFITS_DIRECTORY, "{0}.json".format(outfit.reference_name))
        ):
            renpy.notify("Fallo al borrar atuendo; chequea el registro para mas información.")
            jn_utils.log("Fallo al borrar atuendo {0}, ya que una operación de eliminar no fue posible.".format(outfit.display_name))
            return False
        
        else:
            
            _m1_outfits__deleteOutfit(outfit)
            renpy.notify("¡Atuendo borrado!")
            return True

    def getRealtimeOutfit():
        """
        Returns an outfit based on the time of day, weekday/weekend and affinity.
        """
        if store.Natsuki.isAffectionate(higher=True):
            if store.jn_is_weekday():
                return _OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY.get(store.jn_get_current_time_block())
            
            else:
                return _OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY.get(store.jn_get_current_time_block())
        
        elif store.Natsuki.isUpset(higher=True):
            if store.jn_is_weekday():
                return _OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY.get(store.jn_get_current_time_block())
            
            else:
                return _OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY.get(store.jn_get_current_time_block())
        
        else:
            if store.jn_is_weekday():
                return _OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY.get(store.jn_get_current_time_block())
            
            else:
                return _OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY.get(store.jn_get_current_time_block())

    def getSafePendingUnlocks():
        """
        Gets all pending unlocks that are safe to be mentioned in the gifting sequence.

        A safe unlock is an outfit/wearable with a corresponding item in memory.

        OUT:
            - List of str reference names for outfits/wearables that are pending gifting dialogue, or an empty list
        """
        if not len(store.persistent._jn_pending_outfit_unlocks):
            return []
        
        safe_unlocks = []
        for unlock in store.persistent._jn_pending_outfit_unlocks:
            if wearableExists(unlock) or outfitExists(unlock):
                safe_unlocks.append(unlock)
        
        return safe_unlocks


    _m1_outfits__registerWearable(JNWearable(
        reference_name="jn_none",
        display_name="Ninguno",
        unlocked=False,
        is_jn_wearable=True,
    ))


    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_bedhead",
        display_name="Despeinada",
        unlocked=True,
        is_jn_wearable=True,
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_bun",
        display_name="Moño",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twintails",
        display_name="Coletas con cintas rojas",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_down",
        display_name="Suelto",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_messy_bun",
        display_name="Moño desordenado",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_ponytail",
        display_name="Cola de caballo",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_super_messy",
        display_name="Super desordenado",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_princess_braids",
        display_name="Trenzas de princesa",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_low_bun",
        display_name="Moño bajo",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_pigtails",
        display_name="Coletas",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twin_buns",
        display_name="Doble moño",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_down_long",
        display_name="Cabello largo suelto",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_pixie_cut",
        display_name="Corte pixie",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_low_hoops",
        display_name="Aros bajos",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_high_hoops",
        display_name="Aros altos",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twintails_long",
        display_name="Pelo largo con coletas",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twintails_white_ribbons",
        display_name="Coletas con cintas blancas.",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_wavy",
        display_name="Ondulado",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twintails_braided",
        display_name="Coletas trenzadas",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHairstyle(
        reference_name="jn_hair_twintails_down",
        display_name="Coletas sueltas",
        unlocked=True,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_round_glasses_black",
        display_name="Gafas redondas negras",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_round_glasses_red",
        display_name="Gafas redondas rojas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_round_glasses_brown",
        display_name="Gafas redondos marrones",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_round_sunglasses",
        display_name="Gafas de sol redondas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_rectangular_glasses_black",
        display_name="Gafas rectangulares negras",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNEyewear(
        reference_name="jn_eyewear_rectangular_glasses_red",
        display_name="Gafas rojas rectangulares",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_gray",
        display_name="Cinta de pelo gris",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_green",
        display_name="Cinta de pelo verde",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_hot_pink",
        display_name="Cinta de pelo rosa fuerte",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_purple",
        display_name="Cinta de pelo púrpura",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_red",
        display_name="Cinta de pelo roja",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_white",
        display_name="Cinta de pelo blanca",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_purple_rose",
        display_name="Rosa morada",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_pink_heart_hairpin",
        display_name="Horquilla de corazón rosa",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_gold_star_hairpin",
        display_name="Horquilla de estrella dorada",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_pink_star_hairpin",
        display_name="Horquilla de estrella rosa",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_stars",
        display_name="Cinta con estrellas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_hairband_cat",
        display_name="Cinta de pelo con figuras de gato",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_double_white_hairbands",
        display_name="Cinta doble blanca",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_fried_egg_hairpin",
        display_name="Horquilla de huevo frito",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNAccessory(
        reference_name="jn_accessory_cherry_blossom_hairpin",
        display_name="Horquilla de flor de cerezo",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_school_uniform",
        display_name="Uniforme escolar",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_casual",
        display_name="Ropa casual",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_heart_sweater",
        display_name="Suéter con corazones",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_magical_girl",
        display_name="Cosplay de chica mágica",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_rose_lace_dress",
        display_name="Vestido de encaje con rosas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_sango_cosplay",
        display_name="Cosplay de Sango",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_star_pajamas",
        display_name="Pijama de estrellas",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_trainer_cosplay",
        display_name="Cosplay de entrenadora",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_lolita_christmas_dress",
        display_name="Vestido navideño de loly",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_lolita_school_uniform",
        display_name="Uniforme escolar de loly",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_nya_sweater",
        display_name="¡Suéter Nya!",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_pastel_goth_overalls",
        display_name="Overoles pastel (Goth)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_qeeb_sweater",
        display_name="Suéter Qeeb",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_qt_sweater",
        display_name="Suéter QT",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_ruffled_swimsuit",
        display_name="Traje de baño con volantes",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_bee_off_shoulder_sweater",
        display_name="Suéter de abeja sin mangas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_autumn_off_shoulder_sweater",
        display_name="Suéter otoñal sin mangas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_creamsicle_off_shoulder_sweater",
        display_name="Suéter naranja-crema sin mangas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_nightbloom_off_shoulder_sweater",
        display_name="Suéter nocturno sin mangas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_hoodie_not_cute",
        display_name="'Sudadera 'No es linda'",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_hoodie_turtleneck",
        display_name="Sudadera de cuello largo",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_skater_shirt",
        display_name="Camiseta skater",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_cosy_cardigan",
        display_name="Cardigan cómodo",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_bunny_pajamas",
        display_name="Pijama de conejito",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_ruffle_neck_sweater",
        display_name="Suéter con volantes en el cuello",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_chocolate_plaid_dress",
        display_name="Vestido de cuadros chocolate",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_office_blazer",
        display_name="Blazer de oficina",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_chick_dress",
        display_name="Vestido de pollito",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_cherry_blossom_dress",
        display_name="Vestido de flor de cerezo",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNClothes(
        reference_name="jn_clothes_raincoat",
        display_name="Impermeable",
        unlocked=False,
        is_jn_wearable=True
    ))




    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_santa_hat",
        display_name="Gorro de santa",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_trainer_hat",
        display_name="Gorra de entrenadora",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_cat_ears",
        display_name="Orejas de gato",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_fox_ears",
        display_name="Orejas de zorro",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_basic_white_headband",
        display_name="Diadema básica blanca",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_cat_headband",
        display_name="Diadema de gato",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_purple_rose_headband",
        display_name="Diadema rosa púrpura",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_spiked_headband",
        display_name="Diadema con púas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_bee_headband",
        display_name="Diadema de abeja",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_black_beanie",
        display_name="Gorro negro",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_hairtie",
        display_name="Coleta",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_teddy_hairpins",
        display_name="Horquillas de osito",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_sleep_mask",
        display_name="Máscara para dormir",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_classic_party_hat",
        display_name="Gorro de fiesta clásico",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_new_year_headband",
        display_name="Diadema de año nuevo",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_chocolate_plaid_bow",
        display_name="Moño de cuadros chocolate",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_raincoat_hood",
        display_name="Sombrero de impermeable",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_curly",
        display_name="Ahoge (rizado)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_small",
        display_name="Ahoge (pequeño)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_swoop",
        display_name="Ahoge (ondulado)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_double",
        display_name="Ahoge (doble)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_simple",
        display_name="Ahoge (simple)",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_heart",
        display_name="Ahoge de corazón",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_ahoge_swirl",
        display_name="Ahoge en espiral",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_pompoms",
        display_name="Pompones",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNHeadgear(
        reference_name="jn_headgear_cat_headphones",
        display_name="Auriculares de gato",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_bell_collar",
        display_name="Collar con campana",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_plain_choker",
        display_name="Gargantilla lisa",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_pink_scarf",
        display_name="Bufanda rosa",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_spiked_choker",
        display_name="Gargantilla con púas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_thin_choker",
        display_name="Gargantilla delgada",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_black_choker",
        display_name="Gargantilla negra",
        unlocked=True,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_sango_choker",
        display_name="Gargantilla de Sango",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_twirled_choker",
        display_name="Gargantilla retorcida",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_golden_necklace",
        display_name="Collar dorado",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_formal_necktie",
        display_name="Corbata formal",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_bunny_necklace",
        display_name="Collar de conejito",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNNecklace(
        reference_name="jn_necklace_tight_golden_necklace",
        display_name="Collar dorado (ajustado)",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNFacewear(
        reference_name="jn_facewear_sprinkles",
        display_name="Chispas",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNFacewear(
        reference_name="jn_facewear_plasters",
        display_name="Curitas",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerWearable(JNBack(
        reference_name="jn_back_cat_tail",
        display_name="Cola de gato",
        unlocked=False,
        is_jn_wearable=True
    ))
    _m1_outfits__registerWearable(JNBack(
        reference_name="jn_back_fox_tail",
        display_name="Cola de zorro",
        unlocked=False,
        is_jn_wearable=True
    ))


    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_school_uniform",
        display_name="Uniforme escolar",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_school_uniform"),
        hairstyle=getWearable("jn_hair_twintails"),
        accessory=getWearable("jn_accessory_hairband_red")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_casual_clothes",
        display_name="Ropa casual",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_casual"),
        hairstyle=getWearable("jn_hair_bun"),
        accessory=getWearable("jn_accessory_hairband_white")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_star_pajamas",
        display_name="Pijama de estrella",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_star_pajamas"),
        hairstyle=getWearable("jn_hair_down"),
        accessory=getWearable("jn_accessory_hairband_hot_pink")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_bunny_pajamas",
        display_name="Pijama de conejito",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_bunny_pajamas"),
        hairstyle=getWearable("jn_hair_down"),
        headgear=getWearable("jn_headgear_sleep_mask")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_hoodie_turtleneck",
        display_name="Sudadera de cuello alto",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_hoodie_turtleneck"),
        hairstyle=getWearable("jn_hair_bedhead"),
        accessory=getWearable("jn_accessory_hairband_purple")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_nyatsuki_outfit",
        display_name="Conjunto ¡Suéter Nya!",
        unlocked=True,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_nya_sweater"),
        hairstyle=getWearable("jn_hair_twintails"),
        headgear=getWearable("jn_headgear_cat_headband"),
        accessory=getWearable("jn_accessory_hairband_cat"),
        necklace=getWearable("jn_necklace_bell_collar")
    ))


    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_formal_dress",
        display_name="Vestido formal",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_rose_lace_dress"),
        hairstyle=getWearable("jn_hair_ponytail"),
        accessory=getWearable("jn_accessory_purple_rose")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_christmas_outfit",
        display_name="Atuendo navideño",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_lolita_christmas_dress"),
        hairstyle=getWearable("jn_hair_twintails"),
        accessory=getWearable("jn_accessory_hairband_red"),
        headgear=getWearable("jn_headgear_pompoms")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_trainer_cosplay",
        display_name="Cosplay de entrenadora",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_trainer_cosplay"),
        hairstyle=getWearable("jn_hair_down"),
        accessory=getWearable("jn_accessory_hairband_white"),
        headgear=getWearable("jn_headgear_trainer_hat"),
        necklace=getWearable("jn_necklace_pink_scarf")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_sango_cosplay",
        display_name="Cosplay de Sango",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_sango_cosplay"),
        hairstyle=getWearable("jn_hair_twintails"),
        necklace=getWearable("jn_necklace_sango_choker"),
        accessory=getWearable("jn_accessory_hairband_purple")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_ruffled_swimsuit",
        display_name="Atuendo de playa",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_ruffled_swimsuit"),
        hairstyle=getWearable("jn_hair_down")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_skater_outfit",
        display_name="Atuendo skater",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_skater_shirt"),
        hairstyle=getWearable("jn_hair_twintails_white_ribbons"),
        accessory=getWearable("jn_accessory_double_white_hairbands"),
        necklace=getWearable("jn_necklace_twirled_choker"),
        facewear=getWearable("jn_facewear_plasters")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_cosy_cardigan_outfit",
        display_name="Conjunto acogedor cardigan",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_cosy_cardigan"),
        accessory=getWearable("jn_accessory_hairband_red"),
        headgear=getWearable("jn_headgear_teddy_hairpins"),
        hairstyle=getWearable("jn_hair_twintails")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_pastel_goth_getup",
        display_name="Conjunto pastel goth",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_pastel_goth_overalls"),
        hairstyle=getWearable("jn_hair_down"),
        necklace=getWearable("jn_necklace_spiked_choker"),
        headgear=getWearable("jn_headgear_spiked_headband"),
        facewear=getWearable("jn_facewear_sprinkles")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_ruffle_neck_sweater_outfit",
        display_name="Conjunto con suéter de cuello volado",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_ruffle_neck_sweater"),
        accessory=getWearable("jn_accessory_hairband_red"),
        hairstyle=getWearable("jn_hair_twin_buns")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_heart_sweater_outfit",
        display_name="Conjunto de suéter de corazón",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_heart_sweater"),
        accessory=getWearable("jn_accessory_hairband_red"),
        hairstyle=getWearable("jn_hair_twin_buns")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_chocolate_plaid_collection",
        display_name="Colección de cuadros de chocolate",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_chocolate_plaid_dress"),
        headgear=getWearable("jn_headgear_chocolate_plaid_bow"),
        necklace=getWearable("jn_necklace_golden_necklace"),
        hairstyle=getWearable("jn_hair_ponytail")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_office_outfit",
        display_name="Atuendo de oficina",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_office_blazer"),
        hairstyle=getWearable("jn_hair_wavy"),
        necklace=getWearable("jn_necklace_formal_necktie")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_chick_outfit",
        display_name="Traje de pollito",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_chick_dress"),
        accessory=getWearable("jn_accessory_fried_egg_hairpin"),
        hairstyle=getWearable("jn_hair_twintails_braided"),
        necklace=getWearable("jn_necklace_bunny_necklace")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_cherry_blossom_outfit",
        display_name="Atuendo de flor de cerezo",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_cherry_blossom_dress"),
        accessory=getWearable("jn_accessory_cherry_blossom_hairpin"),
        hairstyle=getWearable("jn_hair_twintails_braided"),
        necklace=getWearable("jn_necklace_bunny_necklace")
    ))
    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_magical_girl_cosplay",
        display_name="Cosplay de chica mágica",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_magical_girl"),
        hairstyle=getWearable("jn_hair_twintails"),
        accessory=getWearable("jn_accessory_hairband_stars"),
        headgear=getWearable("jn_headgear_hairtie"),
        necklace=getWearable("jn_necklace_plain_choker")
    ))




    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_temporary_outfit",
        display_name="Atuendo temporal",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_school_uniform"),
        hairstyle=getWearable("jn_hair_twintails"),
        accessory=getWearable("jn_accessory_hairband_red")
    ))


    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_ahoge_unlock",
        display_name="Desbloqueo de Ahoge",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_star_pajamas"),
        hairstyle=getWearable("jn_hair_super_messy")
    ))


    _m1_outfits__registerOutfit(JNOutfit(
        reference_name="jn_raincoat_unlock",
        display_name="Desbloqueo del impermeable",
        unlocked=False,
        is_jn_outfit=True,
        clothes=getWearable("jn_clothes_raincoat"),
        hairstyle=getWearable("jn_hair_down"),
        accessory=getWearable("jn_accessory_hairband_red"),
        headgear=getWearable("jn_headgear_raincoat_hood")
    ))


    _m1_outfits__PAJAMA_CHOICE = getOutfit("jn_bunny_pajamas") if random.randint(0, 10) == 1 else getOutfit("jn_star_pajamas")


    _OUTFIT_SCHEDULE_WEEKDAY_HIGH_AFFINITY = {
        store.JNTimeBlocks.early_morning: _m1_outfits__PAJAMA_CHOICE,
        store.JNTimeBlocks.mid_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.late_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.afternoon: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.evening: random.choice((getOutfit("jn_casual_clothes"), getOutfit("jn_hoodie_turtleneck"))),
        store.JNTimeBlocks.night: _m1_outfits__PAJAMA_CHOICE
    }

    _OUTFIT_SCHEDULE_WEEKEND_HIGH_AFFINITY = {
        store.JNTimeBlocks.early_morning: _m1_outfits__PAJAMA_CHOICE,
        store.JNTimeBlocks.mid_morning: _m1_outfits__PAJAMA_CHOICE,
        store.JNTimeBlocks.late_morning: _m1_outfits__PAJAMA_CHOICE,
        store.JNTimeBlocks.afternoon: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.evening: random.choice((getOutfit("jn_casual_clothes"), getOutfit("jn_hoodie_turtleneck"))),
        store.JNTimeBlocks.night: _m1_outfits__PAJAMA_CHOICE
    }

    _OUTFIT_SCHEDULE_WEEKDAY_MEDIUM_AFFINITY = {
        store.JNTimeBlocks.early_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.mid_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.late_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.afternoon: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.evening: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.night: getOutfit("jn_casual_clothes")
    }

    _OUTFIT_SCHEDULE_WEEKEND_MEDIUM_AFFINITY = {
        store.JNTimeBlocks.early_morning: _m1_outfits__PAJAMA_CHOICE,
        store.JNTimeBlocks.mid_morning: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.late_morning: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.afternoon: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.evening: getOutfit("jn_casual_clothes"),
        store.JNTimeBlocks.night: random.choice((getOutfit("jn_casual_clothes"), getOutfit("jn_hoodie_turtleneck")))
    }

    _OUTFIT_SCHEDULE_WEEKDAY_LOW_AFFINITY = {
        store.JNTimeBlocks.early_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.mid_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.late_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.afternoon: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.evening: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.night: getOutfit("jn_casual_clothes")
    }

    _OUTFIT_SCHEDULE_WEEKEND_LOW_AFFINITY = {
        store.JNTimeBlocks.early_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.mid_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.late_morning: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.afternoon: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.evening: getOutfit("jn_school_uniform"),
        store.JNTimeBlocks.night: getOutfit("jn_casual_clothes")
    }


label outfits_wear_outfit:
    python:

        jn_outfits.unloadCustomOutfits()
        jn_outfits.unloadCustomWearables()


        jn_outfits.loadCustomWearables()
        jn_outfits.loadCustomOutfits()


        jn_outfits.JNWearable.loadAll()
        jn_outfits.JNOutfit.loadAll()

    if not jn_outfits.getAllOutfits():

        n 4tnmbo "¿Eh? {w=0.5}{nw}"
        extend 1fchbg "¡No tengo más conjuntos, {w=0.2}tonto!"

        jump ch30_loop

    elif len(jn_outfits.getSafePendingUnlocks()):

        n 1nsqpu "...Espera. {w=1.25}{nw}"
        extend 3tnmfl " ¿Qué {i}es eso{/i} que tienes en la mano?"
        n 1fcstrlesi "{i}¡Al menos{/i} muéstrame qué es primero!"

        show natsuki 1fcspol

        $ jnRemoveTopicFromEventList("new_wearables_outfits_unlocked")
        jump new_wearables_outfits_unlocked

    $ dialogue_choice = random.randint(1, 3)
    if dialogue_choice == 1:
        n 4tnmpu "¿Eh? {w=0.75}{nw}"
        extend 4tnmbo " ¿Quieres ver otro atuendo, {w=0.2} [player]?"

    elif dialogue_choice == 2:
        n 4tnmss "¿Oh? {w=0.75}{nw}"
        extend 4clrss " ¿Quieres verme probar algo diferente {w=0.2} [player]?"
    else:

        n 4unmaj "¿Eh? {w=0.75}{nw}"
        extend 4unmbo " ¿Quieres que me pruebe otro conjunto?"

    if Natsuki.isEnamored(higher=True):
        n 1fchbgl "¡Por supuesto!{w=0.75}{nw}"
        $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
        extend 1unmbgl " ¿Qué querías ver, {w=0.2} [chosen_descriptor]?"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchbg "¡Sí! {w=0.2} ¡Puedo hacerlo! {w=0.75}{nw}"
        extend 1tnmss " ¿Qué estás pensando, {w=0.2} [player]?"
    else:

        n 4unmaj "Seguro, {w=0.2} Puedo hacerlo."
        n 7tlrsl "Entonces... {w=1}{nw}"
        extend 7unmbo " ¿Tenías algo en mente, {w=0.2} o?"

    if Natsuki.isAffectionate(higher=True):
        show natsuki option_wait_excited at jn_left
    else:

        show natsuki option_wait_curious at jn_left

    python:

        available_outfits = jn_outfits.JNOutfit.filterOutfits(
            outfit_list=jn_outfits.getAllOutfits(),
            unlocked=True)
        outfit_options = [(jn_utils.escapeRenpySubstitutionString(outfit.display_name), outfit) for outfit in available_outfits]
        outfit_options.sort(key = lambda option: (not option[1].is_jn_outfit, option[1].display_name))
        outfit_options.insert(0, ("¡Tú eliges!", "random"))

    $ outfit_confirmed = False
    while not outfit_confirmed:

        call screen outfit_item_menu(outfit_options)
        show natsuki at jn_center

        if isinstance(_return, jn_outfits.JNOutfit):
            if _return.reference_name == Natsuki.getOutfitName():

                n 2fchsmesm "¡Pffff-!"
                n 2tsqss "En realidad, {w=0.2} [player]? {w=0.75}{nw}"
                extend 4fsgbg " ¿Necesitas que te revisen los ojos o algo?"
                $ chosen_descriptor = "tú {0}".format(jn_utils.getRandomTeaseName()) if Natsuki.isAffectionate(higher=True) else player
                n 4fchgn "Ya lo llevo puesto {w=0.2} [chosen_descriptor]! {w=0.75}{nw}"
                extend 3fsqbg " Al menos elige {i}algo{/i} diferente!"

                show natsuki option_wait_smug at jn_left
            else:


                $ outfit_name = _return.display_name.lower().capitalize()

                if Natsuki.isEnamored(higher=True):
                    n 4ulraj "Mi [outfit_name],{w=0.5}{nw}"
                    extend 2unmbo " [player]?"
                    n 1fcssml "Jejeje. {w=0.75}{nw}"
                    extend 3uchgnl " ¡Apuesto a que sí!"
                    n 3ccsbgl "Sólo un segundo aquí... {w=2}{nw}"

                    show natsuki 4ccssml

                elif Natsuki.isAffectionate(higher=True):
                    n 4unmaj "¿Oh?{w=0.75}{nw}"
                    extend 4tnmbo " Quieres que me ponga mi [outfit_name]?{w=0.75}{nw}"
                    extend 2fchbg " Gotcha!"
                    n 1fcsbg "Sólo dame un segundo aquí... {w=2}{nw}"

                    show natsuki 4fcssm
                else:

                    n 2ullaj "[outfit_name],{w=0.5}{nw}"
                    extend 2tnmbo " ¿eh? {w=0.75}{nw}"
                    extend 4fchsm " ¡Lo entendiste!"
                    n 2clrsssbl "Sólo dame un segundo aquí. {w=0.75}{nw}"
                    extend 2fcspolsbl " ¡Y- {w=0.2}y no mires! {w=2}{nw}"

                    show natsuki 4fcsbol

                play audio clothing_ruffle
                $ Natsuki.setOutfit(_return)
                with Fade(out_time=0.5, hold_time=1, in_time=0.5, color="#181212")

                if Natsuki.isEnamored(higher=True):
                    show natsuki 3ccssml

                elif Natsuki.isAffectionate(higher=True):
                    show natsuki 2fcssm
                else:

                    show natsuki 2fcssm

                if Natsuki.isEnamored(higher=True):
                    n 3nchgnl "¡¡¡Está bien!!!"
                    $ chosen_descriptor = jn_utils.getRandomEndearment() if Natsuki.isLove(higher=True) else player
                    n 3fsqbgl "¿C- {w=0.2}cómo me veo, {w=0.2} [chosen_descriptor]?{w=0.75}{nw}"
                    extend 5fchsml " Jejeje."

                elif Natsuki.isAffectionate(higher=True):
                    n 1fchbg "¡Está bien!"
                    n 4fcsbglsbr "¿C- {w=0.2}cómo me veo{w=0.2} [player]?{w=0.75}{nw}"
                    extend 4fsldvlsbr " Ehehe."
                else:

                    n 2fcsbg "Y... {w=1}{nw}"
                    extend 2fchgn " ¡Estamos bien para ir!"

                $ persistent.jn_natsuki_auto_outfit_change_enabled = False
                $ outfit_confirmed = True

        elif _return == "random":

            n 1fchbg "¡Lo entendiste! {w=0.75}{nw}"
            extend 7fslss " Ahora, ¿qué tenemos aquí ..."
            n 7ccssresp "..."
            n 4fnmbg "¡Aja! {w=0.75}{nw}"
            extend 4fchbg " Esto servirá. {w=0.75}{nw}"
            extend 1uchsm " ¡Un segundo! {w=2}{nw}"

            play audio clothing_ruffle
            $ Natsuki.setOutfit(
                random.choice(
                    jn_outfits.JNOutfit.filterOutfits(
                        outfit_list=jn_outfits.getAllOutfits(),
                        unlocked=True,
                        not_reference_name=Natsuki.getOutfitName())
                )
            )
            with Fade(out_time=0.5, hold_time=1, in_time=0.5, color="#181212")

            n 1nchbg "¡Todo listo!"
            $ persistent.jn_natsuki_auto_outfit_change_enabled = False
            $ outfit_confirmed = True
        else:


            n 1nnmbo "Oh. {w=1.5}{nw}"
            extend 1nllaj " Bien, {w=0.2} está bien."
            n 3nsrpol "De todos modos no me quería cambiar."
            $ outfit_confirmed = True

    return


label outfits_reload:
    n 4tsqpueqm "¿Eh? {w=0.75}{nw}"
    extend 2tnmbo " {i}¿Nuevos artículos{/i}?"

    python:

        jn_outfits.unloadCustomOutfits()
        jn_outfits.unloadCustomWearables()


        jn_outfits.loadCustomWearables()
        jn_outfits.loadCustomOutfits()


        jn_outfits.JNWearable.loadAll()
        jn_outfits.JNOutfit.loadAll()

    if len(jn_outfits.getSafePendingUnlocks()):
        n 2tllsl "..."
        n 2tllfl "No... {w=1}{nw}"
        extend 4tllbo " lo entiendo, {w=0.5}{nw}"
        extend 4tnmbo " [player]."
        n 7tnmfl "¿Qué quieres decir? {w=0.75}{nw}"
        extend 7tlrfl " Yo- {w=0.5}{nw}"
        show natsuki 4udwflleshsbl

        $ jnRemoveTopicFromEventList("new_wearables_outfits_unlocked")
        jump new_wearables_outfits_unlocked
    else:

        n 2tlrbo "..."
        n 2tlrfl "Yo no... {w=1}{nw}"
        extend 2tnmbo " no puedo ver nada, {w=0.2} [player].{w=0.75}{nw}"
        extend 4tsqpu " ¿Por qué lo preguntas, {w=0.2} de todos modos?"
        n 3cllfll "S- {w=0.2}será mejor que no intentes bombardearme con regalos o algo así."

        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 5cllpulsbr "Deberías saber que, de todos modos, ya no tienes por qué demostrar nada de eso. {w=0.5}{nw}"
            extend 2cslpolsbr " [chosen_tease]."

        elif Natsuki.isAffectionate(higher=True):
            n 2ccsfllsbl "Deberías saber que odio que me hagan sentir incómoda a estas alturas. {w=0.75}{nw}"
            extend 5csrcalsbl " E- {w=0.2}especialmente con un montón de cosas elegantes."
        else:

            n 2ccstrlsbl "No quiero sentirme incómoda con las sorpresas."

    return


label outfits_suggest_outfit:

    if len(jn_outfits.getSafePendingUnlocks()):

        n 1nsqpu "...Espera. {w=1.25}{nw}"
        extend 3tnmfl " ¿Qué{i}es eso{/i} que tienes en la mano?"
        n 1fcstrlesi "¡{i}Al menos{/i} muéstrame qué es primero!"
        show natsuki 1fcspol

        $ jnRemoveTopicFromEventList("new_wearables_outfits_unlocked")
        jump new_wearables_outfits_unlocked

    n 4unmaj "¡Oh!{w=1}{nw}"
    extend 4fchbg " Sí.{w=0.2} ¡Aceptaré una sugerencia!{w=0.75}{nw}"
    extend 7unmss " ¿En qué estás pensando,{w=0.2} [player]?"

    python:

        import copy
        jn_outfits._LAST_OUTFIT = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        jn_outfits._PREVIEW_OUTFIT = copy.copy(jn_outfits.getOutfit(Natsuki.getOutfitName()))
        jn_outfits._changes_made = False

    show natsuki option_wait_curious at jn_left
    jump outfits_create_menu


label outfits_remove_outfit:

    if len(jn_outfits.getSafePendingUnlocks()):

        n 1nsqpu "...Espera. {w=1.25}{nw}"
        extend 3fnmpo "¿Estas intentando ocultar algo?"
        n 1fcstrlesi "¡Al menos muéstrame qué es primero!"
        show natsuki 1fcspol

        $ jnRemoveTopicFromEventList("new_wearables_outfits_unlocked")
        jump new_wearables_outfits_unlocked

    elif (
        not jn_outfits.getAllOutfits()
        or len(jn_outfits.JNOutfit.filterOutfits(
            outfit_list=jn_outfits.getAllOutfits(),
            unlocked=True,
            is_jn_outfit=False)) == 0
    ):

        n 1tnmbo "¿Eh?{w=0.5}{nw}"
        $ chosen_tease = jn_utils.getRandomTease() if Natsuki.isEnamored(higher=True) else "dummy"
        extend 1fchbg " {i}¡No hay{/i} ningun atuendo tuyo que pueda olvidar.{w=0.2} [chosen_tease]!"

        jump ch30_loop

    n 1unmpu "¿Quieres que me olvide de un conjunto? {w=0.5}{nw}"
    extend 1nllpu " Supongo que puedo hacerlo."
    n 1nslss "Pero... {w=1}{nw}"
    extend 1fsrpol " Me quedo con las que se me ocurrieron."

    python:

        options = []
        removable_outfits = jn_outfits.JNOutfit.filterOutfits(
            outfit_list=jn_outfits.getAllOutfits(),
            unlocked=True,
            is_jn_outfit=False)

        removable_outfits.sort(key = lambda option: option.display_name)

        for outfit in removable_outfits:
            options.append((jn_utils.escapeRenpySubstitutionString(outfit.display_name), outfit))

    show natsuki option_wait_curious at jn_left
    call screen scrollable_choice_menu(options, ("No importa.", None))
    show natsuki at jn_center

    if isinstance(_return, jn_outfits.JNOutfit):
        $ outfit_name = _return.display_name.lower().capitalize()
        n 1unmaj "¿Oh?{w=0.5} [outfit_name]?{w=0.75}{nw}"
        extend 1unmbo " ¿Ese atuendo?"

        show natsuki option_wait_curious
        menu:
            n "¿Estás seguro que quieres que me olvide de ello?"
            "Sí, olvídate de [outfit_name]":

                if Natsuki.isWearingOutfit(_return.reference_name):

                    n 7ullaj "Bien... {w=1}{nw}"
                    extend 7fslss " ya que no volveré a usar {i}eso{/i} en un futuro próximo..."
                    n 7fchgn "¿Supongo que probablemente debería cambiar,{w=0.2} eh?"
                    show natsuki 4fcssmeme

                    play audio clothing_ruffle
                    $ Natsuki.setOutfit(jn_outfits.getOutfit("jn_casual_clothes"))
                    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

                n 1nchgn "¡¡¡Está bien!!!{w=1}{nw}"
                extend 1ncsbg " Sólo dame un segundo aquí... {w=1}{nw}"

                if jn_outfits.deleteCustomOutfit(_return):
                    n 1fchsm "...¡Y se fue!"
                else:

                    n 4kslfl "...Oh."
                    n 4kllfl "Ey... {w=1}{nw}"
                    extend 5knmpu " [player]?"
                    n 2kdrfl "Yo... {w=1}{nw}"
                    extend 2kdrsssbr " No puedo olvidarme de ese atuendo por alguna razón. {w=0.75}{nw}"
                    extend 5ksrcasbr "Lo siento."
            "No importa":

                n 1nnmbo "Oh."
                n 1ullaj "Bien... {w=1}{nw}"
                extend 1nllca "Está bien entonces."
    else:

        n 1nnmbo "Oh. {w=1}{nw}"
        extend 1nchgn " ¡Bien, {w=0.2} me queda bien!"

    jump ch30_loop


label outfits_create_menu:
    show natsuki option_wait_curious at jn_left
    call screen create_outfit


label outfits_create_select_headgear:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNHeadgear)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin casco", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un casco...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNHeadgear):
        play audio clothing_ruffle
        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.headgear = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_hairstyle:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNHairstyle)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (option[1].is_jn_wearable, option[1].display_name))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un estilo de cabello...")

    if isinstance(_return, jn_outfits.JNHairstyle):
        play audio hair_brush
        python:
            jn_outfits._changes_made = True
            jn_outfits._PREVIEW_OUTFIT.hairstyle = _return
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_eyewear:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNEyewear)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin gafas", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige una gafa...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNEyewear):
        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.eyewear = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_accessory:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNAccessory)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin accesorios", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un accesorio...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNAccessory):
        play audio hair_clip
        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.accessory = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_necklace:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNNecklace)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin collar", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un collar...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNNecklace):
        play audio necklace_clip
        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.necklace = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_clothes:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNClothes)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige una prenda de ropa...")

    if isinstance(_return, jn_outfits.JNClothes):
        if (random.choice([True, False])):
            play audio clothing_ruffle
        else:
            play audio zipper

        python:
            jn_outfits._changes_made = True
            jn_outfits._PREVIEW_OUTFIT.clothes = _return
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_facewear:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNFacewear)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin accesorio facial", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un accesorio para la cara...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNFacewear):
        play audio hair_clip
        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.facewear = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_select_back:
    python:
        unlocked_wearables = jn_outfits.JNWearable.filterWearables(wearable_list=jn_outfits.getAllWearables(), unlocked=True, wearable_type=jn_outfits.JNBack)
        wearable_options = [(jn_utils.escapeRenpySubstitutionString(wearable.display_name), wearable) for wearable in unlocked_wearables]
        wearable_options.sort(key = lambda option: (not option[1].is_jn_wearable, option[1].display_name))
        wearable_options.insert(0, ("Sin accesorio trasero", "none"))

    call screen scrollable_choice_menu(items=wearable_options, last_item=("No importa.", None), menu_caption="Elige un artículo de la parte trasera...")

    if isinstance(_return, basestring) or isinstance(_return, jn_outfits.JNBack):
        if (random.choice([True, False])):
            play audio clothing_ruffle
        else:
            play audio zipper

        python:
            jn_outfits._changes_made = True
            wearable_to_apply = jn_outfits.getWearable("jn_none") if _return == "none" else _return
            jn_outfits._PREVIEW_OUTFIT.back = wearable_to_apply
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_copy:
    python:
        options = []
        available_outfits = jn_outfits.JNOutfit.filterOutfits(
            outfit_list=jn_outfits.getAllOutfits(),
            unlocked=True,
            is_jn_outfit=False)

        available_outfits.sort(key = lambda option: option.display_name)

        for outfit in available_outfits:
            options.append((jn_utils.escapeRenpySubstitutionString(outfit.display_name), outfit))

    call screen scrollable_choice_menu(items=options, last_item=("No importa.", None), menu_caption="¿Qué conjunto quieres copiar?")

    if isinstance(_return, jn_outfits.JNOutfit):
        play audio clothing_ruffle

        python:
            import copy

            jn_outfits._changes_made = True
            jn_outfits._PREVIEW_OUTFIT = copy.copy(_return)
            Natsuki.setOutfit(jn_outfits._PREVIEW_OUTFIT)

    jump outfits_create_menu


label outfits_create_quit:
    if jn_outfits._changes_made:
        n 4unmaj "¿Eh? {w=0.5}{nw}"
        extend 1tnmbo "¿Ya has terminado, {w=0.1} [player]?"

        show natsuki option_wait_curious
        menu:
            n "¿Estás seguro de que no quieres que pruebe más cosas?"
            "Sí, todavía no he terminado":


                n 7fcsbg "¡Entiendo! {w=0.75}{nw}"
                extend 7tsqsm "¿Qué más tienes?"

                jump outfits_create_menu
            "No, hemos terminado aquí":


                n 1nnmbo "Oh. {w=1.5}{nw}"
                extend 1nllaj "Bien... {w=0.3} esta bien."
                n 2nsrpol "Me aburrí de cambiar de todos modos."

                show natsuki at jn_center
                play audio clothing_ruffle
                $ Natsuki.setOutfit(jn_outfits._LAST_OUTFIT)
                with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")
                jump ch30_loop
    else:

        show natsuki at jn_center
        n 4tllaj "Entonces... {w=1}{nw}"
        extend 3tnmpo "¿No quieres que cambie después de todo?"
        n 1nlrbo "Ehh."
        n 1tnmss "Bueno, {w=0.2} si no está roto, no lo arregles, {w=0.2}¿verdad? {w=0.75}{nw}"
        extend 2fcssm " Jejeje."
        jump ch30_loop


label outfits_create_save:
    n 4fllaj "¡Bueno, {w=0.5}finalmente!"
    n 3flrpo "Si hubiera sabido que te gustaba {i}tanto{/i} disfrazarte. {w=0.3}¡Habría puesto un temporizador! {w=1.5}{nw}"
    extend 3fsqsm " Jejeje."
    n 1ullaj "Entonces..."

    show natsuki option_wait_curious
    menu:
        n "Todo terminado, {w=0.2}[player]?"
        "Sí, me gustaría guardar este atuendo":

            n 1fchbg "¡Entendido! {w=1.5}{nw}"
            extend 1unmsm "¿Cómo quieres nombrarlo?"

            $ name_given = False
            $ no_name_count = 0
            $ robot_repeat_count = 0
            $ profanity_repeat_count = 0
            $ duplicate_repeat_count = 0

            show natsuki option_wait_excited at jn_center

            while not name_given:
                $ outfit_name = renpy.input(
                    "¿Cómo se llama este atuendo,[player]?",
                    allow=(jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES+jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES),
                    length=30
                ).strip()


                if len(outfit_name) == 0 or outfit_name is None or outfit_name.isspace():
                    if no_name_count == 0:
                        n 2knmpo "Vamos, {w=0.2}[player]! {w=1.5}{nw}"
                        extend 1fchbg " ¡Cualquier atuendo que valga la pena recordar tiene un {i}nombre{/i}!"

                        show natsuki option_wait_smug

                    elif no_name_count == 1:
                        n 4ccsss "Je. {w=0.75}{nw}"
                        extend 4csqbg " ¿Qué es esto, {w=0.2}[player]?"
                        n 2fsqbg "¿Estás tratando de darme el tratamiento silencioso ahora o algo así?"
                        $ chosen_tease_name = jn_utils.getRandomTeaseName()
                        n 2fcsbg "Escúpelo ya, {w=0.2} tú [chosen_tease_name]!"
                        show natsuki option_wait_smug

                    elif no_name_count == 2:
                        n 3csqflsbr "[player]. {w=0.75}{nw}"
                        extend 3csqcasbr "Vamos."
                        n 3cslbosbr "Ambos sabemos que tengo que nombrarlo {i}de alguna forma{/i}."

                        show natsuki option_wait_sulky
                    else:

                        n 2csqtrsbr "...Deja de hacer tonterías, {w=0.2}[player]."

                        show natsuki option_wait_sulky

                    $ no_name_count += 1


                elif re.search("^jn_.", outfit_name.lower()):
                    if robot_repeat_count == 0:
                        n 2csqfl "[outfit_name]?"
                        n 2tsqsssbl "...¿Es algún tipo de nombre de robot o algo así?"
                        n 7fcsbg "Esfuérzate más, {w=0.2}[player]!"

                        show natsuki option_wait_smug

                    elif robot_repeat_count == 1:
                        n 2tsqpu "...¿En serio? {w=0.75}{nw}"
                        extend 2csqsssbl "¿Esto otra vez?"
                        n 2ccsss "Lo siento, {w=0.2}[player]. {w=0.75}{nw}"
                        extend 2ccssmesm "¡Supongo que simplemente no hablo robot!"

                        show natsuki option_wait_smug

                    elif robot_repeat_count == 2:
                        n 3csqbo "..."
                        n 3csqtr "...De ninguna manera {w=0.2}[player]."

                        show natsuki option_wait_sulky
                    else:

                        n 3csqcasbr "... No."

                        show natsuki option_wait_sulky

                    $ robot_repeat_count += 1


                elif (
                    jn_utils.getStringContainsProfanity(outfit_name.lower())
                    or jn_utils.getStringContainsInsult(outfit_name.lower())
                ):
                    if profanity_repeat_count == 0:
                        n 2fsqem "...Enserio, {w=0.5} [player]."
                        n 2fsqsr "Vamos. {w=1}{nw}"
                        extend 4fllsr " Deja de ser un idiota."

                        show natsuki_option_wait_annoyed

                    elif profanity_repeat_count == 1:
                        n 4fsqfl "En serio, {w=0.2}[player]. {w=0.75}{nw}"
                        extend 4fsqan " La primera vez ni siquiera fue gracioso."
                        n 2fcsem "Ahora toca. {w=1}{nw}"
                        extend 2fcsan " Él. {w=1}{nw}"
                        extend 2fsqfr " Botón."

                        show natsuki_option_wait_annoyed
                    else:

                        n 2fsqsr "..."

                        show natsuki_option_wait_annoyed

                    $ profanity_repeat_count += 1
                    $ Natsuki.addApology(jn_apologies.ApologyTypes.rude)
                    $ Natsuki.percentageAffinityLoss(2)

                    if Natsuki.isNormal(lower=True):

                        n 2fcsemesi "..."
                        n 2fcsfl "...De hecho."
                        extend 2fsqan "¿Sabes que?"
                        extend 4fsqwr "Olvídalo."
                        n 4fcsem "Hemos terminado aquí, {w=0.2} [player]."
                        n 4fsqan "Idiota."

                        $ jn_outfits._changes_made = False
                        show natsuki 4fcsfr
                        $ jnPause(0.1)
                        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                        $ Natsuki.setOutfit(jn_outfits.getOutfit("jn_school_uniform"))
                        play audio clothing_ruffle
                        $ jnPause(2)
                        show natsuki 2fsrfr
                        hide black with Dissolve(1.25)

                        jump ch30_loop


                elif len(jn_outfits.JNOutfit.filterOutfits(outfit_list=jn_outfits.getAllOutfits(), display_name=[outfit_name])) != 0:
                    if duplicate_repeat_count == 0:
                        n 2nsqaj "Guau. {w=0.75}{nw}"
                        extend 2tsqfl " ¿En serio, {w=0.2}[player]? {w=0.75}{nw}"
                        extend 4fsqbg " ¿En serio ya lo olvidaste?"
                        $ chosen_descriptor = "tú {0}".format(jn_utils.getRandomTeaseName()) if Natsuki.isAffectionate(higher=True) else player
                        n 6fcsbg "Ya {i}tengo{/i}un conjunto que se llama así, {w=0.5}{nw}"
                        extend 3fchgn "[chosen_descriptor]!"
                        n 3clrbg "Por Dios... {w=1}{nw}"
                        extend 7ccsbgesm " Podrías al menos {i}intentar{/i} ser original, {w=0.2}sabes."
                        n 7fsqsm "Jejeje."
                        n 3fcsbg "¡Dame otro, {w=0.2}[player]!"

                        show natsuki option_wait_smug

                    elif duplicate_repeat_count == 1:
                        n 2tsqsl "..."
                        n 2tsrfl "Tú... {w=1.5}{nw}"
                        extend 4tlrfl "Me gusta mucho ese nombre, {w=0.5}{nw}"
                        extend 4tnmbo "eh."
                        n 1tllbo "..."
                        n 3ccsbg "Bueno, {w=0.2}todavía no sucede, {w=0.2}[player]. {w=0.75}{nw}"
                        extend 3fchgn "¡Lo siento!"

                        show natsuki option_wait_smug

                    elif duplicate_repeat_count == 2:
                        n 2tsqpu "..."
                        n 2tsqslsbl "...¿En realidad, {w=0.2}[player]?"

                        show natsuki option_wait_sulky
                    else:

                        n 2csqflsbr "...¿No tienes nada mejor que hacer?"

                        show natsuki option_wait_sulky

                    $ duplicate_repeat_count += 1
                else:


                    python:
                        jn_outfits._PREVIEW_OUTFIT.display_name = outfit_name
                        name_given = True

            show natsuki at jn_center

            n 1nchbg "¡¡¡Está bien!!! {w=1.5}{nw}"
            extend 1ncsss " Sólo voy a hacer una nota mental rápida aquí... {w=1.5}{nw}"

            if jn_outfits.saveCustomOutfit(jn_outfits._PREVIEW_OUTFIT):
                n 1uchsm "...¡Y listo!"
                n 1fchbg "¡Gracias, {w=0.2}[player]! {w=0.75}{nw}"
                extend 4uchsm " Jejeje."

                $ jn_outfits._changes_made = False
                jump ch30_loop
            else:

                n 4kslfl "...Oh."
                n 4kllfl "Ey... {w=1}{nw}"
                extend 5knmpu " [player]?"
                n 2kdrfl "Yo... {w=1}{nw}"
                extend 2kdrsssbr " No puedo tomar nota de ese atuendo por alguna razón. {w=0.75}{nw}"
                extend 5ksrcasbr "¡Lo siento!."

                jump outfits_create_menu
        "Sí, pero no te preocupes por guardar este atuendo":

            n 4tnmpueqm "¿Eh? {w=0.75}{nw}"
            extend 1tnmaj "¿No {i}quieres{/i} que me acuerde de esto?"
            n 1ullaj "Bueno... {w=0.75}{nw}"
            extend 2tnmss " Si insistes."
            n 1nchgneme "¡Menos toma de notas para mí!"

            $ jn_outfits._changes_made = False
            $ jn_outfits.saveTemporaryOutfit(jn_outfits._PREVIEW_OUTFIT)
            jump ch30_loop
        "No, aún no he terminado":

            n 3nslpo "Yo {i}sabía{/i}, que debería haber traído un libro. {w=0.75}{nw}"
            extend 1fsqsm " Jejeje."
            n 1ulrss "Bueno, {w=0.2} lo que sea. {w=0.5}{nw}"
            extend 4unmbo "¿Qué más tenías en mente, {w=0.2}[player]?"

            jump outfits_create_menu


label outfits_auto_change:
    if Natsuki.isEnamored(higher=True):
        n 1uchbg "¡Oh!{w=0.2} Tengo que cambiarme, {w=0.1} solo dame un segundo... {w=0.75}{nw}"

    elif Natsuki.isHappy(higher=True):
        n 4unmpu "¡Oh!{w=0.2} Probablemente debería cambiarme, {w=0.1} un segundo.{w=0.75} .{w=0.75} .{w=0.75}{nw}"
        n 2flrpol "¡¿Y-{w=0.1}y sin mirar, {w=0.1} entiendes?! {w=0.75}{nw}"

    elif Natsuki.isNormal(higher=True):
        n 4unmpu "Oh -{w=0.1}Tengo que cambiarme. {w=0.2} Regresaré en un segundo.{w=0.75}{nw}"

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "Vuelvo en un segundo. {w=0.75}{nw}"
    else:

        n 2fsqsl "Estoy cambiandome {w=0.75}{nw}"

    play audio clothing_ruffle
    $ Natsuki.setOutfit(jn_outfits.getRealtimeOutfit())
    with Fade(out_time=0.1, hold_time=1, in_time=0.5, color="#181212")

    if Natsuki.isAffectionate(higher=True):
        n 4uchgn "¡Ta-da! {w=0.2}¡Allá vamos! {w=0.2}Jejeje. {w=0.75}{nw}"

    elif Natsuki.isHappy(higher=True):
        n 1nchbg "¡¡¡Está bien!!! {w=0.2}¡Ya estoy de vuelta! {w=0.75}{nw}"

    elif Natsuki.isNormal(higher=True):
        n 1nnmsm "Y... {w=0.3}todo listo. {w=0.75}{nw}"

    elif Natsuki.isDistressed(higher=True):
        n 3nllsl "Ya estoy de vuelta. {w=0.75}{nw}"
    else:

        n 2fsqsl "... {w=0.75}{nw}"

    $ jnShowNatsukiIdle(jn_center)
    return

label new_wearables_outfits_unlocked:
    python:
        jn_globals.force_quit_enabled = False
        giftbox = random.choice([
            jn_gifts.GIFT_BLUE,
            jn_gifts.GIFT_GREEN,
            jn_gifts.GIFT_PINK,
            jn_gifts.GIFT_PURPLE,
        ])
        giftbox.present()
        jnPause(2.25)
        unlocks = jn_outfits.getSafePendingUnlocks()

    if Natsuki.isEnamored(higher=True):
        n 1uskemleex "...!"
        n 4ksrunlsbl "..."
        n 4knmpulsbl "[player]... {w=1.25}{nw}"
        extend 2kllpulsbl " S- {w=0.2}sabes que no tienes que comprarme cosas sólo para gustarme..."
        n 1knmsllsbr "¿verdad?"

        if jnIsPlayerBirthday():
            n 1uskgslesh "...¡Espera! {w=0.75}{nw}"
            extend 1knmemlsbl " ¡D- {w=0.2}de todos modos ni siquiera deberías ser tú el que {i}da{/i} cosas hoy!"
            n 2kslemlsbl "...Es {i}raro{/i}, {w=0.2} [player]..."
            n 1kslbolsbl "..."

        elif jnIsNatsukiBirthday():
            if persistent._jn_natsuki_birthday_known:
                n 1ccsfllsbr "...A- {w=0.2}aunque sea {i}{/i} mi cumpleaños. {w=0.75}{nw}"
                extend 2clrbolsbr " Por Dios."
                n 2ksrcalsbr "Deberías {i}saber{/i} que, por ahora no estoy acostumbrado a recibir todas las cosas de lujo..."
            else:

                n 2ccsemlsbr "¡N- {w=0.2}no importa qué día pase! {w=0.75}{nw}"
                extend 2cllslfsbr " Por Dios..."

        elif jnIsChristmasEve():
            n 2ksrbofsbl "...Especialmente esta noche, {w=0.3} de todas las noches ..."

        elif jnIsChristmasDay():
            n 4kllajlsbr "Y- {w=0.2}y de todos modos, {w=0.75}{nw}"
            extend 1kwmpulsbl " Todavía no estoy acostumbrado a conseguir cosas en el día de Navidad..."
            n 2kslsllsbl "..."

        n 1uskemlesusbr "¡N- {w=0.2}no es que no lo aprecie! {w=0.5}{nw}"
        extend 1fcsemless " ¡No me malentiendas! {w=1}{nw}"
        extend 2knmpoless " ¡L- {w=0.2}lo hago totalmente!"
        n 1kllemless "Yo sólo..."
        n 2ksrunlsbl "..."
        n 1fcsunl "Yo... {w=0.3} sabes... {w=1}{nw}"
        extend 2ksrpolsbr " No puedo devolverte exactamente el favor."
        n 1fcsajlsbl "Y- {w=0.2}y ya has hecho mucho por mí, {w=0.5}{nw}"
        extend 4kslbolsbl "Entonces..."
        n 1kcsbolsbl "..."
        n 1kcsemlesi "...Bien. {w=0.75}{nw}"
        extend 1ksrsl " Voy a echar un vistazo. {w=1.25}{nw}"
        extend 2kslpo " Pero todavía me siento un poco idiota por eso..."

    elif Natsuki.isAffectionate(higher=True):
        n 1uskeml "¿E- {w=0.2}eh?"
        n 1uskwrl "¿[player]? {w=1}{nw}"
        extend 4knmwrl " ¿¡E- {w=0.2}en serio me compraste todo esto?!"
        n 1fslunl "..."
        n 2fcsanl "¡Uuuuuuuuu-!"
        n 4fpawrledr "¡¿Por qué harías eso?! {w=1}{nw}"

        if jnIsPlayerBirthday():
            n 1uskwrlesh "¡E- {w=0.2}especialmente hoy! {w=1}{nw}"
            extend 4kbkwrl " ¿{i}Olvidaste{/i} que es {i}tú cumpleaños{/i}?"

        elif jnIsNatsukiBirthday():
            if persistent._jn_natsuki_birthday_known:
                n 1fcswrlsbr "Y- {w=0.2}Ya {i}sé{/i} que es mi cumpleaños,{w=0.2}¿de acuerdo? {w=0.75}{nw}"
                extend 2fllfllsbr "¡Lo entiendo!"
                n 2csrcalsbl "No tienes que llenarme de cosas sólo para demostrar algo..."
            else:

                n 2flrfllsbr "N- {w=0.2}ni siquiera es como si hoy fuera realmente {i}importante{/i}, {w=0.5}{nw}"
                extend 2fcsemlsbr "o algo así."
                n 2csrslfsbr "..."

        elif jnIsChristmasEve():
            extend 1fllemf " Q-{w=0.2}Quiero decir..."
            n 4knmgsf "¡¿N-{w=0.2}no podrías al menos haber esperado hasta mañana?!{w=1}{nw}"
            extend 4kbkwrlesd " ¡Ni siquiera hice una lista ni nada!"

        elif jnIsChristmasDay():
            extend 1kllemf " Me refiero a ..."
            n 4kwmunlsbl "Deberías saber que no estoy acostumbrado a recibir cosas el día de Navidad..."
        else:

            extend 1kbkwrless " ¡N- {w=0.2}ni siquiera pedí nada!"

        n 2fslunl "..."
        n 2fcseml "Por dios... {w=0.5}{nw}"
        extend 1flrsrf " Y ahora parezco un completo idiota por no tener nada que dar a cambio...{w=1}{nw}"
        extend 4fsqsrfsbr "Espero que seas feliz {w=0.1}[player]."
        n 1fcsemlesisbr "..."
        n 1kcsbolsbr "...Está bien. {w=0.75}{nw}"
        extend 2fslpolsbr " S- {w=0.2}sólo un vistazo rápido..."
    else:

        n 1uwdeml "...¿Eh?"
        n 1ulreml "¿Y esto...?"
        n 4uskemfeex "...!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 1fbkwrf "[player_initial]- {w=0.2}¡[player]!"
        n 1kbkwrf "¡¿Qué es todo esto?!"

        if jnIsNatsukiBirthday():
            if persistent._jn_natsuki_birthday_known:
                n 2ccseml "¡Y {w=0.2}ya sé qué día es hoy! {w=0.75}{nw}"
                extend 2clreml " Por dios..."
                n 4csrsrl "No tienes que seguir bañándome con cosas elegantes también..."
            else:

                n 2ccseml "¡N- {w=0.2}no es como si hoy fuera realmente {i}especial{/i}!"

        elif jnIsChristmasEve():
            n 1knmgsf "¡Y-{w=0.2}y vamos, {w=0.2}[player]!{w=1}{nw}"
            extend 4kbkwrfesd " ¡Aún no es Navidad!"

        elif jnIsChristmasDay():
            n 1fcsemfsbl "Q-{w=0.2}quiero decir,{w=0.75}{nw}"
            extend 2kwmemfsbl " {i}Entiendo{/i} qué día es{w=0.75}{nw}"
            extend 2kslemfsbl " pero..."
            n 1kcspufesisbl "..."

        n 1fllemlesssbl "¡S- {w=0.2}será mejor que no intentes conquistarme con regalos o algo así! {w=1}{nw}"
        extend 2fcsemlsbr " ¡Sí!"
        n 1flremlsbl "¡T- {w=0.2}te haré saber que soy mucho más profunda que eso!"
        n 1fsqpulsbl "Juro que a veces es como si estuvieras tratando de avergonzarme... {w=1}{nw}"
        extend 2fslpolsbl " Eres un idiota."
        n 1ksrcalsbl "Sabes que {i}tampoco puedo devolverte{/i}, {w=0.1}nada..."
        n 1fcscalesssbl "..."
        n 1kcsemlesi "..."
        n 2fslsll "...Bien. {w=1}{nw}"
        extend 1fcseml " Bien. {w=0.75}{nw}"
        extend 1flremlsbr " ¡Lo miraré! {w=1}{nw}"
        extend 2fsrpolsbr " ...Pero sólo porque pones el esfuerzo."

    python:
        import random
        alt_dialogue = False
        random.shuffle(unlocks)
        giftbox.open()

    while len(unlocks) > 0:
        play audio gift_rustle
        $ unlock = unlocks.pop()
        $ unlock = jn_outfits.getOutfit(unlock) if jn_outfits.outfitExists(unlock) else jn_outfits.getWearable(unlock)

        if (len(unlocks) == 0):
            $ giftbox.empty()

        n 1tlrbo "..."


        if type(unlock) is jn_outfits.JNHairstyle:
            if alt_dialogue:
                n 1unmpuesu "¿Mmm? {w=1}{nw}"
                extend 4tnmajeqm " ¿Una... {w=0.3} nota...?"
                n 1tslpu "..."
                n 1unmgsesu "...¡Oh! {w=1}{nw}"
                extend 1unmbol " ¿Querías que probara mi cabello así? {w=0.5}[unlock.display_name]?"
                n 3nllunl "..."
                n 1nllajl "Bien...{w=1}{nw}"
                extend 4nnmajl " bueno."

                if Natsuki.isEnamored(higher=True):
                    n 1nlrssl "{i}Supongo{/i} que puedo intentarlo más tarde."
                    n 4fsqsslsbl "Apuesto a que a alguien le gustaría eso, {w=0.1}¿eh?{w=0.5}{nw}"
                    extend 4fsldvlsbl "Jejeje..."

                elif Natsuki.isAffectionate(higher=True):
                    n 1nlrpol "{i}Supongo{/i} que puedo intentarlo más tarde."
                    extend 1nlrsslsbr " Ehehe..."
                else:

                    n 2fcspol "{i}Supongo{/i} que puedo intentarlo más tarde."
                    n 2flrajl "P-pero sólo porque quiero, {w=0.75}{nw}"
                    extend 1fsrpol " obviamente."
            else:

                n 4tnmpueqm "¿Eh? {w=1}{nw}"
                extend 1tlrpueqm "¿Qué hace esta nota aquí...?"
                n 2tllbo "..."
                n 1unmgsesu "¡G- {w=0.2}guau!"
                n 1flldvl "Je. {w=0.5}{nw}"
                extend 1fllsslsbr "Tengo que admitirlo. {w=1}{nw}"
                extend 3fsrnvlsbr "Nunca pensé siquiera en intentar {i}eso{/i} con mi cabello..."
                n 1unmbo "[unlock.display_name], {w=0.1} ¿eh?"
                n 1nllajl "{i}Supongo{/i} que valdría la pena intentarlo..."

                if Natsuki.isEnamored(higher=True):
                    n 4fsqsslsbr "¿Me pregunto a quién le gustaría, {w=0.1}eso? {w=0.5}{nw}"
                    extend 4fsqsmlsbr "Jejeje..."

                elif Natsuki.isAffectionate(higher=True):
                    n 1nlrsslsbr "Ya veremos."
                else:

                    n 1fcsgsl "¡P- {w=0.2}pero sólo por curiosidad! {w=1}{nw}"
                    extend 2fsqpol " ¿Entiendes?"
        else:

            if Natsuki.isEnamored(higher=True):
                if alt_dialogue:
                    n 1kcsemlesi "Por dios... {w=1}{nw}"
                    extend 3knmpol " ¿Por qué intentas malcriarme tanto?"
                    n 3fllpol "Ya sabes que odio que me bañen con cosas llamativas..."
                    n 1kslsrl "..."
                    n 1ksqsrlsbl "...Especialmente cosas como ésta [unlock.display_name].{w=0.75}{nw}"
                    extend 1kslsslsbl " Aunque es bastante impresionante."
                    n 1kslsrl "..."
                    n 1nllajl "Yo... {w=1}{nw}"
                    extend 2ksrpol " Sólo voy a conservar eso también."
                    n 2nsrdvf "...Gracias."
                else:

                    n 1uskgsfesu "...!"
                    n 1fsldvl "...Je. {w=1}{nw}"
                    extend 4tsqpufsbl " ¿De verdad estás intentando conquistarme {i}con todo esto{/i},{w=0.1} eh?"
                    n 1kslsllsbl "..."
                    n 1fcspulsbl "El [unlock.display_name]..."
                    n 1knmpulsbr "Es...{w=0.5}Muy agradable. {w=0.75}{nw}"
                    extend 4kllsrlsbr "¿Bueno?"
                    n 1kslunlesssbr "Gracias..."

            elif Natsuki.isAffectionate(higher=True):
                if alt_dialogue:
                    n 1uwdajlesu "...!"
                    n 2fcsemlesssbl "¡E- {w=0.1}ejem!{w=1}{nw}"
                    extend 2fslpol " Otra buena opción, {w=0.5}{nw}"
                    extend 4fsqpolsbr " Odio admitirlo."
                    n 1klrbolsbr "..."
                    n 1fcsunlsbr "...Gracias, {w=0.1}[player]."
                    n 1fllunlsbr "Por el [unlock.display_name],{w=0.5}{nw}"
                    extend 4fnmpulsbl " Q- {w=0.2}Quiero decir."
                    n 1kslpulsbl "Es... {w=1}{nw}"
                    extend 1kslsslsbl "Realmente genial."
                    n 2fslpofsbl "...Gracias."
                else:

                    n 1uwdajledz "...!"
                    n 1fcsunlesdsbl "..."
                    n 1fcssslsbl "Je, {w=1}{nw}"
                    extend 3fllbglesssbr " ¡Y- {w=0.2}y yo que pensaba que tendría que enseñarte {i}todo{/i} sobre estilo!"
                    n 3kllsllsbr "..."
                    n 1knmbolsbr "...Pero gracias, {w=0.3} [player].{w=0.75}{nw}"
                    extend 1flrunlsbr " Por el [unlock.display_name]."
                    n 1fcsunlsbr "Yo...{w=0.75}{nw}"
                    extend 4ksrunfsbl "Realmente lo aprecio."
            else:

                if alt_dialogue:
                    n 1uskgslesh "...!"
                    n 4fdwanfess "¡Nnnnnnn-!"
                    n 1fcsemfesssbl "T-{w=0.2}tienes suerte de ser bueno eligiendo regalos, {w=0.5}{nw}"
                    extend 3fsqpofesssbl "Eres un idiota."
                    n 3fslpofesssbr "Supongo que tendré que quedarme con [unlock.display_name] ahora. {w=0.75}{nw}"
                    extend 3fnmpofesssbl " E- {w=0.2}espero que seas feliz."
                else:

                    n 1fspgsledz "¡G- {w=0.2}guau!"
                    n 1uskemfesh "...!"
                    n 4fbkwrf "¡¿Qué?! {w=1}{nw}"
                    extend 4fllwrfeszsbl " ¡No me mires así!"
                    n 1fcseml "¡M- {w=0.2}me alegra ver que después de todo tienes {i}algo{/i} de buen gusto al haber encontrado esto."
                    n 2fllcal "[unlock.display_name],{w=0.1}¿eh? {w=1}{nw}"
                    extend 2fcscal " S- {w=0.2}supongo que lo mantendré por aquí."
                    n 2fcspofess "Poooor si acaso."

        $ alt_dialogue = not alt_dialogue
        $ persistent._jn_pending_outfit_unlocks.remove(unlock.reference_name)

        if len(persistent._jn_pending_outfit_unlocks) > 0:
            if Natsuki.isEnamored(higher=True):
                n 1klrpul "...No puedo creer que haya aún más. {w=1}{nw}"
                extend 4fcspul " Por dios, {w=0.1}[player]..."
                n 4kcspul "...Bien. {w=1}{nw}"
                extend 4fslssl "Veamos qué sigue..."

            elif Natsuki.isAffectionate(higher=True):
                n 2ksrunl "Uuuuuuu...{w=1}{nw}"
                extend 1ksremlesd "¡¿Aún hay más?!"
                n 1kcsemlesisbl "Por dios..."
            else:

                n 3fnmpol "¿C- {w=0.2}cuánto hay aquí?{w=0.1} [player]{w=1}{nw}?"
                extend 3fslpofesssbr "Por dios..."

    if Natsuki.isEnamored(higher=True):
        n 1fcsssl "Finalmente te quedaste sin cosas que tirarme, {w=0.5}{nw}"
        extend 1fllsslsbl "¿eh?"
        n 4kllbolsbl "..."
        n 4ksrpulsbl "Yo... {w=1}{nw}"
        extend 1ksqsrlsbl " Realmente desearía que no hicieras eso, {w=0.1}tu sabes.."
        n 1kllbolsbl "..."
        n 1kllpulsbr "Pero... {w=0.75}{nw}"
        extend 4knmsslsbr "¿[player]?"
        n 4fsrunfsbr "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5, hard=True)

        if Natsuki.isLove(higher=True):
            show natsuki 1nslunfsbl zorder JN_NATSUKI_ZORDER at jn_center
            play audio kiss
            $ jnPause(1.5, hard=True)
            hide black with Dissolve(1.25)
            $ chosen_tease = jn_utils.getRandomTease()
            n 1knmssf "...Gracias, {w=0.1}[chosen_tease]."
            n 2klrsmfeme "Jejeje."
        else:

            hide black with Dissolve(1.25)
            n 2fslunf "...Gracias. {w=0.75}{nw}"
            extend 2fslsmfsbr "Jejeje."

    elif Natsuki.isAffectionate(higher=True):
        n 1fllun "...¿Eso es todo? {w=0.75}{nw}"
        extend 3flrunl " ¿Eso es todo?"
        n 1fcsemlesi "Por dios..."
        n 4fnmtrl "Realmente necesitas dejar de regalar tantas cosas, {w=0.1}[player]. {w=1}{nw}"
        extend 4fsqcal " ¡No quiero que adquieras un hábito tonto!"
        n 1fslunlsbl "Especialmente cuando no puedo hacer nada bueno a cambio..."
        n 1kslunlsbl "..."
        n 1kslpulsbl "Pero... {w=0.75}{nw}"
        extend 4knmsllsbr "¿[player]?"
        n 2fsrunfsbr "..."

        show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
        show natsuki 1flrcafsbr zorder JN_NATSUKI_ZORDER at jn_center
        play audio clothing_ruffle
        $ jnPause(2, hard=True)
        hide black with Dissolve(1.25)

        n 1ksrcafsbr "..."
        n 1fcstrlsbl "G- {w=0.2}gracias."
    else:

        n 1kslemlesi "Viejo... {w=1}{nw}"
        extend 2flrtrl " ¿Eso es todo? {w=0.5}{nw}"
        extend 1fcspulsbl "Por dios..."
        n 1fslunlsbr "..."
        n 1nslajlsbr "Yo... {w=0.75}{nw}"
        extend 4nsqajlsbl "Supongo que será mejor que guarde todo esto ahora."
        n 1kslunlsbr "..."
        n 1kslpulsbl "Pero..."
        extend 4knmsllsbr "¿[player]?"
        n 2fsrunlsbr "..."
        n 2fsrajlsbr "Yo..."
        extend 1ksrcafsbr "Realmente aprecio las cosas que me conseguiste."
        n 1kllcalsbr "..."
        n 1fcstrlsbl "G- {w=0.2}gracias."

    show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
    $ giftbox.close()
    $ giftbox.hide()
    $ jnPause(2, hard=True)
    play audio chair_out
    $ jnPause(3, hard=True)
    play audio clothing_ruffle
    $ jnPause(1, hard=True)
    play audio drawer
    $ jnPause(1, hard=True)
    $ jnPause(3, hard=True)
    play audio chair_in
    $ jnPause(3, hard=True)
    hide black with Dissolve(1.25)

    n 1ullajl "Entonces..."
    n 4tnmsslsbl "¿Dónde estábamos? {w=1}{nw}"
    extend 4fslsslsbr "Jejeje..."

    $ Natsuki.calculatedAffinityGain(bypass=True)
    $ jn_globals.force_quit_enabled = True

    jump ch30_loop

screen create_outfit():
    if jn_outfits._changes_made:
        text "¡Cambios no guardados!" size 30 xpos 555 ypos 40 style "categorized_menu_button"


    vbox:
        xpos 600
        ypos 140
        hbox:

            textbutton _("Sombreros"):
                style "hkbd_option"
                action Jump("outfits_create_select_headgear")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.headgear.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.headgear, jn_outfits.JNHeadgear) else "None"):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Peinados"):
                style "hkbd_option"
                action Jump("outfits_create_select_hairstyle")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.hairstyle.display_name)):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Gafas"):
                style "hkbd_option"
                action Jump("outfits_create_select_eyewear")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.eyewear.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.eyewear, jn_outfits.JNEyewear) else "None"):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Accesorios faciales"):
                style "hkbd_option"
                action Jump("outfits_create_select_facewear")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.facewear.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.facewear, jn_outfits.JNFacewear) else "None"):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Accesorios"):
                style "hkbd_option"
                action Jump("outfits_create_select_accessory")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.accessory.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.accessory, jn_outfits.JNAccessory) else "None"):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Collares"):
                style "hkbd_option"
                action Jump("outfits_create_select_necklace")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.necklace.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.necklace, jn_outfits.JNNecklace) else "None"):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Ropa"):
                style "hkbd_option"
                action Jump("outfits_create_select_clothes")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.clothes.display_name)):
                style "hkbd_label"
                left_margin 10

        hbox:

            textbutton _("Artículo posterior"):
                style "hkbd_option"
                action Jump("outfits_create_select_back")

            label _(jn_utils.escapeRenpySubstitutionString(jn_outfits._PREVIEW_OUTFIT.back.display_name) if isinstance(jn_outfits._PREVIEW_OUTFIT.back, jn_outfits.JNBack) else "None"):
                style "hkbd_label"
                left_margin 10


    vbox:
        xpos 600
        ypos 450
        null height 60

        textbutton _("Copiar de..."):
            style "hkbd_option"
            action Jump("outfits_create_copy")

        textbutton _("Finalizado"):
            style "hkbd_option"
            action Jump("outfits_create_save")

        textbutton _("Salir"):
            style "hkbd_option"
            action Jump("outfits_create_quit")

screen outfit_item_menu(items):
    $ option_width = 560

    fixed:
        area (1280 - (40 + option_width), 40, option_width, 440)
        vbox:
            ypos 0
            yanchor 0

            textbutton "No importa":
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
                for display_prompt, _value in items:
                    textbutton display_prompt:
                        style "categorized_menu_button"
                        xsize option_width
                        action Return(_value)
                        hover_sound gui.hover_sound
                        activate_sound gui.activate_sound


                        if (type(_value) is jn_outfits.JNOutfit and _value.is_jn_outfit) or (issubclass(type(_value), jn_outfits.JNWearable) and _value.is_jn_wearable):
                            idle_background Frame("mod_assets/buttons/choice_hover_blank_cd.png", gui.frame_hover_borders, tile=gui.frame_tile)

                        elif (not isinstance(_value, basestring)):
                            idle_background Frame("mod_assets/buttons/choice_hover_blank_folder.png", gui.frame_hover_borders, tile=gui.frame_tile)

                    null height 5

        bar:
            style "classroom_vscrollbar"
            value YScrollValue("viewport")
            xalign scroll_align
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
