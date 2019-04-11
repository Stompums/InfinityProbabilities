class Judge:

    def __init__(self, *args):
        self.models = args


    @staticmethod
    def roll_result(rolls, attribute):
        roll_types = {'Successes': [],
                      'Crits': 0}
        if attribute > 20:
            for i in range(len(rolls)):
                rolls[i] += attribute - 20
        for roll in rolls:
            if roll == attribute or roll > 20:
                roll_types['Crits'] += 1
            elif roll < attribute:
                roll_types['Successes'].append(roll)
        roll_types['Successes'].sort()
        return roll_types

    @staticmethod
    def contested_results(a_roll_results, b_roll_results):
        """

        :rtype: Int
        """
        a_crits = a_roll_results.roll_types['Crit']
        b_crits = b_roll_results.roll_types['Crit']
        a_successes = a_roll_results.roll_types['Successes']
        b_successes = b_roll_results.roll_types['Successes']
        if a_crits != 0 or b_crits != 0:
            if a_crits != 0 and b_crits != 0:
                return 0
            elif a_crits != 0:
                return a_crits
            else:
                return -b_crits
        elif max(a_successes) > max(b_successes):
            return sum(i > max(b_successes) for i in a_successes)
        elif max(b_successes) > max(a_successes):
            return -sum(i > max(a_successes) for i in b_successes)
        else:
            return 0

