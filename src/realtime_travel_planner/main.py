#!/usr/bin/env python
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from realtime_travel_planner.crew import ResearchCrew  # Import from the correct module

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew with user-defined inputs.
    """
    # Gather user inputs
    travel_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    num_days = input("Enter the number of days for the trip: ").strip()
    location = input("Enter the travel location: ").strip()
    preferred_food = input("Enter your preferred cuisine or food type: ").strip()
    budget = input("Enter your budget (e.g., in USD): ").strip()

    # Prepare inputs with new keys for itinerary-specific information.
    inputs = {
        'date': travel_date,
        'days': num_days,
        'location': location,
        'preferred_food': preferred_food,
        'budget': budget
    }

    # Create and run the research crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the final report
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()
