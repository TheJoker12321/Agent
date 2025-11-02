from classes.agent import Agent


class Report:
    def __init__(self, summary, urgency_level):
        self.summary = summary
        self.urgency_level = urgency_level
        self.submitted_by = Agent("Idan",4)
