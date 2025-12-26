
default persistent.jn_snap_unlocked = False
default persistent.jn_snap_explanation_given = False


default persistent.jn_snap_player_is_cheater = False


default persistent._jn_snap_player_wins = 0
default persistent._jn_snap_natsuki_wins = 0

init python in jn_snap:
    from Enum import Enum
    import random
    import store
    import store.jn_apologies as jn_apologies
    import time


    _player_win_streak = 0
    _natsuki_win_streak = 0
    last_game_result = None


    _is_player_turn = None
    _player_forfeit = False
    _player_is_snapping = False
    _player_failed_snap_streak = 0
    _natsuki_can_fake_snap = False
    _natsuki_skill_level = 0
    _controls_enabled = False


    _cards_in_deck = []
    _cards_on_table = []
    _natsuki_hand = []
    _player_hand = []


    if random.choice(range(1, 100)) == 1:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/card_fan_icon_alt.png"

    else:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/card_fan_icon.png"

    class JNSnapStates(Enum):
        """
        Identifiers for the different ways a snap game can end.
        """
        draw = 1
        forfeit = 2
        natsuki_win = 3
        player_win = 4

    def _clear(complete_reset=False):
        """
        Resets the in-game variables associated with Snap

        IN:
            - true_reset - boolean flag; if True will also reset Natsuki's skill level, etc.
        """
        global _is_player_turn
        global _player_forfeit
        global _player_is_snapping
        global _player_failed_snap_streak
        global _natsuki_can_fake_snap
        
        _is_player_turn = None
        _player_forfeit = False
        _player_is_snapping = False
        _player_failed_snap_streak = 0
        _natsuki_can_fake_snap = False
        del _cards_in_deck[:]
        del _cards_on_table[:]
        
        if complete_reset:
            _natsuki_skill_level = 1

    def _setup():
        """
        Generates a deck of cards based on the card configuration
        Deck is then shuffled, and the players are then assigned their hands
        Finally, the deck is cleared
        """
        
        del _player_hand[:]
        del _natsuki_hand[:]
        
        
        for card_suit in [
            "clubs",
            "diamonds",
            "hearts",
            "spades"
        ]:
            for card_value in range(1, 11):
                _cards_in_deck.append((card_suit, card_value))
        
        
        random.shuffle(_cards_in_deck)
        switch = False
        for card in _cards_in_deck:
            
            if switch:
                switch = False
                _player_hand.append(card)
            
            else:
                switch = True
                _natsuki_hand.append(card)
        
        
        del _cards_in_deck[:]

    def _placeCard(is_player=False):
        """
        Takes the top-most card from the player's hand and places it on the table pile

        IN:
            - is_player boolean value representing if the player or Natsuki is the one placing their card down.
        """
        global _is_player_turn
        if is_player:
            if (len(_player_hand) > 0):
                new_card = _player_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))
                _is_player_turn = False
        
        else:
            if (len(_natsuki_hand) > 0):
                new_card = _natsuki_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))
                _is_player_turn = True

    def _getSnapResult():
        """
        Compares the last two cards placed on the table pile, and returns True if either:
            - The suits on both cards match
            - The values on both cards match
        Otherwise, returns False
        Used by Natsuki's logic to determine if she should "spot" the snap opportunity
        """
        if len(_cards_on_table) >= 2:
            return _cards_on_table[-1][0] == _cards_on_table[-2][0] or _cards_on_table[-1][1] == _cards_on_table[-2][1]
        
        else:
            return False

    def _callSnap(is_player=False):
        """
        Attempts to call snap and award cards for the player or Natsuki, based on who made the call

        IN:
            - is_player boolean value representing if the player or Natsuki was the one who made the call
        """
        global _is_player_turn
        global _player_is_snapping
        
        
        if is_player:
            _player_is_snapping = True
        
        
        if _getSnapResult():
            if is_player:
                
                for card in _cards_on_table:
                    _player_hand.append(card)
            
            else:
                
                for card in _cards_on_table:
                    _natsuki_hand.append(card)
            
            
            del _cards_on_table[:]
            renpy.play("mod_assets/sfx/card_shuffle.ogg")
            
            
            
            
            
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=True)
        
        else:
            
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=False)

    def _showSplashImage(is_player_snap=False):
        """
        Shows a splash image for a Snap call.

        IN:
            - is_player_snap - bool flag as to if the player is calling Snap. Determines if the popup has a Nat chibi.
        """
        snap_image = "you_snap" if is_player_snap else "nat_snap"
        renpy.show(
            name="snap_popup",
            at_list=[store.snap_popup],
            layer="overlay",
            what=store.Image("mod_assets/games/snap/{0}.png".format(snap_image)),
            zorder=10)
        
        return

    def _getCurrentTopCard():
        """
        Returns the sprite path of the card currently on top of the table pile, or nothing if no cards are on the pile
        
        OUT:
            - str sprite path of the card to show on top of the pile
        """
        return "mod_assets/games/cards/{0}/{1}.png".format(_cards_on_table[-1][0], _cards_on_table[-1][1]) if len(_cards_on_table) else "mod_assets/games/cards/blank.png"

    def _getCurrentTurnIndicator():
        """
        Returns the sprite path of the turn indicator to display on the snap UI.

        OUT:
            - Arrow pointing to Natsuki or the player, based on the current turn
        """
        if _is_player_turn is None:
            return "mod_assets/games/snap/turn_indicator_none.png"
        
        else:
            return "mod_assets/games/snap/turn_indicator_player.png" if _is_player_turn else "mod_assets/games/snap/turn_indicator_natsuki.png" 

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the snap UI.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _is_player_turn is None:
            return "¡Nadie!"
        
        return "¡Tuyo!" if _is_player_turn else "[n_name]"

label snap_intro:
    n 1nchbs "¡Muuuuy bien!{w=0.75}{nw}"
    extend 1fcsbg " ¡Juguemos un poco de Snap!"

    if not persistent.jn_snap_explanation_given:
        n 1nnmaj "Oh -{w=0.3} antes de empezar,{w=0.2} ¿quieres una explicación?{w=0.5}{nw}"
        extend 4tllca " Ya sabes,{w=0.2} ¿de cómo funciona?"
        n 4nchsm "Es un juego súper simple,{w=0.2} pero pensé que mejor preguntaba."
        n 2fcsbg "¡No quiero ganar solo porque no sabías lo que hacías!"
        n 2usqfs "Así que...{w=1}{nw}"
        extend 4fchss " ¿qué dices?"

        show natsuki 4fchsm
        menu:
            n "¿Necesitas que repase las reglas rápido?"
            "¡Sí, por favor!":

                jump snap_explanation
            "No, estoy listo":

                n 4tsqss "¿Oh?{w=0.75}{nw}"
                extend 4flrbg " Estás listo,{w=0.5}{nw}"
                extend 4fsqbg " ¿eh?"
                n 2fchgn "¡Listo para que te pateen el trasero!{w=0.75}{nw}"
                extend 2fchbs " ¡Vamos,{w=0.2} [player]!"
                $ persistent.jn_snap_explanation_given = True

    jump snap_start

label snap_explanation:
    n 1nnmss "¡Muy bien!{w=0.2} Las reglas son sencillísimas,{w=0.5}{nw}"
    extend 4nslsm " como decía antes."
    n 4unmaj "Básicamente,{w=0.2} cada uno recibe medio mazo de cartas."
    n 2nchss "Entonces,{w=0.2} tomamos turnos poniendo una carta boca arriba en la mesa -{w=0.5}{nw}"
    extend 2fsrdv " ¡aunque no podemos {i}escoger o ver{/i} la carta antes,{w=0.2}!"
    n 4fsgbg "¿Me sigues hasta ahora,{w=0.2} [player]?{w=0.2} Ehehe."
    n 1nnmbg "Si la carta recién puesta en la mesa coincide en {i}valor o palo{/i} con la carta que estaba ahí antes..."
    n 4usqsm "Entonces tenemos que gritar{w=0.5}{nw}"
    extend 4fchbs " ¡Snap!"
    n 1nnmsm "Quien lo grite primero se lleva las cartas de la mesa."
    n 1unmaj "Oh -{w=0.5}{nw}"
    extend 2tsqss " pero tienes que tener cuidado,{w=0.2} [player]."
    n 4fllsg "Cuando gritas snap,{w=0.2} se vuelve el turno del otro jugador..."
    n 2fsqsm "Así que no grites a menos que sepas que lo tienes,{w=0.5}{nw}"
    extend 2nchgn " ¿vale?"
    n 1uchbg "¡El ganador es quien termine con todas las cartas primero!"
    n 4tsqsm "Que usualmente soy yo,{w=0.75}{nw}"
    extend 2fsldv " obviamente."
    n 4uwdaj "Oh,{w=0.2} cierto -{w=0.5}{nw}"
    extend 1nnmsm " también pierdes si te quedas sin cartas para jugar,{w=0.2} así que deberías tener eso en mente también."
    n 4tsqss "Así que...{w=0.3} ¿qué dices,{w=0.2} [player]?{w=0.2} ¿Entendiste todo eso?"

    show natsuki 4unmbo
    menu:
        n "¿Todo eso tuvo sentido para ti?"
        "¿Puedes repasar las reglas otra vez?":

            n 1tsqpueqm "¿Eh?{w=0.75}{nw}"
            extend 1tllca " Bueno,{w=0.2} está bien..."

            jump snap_explanation
        "Entendido. ¡Juguemos!":

            n 1fcsbg "Ahora {i}así{/i} es como me gusta.{w=0.75}{nw}"
            extend 1fchgn " ¡Algo de espíritu de lucha!"
            n 2fsqbg "Aunque debería advertirte,{w=0.2} [player]..."
            n 2fcsbs "¡No me voy a contener!{w=0.75}{nw}"
            extend 2uchgn " ¡Hagamos esto!"

            $ persistent.jn_snap_explanation_given = True
            jump snap_start
        "Gracias, [n_name]. Jugaré luego":

            n 1tsqpueqm "¿Huh?{w=0.75}{nw}"
            extend 2nsqflsbl " ¿En serio?"
            n 2nslpo "..."
            n 4nllfl "Bueno...{w=1.25}{nw}"
            extend 4nslca " bien."
            n 2flrpo "...Aguafiestas."

            if not Natsuki.getDeskSlotClear(jn_desk_items.JNDeskSlots.right):
                show natsuki 2ccspo
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)
                show natsuki 2nlrbo
                $ jnPause(1)
                hide black with Dissolve(1.25)

            jump ch30_loop

label snap_start:

    play audio card_shuffle
    $ jn_snap._clear()
    $ jn_snap._setup()

    show natsuki 1uchsm at jn_left
    show screen snap_ui
    $ jnPause(1)

    n 1nchbg "¡Vale!{w=0.75}{nw}"
    extend 1fchsm " ¡El mazo está barajado!"
    n 4fsqsm "Veamos a quién le toca primero..."

    play audio coin_flip

    n 4fnmpu "..."
    $ jn_snap._is_player_turn = random.choice([True, False])

    if jn_snap._is_player_turn:
        n 1fcssm "Ehehe.{w=0.5}{nw}"
        extend 1fcsbg " Mala suerte,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fchgn " ¡Parece que vas primero!"
    else:

        n 2nsqsl "..."
        n 2fslpo "Hmph.{w=0.5}{nw}"
        extend 2fcsaj " Solo tuviste suerte esta vez.{w=0.75}{nw}"
        extend 2fcsca " Supongo que iré primero entonces,{w=0.2} [player]."

    show natsuki snap
    $ Natsuki.setInGame(True)
    $ jn_snap._controls_enabled = True
    jump snap_main_loop

label snap_main_loop:


    if len(jn_snap._player_hand) == 0 and len(jn_snap._natsuki_hand) == 0:

        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.JNSnapStates.draw
        jump snap_end

    elif len(jn_snap._player_hand) == 0:

        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak += 1
        $ persistent._jn_snap_natsuki_wins += 1
        $ jn_snap.last_game_result = jn_snap.JNSnapStates.natsuki_win
        jump snap_end

    elif len(jn_snap._natsuki_hand) == 0:

        $ jn_snap._player_win_streak += 1
        $ persistent._jn_snap_player_wins += 1
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.JNSnapStates.player_win
        jump snap_end

    $ jnPause(delay=max(0.33, (3.0 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)




    if not jn_snap._player_is_snapping:
        if jn_snap._getSnapResult():
            $ jn_snap._callSnap()


        elif (
            random.choice(range(0,10 + jn_snap._natsuki_skill_level)) == 1
            and len(jn_snap._cards_on_table) >= 2
            and jn_snap._natsuki_can_fake_snap
            and not jn_snap._player_failed_snap_streak
        ):
            $ jn_snap._callSnap()
            $ jn_snap._natsuki_can_fake_snap = False

    if not jn_snap._is_player_turn:

        $ jn_snap._placeCard(False)


        if len(jn_snap._natsuki_hand) == 0:
            $ jnPause(delay=max(0.33, (1.25 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)

            if jn_snap._getSnapResult():
                $ jn_snap._callSnap()

        $ jn_snap._is_player_turn = True
        $ jn_snap._natsuki_can_fake_snap = True

    jump snap_main_loop

label snap_quip(is_player_snap, is_correct_snap):

    $ cheat_check = False


    if is_player_snap:


        if is_correct_snap:
            $ jn_snap._player_failed_snap_streak = 0
            $ quip = renpy.substitute(random.choice([
                "¡Nnnnn-!",
                "¡Ugh!{w=0.2} ¡Vamos!",
                "¡E-{w=0.2}eres rápido!",
                "¡Pero justo iba a gritarlooo!",
                "Solo espera,{w=0.2} [player]...",
                "¡Uuuuuu-!",
                "¡Otra vez no!{w=0.2} Grrr...",
                "Maldición...",
                "Miercoles...",
                "Qué tonto...",
                "¿Otra vez?{w=0.2} ¿En serio?",
                "Ugh...",
                "Tan ridículo...",
                "Qué tonto...",
                "¡Jeez! Como sea...",
                "¡Jeez!",
                "¡Jeeeeeez!",
                "¡Oh vamos,{w=0.2} [player]!",
                "¿Cómo eres {i}tan{/i} rápido?!"
            ]))
            show natsuki 4klrca zorder JN_NATSUKI_ZORDER


            play audio smack
            $ jn_utils.fireAndForgetFunction(function=jn_snap._showSplashImage, args=(True,))
            $ jnPause(0.75)
        else:


            $ jn_snap._player_failed_snap_streak += 1


            if jn_snap._player_failed_snap_streak == 3 and not persistent.jn_snap_player_is_cheater:
                $ cheat_check = True
                n 4fnmaj "¡[player]!{w=0.5}{nw}"
                extend 2fnmsf " ¡Solo estás gritando Snap cuando es tu turno!{w=0.5}{nw}"
                extend 2fsqaj " ¡Así no es como se juega para nada!"
                n 2fllca "Espero que no estés intentando hacer trampa,{w=0.2} [player].{w=0.75}{nw}"
                extend 2fsqsl " No soporto jugar con tramposos."


            elif jn_snap._player_failed_snap_streak == 6 and not persistent.jn_snap_player_is_cheater:
                $ jn_snap_controls_enabled = False
                n 2fupfl "Ugh...{w=1.25}{nw}"
                extend 2fcsfl " mira,{w=0.2} [player]."
                n 2fcsaj "Si no vas a jugar limpio,{w=0.5}{nw}"
                extend 2flrem " entonces ¿por qué debería molestarme en jugar siquiera?"
                n 4fllfl "¡Incluso te {i}advertí{/i} antes,{w=0.5}{nw}"
                extend 4fnmfl " también!"
                n 4fcsemesi "..."
                n 4fcssl "¿Sabes qué?{w=0.75}{nw}"
                extend 2fcsfl " Bien."
                n 2fsrbo "Terminamos con este juego,{w=0.2} [player]."

                $ _player_win_streak = 0
                $ persistent.jn_snap_player_is_cheater = True
                $ Natsuki.percentageAffinityLoss(1)
                $ Natsuki.addApology(jn_apologies.ApologyTypes.cheated_game)


                hide screen snap_ui

                show natsuki 2fcsbo
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)
                show natsuki 2cslbo
                $ jnPause(1)
                hide black with Dissolve(1.25)


                $ Natsuki.setInGame(False)
                $ Natsuki.resetLastTopicCall()
                $ Natsuki.resetLastIdleCall()
                jump ch30_loop
            else:


                $ quip = renpy.substitute(random.choice([
                    "¿Oh?{w=0.2} Alguien está impaciente,{w=0.2} ¿eh?",
                    "Ups,{w=0.2} [player]~.{w=0.2} Ehehe.",
                    "Buena esa,{w=0.2} tonto.{w=0.2} ¡Ahaha!",
                    "Muy suave,{w=0.2} [player].{w=0.2} Ehehe.",
                    "¡Ahaha!{w=0.2} ¿Qué fue eso,{w=0.2} [player]?",
                    "Oye,{w=0.2} [player] -{w=0.2} ¡se supone que debes leer las cartas!{w=0.2} Ehehe.",
                    "¡Gran jugada,{w=0.2} tonto!{w=0.2} ¡Ahaha!"
                ]))
                show natsuki 2fsqsm zorder JN_NATSUKI_ZORDER
    else:



        if is_correct_snap:
            $ quip = renpy.substitute(random.choice([
                "¡SNAP!{w=0.2} ¡Ahaha!",
                "¡Snap!{w=0.2} ¡Ahaha!",
                "¡SNAP!{w=0.2} Ehehe.",
                "¡SNAP!",
                "¡Snap!",
                "¡Snap~!",
                "¡Snap!{w=0.2} ¡Snap snap snap!",
                "¡Snappy snap!",
                "¡Boom!{w=0.2} ¡Snap!",
                "¡Snap!{w=0.2} ¡Snap!",
                "¡Snap!{w=0.2} ¡Snap!{w=0.2} ¡Snap!",
                "¡Sí!{w=0.2} ¡SNAP!",
                "¡Sii!{w=0.2} ¡SNAP!",
                "¡Sii!{w=0.2} ¡Snap!{w=0.2} ¡Snap!",
                "¡Snap snap maldito snap!",
                "¡SNAAAP!{w=0.2} Ehehe.",
                "¡Bam!{w=0.2} ¡Snap!"
            ]))
            show natsuki 4uchbg zorder JN_NATSUKI_ZORDER



            play audio smack
            $ jn_utils.fireAndForgetFunction(function=jn_snap._showSplashImage)
            $ jnPause(0.75)
        else:


            $ quip = renpy.substitute(random.choice([
                "Sn-...{w=0.3} oh.",
                "¡Snap!{w=0.2} Espera...",
                "¡SNAP!{w=0.2} ¿Huh...?{w=0.2} O-{w=0.2}oh.",
                "Snap sna-...{w=0.3} grrr."
            ]))
            show natsuki 2fsqsr zorder JN_NATSUKI_ZORDER


    $ jn_snap._controls_enabled = False

    if not cheat_check:
        n "[quip]"

    show natsuki snap at jn_left
    $ jn_snap._controls_enabled = True


    if is_player_snap:
        $ jn_snap._player_is_snapping = False
        $ jn_snap._is_player_turn = False
    else:

        $ jn_snap._is_player_turn = True

    return

label snap_end:
    hide screen snap_ui
    $ jn_snap._controls_enabled = False


    if jn_snap.last_game_result == jn_snap.JNSnapStates.player_win:

        if jn_snap._player_win_streak > 10:
            n 2csltr "Sí,{w=0.3} sí.{w=1}{nw}"
            extend 2cslpo " Ganaste otra vez."
            n 2csrsssbr "...Nerd."

        elif jn_snap._player_win_streak == 10:
            n 2fcsaj "Oh,{w=0.5}{nw}"
            extend 2fcsan " ¡vamos{w=0.75}{nw}"
            extend 2fbkwrl " {b}ya{/b}!"
            n 4fllgs "¡¿En serio?!{w=0.75}{nw}"
            extend 4fnmgs " ¡¿Diez seguidas?!{w=0.75}{nw}"
            extend 2clremsbl " Hombre..."
            n 2ccsfl "Si querías probar un punto,{w=0.2} ya lo hiciste,{w=0.75}{nw}"
            extend 2csqpo " ¿ok?{w=1}{nw}"
            extend 2cslcasbr " Jeez..."

        elif jn_snap._player_win_streak == 5:
            n 4fcsem "¡J-{w=0.2}jeez!{w=0.5}{nw}"
            extend 4flrgs " ¡¿Cinco {i}ya{/i}?!{w=0.75}{nw}"
            extend 2cslca " Vamos."
            n 2fcsajsbl "Nunca {i}dije{/i} que fuera una profesional,{w=0.5}{nw}"
            extend 2fcsposbl " sabes."

        elif jn_snap._player_win_streak == 3:
            n 1fcsss "Je.{w=0.75}{nw}"
            extend 1fllsssbr " Mejor presume mientras puedas,{w=0.2} [player]."
            n 1fcsbgsbr "¡Porque esa racha de suerte no durará para siempre!"
        else:

            n 2nllpo "Bueno,{w=0.2} diablos.{w=0.5}{nw}"
            extend 2nslsssbr " Supongo que eso es todo,{w=0.2} ¿eh?"
            n 2fcssssbr "B-{w=0.2}bien jugado,{w=0.2} [player].{w=0.75}{nw}"
            extend 2csrposbr " Supongo."


    elif jn_snap.last_game_result == jn_snap.JNSnapStates.natsuki_win:

        if jn_snap._natsuki_win_streak > 10:
            n 1fcsss "Hombre,{w=0.5}{nw}"
            extend 4fcsbg " ¡esto es demasiado{w=0.25}{nw}"
            extend 4fchgn " {i}fácil{/i}!{w=0.75}{nw}"
            extend 4fcsbg " {i}Casi{/i} me siento mal."
            n 2fsqsm "...Casi.{w=0.75}{nw}"
            extend 2fchsmeme " Ehehe."

        if jn_snap._natsuki_win_streak == 10:
            n 2cllss "Wow...{w=1}{nw}"
            extend 2fchgn " ¿{i}alguien{/i} está teniendo un mal día o qué?"
            n 4fsqbg "...¿O soy yo así de {i}buena{/i}?{w=0.75}{nw}"
            extend 2fsqsmeme " Ehehe."

        elif jn_snap._natsuki_win_streak == 5:
            n 2fcsbg "¿Oh?{w=0.75}{nw}"
            extend 2fsqbg " ¿Qué es eso?"
            n 4fchgn "¿El sonido de cinco seguidas {i}ya{/i}?{w=0.75}{nw}"
            extend 1nchgn " Ehehe."
            n 2fcscs "Pero no te preocupes,{w=0.2} [player].{w=0.75}{nw}"
            extend 2fcsbgeme " ¡Hay muchas más de donde vino {i}esa{/i}!"

        elif jn_snap._natsuki_win_streak == 3:
            n 1fcssm "Ehehe.{w=0.75}{nw}"
            extend 2fchbg " ¡Sip!{w=0.75}{nw}"
            extend 2fcssmesm " ¡Otro más para el Equipo [n_name]!"
        else:

            n 1unmbs "¡Sí!{w=0.5}{nw}"
            extend 1uchbg " ¡Gané!{w=0.75}{nw}"
            extend 1fcsbgsbl " C-{w=0.2}como si fuera a terminar de otra forma."
            n 1fsqsmeme "Ehehe."


    elif jn_snap.last_game_result == jn_snap.JNSnapStates.draw:
        n 1csrfl "...Huh.{w=0.75}{nw}"
        extend 1tnmfl " ¿{i}Realmente{/i} empatamos?"
        n 2tslpu "..."
        n 2tslaj "Eso es...{w=1}{nw}"
        extend 4tllsl " casi impresionante,{w=0.2} de hecho.{w=1}{nw}"
        extend 2cllsssbr " Raro."
        n 2ccssssbr "Bueno,{w=0.2} como sea."
    else:


        n 4tnmpu "¿Huh?{w=0.5}{nw}"
        extend 4tnmbo " ¿Te rindes?"
        n 1ullaj "Bueno,{w=0.2} supongo que está bien.{w=0.75}{nw}"
        extend 1fchgn " ¡Tomo eso como una victoria para mí!"


    $ Natsuki.calculatedAffinityGain()
    $ play_again_prompt = "¡Juguemos de nuevo!"

    if jn_snap._player_win_streak >= 3:
        n 2fcsan "¡Uuuuuu-!"
        n 4fcsgsl "¡E-{w=0.2}exijo una revancha!{w=0.75}{nw}"
        extend 2fcspol " ¡No voy a caer así!"

        show natsuki 2fcsgsl
        $ play_again_prompt = "¡Vamos a jugar otra vez!"

    elif jn_snap._natsuki_win_streak >= 3:
        n 4fnmaj "¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
        extend 2fcsbs " ¡Eso {i}no puede{/i} ser todo lo que tienes!"
        n 2fchbs "¡Revancha!{w=0.3} ¡Revancha!"

        show natsuki 2fchbg
        $ play_again_prompt = "¡Otra vez!"
    else:

        n 2nsqsm "Así que..."

        show natsuki 2fchbg

    menu:
        n "[play_again_prompt]"
        "¡Acepto el reto!":

            n 2fcsbg "¡Puedes apostarlo,{w=0.2} [player]!"

            $ jn_snap._natsuki_skill_level += 1
            jump snap_start
        "Paso":

            n 1cllsl "Awww..."
            n 2fsqss "...Aguafiestas.{w=0.75}{nw}"
            extend 2fchsm " Ehehe."
            n 4ullss "Nah,{w=0.5}{nw}"
            extend 4nslss " supongo que está bien.{w=0.75}{nw}"

            if jn_snap._player_win_streak >= 3:
                extend 4fchsm " Y gracias por jugar."
                n 2csrpo "...Aunque me hayas pateado el trasero."
                show natsuki 2nsrpo

            elif jn_snap._natsuki_win_streak >= 3:
                extend 4fchsm " Y gracias por jugar."
                n 2fsqcs "...Solo trae más pelea la próxima vez."
                extend 2fcssm " Ahaha."
                show natsuki 1fcssm
            else:

                extend 2fchsm " ¡Gracias por jugar~!"
                show natsuki 1fcssm

            if random.choice([True, False]):
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)
                $ jnPause(1)
                hide black with Dissolve(1.25)


            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            jump ch30_loop

label snap_forfeit:
    hide screen snap_ui

    $ jn_snap._controls_enabled = False
    n 4ccsflsbr "E-{w=0.2}espera,{w=0.5}{nw}"
    extend 4cnmfl " ¿qué?{w=0.75}{nw}"
    extend 2knmfl " ¡Vamos,{w=0.2} [player]!"
    n 2cslaj "No te rendirás {i}en serio{/i} tan pronto...{w=0.5}{nw}"

    show natsuki 2csqca
    menu:
        n "¿Verdad?"
        "Sí, me rindo":

            n 2ccscaesm "..."
            n 2nllsl "Bueno,{w=0.2} supongo que está bien.{w=0.75}{nw}"
            extend 2fcsbg " ¡Pero lo tomaré como una victoria para mí!"


            $ jn_snap._player_win_streak = 0
            $ jn_snap._natsuki_win_streak += 1
            $ persistent._jn_snap_natsuki_wins += 1

            if random.choice([True, False]):
                show natsuki 1fcssm
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)
                $ jnPause(1)
                hide black with Dissolve(1.25)


            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()

            jump ch30_loop
        "¡En tus sueños!":

            n 4fcsaj "Oh,{w=0.5}{nw}"
            extend 4fcsbg " ¡{b}ahora{/b} sí,{w=0.2} [player]!"
            show natsuki 4fsqsm

            $ jn_snap._controls_enabled = True
            $ jn_snap._natsuki_skill_level += 1

            show screen snap_ui
            jump snap_main_loop


transform snap_popup:
    easeout 0.75 alpha 0


screen snap_ui():
    zorder 4


    add jn_snap._getCurrentTopCard() anchor (0, 0) pos (1000, 100)


    add jn_snap._CARD_FAN_IMAGE_PLAYER anchor (0,0) pos (675, 110)
    add "mod_assets/games/snap/card_fan_icon.png" anchor (0,0) pos (675, 180)


    add jn_snap._getCurrentTurnIndicator() anchor (0,0) pos (675, 250)


    text "Cartas abajo: {0}".format(len(jn_snap._cards_on_table)) size 32 xpos 1000 ypos 50 style "categorized_menu_button"
    text "Tu mano: {0}".format(len(jn_snap._player_hand)) size 22 xpos 750 ypos 125 style "categorized_menu_button"
    text "Mano de [n_name]: {0}".format(len(jn_snap._natsuki_hand)) size 22 xpos 750 ypos 195 style "categorized_menu_button"
    text "Turno: {0}".format(jn_snap._getCurrentTurnLabel()) size 22 xpos 750 ypos 265 style "categorized_menu_button"


    style_prefix "hkb"
    vbox:
        xpos 1012
        ypos 420


        key "1" action [
            
            If(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled, Function(jn_snap._placeCard, True)) 
        ]
        key "2" action [
            
            If(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled, Function(jn_snap._callSnap, True))
        ]


        textbutton _("Colocar"):
            style "hkbd_option"
            action [
                Function(jn_snap._placeCard, True),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]


        textbutton _("¡Snap!"):
            style "hkbd_option"
            action [
                Function(jn_snap._callSnap, True),
                SensitiveIf(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        null height 20


        textbutton _("Rendirse"):
            style "hkbd_option"
            action [
                Function(renpy.jump, "snap_forfeit"),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
