from agents.planner import PlannerAgent
from agents.analyst import AnalystAgent
from agents.executor import ExecutorAgent

planner = PlannerAgent()
analyst = AnalystAgent()
executor = ExecutorAgent()


class Workflow:

    def run(self, task: str):

        plan = planner.run(task)

        analysis = analyst.analyze(plan)

        execution = executor.execute(analysis)

        return {
            "task": task,
            "plan": plan,
            "analysis": analysis,
            "execution": execution
        }
