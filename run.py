'''
    DS2500
    Spring 2021
    OOP Lab - Run class

'''

class Run:
    ''' Class to represent a run.
        Attributes: distance (float), mins (int), secs (int), pace (tuple)
        Methods: constructor is given.
        TODO: Create compute_pace method.
    '''
    def __init__(self, dist, mins, secs):
        self.dist = dist
        self.mins = float(mins)
        self.secs = float(secs)
        self.pace = self.compute_pace()

    def compute_pace(self):
        total_secs = (self.mins * 60) + self.secs
        pace = total_secs / self.dist
        pace_mins = pace // 60
        pace_secs = pace - (pace_mins * 60)
        return (pace_mins, pace_secs)

    def to_dict(self):
        run_dict = {'dist': self.dist, 'mins': self.mins, 'secs': self.secs, 'pace min': self.pace[0], 'pace sec': self.pace[1]}
        return run_dict
