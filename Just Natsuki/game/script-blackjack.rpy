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
            return _("It's a draw!")
        
        if (
            _game_state == JNBlackjackStates.natsuki_bust
            or _game_state == JNBlackjackStates.player_blackjack
            or _game_state == JNBlackjackStates.player_closest
            or _game_state == JNBlackjackStates.player_exact
        ):
            return _("You win!")
        
        if (
            _game_state == JNBlackjackStates.player_bust
            or _game_state == JNBlackjackStates.natsuki_blackjack
            or _game_state == JNBlackjackStates.natsuki_closest
            or _game_state == JNBlackjackStates.natsuki_exact
        ):
            return _("You lose!")
        
        if _is_player_turn is None:
            return _("Nobody!")
        
        return _("Yours!") if _is_player_turn else "[n_name]"

    def _m1_script0x2dblackjack__getQuitOrForfeitLabel():
        """
        Returns text for the quit/forfeit button, based on if the player has committed to the game by making a move.

        OUT:
            - str "Forfeit" if the player has made any move, otherwise "Quit"
        """
        return _("Forfeit") if _is_player_committed else _("Quit")

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
    n 2fnmbg "Alright!{w=0.75}{nw}"
    extend 4fchgn " Let's play some blackjack!"

    if not persistent._jn_blackjack_explanation_given:
        n 4unmajeex "Oh,{w=0.2} right.{w=0.75}{nw}"
        extend 4flrsssbl " I almost forgot."
        n 2nsrsssbl "So before I get {i}too{/i} ahead of myself here..."

        show natsuki option_wait_curious

        menu:
            n "Did you need an explanation on how it all works,{w=0.2} or...?"
            "Yes please!":
                jump blackjack_explanation
            "No, I'm ready.":

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 2fcssm "Heh."
                    n 2fnmss "You're ready,{w=0.5}{nw}"
                    extend 4fsqbg " are you?"
                    n 6fchgn "Ready to get a grade A butt kicking!{w=0.75}{nw}"
                    extend 4fnmbgedz " Let's go,{w=0.2} [player]!"

                elif dialogue_choice == 2:
                    n 7ttrbo "Hmm..."
                    n 7ulraj "Yeah,{w=0.5}{nw}"
                    extend 3unmbo " I'd say you're about ready too."
                    n 4fcsbg "...Ready for the bitter taste of defeat!{w=0.75}{nw}"
                    extend 4fchbgedz " Now let's go already!"
                else:

                    n 1fcssm "Ehehe.{w=0.75}{nw}"
                    extend 2tsqss " Oh?{w=0.75}{nw}"
                    extend 2fsqbg " You're ready,{w=0.2} huh?"
                    n 4fnmbg "...Ready for a total thrashing!{w=0.75}{nw}"
                    extend 4nchgnedz " Bring it,{w=0.2} [player]!"

                $ persistent._jn_blackjack_explanation_given = True

    jump blackjack_start

label blackjack_explanation:
    if persistent._jn_blackjack_explanation_given:
        n 7ulraj "So like I was saying before,{w=0.5}{nw}"
        extend 7unmbo " Blackjack is pretty simple once you've got your head around the rules."
    else:

        n 4fcsbg "So!{w=0.75}{nw}"
        extend 7ullss " Blackjack is actually pretty simple,{w=0.5}{nw}"
        extend 3unmaj " once you've got your head around the rules."

    n 5nsrsssbl "There's a bunch of different ways people play it,{w=0.5}{nw}"
    extend 4ulraj " so...{w=1}{nw}"
    extend 6ccssm " we'll just go with something that works with only the two of us here."
    n 3ullaj "To start off,{w=0.2} we both get a couple random cards each from the deck."

    if not persistent._jn_blackjack_explanation_given:
        n 4fcsss "Yeah,{w=0.2} yeah.{w=0.75}{nw}"
        extend 2fsqsm " Don't worry,{w=0.2} [player].{w=0.75}{nw}"
        extend 2fcsbgeme " I {i}always{/i} shuffle."

    n 3unmaj "Next,{w=0.2} we both take it in turns to either {i}hit{/i} -{w=0.5}{nw}"
    extend 3clrss " draw another card,{w=0.5}{nw}"
    extend 6unmbo " or {i}stay{/i} -{w=0.5}{nw}"
    extend 3cllsm " which is just skipping our turn."
    n 4tnmss "What's the goal,{w=0.2} you ask?"
    n 7tlrss "Well...{w=1}{nw}"
    extend 3fnmsm " we're basically trying to get the total value of our cards as close to twenty one as we can.{w=0.75}{nw}"
    extend 3fcsbg " If you get it with just two cards,{w=0.2} that's called a {i}blackjack{/i}!"

    if not persistent._jn_blackjack_explanation_given:
        n 7cllss "As for how the cards are gonna work..."

        if persistent.jn_snap_explanation_given:
            n 7tnmbo "You remember Snap,{w=0.2} right?"
        else:

            n 3tnmbo "You've at least seen playing cards before,{w=0.2} right?"

        n 6ullaj "Well each card has a value -{w=0.5}{nw}"
        extend 3ccssm " obviously -{w=0.5}{nw}"
        extend 4nnmfl " but don't worry about the actual {i}suit{/i}:{w=0.75}{nw}"
        extend 1tlrbo " diamonds or spades or whatever.{w=0.75}{nw}"
        extend 2fcssmesm " We only care about the {i}numbers{/i}!"
    else:

        n 3clrss "Like I said last time:{w=0.5}{nw}"
        extend 4tlraj " the suits of the cards don't matter here,{w=0.5}{nw}"
        extend 2fnmsm " so it's just the numbers you gotta keep an eye on."

    n 4clrss "The {i}face cards{/i} work kinda differently to the normal ones."
    n 6tnmaj "If you get a {i}king,{w=0.2} queen,{w=0.2} or jack{/i},{w=0.5}{nw}"
    extend 3ccssm " then those just count as being worth {i}ten{/i}."
    n 7tllfl "As for aces...{w=1}{nw}"
    extend 3nchgn " depends when you draw them!{w=0.75}{nw}"
    n 3ulrss "We'll say aces are worth {i}eleven{/i},{w=0.2} {i}unless{/i} you got one to start with that would make you bust instantly.{w=0.75}{nw}"
    extend 3fcssm " I'm not {i}that{/i} mean."
    n 4cllbg "But yeah -{w=0.5}{nw}"
    extend 2ullpu " if the ace would make you {i}lose on your first turn{/i},{w=0.5}{nw}"
    extend 2nnmbo " then it's just worth {i}one{/i} instead."
    n 7ulraj "We keep taking it in turns until one of us hits twenty one,{w=0.2} we both decide to {i}stay{/i} -{w=0.5}{nw}"
    extend 7unmbo " or one of us ends up with a hand that goes over twenty one."
    n 6fchbl "...That means you bust!"
    n 1cllss "Otherwise if neither of us end up busting,{w=0.5}{nw}"
    extend 2ccssm " then whoever got {i}closest{/i} to twenty one wins the round.{w=0.75}{nw}"
    extend 2fchbg " Easy peasy!"
    n 4unmaj "Oh,{w=0.2} yeah -{w=0.5}{nw}"
    extend 7clrss " and don't worry about keeping tabs on the score or anything.\n{w=0.75}{nw}"
    extend 6fcsbg " I've got it all covered!"
    n 3fchsm "Ehehe."
    n 4fnmsm "But yeah!{w=0.75}{nw}"
    extend 4ullss " I think that's pretty much everything I had."
    n 3ullaj "So...{w=1}{nw}"
    extend 7unmbo " how about it,{w=0.2} [player]?"

    $ persistent._jn_blackjack_explanation_given = True
    show natsuki option_wait_curious

    menu:
        n "Did you catch all that,{w=0.2} or...?"
        "Can you go over the rules again?":
            n 7tsqpueqm "Huh?{w=0.75}{nw}"
            extend 7tsqfl " You need me to go over that stuff again?"
            n 7cllfl "Well...{w=1}{nw}"
            extend 3nslbo " fine."
            n 3ccspoesi "But you better be listening this time,{w=0.2} [player]."

            jump blackjack_explanation
        "Got it. Let's play!":

            n 7tnmaj "Oh?{w=0.75}{nw}"
            extend 7tnmfl " You got all that?{w=0.75}{nw}"
            extend 3tsqsm " You sure,{w=0.2} [player]?"
            n 1fcssm "Ehehe."
            n 2fcsbg "Well then."
            n 2fnmbg "...Guess it's about time we put that to the test!{w=0.75}{nw}"
            extend 4fchgn " Let's do this,{w=0.2} [player]!"

            jump blackjack_start
        "Thanks, [n_name]. I'll play later.":

            n 1ccsemesi "..."
            n 2ccsfl "...Really,{w=0.5}{nw}"
            extend 2csqfl " [player]?"
            n 4fcsgs "I went through all that just for you to say you're gonna play{w=0.5}{nw}"
            extend 4ftlem " {i}later{/i}?"
            n 1fsqca "..."
            n 3fchgn "Well,{w=0.75} your loss!{w=0.75}{nw}"
            extend 6fcssmesm " Just a word of warning though,{w=0.2} [player]..."

            if Natsuki.isLove(higher=True):
                n 3fcsbg "Don't think I'm gonna go any easier on you later either!"
                n 3fchbllsbr "You aren't gonna sweet-talk your way out of losing!"
            else:

                n 3fcsbg "Don't think I'm gonna go any easier on you later either!{w=0.75}{nw}"
                extend 3nchgnl " Ahaha."

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
                "¿Oh?{w=0.75} ¿Tres victorias ahora?{w=0.75} ¡Parece que {i}alguien{/i} tiene los ingredientes para una racha!",
                "¡Sí!{w=0.75} ¡Eso hace tres seguidos!{w=0.75} Jejeje.",
                "¡Tres victorias y contando,{w=0.2} [player]!{w=0.75} Jejeje.",
                "¿Qué es eso?{w=0.75} ¿Tres victorias?{w=0.75} ¡A mí me parece una racha!",
                "¡Oh, sí!{w=0.75} ¡Tres seguidos!"
            ],
            5: [
                "¡Ja!{w=0.75} ¡Ya son cinco seguidos,{w=0.2} [player]!",
                "¡Sí!{w=0.75} ¡Cinco seguidos!{w=1}¡Supera eso,{w=0.2} {i}[player]{/i}!.",
                "¡Y con eso hace cinco! {W = 0.75} ¿No te {i}dije{/i} que era buena?",
                "¡Sí!{w=0.75} ¡Son cinco victorias y contando!",
                "Yeah!{w=0.75} ¡Cinco seguidos!{w=0.75} Ehehe."
            ],
            10: [
                "¡Oh, sí!{w=0.75} ¡Diez!{w=0.75} Ahora se lo que significa ser una profesional,{w=0.2} [player]!",
                "Caray...{w=1} ¿Diez victorias?{w=0.75} ¡Hoy estoy {i}imparable{/i}!{w=0.75} Jeje.",
                "¡Ja!{w=0.75} ¡Diez victorias!{w=0.75} ¿Qué opinas de eso,{w=0.2} [player]?",
                "¡Sí!{w=0.75} ¡Diez en fila!{w=0.75} Hombre...{w=1} ¡soy imparable!",
                "Tsk...{w=1} ¿Cuántas van ya?{w=0.75} ¿Diez?¡Al menos {i}intenta{/i} seguirme el ritmo,{w=0.2} [player]!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(natsuki_streak_milestone_map[persistent._jn_blackjack_natsuki_streak]))

    elif persistent._jn_blackjack_player_streak in [3, 5, 10] and jn_blackjack._game_state in [jn_blackjack.JNBlackjackStates.player_blackjack, jn_blackjack.JNBlackjackStates.player_closest, jn_blackjack.JNBlackjackStates.player_exact]:
        $ player_streak_milestone_map = {
            3: [
                "F-{w=0.2}fue suerte,{w=0.2} [player].{w=0.75} ¡Cualquiera puede tener suerte tres veces seguidas!",
                "Sí,{w=0.2} sí.{w=0.75} ¡T-{w=0.2}tres seguidas no son nada de todas formas!",
                "¡A-{w=0.2}apuesto a que no puedes lograr cuatro seguidas,{w=0.2} [player]!",
                "N-{w=0.2}no te emociones demasiado.{w=0.75} ¡Tres seguidas no son nada,{w=0.2} [player]!!",
                "¡P-{w=0.2}perder tres veces seguidas es normal!{w=0.75} ¡Solo estaba calentando!"
            ],
            5: [
                "¡Uuuugh...!{w=0.75} Y-{w=0.2}ya puedes dejar de tener tanta suerte,{w=0.2} [player]!{w=0.75} Qué fastidio...",
                "¿C-{w=0.2}cinco seguidas ahora?{w=0.75} ¡¿Me estás tomando el pelo?!",
                "¿En serio?{w=0.75} ¡¿Con esa son cinco veces seguidas?!{w=0.75} Ugh...",
                "¡Agh-!{w=0.75} ¡N-{w=0.2}no hay forma de que hayas sacado cinco seguidas!{w=0.75} ¡Dame un respiro...",
                "¡T-{w=0.2}tienes que estar bromeando!{w=0.75} ¡¿Cinco veces?!{w=0.75} ¡N-{w=0.2}no hay forma de que esto sea otra cosa que suerte!"
            ],
            10: [
                "¡¿A-{w=0.2}acaso me estás leyendo las cartas o qué?!{w=0.75} ¡¿Diez victorias?!{w=0.75} ¡Qué fastidio...!",
                "¡Oh,{w=0.75} ya {b}basta{/b}!{w=0.75} ¡No hay forma de que hayas ganado diez seguidas!{w=0.75} Ugh...",
                "¡E-{w=0.2}esto ya se está volviendo ridículo!{w=0.75} ¡¿Diez seguidas?!{w=0.75} ¡Juro que estas cartas están arregladas...",
                "¡Bien!{w=0.75} ¡Bien!{w=0.75} Ya entendí...{w=1} ¿ahora puedes dejarme ganar? Qué fastidio...",
                "¡Grrr!{w=0.75} ¡Y-{w=0.2}ya solo pierde de una vez,{w=0.2} [player]!{w=0.75} ¡No me voy a ir sin ganar!"
            ]
        }
        $ chosen_response = renpy.substitute(random.choice(player_streak_milestone_map[persistent._jn_blackjack_player_streak]))
    else:

        $ response_map = {
            jn_blackjack.JNBlackjackStates.draw: [
                "¿Empatamos?{w=0.75} Eh.",
                "Eh.{w=0.75} ¿Empatamos?{w=0.75} Qué extraño.",
                "¿Qué?,{w=0.2} ¿un empate?{w=0.75} Mmm.",
                "¿Un empate?{w=0.75} ¡Qué molesto!",
                "¡Vamos,{w=0.2} [player]...!{w=1} ¡Tienes que perder en algún momento!",
                "Eh.{w=0.75} Otro empate.",
                "¿Otro empate,{w=0.2} en serio?{w=0.75} Esto es extraño."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_bust: [
                "¿Me pasé?{w=0.75} ¡¿Me estás tomando el pelo?!{w=0.75} Ugh...",
                "¡Oh,{w=0.2} vamos!{w=0.75} ¡¿Me pasé {i}otra vez{/i}?!{w=0.75} Qué fastidio...",
                "¡Ay,{w=0.2} no!{w=0.75} ¿{i}Otro{/i} que se pasa?{w=0.75} En serio...",
                "¡N-{w=0.2}no me pasé!{w=0.75} Pff...",
                "¡¿Estás bromeando?!{w=0.75} ¡¿Me pasé otra vez?!",
                "¡{i}Tienes{/i} que estar bromeando!{w=0.75} ¡¿Otra vez?!",
                "¡Vamos,{w=0.5} [n_name]...!{w=1} ¡Concéntrate",
                "¡Uuuugh...!{w=0.75} ¡Sabía que esa fue una jugada tonta!{w=0.75} Agh..."
            ],
            jn_blackjack.JNBlackjackStates.natsuki_blackjack: [
                "¡Sí!{w=0.5} ¡Sí!{w=0.5} ¡Blackjack!{w=0.75} Jejeje.",
                "¡Blackjack!{w=0.5} ¡Blackjack!{w=0.5} Jejeje.",
                "¡Blackjack!{w=0.5} ¡Sí!{w=0.5} ¡{i}Así{/i} es como se Juega",
                "¡Sí!{w=0.5} ¡{i}Esto{/i} me esta gustando!{w=0.75} Jajaja.",
                "¡Observa y aprende,{w=0.2} [player]!{w=0.75} Jaja.",
                "¡Oh, sí!{w=0.75} ¡Blackjack!",
                "¡Blackjack!{w=0.75} ¡Blackjack!{w=0.75} ¡Sí!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_closest: [
                "¡Sí!{w=0.5} ¡Gané!{w=0.3} ¡Gané!{w=0.75} Jejeje.",
                "¡Sí!{w=0.5} ¡Gané otra vez!",
                "¡Mira!{w=0.5} ¡Estabas tan cerca!{w=0.3} ¡Gané!{w=0.3} ¡Gané!",
                "Yes!{w=0.5} Take that,{w=0.2} [player]!{w=0.75} Ehehe.",
                "¡Sí!{w=0.5} ¡En tu cara,{w=0.2} [player]!{w=0.75} Jajaja.",
                "¡Sí!{w=0.75} ¡A {i}esto{/i} es lo que yo llamo ganar!",
                "Jejeje.{w=0.75} ¡Ahora se como se juega,{w=0.2} [player]!"
            ],
            jn_blackjack.JNBlackjackStates.natsuki_exact: [
                "Bueno...{w=0.75} no es un {i}blackjack{/i}...{w=0.75} ¡pero lo tomo de todos modos!",
                "Jejeje.{w=0.75} ¡Una victoria es una victoria,{w=0.2} [player]!",
                "¡Ya verás,{w=0.2} [player]!{w=0.75} ¡Mi próxima victoria será un {i}blackjack{/i}!",
                "Jeje.{w=0.75} No importa,{w=0.2} [player],{w=0.2} ¡la victoria es mía!",
                "¿Q-{w=0.2}quién dice que necesitas un blackjack para ser un profesional?{w=0.75} Jejeje.",
                "¡O-{w=0.2}oye!{w=0.75} ¡Sigue siendo veintiuno,{w=0.2} te guste o no!",
                "Jejeje.{w=0.75} ¡Sigue siendo veintiuno,{w=0.2} [player]"
            ],
            jn_blackjack.JNBlackjackStates.player_bust: [
                "¡Pfff!{w=0.75} ¡Qué bien te pasaste,{w=0.2} [player]!{w=0.75} Jejeje.",
                "Sí.{w=0.5} ¡Totalmente, mal jugado,{w=0.2} [player]!",
                "¡A eso le llamo pasarse!{w=0.75} Jejeje.",
                "Jajaja.{w=0.75} ¡Qué mala suerte,{w=0.2} [player]!",
                "¡Pffft!{w=0.75} ¿Estás {i}seguro{/i} de que sabes jugar,{w=0.2} [player]?",
                "¡{i}Qué{/i} jugada más fluida,{w=0.2} [player]!{w=0.75} Jejeje.",
                "Oye,{w=0.2} [player],{w=0.5} ¡se supone que debes contar las cartas!{w=0.75} Jejeje."
            ],
            jn_blackjack.JNBlackjackStates.player_blackjack: [
                "¿En serio?{w=0.75} ¡¿Sacaste un blackjack?!{w=0.75} Ugh...",
                "Sí,{w=0.2} sí.{w=0.75} Disfruta tu suerte mientras dure,{w=0.2} [player].",
                "Hmph.{w=0.75} Solo tuviste suerte esta vez.",
                "¡Ay,{w=0.2} por {i}favor{/i}!{w=0.75} ¿Otra vez?{w=0.75} En serio...",
                "¡E-{w=0.2}eso fue pura suerte!{w=0.75} Ugh...",
                "¡E-{w=0.2}eso fue solo casualidad!{w=0.75} Vamos...",
                "Ugh...{w=1} ¿De verdad?{w=0.75} ¿Sacaste otro blackjack?"
            ],
            jn_blackjack.JNBlackjackStates.player_closest: [
                "Je.{w=0.75} Disfruta la suerte mientras dure,{w=0.2} [player].",
                "¿{i}En serio{/i}?{w=0.75} Ugh...",
                "¡Vamos!{w=0.75} ¿De verdad?{w=0.75} Vaya...",
                "Sí,{w=0.2} sí.{w=0.75} Ríete todo lo que quieras,{w=0.2} [player].{w=0.75} Ya verás...",
                "Hmph.{w=1} Tuviste suerte,{w=0.2} [player].{w=0.75} Es todo lo que diré.",
                "¡Uuuuugh!{w=0.75} ¡Te tocó una mano mucho mejor!{w=0.75} Ugh...",
                "S-{w=0.2}solo tuviste suerte esta vez,{w=0.2} [player].{w=0.75} Eso es todo."
            ],
            jn_blackjack.JNBlackjackStates.player_exact: [
                "Je.{w=0.75} ¡Qué mal que no fue un blackjack,{w=0.2} [player]!",
                "¡Nnnnn-!{w=0.75} A-{w=0.2}al menos no sacaste un blackjack.",
                "Sí,{w=0.2} sí,{w=0.2} como sea.{w=0.75} Tuviste suerte,{w=0.2} [player].",
                "¡G-{w=0.2}golpe de suerte!{w=0.75} Ahora intenta hacer {i}realmente{/i} un blackjack...",
                "¡C-{w=0.2}como si {i}esa{/i} mano pudiera ganar!{w=0.75} Ugh...",
                "¡¿Me estás tomando el pelo?!{w=0.75} ¡¿Ganaste con eso?!{w=0.75} Vaya...",
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
        n 1tnmpueqm "Eh?{w=0.75}{nw}"
        extend 2tnmsleqm " You're done playing,{w=0.2} [player]?"

        if jn_blackjack._rounds == 0:
            n 4ccsflsbr "...W-{w=0.2}wait.{w=0.75}{nw}"
            extend 3fcsgssbr " Hang on just a second here,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3fnmgs " What do you mean?"
            n 4fcswr "We literally only just started {i}playing{/i}!{w=0.75}{nw}"
            extend 2flrem " Jeez..."
            n 2csqcasbl "You better not be pulling my leg again,{w=0.2} [player]."

            $ natsuki_prompt = "Do you actually {i}want{/i} to play blackjack or not?"
            show natsuki option_wait_sulky

        elif jn_blackjack._rounds < 6:
            n 1kslfl "Man...{w=1}{nw}"
            extend 4cnmem " really?{w=0.75}{nw}"
            extend 4ccsgssbl " Come on,{w=0.2} [player]!{w=0.75}{nw}"
            extend 3ccsposbl " You can't be done this soon {i}already{/i}."
            n 3flrflsbr "Seriously -{w=0.5}{nw}"
            extend 3tnmfl " it's only been like [jn_blackjack._rounds] rounds!{w=0.75}{nw}"
            extend 4cnmaj " We've barely even started!"

            $ natsuki_prompt = "You can {i}easily{/i} play at least a couple more games...{w=0.5} right?"
            show natsuki option_wait_sulky
        else:

            n 2tdrsl "..."
            n 2tdrfl "Well...{w=1}{nw}"
            extend 2tlrbo " you have been playing a while.{w=0.75}{nw}"
            extend 4csrpo " I {i}guess{/i}."
            n 2nsqca "...Even if you {i}are{/i} calling it quits right in the middle of a game."
            n 2nllaj "So..."

            $ natsuki_prompt = "You're sure you don't wanna keep playing,{w=0.2} [player]?"
            show natsuki option_wait_curious
    else:

        n 4ccsss "Oh?{w=0.75}{nw}"
        extend 4fllss " What's this,{w=0.2} [player]?{w=0.75}{nw}"
        extend 3fsqbg " Why the cold feet all of a sudden?"
        n 1fsqsm "Ehehe."
        n 2fnmbg "Come on!{w=0.75}{nw}"
        extend 2fcsbs " Don't tell me you're giving up {i}that{/i} easily!"

        $ natsuki_prompt = "You can at {i}least{/i} stick it out to the end of this one,{w=0.2} right?"
        show natsuki option_wait_smug

    $ natsuki_prompt = renpy.substitute(natsuki_prompt)

    menu:
        n "[natsuki_prompt]"
        "No, I'm done playing for now.":
            if jn_blackjack._is_player_committed:
                n 1kcsflesi "...Man.{w=0.75}{nw}"
                extend 4ksqfl " For real,{w=0.2} [player]?"
                n 2cslbo "..."
                n 2nslaj "Well...{w=1}{nw}"
                extend 5cdrca " I can't say I'm not at least a little disappointed.{w=0.75}{nw}"
                extend 5nlraj " But I guess that's fine."
                n 4ccsss "After all..."

                $ dialogue_choice = random.randint(1, 3)
                if dialogue_choice == 1:
                    n 3fcsbg "Just means another win for me!{w=0.75}{nw}"

                elif dialogue_choice == 2:
                    n 3fcssmesm "As if I'm turning down an easy win!{w=0.75}{nw}"
                else:

                    n 3nchgn "That's still a win for me!{w=0.75}{nw}"

                extend 3fcssmeme " Ehehe."
            else:

                n 1nsqpu "...Wow.{w=0.75}{nw}"
                extend 4tnmfl " And you didn't even end up making a single move that round!{w=0.75}{nw}"
                extend 4tlrbo " Huh."
                n 2tlrsl "..."
                n 2ulrfl "Well.{w=0.75}{nw}"
                extend 2fcsss " Looks like {i}you{/i} know what they say at least,{w=0.5}{nw}"
                extend 2fsqbg " [player]."
                n 6fcsbs "Guess the only winning move for you was not to play!{w=0.75}{nw}"
                extend 7fchsmeme " Ehehe."

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
        "You're on!":

            if not jn_blackjack._is_player_committed:
                n 4fcsbgsbr "Y-{w=0.2}yeah!{w=0.75}{nw}"
                extend 2fcsbssbr " Now that's more like it!{w=0.75}{nw}"
                extend 2fsqbg " Some fighting spirit!"
                n 4fnmgsedz "Bring it on already,{w=0.2} [player]!"

            elif jn_blackjack._rounds == 0:
                n 1fspgs "Yeah!{w=0.75}{nw}"
                extend 3fcsbg " See?{w=0.75}{nw}"
                extend 3fchgn " I knew you had some kind of fight left in you!"
                n 1ccsbg "Besides..."
                n 2fsqbg "Only a real sore loser would just chicken out before they've even {i}lost{/i}.{w=0.75}{nw}"
                extend 2fsqsm " Ehehe."
                n 4fnmbs "Prove me wrong,{w=0.2} [player]!"
            else:

                n 1fsqsm "Ehehe.{w=0.75}{nw}"
                extend 3fcsbs " Now {i}that's{/i} what I'm talking about!"
                n 3fnmsm "..."
                n 3fsqbg "Well?{w=0.75}{nw}"
                extend 4fcsbg " What're you waiting for?"
                n 4fchgn "Make your move already,{w=0.2} [player]!"

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
            text "Turno: {0}".format(jn_blackjack._getCurrentTurnLabel()) style "blackjack_note_text"

        null height 120


        style_prefix "hkb"


        key "1" action [
            If(jn_blackjack._is_player_turn and jn_blackjack._controls_enabled and len(jn_blackjack._player_hand) < 5, Function(jn_blackjack._stayOrHit, True, True)) 
        ]
        textbutton _("¡Apostar!"):
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
