from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os

@CrewBase
class ResearchCrew():
    """Research crew for comprehensive travel planning"""

    @agent
    def local_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['local_analyst'],
            verbose=True
        )

    @agent
    def budget_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_planner'],
            verbose=True
        )

    @agent
    def news_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['news_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def analysis_task_budget(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task_budget'],
            output_file='output/budget_travel_plan.md'
        )

    @task
    def analysis_task_news(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task_news'],
            output_file='output/news_travel_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the travel planning crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
