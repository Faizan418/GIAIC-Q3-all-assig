import os
from agents import Agent, Runner
from dotenv import load_dotenv
from game_tools import roll_dice, generate_event

load_dotenv()

narrator_agent = Agent(
    name = "Narrator Agent",
    instructions = "You narrate the adventure. Ask the player for choise."
)
monster_agent = Agent(
    name = "Monster Agent",
    instructions = "You handle monster encounters using roll_dice and generate_event.",
    tools = [
        roll_dice, generate_event
    ]
)
item_agent = Agent(
    name = "Item Agent",
    instructions = "You provide rewards or items to the played."
)

def main():
    print("\n Welcome to Fantasy Game!")
    choice = input("Do you enter the forest or turn back: ")

    result1 = Runner.run_sync(narrator_agent, choice)
    print("\n Story:", result1.final_output)

    result2 = Runner.run_sync(monster_agent, "Start Encounter")
    print("\n Encounter:", result2.final_output)

    result3 = Runner.run_sync(item_agent, "Give Reward")
    print("\n Reward:", result3.final_output)
    
if __name__ == "__main__":
    main()
