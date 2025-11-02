class Mission:
    def __init__(self, mission_name : str, target_location : str, assigned_agent = None):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def assign(self, agent):
        self.assigned_agent = agent

    def method_brief(self):
        print(f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}")


