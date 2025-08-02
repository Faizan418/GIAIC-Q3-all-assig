from dotenv import load_dotenv
from roadmap_tool import get_career_roadmap
from agents import Agent, Runner

load_dotenv()

career_agent = Agent(
    name = "Career Agent",
    instructions = "You ask interests and suggest a career field."
)
skill_agent = Agent(
    name = "Skill Agent",
    instructions = "You share the roadmap using the get_cureer_roadmap tool.",
    tools = [get_career_roadmap]
)
job_agent = Agent(
    name = "Job Agent",
    instructions = "You suggest job titles in the chosen career."
)

def main():
    print("\nCareer Monter Agent\n")
    interest = input("What are your interest: ")

    result1 = Runner.run_sync(career_agent, interest)
    field = result1.final_output.strip()
    print("\nSuggested Career: ", field)

    result2 = Runner.run_sync(skill_agent, field)
    print("\nRequired skills: ", result2.final_output)

    result3 = Runner.run_sync(job_agent, field)
    print("\nPossible Jobs: ", result3.final_output)


if __name__ == "__main__":
    main()

