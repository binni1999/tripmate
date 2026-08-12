from tools.flight_tool import search_flights
from backend import run_travel_agent


user_input = input('Enter travel requests: ')

response = run_travel_agent(
    user_input = user_input,
    thread_id = "test_user"
)

print("\n FInal Response : \n")
print(response["answer"])