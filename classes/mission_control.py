from classes.report import Report


class MissionControl:
    @staticmethod
    def analyze_report(r: Report):
        if r.urgency_level >= 4:
            print("Immediate response required.")
        elif r.urgency_level == 3:
            print("high priority. Monitor closely.")
        else:
            print("Routine analysis")