import os
from agents import Agent, Runner
from dotenv import load_dotenv
from travel_tools import get_flights, suggest_hotels

load_dotenv()

destination_agent = Agent(
    name = "Destination Agent",
    instructions = "You recommend travel destinations based on user's mood."
)
booking_agent = Agent(
    name = "Booking Agent",
    instructions = "You give flight and hotel info using tools.",
    tools = [
        get_flights, suggest_hotels
    ] 
)
explore_agent = Agent(
    name = "Explore Agent",
    instructions = "You suggest food & places to explore in the destination."
)


def main():
    print("\nAI Travel Designer!\n")
    mood = input("What's your travel mood (Relaxing/Adventure/etc.): ")

    result1 = Runner.run_sync(destination_agent, mood)
    dest = result1.final_output.strip()
    print("\nDestination Suggest: ", dest)
    
    result2 = Runner.run_sync(booking_agent, dest)
    print("\nBooking Info: ", result2.final_output)

    result3 = Runner.run_sync(explore_agent, dest)
    print("\nExplore Tips: ", result3.final_output)


if __name__ == "__main__":
    main()
