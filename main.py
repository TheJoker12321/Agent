from classes.agent import Agent
from classes.mission import Mission
from classes.inteltools import IntelTools
from classes.mission_control import MissionControl
from classes.report import Report


unit_8200 = Agent("8200",4)
repo = Report("Idan",4)
MissionControl.analyze_report(repo)
msg = IntelTools.encrypt_message("hello")
IntelTools.log_transmission(unit_8200.code_name,msg)

