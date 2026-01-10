default persistent.affinity = 25.0
default persistent.affinity_daily_gain = 5
default persistent.affinity_gain_reset_date = None
default persistent._affinity_daily_bypasses = 5

init -2 python in jn_affinity:
    import store
    import store.jn_utils as jn_utils
    import random


    AFF_THRESHOLD_LOVE = 1000
    AFF_THRESHOLD_ENAMORED = 500
    AFF_THRESHOLD_AFFECTIONATE = 250
    AFF_THRESHOLD_HAPPY = 100
    AFF_THRESHOLD_NORMAL = 0
    AFF_THRESHOLD_UPSET = -25
    AFF_THRESHOLD_DISTRESSED = -50
    AFF_THRESHOLD_BROKEN = -100
    AFF_THRESHOLD_RUINED = -125











    RUINED = 1
    BROKEN = 2
    DISTRESSED = 3
    UPSET = 4
    NORMAL = 5
    HAPPY = 6
    AFFECTIONATE = 7
    ENAMORED = 8
    LOVE = 9

    _AFF_STATE_ORDER = [
        RUINED,
        BROKEN,
        DISTRESSED,
        UPSET,
        NORMAL,
        HAPPY,
        AFFECTIONATE,
        ENAMORED,
        LOVE
    ]

    def getRelationshipLengthMultiplier():
        """
        Gets the multiplier for affinity changes, based on the length of the relationship in months.

        OUT:
            - relationship multiplier value, capped at 1.75
        """
        relationship_length_multiplier = 1 + (jn_utils.get_total_gameplay_months() / 10)
        return relationship_length_multiplier if relationship_length_multiplier <= 1.75 else 1.75

    def _isAffStateValid(state):
        """
        Checks if the given state is valid.

        IN:
            state - the integer representing the state we wish to check is valid

        OUT:
            True if valid state otherwise False
        """
        return (
            state in _AFF_STATE_ORDER
            or state is None
        )

    def _compareAffThresholds(value, threshold):
        """
        Generic compareto function for values
        """
        return value - threshold

    def _compareAffinityStates(state_1, state_2):
        """
        Internal compareto function which compares two affinity states

        IN:
            state_1 - the first state
            state_2 - the second state

        OUT:
            integer:
                -1 if state_1 is less than state_2
                0 if either state is invalid or both states are the same
                1 if state_1 is greater than state_2
        """
        if state_1 == state_2:
            return 0
        
        if not _isAffStateValid(state_1) or not _isAffStateValid(state_2):
            return 0
        
        
        if _AFF_STATE_ORDER.index(state_1) < _AFF_STATE_ORDER.index(state_2):
            return -1
        
        
        return 1

    def _isAffRangeValid(affinity_range):
        """
        Checks if the given affinity range is valid

        IN:
            affinity_range - The affintiy_range structure used in Topics (a tuple of the format):
                [0] - low bound (Can be None)
                [1] - high bound (Can be None)

        OUT:
            True if affinity_range is valid, False if not
        """
        if affinity_range is None:
            return True
        
        
        low_bound, high_bound = affinity_range
        
        
        if low_bound is None and high_bound is None:
            return True
        
        
        if (
            not _isAffStateValid(low_bound)
            or not _isAffStateValid(high_bound)
        ):
            return False
        
        
        if low_bound is None or high_bound is None:
            return True
        
        
        return _compareAffinityStates(low_bound, high_bound) <= 0

    def _isAffStateWithinRange(affinity_state, affinity_range):
        """
        Checks if the given affinity_state is within the given affinity_range

        IN:
            affinity_state - the state value to check if is within the affinity_range
                (NOTE: The affinity_range is considered INCLUSIVE)
            affinity_range - a tuple of the form:
                [0] - low_bound
                [1] - high_bound
        """
        
        if affinity_state is None or not _isAffStateValid(affinity_state):
            return False
        
        
        if affinity_range is None:
            return True
        
        
        low_bound, high_bound = affinity_range
        
        
        if low_bound is None and high_bound is None:
            return True
        
        
        
        if low_bound is None:
            
            return _compareAffinityStates(affinity_state, high_bound) <= 0
        
        if high_bound is None:
            
            return _compareAffinityStates(affinity_state, low_bound) >= 0
        
        
        if low_bound == high_bound:
            return affinity_state == low_bound
        
        
        return (
            _compareAffinityStates(affinity_state, low_bound) >= 0
            and _compareAffinityStates(affinity_state, high_bound) <= 0
        )

#⚠: —Pass