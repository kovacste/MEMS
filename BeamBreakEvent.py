class BeamBreakEvent:

    def __init__(self, time, description, status):
        self.event_time = time
        self.event_description = description
        self.beam_is_broken = status
