default persistent._jn_blackjack_unlocked = False
default persistent._jn_blackjack_explanation_given = False


default persistent._jn_blackjack_player_wins = 0
default persistent._jn_blackjack_natsuki_wins = 0
default persistent._jn_blackjack_player_streak = 0
default persistent._jn_blackjack_natsuki_streak = 0
default persistent._jn_blackjack_player_best_streak = 0














init python in jn_blackjack:
    from Enum import Enum
    import random
    import store
    import time


    _controls_enabled = False
    _is_player_turn = None
    _is_player_committed = False
    _game_state = None

    _natsuki_staying = False
    _player_staying = False
    _rounds = 0


    _deck = []
    _natsuki_hand = []
    _player_hand = []

    class JNBlackjackStates(Enum):
        """
        Identifiers for the different ways a blackjack game can end.
        """
        draw = 1
        forfeit = 2
        natsuki_bust = 3
        natsuki_blackjack = 4
        natsuki_closest = 5
        natsuki_exact = 6
        player_bust = 7
        player_blackjack = 8
        player_closest = 9
        player_exact = 10

    def _getHandSum(is_player):
        """
        Returns the total card value of a hand in blackjack.

        IN:
            - is_player - bool flag for whether to retrieve the sum from the players hand.

        OUT:
            - Total card value of the player's hand if is_player is True, otherwise total card value of Natsuki's hand.
        """
        return sum(card[1] for card in _player_hand) if is_player else sum(card[1] for card in _natsuki_hand)

    def _setup():
        """
        Performs initial setup for blackjack.
        The player and Natsuki are assigned two cards each to begin from a deck of shuffled cards.
        """
        del _deck[:]
        del _player_hand[:]
        del _natsuki_hand[:]
        
        global _is_player_committed
        global _controls_enabled
        global _game_state
        global _player_staying
        global _natsuki_staying
        
        _is_player_committed = False
        _controls_enabled = None
        _game_state = None
        _player_staying = False
        _natsuki_staying = False
        
        
        for card_suit in [
            "clubs",
            "diamonds",
            "hearts",
            "spades"
        ]:
            for card_number in range(1, 14):
                card_value = card_number
                
                if card_value == 1:
                    
                    card_value = 11
                
                else:
                    
                    card_value = 10 if card_value > 10 else card_value
                
                _deck.append(["mod_assets/games/cards/{0}/{1}.png".format(card_suit, card_number), card_value])
        
        random.shuffle(_deck)
        
        
        _player_hand.append(_deck.pop(0))
        _player_hand.append(_deck.pop(0))
        
        _natsuki_hand.append(_deck.pop(0))
        _natsuki_hand.append(_deck.pop(0))
        
        
        if _getHandSum(is_player=False) > 21:
            for card in _natsuki_hand:
                card[1] = 1 if card[1] == 11 else card[1]
        
        
        if _getHandSum(is_player=True) > 21:
            for card in _player_hand:
                card[1] = 1 if card[1] == 11 else card[1]
        
        
        global _is_player_turn
        _is_player_turn = True
        
        return

    def _stayOrHit(is_player, is_hit):
        """
        Handles the action/display for the player or Natsuki staying or hitting during a game, then checks win conditions post-turn.
        Staying refers to passing the turn.
        Hitting refers to pulling another card, adding it to the hand.

        IN:
            - is_player - bool flag for whether it is the player making the move. If False, it is Natsuki's move.
            - is_hit - bool flag for whether the move is a hit (drawing a card). If False, it is a stay.
        """
        global _is_player_turn
        
        if is_player:
            
            if is_hit:
                _player_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))
            
            _is_player_turn = False
            global _player_staying
            global _is_player_committed
            _player_staying = not is_hit
            _is_player_committed = True
        
        else:
            
            if is_hit:
                _natsuki_hand.append(_deck.pop())
                renpy.play("mod_assets/sfx/card_flip_{0}.ogg".format(random.choice(["a", "b", "c"])))
            
            _is_player_turn = True
            global _natsuki_staying
            _natsuki_staying = not is_hit
        
        _checkWinConditions()
        
        return

    def _checkWinConditions():
        """
        Checks the current game conditions to determine if either the player or Natsuki has won.
        """
        natsuki_hand_sum = _getHandSum(is_player=False)
        player_hand_sum = _getHandSum(is_player=True)
        
        natsuki_wins = False
        player_wins = False
        
        global _game_state
        
        
        if natsuki_hand_sum == 21 and player_hand_sum != 21:
            natsuki_wins = True
            _game_state = JNBlackjackStates.natsuki_blackjack if len(_natsuki_hand) == 2 else JNBlackjackStates.natsuki_exact
        
        elif player_hand_sum == 21 and natsuki_hand_sum != 21:
            player_wins = True
            _game_state = JNBlackjackStates.player_blackjack if len(_player_hand) == 2 else JNBlackjackStates.player_exact
        
        elif player_hand_sum == 21 and natsuki_hand_sum == 21:
            _game_state = JNBlackjackStates.draw
        
        elif natsuki_hand_sum > 21 and player_hand_sum < 21:
            player_wins = True
            _game_state = JNBlackjackStates.natsuki_bust
        
        elif player_hand_sum > 21 and natsuki_hand_sum < 21:
            natsuki_wins = True
            _game_state = JNBlackjackStates.player_bust
        
        elif player_hand_sum > 21 and natsuki_hand_sum > 21:
            _game_state = JNBlackjackStates.draw
            store.persistent._jn_blackjack_natsuki_streak = 0
            store.persistent._jn_blackjack_player_streak = 0
        
        
        elif (len(_natsuki_hand) == 5 and len(_natsuki_hand) == 5) or (_player_staying and _natsuki_staying):
            if natsuki_hand_sum > player_hand_sum:
                natsuki_wins = True
                _game_state = JNBlackjackStates.natsuki_closest
            
            elif player_hand_sum > natsuki_hand_sum:
                player_wins = True
                _game_state = JNBlackjackStates.player_closest
            
            else:
                
                _game_state = JNBlackjackStates.draw
        
        if _game_state is not None:
            _controls_enabled = False
        
        if natsuki_wins:
            renpy.play("mod_assets/sfx/pencil_scribble.ogg")
            store.persistent._jn_blackjack_natsuki_wins += 1
            store.persistent._jn_blackjack_natsuki_streak += 1
            store.persistent._jn_blackjack_player_streak = 0
        
        if player_wins:
            renpy.play("mod_assets/sfx/pencil_scribble.ogg")
            store.persistent._jn_blackjack_player_wins += 1
            store.persistent._jn_blackjack_player_streak += 1
            store.persistent._jn_blackjack_natsuki_streak = 0
            
            if store.persistent._jn_blackjack_player_streak > store.persistent._jn_blackjack_player_best_streak:
                store.persistent._jn_blackjack_player_best_streak = store.persistent._jn_blackjack_player_streak
        
        return

    def _showSplashImage():
        """
        Shows a splash image corresponding to the current game state.
        """
        image_state_map = {
            JNBlackjackStates.natsuki_blackjack: "nat_blackjack",
            JNBlackjackStates.player_blackjack: "you_blackjack",
            JNBlackjackStates.natsuki_bust: "nat_bust",
            JNBlackjackStates.player_bust: "you_bust",
            JNBlackjackStates.natsuki_closest: "nat_wins",
            JNBlackjackStates.player_closest: "you_win",
            JNBlackjackStates.natsuki_exact: "nat_wins",
            JNBlackjackStates.player_exact: "you_win",
            JNBlackjackStates.draw: "draw"
        }
        if _game_state in image_state_map:
            renpy.show(
                name="blackjack_popup",
                at_list=[store.blackjack_popup],
                layer="overlay",
                what=store.Image("mod_assets/games/blackjack/{0}.png".format(image_state_map[_game_state])),
                zorder=10)
        
        return

    def _getCurrentTurnLabel():
        """
        Returns the turn text to display on the blackjack UI, including win/lose states.

        OUT:
            - Nobody if it is nobody's turn; otherwise the player or Natsuki's current nickname
        """
        if _game_state == JNBlackjackStates.draw:
            return "¡Es un empate!"
        
        if (
            _game_state == JNBlackjackStates.natsuki_bust
            or _game_state == JNBlackjackStates.player_blackjack
            or _game_state == JNBlackjackStates.player_closest
            or _game_state == JNBlackjackStates.player_exact
        ):
            return "¡Ganaste!"
        
        if (
            _game_state == JNBlackjackStates.player_bust
            or _game_state == JNBlackjackStates.natsuki_blackjack
            or _game_state == JNBlackjackStates.natsuki_closest
            or _game_state == JNBlackjackStates.natsuki_exact
        ):
            return "¡Perdiste!"
        
        if _is_player_turn is None:
            return "¡Nadie!"
        
        return "¡Tuyo!" if _is_player_turn else "[n_name]"

    def _m1_script0x2dblackjack__getQuitOrForfeitLabel():
        """
        Returns text for the quit/forfeit button, based on if the player has committed to the game by making a move.

        OUT:
            - str "Forfeit" if the player has made any move, otherwise "Quit"
        """
        return "Rendirse" if _is_player_committed else "Salir"

    def _getNatsukiHandSumLabel():
        """
        Returns text for Natsuki's hand display, based on the current game state.
        The value of the first card in Natsuki's hand is always obfuscated, except for at the end of a round.

        OUT:
            - str "[n_name]: ? + X" if the round is ongoing, "[n_name]: 0" if Nat has yet to draw any cards, or "[n_name]: X" if the round is over.
        """
        if _game_state is None:
            return "[n_name]: ? + {0}".format(_getHandSum(is_player=False) - _natsuki_hand[0][1]) if len(_natsuki_hand) > 1 else "[n_name]: 0"
        
        return "[n_name]: {0}".format(_getHandSum(is_player=False))

    def _getCardDisplayable(is_player, index):
        """
        Returns a layered displayable for a card in a hand for blackjack, consisting of the card face and a shadow (or nothing if no card exists for the index).
        Note that Nat's first card is always hidden/obfuscated unless the game is over.
        
        IN:
            - is_player - bool flag for whether to get a displayable for the player's or Natsuki's hand
            - index - int value for the card in the hand to get the displayable for
        
        OUT:
            - Displayable for the card at the given index

        """
        top_sprite = ""
        bottom_sprite = ""
        
        if is_player:
            top_sprite = _player_hand[index][0] if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"
            bottom_sprite = "mod_assets/games/cards/card_shadow.png" if 0 <= index < len(_player_hand) else "mod_assets/natsuki/etc/empty.png"
        
        else:
            if _game_state is None and index == 0:
                
                top_sprite =  "mod_assets/games/cards/hide.png"
                bottom_sprite =  "mod_assets/natsuki/etc/empty.png"
            
            else:
                top_sprite = _natsuki_hand[index][0] if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"
                bottom_sprite = "mod_assets/games/cards/card_shadow.png" if 0 <= index < len(_natsuki_hand) else "mod_assets/natsuki/etc/empty.png"
        
        return renpy.display.layout.LiveComposite(
            (223, 312), 
            (5, 5), bottom_sprite, 
            (0, 0), top_sprite
        )

label blackjack_intro:
    n 2fnmbg "¡Muy bien!{w=0.75}{nw}"
    extend 4fchgn " ¡Juguemos un poco de blackjack!"

    if not persistent._jn_blackjack_explanation_given:
        n 4unmajeex "Oh,{w=0.2} cierto.{w=0.75}{nw}"
        extend 4flrsssbl " Casi lo olvido."
        n 2nsrsssbl "Así que antes de adelantarme {i}demasiado{/i}"

        show natsuki option_wait_curious
        menu:
            n "¿Necesitas una explicación de cómo funciona todo,{w=0.2} o...?"
            "¡Sí, por favor!":

                jump blackjack_explanation
            "No, estoy listo":

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 2fcssm "Je."
                    n 2fnmss "Estás listo,{w=0.5}{nw}"
                    extend 4fsqbg " ¿verdad?"
                    n 6fchgn "¡Listo para recibir una paliza de grado A!{w=0.75}{nw}"
                    extend 4fnmbgedz " ¡Vamos,{w=0.2} [player]!"

                elif dialogue_choice == 2:
                    n 7ttrbo "Hmm..."
                    n 7ulraj "Sí,{w=0.5}{nw}"
                    extend 3unmbo " diría que también estás listo."
                    n 4fcsbg "...¡Listo para el amargo sabor de la derrota!{w=0.75}{nw}"
                    extend 4fchbgedz " ¡Ahora vamos de una vez!"
                else:

                    n 1fcssm "Ehehe.{w=0.75}{nw}"
                    extend 2tsqss " ¿Oh?{w=0.75}{nw}"
                    extend 2fsqbg " Estás listo,{w=0.2} ¿eh?"
                    n 4fnmbg "...¡Listo para una paliza total!{w=0.75}{nw}"
                    extend 4nchgnedz " ¡Venga,{w=0.2} [player]!"

                $ persistent._jn_blackjack_explanation_given = True

    jump blackjack_start

label blackjack_explanation:
    if persistent._jn_blackjack_explanation_given:
        n 7ulraj "Así que como decía antes,{w=0.5}{nw}"
        extend 7unmbo " el Blackjack es bastante simple una vez que entiendes las reglas."
    else:

        n 4fcsbg "¡Muy bien!{w=0.75}{nw}"
        extend 7ullss " El Blackjack es en realidad bastante simple,{w=0.5}{nw}"
        extend 3unmaj " una vez que entiendes las reglas."

    n 5nsrsssbl "Hay un montón de formas diferentes en que la gente lo juega,{w=0.5}{nw}"
    extend 4ulraj " así que...{w=1}{nw}"
    extend 6ccssm " solo iremos con algo que funcione con solo nosotros dos aquí."
    n 3ullaj "Para empezar,{w=0.2} ambos recibimos un par de cartas aleatorias de la baraja."

    if not persistent._jn_blackjack_explanation_given:
        n 4fcsss "Sí,{w=0.2} sí.{w=0.75}{nw}"
        extend 2fsqsm " No te preocupes,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fcsbgeme " Yo {i}siempre{/i} barajo."

    n 3unmaj "A continuación,{w=0.2} ambos tomamos turnos ya sea para {i}pedir{/i} -{w=0.5}{nw}"
    extend 3clrss " sacar otra carta,{w=0.5}{nw}"
    extend 6unmbo " o {i}plantarse{/i} -{w=0.5}{nw}"
    extend 3cllsm " que es simplemente saltar nuestro turno."
    n 4tnmss "¿Cuál es el objetivo,{w=0.2} preguntas?"
    n 7tlrss "Bueno...{w=1}{nw}"
    extend 3fnmsm " básicamente estamos tratando de que el valor total de nuestras cartas sea lo más cercano a veintiuno como podamos.{w=0.75}{nw}"
    extend 3fcsbg " Si lo consigues con solo dos cartas,{w=0.2} ¡eso se llama un {i}blackjack{/i}!"

    if not persistent._jn_blackjack_explanation_given:
        n 7cllss "En cuanto a cómo van a funcionar las cartas..."

        if persistent.jn_snap_explanation_given:
            n 7tnmbo "Recuerdas el Snap,{w=0.2} ¿verdad?"
        else:

            n 3tnmbo "Al menos has visto cartas de juego antes,{w=0.2} ¿verdad?"

        n 6ullaj "Bueno, cada carta tiene un valor -{w=0.5}{nw}"
        extend 3ccssm " obviamente -{w=0.5}{nw}"
        extend 4nnmfl " pero no te preocupes por el {i}palo{/i} real:{w=0.75}{nw}"
        extend 1tlrbo " diamantes, espadas o lo que sea.{w=0.75}{nw}"
        extend 2fcssmesm " ¡Solo nos importan los {i}números{/i}!"
    else:

        n 3clrss "Como dije la última vez:{w=0.5}{nw}"
        extend 4tlraj " los palos de las cartas no importan aquí,{w=0.5}{nw}"
        extend 2fnmsm " así que son solo los números a los que tienes que echarles un ojo."

    n 4clrss "Las {i}cartas de figuras{/i} funcionan un poco diferente a las normales."
    n 6tnmaj "Si obtienes un {i}rey,{w=0.2} reina,{w=0.2} o jota{/i},{w=0.5}{nw}"
    extend 3ccssm " entonces esas solo cuentan como si valieran {i}diez{/i}."
    n 7tllfl "En cuanto a los ases...{w=1}{nw}"
    extend 3nchgn " ¡depende de cuándo los saques!{w=0.75}{nw}"
    n 3ulrss "Diremos que los ases valen {i}once{/i},{w=0.2} {i}a menos{/i} que obtengas uno al principio que te haría pasarte al instante.{w=0.75}{nw}"
    extend 3fcssm " No soy {i}tan{/i} mala."
    n 4cllbg "Pero sí -{w=0.5}{nw}"
    extend 2ullpu " si el as te hiciera {i}perder en tu primer turno{/i},{w=0.5}{nw}"
    extend 2nnmbo " entonces solo vale {i}uno{/i} en su lugar."
    n 7ulraj "Seguimos tomando turnos hasta que uno de nosotros llegue a veintiuno,{w=0.2} ambos gdecidamos {i}plantarnos{/i} -{w=0.5}{nw}"
    extend 7unmbo " o uno de nosotros termine con una mano que pase de veintiuno."
    n 6fchbl "...¡Eso significa que te pasaste!"
    n 1cllss "De lo contrario, si ninguno de nosotros termina pasándose,{w=0.5}{nw}"
    extend 2ccssm " entonces quien se haya acercado {i}más{/i} a veintiuno gana la ronda.{w=0.75}{nw}"
    extend 2fchbg " ¡Pan comido!"
    n 4unmaj "Oh,{w=0.2} sí -{w=0.5}{nw}"
    extend 7clrss " y no te preocupes por llevar la cuenta de la puntuación ni nada.\n{w=0.75}{nw}"
    extend 6fcsbg " ¡Lo tengo todo cubierto!"
    n 3fchsm "Jejeje."
    n 4fnmsm "¡Pero sí!{w=0.75}{nw}"
    extend 4ullss " Creo que eso es prácticamente todo lo que tenía que explicar."
    n 3ullaj "Así que...{w=1}{nw}"
    extend 7unmbo " ¿qué te parece,{w=0.2} [player]?"

    $ persistent._jn_blackjack_explanation_given = True
    show natsuki option_wait_curious
    menu:
        n "¿Entendiste todo eso,{w=0.2} o...?"
        "¿Puedes repasar las reglas de nuevo?":

            n 7tsqpueqm "¿Huh?{w=0.75}{nw}"
            extend 7tsqfl " ¿Necesitas que repase esas cosas de nuevo?"
            n 7cllfl "Bueno...{w=1}{nw}"
            extend 3nslbo " bien."
            n 3ccspoesi "Pero será mejor que estés escuchando esta vez,{w=0.2} [player]."

            jump blackjack_explanation
        "Entendido. ¡Juguemos!":

            n 7tnmaj "¿Oh?{w=0.75}{nw}"
            extend 7tnmfl " ¿Entendiste todo eso?{w=0.75}{nw}"
            extend 3tsqsm " ¿Seguro,{w=0.2} [player]?"
            n 1fcssm "Jejeje."
            n 2fcsbg "Bueno entonces."
            n 2fnmbg "...¡Supongo que es hora de poner eso a prueba!{w=0.75}{nw}"
            extend 4fchgn " ¡Hagámoslo,{w=0.2} [player]!"

            jump blackjack_start
        "Gracias, [n_name]. Jugaré luego":

            n 1ccsemesi "..."
            n 2ccsfl "...¿En serio,{w=0.5}{nw}"
            extend 2csqfl " [player]?"
            n 4fcsgs "Pasé por todo eso solo para que digas que vas a jugar{w=0.5}{nw}"
            extend 4ftlem " {i}luego{/i}?"
            n 1fsqca "..."
            n 3fchgn "Bueno,{w=0.75} ¡tú te lo pierdes!{w=0.75}{nw}"
            extend 6fcssmesm " Solo una advertencia sin embargo,{w=0.2} [player]..."

            if Natsuki.isLove(higher=True):
                n 3fcsbg "¡No creas que voy a ser más suave contigo luego tampoco!"
                n 3fchbllsbr "¡No vas a salirte con la tuya con palabras dulces!"
            else:

                n 3fcsbg "¡No creas que voy a ser más suave contigo luego tampoco!{w=0.75}{nw}"
                extend 3nchgnl " Jajaja."

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

label blackjack_start:
    $ HKBHideButtons()
    show screen blackjack_ui
    show natsuki option_wait_smug
    play audio card_place
    $ jn_blackjack._setup()
    $ Natsuki.setInGame(True)
    $ jn_blackjack._controls_enabled = True

    jump blackjack_main_loop

label blackjack_main_loop:
    if jn_blackjack._game_state is not None:
        $ jn_utils.fireAndForgetFunction(jn_blackjack._showSplashImage)
        $ jnPause(0.85)
        jump blackjack_end


    elif not jn_blackjack._is_player_turn:
        $ jn_blackjack._controls_enabled = False
        $ natsuki_hand_sum = jn_blackjack._getHandSum(is_player=False)

        $ nat_safe_range = [20]
        if persistent._jn_blackjack_player_streak > 1:
            $ nat_safe_range.append(19)

        if persistent._jn_blackjack_player_streak > 3:
            $ nat_safe_range.append(18)

        if natsuki_hand_sum in nat_safe_range or len(jn_blackjack._natsuki_hand) == 5:
            $ jnPause(delay=random.randint(1, 3), hard=True)
            $ jn_blackjack._stayOrHit(is_player=False, is_hit=False)
        else:

            python:
                hit_percent = 0.50
                deck_used_high_cards = 0
                deck_used_low_cards = 0
                needed_to_blackjack = 21 - natsuki_hand_sum

                for card in jn_blackjack._natsuki_hand:
                    if card[1] > 6:
                        deck_used_high_cards += 1
                    else:
                        deck_used_low_cards +=1

                if (
                    deck_used_high_cards > deck_used_low_cards and needed_to_blackjack <= 6
                    or deck_used_low_cards > deck_used_high_cards and needed_to_blackjack > 6
                ):
                    hit_percent += 0.35
                elif (
                    deck_used_high_cards == deck_used_low_cards and needed_to_blackjack <= 6
                    or deck_used_high_cards == deck_used_low_cards and needed_to_blackjack > 6
                ):
                    hit_percent += 0.20

                if hit_percent == 0.50 and needed_to_blackjack <= 6:
                    hit_percent -= 0.55

                risk_percent = jn_blackjack.store.persistent._jn_blackjack_natsuki_streak / 100 if jn_blackjack.store.persistent._jn_blackjack_natsuki_streak > 0 else 0
                risk_percent = 0.05 if risk_percent > 0.05 else risk_percent

                hit_percent += risk_percent
                hit_percent = 0.85 if hit_percent > 0.85 else hit_percent

                will_hit = random.randint(0, 100) / 100 <= hit_percent
                jnPause(delay=random.randint(2, 4), hard=True)
                jn_blackjack._stayOrHit(is_player=False, is_hit=will_hit)

    if jn_blackjack._game_state is None:
        $ jn_blackjack._controls_enabled = True

    $ jnPause(1)
    jump blackjack_main_loop

label blackjack_end:
    $ jn_blackjack._controls_enabled = False
    $ jn_blackjack._rounds += 1
    $ jnPause(delay=1, hard=True)
    $ chosen_response = ""

    if persistent._jn_blackjack_natsuki_streak in [3, 5, 10] and jn_blackjack._game_state in [jn_blackjack.JNBlackjackStates.natsuki_blackjack, jn_blackjack.JNBlackjackStates.natsuki_closest, jn_blackjack.JNBlackjackStates.natsuki_exact]:
        $ natsuki_streak_milestone_map = {
            3: [
                "¿Oh?{w=0.75} ¿Tres victorias ahora?{w=0.75} ¡Parece que {i}alguien{/i} tiene los ingredientes de una racha!",
                "¡Sí!{w=0.75} ¡Eso hace tres seguidas!{w=0.75} Jejeje.",
                "¡Tres victorias y contando,{w=0.2} [player]!{w=0.75} Jejeje.",
                "¿Qué es eso?{w=0.75} ¿Tres victorias ahora?{w=0.75} ¡Suena a una racha para mí!",
                "¡Oh sí!{w=0.75} ¡Tres seguidas!"
            ],
            5: [
                "¡Ja!{w=0.75} ¡Eso hace cinco seguidas ahora,{w=0.2} [player]!",
                "¡Sí!{w=0.75} ¡Cinco seguidas!{w=1} Supera eso,{w=0.2} {i}[player]{/i}.",
                "¡Y eso hace cinco!{w=0.75} ¿No {i}dije{/i} que era buena?",
                "¡Sí!{w=0.75} ¡Esas son cinco victorias y contando!",
                "¡Sí!{w=0.75} ¡Cinco seguidas!{w=0.75} Jejeje."
            ],
            10: [
                "¡Oh sí!{w=0.75} ¡Diez!{w=0.75} ¡Ahora {i}eso{/i} es lo que significa ser una pro,{w=0.2} [player]!",
                "Viejo...{w=1} ¿diez seguidas?{w=0.75} ¡Estoy en {i}racha{/i} hoy!{w=0.75} Jejeje.",
                "¡Ja!{w=0.75} ¡El gran diez!{w=0.75} ¿Qué tienes que decir respecto a eso,{w=0.2} [player]?",
                "¡Sí!{w=0.75} ¡Diez seguidas!{w=0.75} Viejo...{w=1} ¡Soy imparable!",
                "Cielos...{w=1} ¿cuánto es ahora?{w=0.75} ¿Diez?{w=0.75} ¡Al menos {i}intenta{/i} seguirme el ritmo,{w=0.2} [player]!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(natsuki_streak_milestone_map[persistent._jn_blackjack_natsuki_streak]))

    elif persistent._jn_blackjack_player_streak in [3, 5, 10] and jn_blackjack._game_state in [jn_blackjack.JNBlackjackStates.player_blackjack, jn_blackjack.JNBlackjackStates.player_closest, jn_blackjack.JNBlackjackStates.player_exact]:
        $ player_streak_milestone_map = {
            3: [
                "G-{w=0.2}golpe de suerte,{w=0.2} [player].{w=0.75} ¡Cualquiera puede tener suerte tres veces seguidas!",
                "Sí,{w=0.2} sí.{w=0.75} ¡T-{w=0.2}tres seguidas no es nada de todos modos!",
                "¡A-{w=0.2}apuesto a que no puedes hacer que sean cuatro seguidas,{w=0.2} [player]!",
                "M-{w=0.2}mejor no te pongas arrogante.{w=0.75} Tres seguidas no es nada,{w=0.2} [player]!",
                "¡T-{w=0.2}tres derrotas seguidas no es nada!{w=0.75} ¡Seriamente solo estoy empezando!"
            ],
            5: [
                "¡Uuuuuu...!{w=0.75} ¡P-{w=0.2}puedes dejar de tener tanta suerte ahora,{w=0.2} [player]!{w=0.75} Cielos...",
                "¿C-{w=0.2}cinco seguidas ahora?{w=0.75} ¡¿Me estás tomando el pelo?!",
                "¿En serio?{w=0.75} ¡¿Son cinco veces seguidas?!{w=0.75} Ugh...",
                "¡Nnnnnn-!{w=0.75} ¡N-{w=0.2}no hay manera de que acabes de ganar cinco seguidas!{w=0.75} Dame un respiro...",
                "¡T-{w=0.2}tienes que estar bromeando!{w=0.75} ¡¿Cinco veces?!{w=0.75} ¡N-{w=0.2}no hay manera de que esto sea otra cosa que suerte!"
            ],
            10: [
                "¿A-{w=0.2}acaso estás leyendo mis cartas o qué?{w=0.75} ¡¿{i}Diez{/i}?!{w=0.75} Cielos...",
                "¡Oh{w=0.2},{w=0.75} vamos!{w=0.75} ¡No hay {i}manera{/i} de que acabes de ganar diez seguidas!{w=0.75} Ugh...",
                "¡E-{w=0.2}esto se está volviendo ridículo!{w=0.75} ¡¿Diez seguidas?!{w=0.75} {i}Juro{/i} que estas cartas están amañadas...",
                "¡Bien!{w=0.75} ¡Bien!{w=0.75} Ya dejaste tu punto claro...{w=1} ¿ahora puedes volver a perder de una vez? Cielos...",
                "¡Nnnnnnnn-!{w=0.75} ¡S-{w=0.2}solo pierde ya,{w=0.2} [player]!{w=0.75} ¡Es mi turno de ganar algo!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(player_streak_milestone_map[persistent._jn_blackjack_player_streak]))
    else:

        $ response_map = {
            jn_blackjack.JNBlackjackStates.draw: [
                "¿Empatamos?{w=0.75} Huh.",
                "Huh.{w=0.75} ¿Empatamos?{w=0.75} Que raro.",
                "Espera,{w=0.2} ¿empatamos?{w=0.75} Huh.",
                "¿Un empate?{w=0.75} Raro.",
                "Vamos,{w=0.2} [player]...{w=1} ¡tienes que perder alguna vez!",
                "Huh.{w=0.75} Otro empate.",
                "Otro empate,{w=0.2} ¿eh?{w=0.75} Raro."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_bust: [
                "¿Me pasé?{w=0.75} ¡¿Me estás tomando el pelo?!{w=0.75} Ugh...",
                "¡Oh,{w=0.2} vamos!{w=0.75} ¡¿Me pasé {i}de nuevo{/i}?!{w=0.75} Cielos...",
                "¡Oh,{w=0.2} por-!{w=0.75} ¡¿{i}Otra{/i} vez me pasé?!{w=0.75} En serio...",
                "¡C-{w=0.2}como {i}si{/i} me hubiera pasado!{w=0.75} Viejo...",
                "¡¿Estás bromeando?!{w=0.75} ¡¿Me pasé de nuevo?!",
                "Tienes {i}que{/i} estar bromeando.{w=0.75} ¡¿De nuevo?!",
                "Vamos,{w=0.5} [n_name]...{w=1} ¡compórtate!",
                "¡Uuuuuuu...!{w=0.75} ¡{i}Sabía{/i} que ese era un movimiento de mierda!{w=0.75} Ugh..."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_blackjack: [
                "¡Sí!{w=0.5} ¡Sí!{w=0.5} ¡Blackjack!{w=0.75} Jejeje.",
                "¡Blackjack!{w=0.5} ¡Blackjack!{w=0.5} Jejeje.",
                "¡Blackjack!{w=0.5} ¡Sí!{w=0.5} ¡Ahora {i}así{/i} es como se hace!",
                "¡Sí!{w=0.5} ¡Ahora {i}eso{/i} es más como lo que quería!{w=0.75} Jajaja.",
                "¡Mejor toma notas,{w=0.2} [player]!{w=0.75} Jejeje.",
                "¡Oh sí!{w=0.75} ¡Blackjack!",
                "¡Blackjack!{w=0.75} ¡Blackjack!{w=0.75} ¡Sí!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_closest: [
                "¡Sí!{w=0.5} ¡Gané!{w=0.3} ¡Gané!{w=0.75} Jejeje.",
                "¡Sí!{w=0.5} ¡Gané de nuevo!",
                "¡Mira!{w=0.5} ¡Estuve más cerca!{w=0.3} ¡Gané!{w=0.3} ¡Gané!",
                "¡Sí!{w=0.5} ¡Toma esa,{w=0.2} [player]!{w=0.75} Jejeje.",
                "¡Oh sí!{w=0.75} ¡Ahora {i}eso{/i} es más como lo que quería!",
                "¡Sí!{w=0.75} Mala suerte,{w=0.2} [player]!{w=0.75} Jejeje.",
                "Jejeje.{w=0.75} ¡Ahora {i}así{/i} es como se juega,{w=0.2} [player]!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_exact: [
                "Bueno...{w=0.75} no es un {i}blackjack{/i}...{w=0.75} ¡pero lo tomaré!",
                "Jejeje.{w=0.75} Una victoria es una victoria,{w=0.2} [player]!",
                "¡Solo mira,{w=0.2} [player]!{w=0.75} ¡La próxima victoria es un blackjack!",
                "Je.{w=0.75} No importa,{w=0.2} [player] -{w=0.2} ¡sigue siendo una victoria!",
                "¿Q-{w=0.2}quién dice que necesitas blackjack para ser una profesional?{w=0.75} Jejeje.",
                "¡H-{w=0.2}hey!{w=0.75} ¡Todavía es veintiuno,{w=0.2} te guste o no!",
                "Jejeje.{w=0.75} ¡Todavía veintiuno,{w=0.2} [player]!"
            ],
            jn_blackjack.JNBlackjackStates.player_bust: [
                "¡Pfft-!{w=0.75} ¡Bonita pasada ahí,{w=0.2} [player]!{w=0.75} Jejeje.",
                "Sip.{w=0.5} Jugada totalmente equivocada,{w=0.2} [player]!",
                "¡Ahora a eso le llamo pasarse!{w=0.75} Jejeje.",
                "Jajaja.{w=0.75} Apesta ser tú,{w=0.2} [player]!",
                "¡Pffft!{w=0.75} ¿Seguro que {i}sabes{/i} jugar,{w=0.2} [player]?",
                "¡{i}Muy{/i} suave ahí,{w=0.2} [player]!{w=0.75} Jejeje.",
                "Oye,{w=0.2} [player] -{w=0.5} ¡se supone que tienes que contar las cartas!{w=0.75} Jejeje."
            ],
            jn_blackjack.JNBlackjackStates.player_blackjack: [
                "¿En serio?{w=0.75} ¡¿Conseguiste un blackjack?!{w=0.75} Ugh...",
                "Sí,{w=0.2} sí.{w=0.75} Disfruta tu suerte mientras dure,{w=0.2} [player].",
                "Hmph.{w=0.75} Solo tuviste suerte esta vez.",
                "¡Oh,{w=0.2} vamos!{w=0.75} ¿De nuevo?{w=0.75} En serio...",
                "¡A-{w=0.2}ahora esa fue pura suerte!{w=0.75} Ugh...",
                "¡E-{w=0.2}esa fue pura casualidad!{w=0.75} Vamos...",
                "Ugh...{w=1} ¿de verdad?{w=0.75} ¿Obtuviste otro blackjack?"
            ],
            jn_blackjack.JNBlackjackStates.player_closest: [
                "Je.{w=0.75} Disfruta la suerte mientras dure,{w=0.2} [player].",
                "¿{i}En serio{/i}?{w=0.75} Ugh...",
                "¡Vamos!{w=0.75} ¿De verdad?{w=0.75} Viejo...",
                "Sí,{w=0.2} sí.{w=0.75} Ríete,{w=0.2} [player].{w=0.75} Solo espera...",
                "Hmph.{w=1} Golpe de suerte,{w=0.2} [player].{w=0.75} Eso es todo lo que digo.",
                "¡Uuuuuu-!{w=0.75} ¡Totalmente acabas de tener la mejor mano!{w=0.75} Ugh...",
                "T-{w=0.2}totalmente tuviste suerte esta vez,{w=0.2} [player].{w=0.75} Eso es todo lo que es."
            ],
            jn_blackjack.JNBlackjackStates.player_exact: [
                "Je.{w=0.75} ¡Lástima que no fuera un blackjack,{w=0.2} [player]!",
                "¡Nnnnn-!{w=0.75} A-{w=0.2}al menos no hiciste blackjack.",
                "Sí,{w=0.2} sí,{w=0.2} lo que sea.{w=0.75} Mano de suerte,{w=0.2} [player].",
                "¡G-{w=0.2}golpe de suerte!{w=0.75} Ahora intenta hacer {i}realmente{/i} blackjack...",
                "¡C-{w=0.2}como si {i}esa{/i} mano ganara!{w=0.75} Ugh...",
                "¡¿Me estás tomando el pelo?!{w=0.75} ¡¿Ganaste con eso?!{w=0.75} Viejo...",
                "Ugh...{w=0.75} y ni siquiera fue un {i}blackjack{/i}..."
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(response_map[jn_blackjack._game_state]))

    n "[chosen_response]"
    $ jnPause(0.5)
    jump blackjack_start

label blackjack_quit_forfeit:
    hide screen blackjack_ui
    $ natsuki_prompt = ""

    if jn_blackjack._is_player_committed:
        n 1tnmpueqm "¿Eh?{w=0.75}{nw}"
        extend 2tnmsleqm " ¿Terminaste de jugar,{w=0.2} [player]?"

        if jn_blackjack._rounds == 0:
            n 4ccsflsbr "...E-{w=0.2}espera.{w=0.75}{nw}"
            extend 3fcsgssbr " ¡Aguanta un segundo,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3fnmgs " ¿Qué quieres decir?"
            n 4fcswr "¡Literalmente acabamos de empezar a {i}jugar{/i}!{w=0.75}{nw}"
            extend 2flrem " Cielos..."
            n 2csqcasbl "Será mejor que no me estés tomando el pelo de nuevo,{w=0.2} [player]."

            $ natsuki_prompt = "¿Realmente {i}quieres{/i} jugar blackjack o no?"
            show natsuki option_wait_sulky

        elif jn_blackjack._rounds < 6:
            n 1kslfl "Viejo...{w=1}{nw}"
            extend 4cnmem " ¿en serio?{w=0.75}{nw}"
            extend 4ccsgssbl " ¡Vamos,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3ccsposbl " No puedes haber terminado tan pronto {i}ya{/i}."
            n 3flrflsbr "Seriamente -{w=0.5}{nw}"
            extend 3tnmfl " ¡solo han pasado como [jn_blackjack._rounds] rondas!{w=0.75}{nw}"
            extend 4cnmaj " ¡Apenas hemos empezado!"

            $ natsuki_prompt = "Podrías {i}fácilmente{/i} jugar al menos un par de juegos más...{w=0.5} ¿verdad?"
            show natsuki option_wait_sulky
        else:

            n 2tdrsl "..."
            n 2tdrfl "Bueno...{w=1}{nw}"
            extend 2tlrbo " has estado jugando un tiempo.{w=0.75}{nw}"
            extend 4csrpo " {i}Supongo{/i}."
            n 2nsqca "...Incluso si {i}estás{/i} renunciando justo en medio de un juego."
            n 2nllaj "Así que..."

            $ natsuki_prompt = "¿Estás seguro de que no quieres seguir jugando,{w=0.2} [player]?"
            show natsuki option_wait_curious
    else:

        n 4ccsss "¿Oh?{w=0.75}{nw}"
        extend 4fllss " ¿Qué es esto,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqbg " ¿Por qué las dudas de repente?"
        n 1fsqsm "Jejeje."
        n 2fnmbg "¡Vamos!{w=0.75}{nw}"
        extend 2fcsbs " ¡No me digas que te rindes {i}así{/i} de fácil!"

        $ natsuki_prompt = "Puedes al {i}menos{/i} aguantar hasta el final de esta,{w=0.2} ¿verdad?"
        show natsuki option_wait_smug

    $ natsuki_prompt = renpy.substitute(natsuki_prompt)
    menu:
        n "[natsuki_prompt]"
        "No, terminé de jugar por ahora":

            if jn_blackjack._is_player_committed:
                n 1kcsflesi "...Viejo.{w=0.75}{nw}"
                extend 4ksqfl " ¿De verdad,{w=0.2} [player]?"
                n 2cslbo "..."
                n 2nslaj "Bueno...{w=1}{nw}"
                extend 5cdrca " No puedo decir que no esté al menos un poco decepcionada.{w=0.75}{nw}"
                extend 5nlraj " Pero supongo que está bien."
                n 4ccsss "Después de todo..."

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 3fcsbg "¡Solo significa otra victoria para mí!{w=0.75}{nw}"

                elif dialogue_choice == 2:
                    n 3fcssmesm "¡Como si fuera a rechazar una victoria fácil!{w=0.75}{nw}"
                else:

                    n 3nchgn "¡Eso sigue siendo una victoria para mí!{w=0.75}{nw}"

                extend 3fcssmeme " Jejeje."
            else:

                n 1nsqpu "...Wow.{w=0.75}{nw}"
                extend 4tnmfl " ¡Y ni siquiera terminaste haciendo un solo movimiento en esa ronda!{w=0.75}{nw}"
                extend 4tlrbo " Huh."
                n 2tlrsl "..."
                n 2ulrfl "Bueno.{w=0.75}{nw}"
                extend 2fcsss " Parece que {i}tú{/i} sabes lo que dicen al menos,{w=0.5}{nw}"
                extend 2fsqbg " [player]."
                n 6fcsbs "¡Supongo que el único movimiento ganador para ti era no jugar!{w=0.75}{nw}"
                extend 7fchsmeme " Jejeje."

            if random.choice([True, False]):
                show natsuki 4fcssm
                show black zorder JN_BLACK_ZORDER with Dissolve(0.5)
                $ jnPause(1)
                play audio drawer
                $ Natsuki.clearDeskItem(jn_desk_items.JNDeskSlots.right)
                $ jnPause(1)
                hide black with Dissolve(1.25)

            if jn_blackjack._rounds > 0:
                $ Natsuki.calculatedAffinityGain()

            $ jn_blackjack._rounds = 0
            $ Natsuki.setInGame(False)
            $ Natsuki.resetLastTopicCall()
            $ Natsuki.resetLastIdleCall()
            $ HKBShowButtons()

            jump ch30_loop
        "¡Acepto!":

            if not jn_blackjack._is_player_committed:
                n 4fcsbgsbr "¡S-{w=0.2}sí!{w=0.75}{nw}"
                extend 2fcsbssbr " ¡Ahora eso es más como lo que quería!{w=0.75}{nw}"
                extend 2fsqbg " ¡Un poco de espíritu de lucha!"
                n 4fnmgsedz "¡Venga ya,{w=0.2} [player]!"

            elif jn_blackjack._rounds == 0:
                n 1fspgs "¡Sí!{w=0.75}{nw}"
                extend 3fcsbg " ¿Ves?{w=0.75}{nw}"
                extend 3fchgn " ¡Sabía que te quedaba algo de lucha!"
                n 1ccsbg "Además..."
                n 2fsqbg "Solo un verdadero mal perdedor se acobardaría antes de haber siquiera {i}perdido{/i}.{w=0.75}{nw}"
                extend 2fsqsm " Jejeje."
                n 4fnmbs "¡Demuéstrame que me equivoco,{w=0.2} [player]!"
            else:

                n 1fsqsm "Jejeje.{w=0.75}{nw}"
                extend 3fcsbs " ¡Ahora de {i}eso{/i} estoy hablando!"
                n 3fnmsm "..."
                n 3fsqbg "¿Y bien?{w=0.75}{nw}"
                extend 4fcsbg " ¿Qué estás esperando?"
                n 4fchgn "¡Haz tu movimiento ya,{w=0.2} [player]!"

            show screen blackjack_ui
            show natsuki option_wait_smug
            jump blackjack_main_loop

    return

style blackjack_note_text:
    font gui.interface_font
    size gui.interface_text_size
    color "#000000"
    outlines []

    line_overlap_split 8
    line_spacing 8
    line_leading 8

transform blackjack_card_scale_down:
    zoom 0.675

transform blackjack_popup:
    parallel:
        ease 0.25 alpha 1.0 yoffset -30
        easeout 0.75 alpha 0

screen blackjack_ui():
    zorder 5

    add "mod_assets/natsuki/desk/table/topdown/table.png" anchor (0, 0) pos (0, 0)
    add "mod_assets/natsuki/desk/table/topdown/accessories.png" anchor (0, 0) pos (0, 0)
    add "mod_assets/natsuki/desk/table/topdown/nameplates.png" anchor (0, 0) pos (0, 0)


    vbox:
        pos (40, 60)
        if persistent._jn_blackjack_show_hand_value:
            text jn_blackjack._getNatsukiHandSumLabel() style "categorized_menu_button" size 24 xysize (300, None) outlines [(3, "#2E1503EF", 0, 0)]

        else:
            text "[n_name]" style "categorized_menu_button" size 24 xysize (300, None) outlines [(3, "#2E1503EF", 0, 0)]

        null height 10

        grid 5 1:
            spacing 10
            add jn_blackjack._getCardDisplayable(is_player=False, index=0) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=1) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=2) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=3) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=False, index=4) anchor (0,0) at blackjack_card_scale_down


    vbox:
        pos (40, 342)
        if persistent._jn_blackjack_show_hand_value:
            text "[player]: {0}".format(jn_blackjack._getHandSum(True)) style "categorized_menu_button" size 24 outlines [(3, "#2E1503EF", 0, 0)]

        else:
            text "[player]" style "categorized_menu_button" size 24 outlines [(3, "#2E1503EF", 0, 0)]

        null height 10

        grid 5 1:
            spacing 10
            add jn_blackjack._getCardDisplayable(is_player=True, index=0) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=1) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=2) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=3) anchor (0,0) at blackjack_card_scale_down
            add jn_blackjack._getCardDisplayable(is_player=True, index=4) anchor (0,0) at blackjack_card_scale_down


    vbox:
        xpos 960 ypos 230

        grid 1 3:
            spacing 10
            text "[player]: {0}".format(persistent._jn_blackjack_player_wins) style "blackjack_note_text"
            text "[n_name]: {0}".format(persistent._jn_blackjack_natsuki_wins) style "blackjack_note_text"
            text "Turn: {0}".format(jn_blackjack._getCurrentTurnLabel()) style "blackjack_note_text"

        null height 120


        style_prefix "hkb"


        key "1" action [
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 5, Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        textbutton _("¡Pedir!"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, True),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 5)]


        key "2" action [
            
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled, Function(jn_blackjack._stayOrHit, True, False))
        ]
        textbutton _("Plantarse"):
            style "hkbd_option"
            action [
                Function(jn_blackjack._stayOrHit, True, False),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]

        null height 20


        textbutton _(jn_blackjack._m1_script0x2dblackjack__getQuitOrForfeitLabel()):
            style "hkbd_option"
            action [
                Function(renpy.jump, "blackjack_quit_forfeit"),
                SensitiveIf(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
