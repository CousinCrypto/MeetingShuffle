import pandas as pd
import random
import itertools

# Define the list of possible start times and convert them to minutes
possible_start_times = ['09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45',
                        '12:00', '12:15', '12:30', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45',
                        '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30']

def time_to_minutes(time_str):
    """Converts a time string to minutes since 9:00."""
    hours, minutes = map(int, time_str.split(':'))
    return (hours - 9) * 60 + minutes

start_times_in_minutes = [time_to_minutes(time) for time in possible_start_times]


# Define the list of people
people = ['Odin','John','Jim','Bill']
# Combine the initial meetings with the additional random meetings
meetings = [{'summary': 'Test moveable', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 0}, {'summary': 'Trial test calendar', 'participants': ['Odin','John'], 'type': 'Google Meet', 'duration': 60, 'start_time': 60}, {'summary': '15 mino', 'participants': ['Odin','Ellie'], 'type': 'Google Meet', 'duration': 15, 'start_time': 120}, {'summary': 'Another 15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 150}, {'summary': 'First OOO Test', 'participants': ['Odin'], 'type': 'outOfOffice', 'duration': 60, 'start_time': 360}]

    

def assign_meeting_times(meetings, start_times):
    """Assigns random start times to meetings ensuring no overlap for each participant."""
    assigned_meetings = []

    for meeting in meetings:
        possible_times = start_times.copy()
        for participant in meeting['participants']:
            # Remove times that would cause overlap with this participant's other meetings
            for m in assigned_meetings:
                if participant in m['participants']:
                    start = m['start_time']
                    end = start + m['duration']
                    possible_times = [t for t in possible_times if not (start <= t < end or t <= start < t + meeting['duration'])]

        if possible_times:
            meeting['start_time'] = random.choice(possible_times)
            assigned_meetings.append(meeting)

    return assigned_meetings  # Ensure this function returns the list of meetings


        



def calculate_combined_total_spare_time(assigned_meetings, people):
    """Calculates and returns the combined total spare time for all people."""
    combined_total_spare_time = 0

    for person in people:
        person_meetings = sorted(
            [m for m in assigned_meetings if person in m['participants']], 
            key=lambda m: m['start_time']
        )

        last_end_time = None
        for meeting in person_meetings:
            start_time = meeting['start_time']
            duration = meeting['duration']
            end_time = start_time + duration

            if last_end_time is not None:
                spare_time = start_time - last_end_time
                combined_total_spare_time += spare_time

            last_end_time = end_time

    return combined_total_spare_time  # Return the total spare time



best_schedule = None
min_spare_time = float('inf')
count = 0
best_schedules = []


for _ in range(10000):
    assigned_meetings = assign_meeting_times(meetings, start_times_in_minutes)
    total_spare_time = calculate_combined_total_spare_time(assigned_meetings, people)


    if total_spare_time < min_spare_time:
        min_spare_time = total_spare_time
        best_schedule = assigned_meetings
        best_schedules.append(best_schedule)
        print("Best time:", min_spare_time)
        print("Best Schedule:", best_schedule)


# Print the last best schedule and minimum spare time after the loop
if best_schedules:
    last_best_schedule = best_schedules[-1]
    print("Proper Best time:", min_spare_time)
    print("Proper Best Schedule:", last_best_schedule)



all_schedules = last_best_schedule
   

def time_to_minutes(time_str):
    """Converts a time string to minutes since 9:00."""
    hours, minutes = map(int, time_str.split(':'))
    return (hours - 9) * 60 + minutes

start_times_in_minutes = [time_to_minutes(time) for time in possible_start_times]


def format_meetings_for_all(people, meetings):
    """Formats the meeting schedule for all people."""
    all_schedules = {person: [] for person in people}
    for meeting in meetings:
        for person in people:
            if 'participants' in meeting and person in meeting['participants']:
                if 'start_time' in meeting and 'duration' in meeting and 'summary' in meeting:  # Check for 'summary'
                    formatted_meeting = {
                        'start_time': meeting['start_time'],
                        'duration': meeting['duration'],
                        'summary': meeting['summary']  # Include the 'summary' key
                    }
                    all_schedules[person].append(formatted_meeting)
    return all_schedules




# Extract and format meetings for all people
all_people_meetings = format_meetings_for_all(people, meetings)
all_people_meetings


# Create a list of time slots from 0 to the end of the workday, assuming 15-minute intervals
time_slots = list(range(0, 18 * 60, 15))  # 18 hours * 60 minutes, with 15-minute intervals

# Initialize a DataFrame
schedule_spreadsheet = pd.DataFrame(index=time_slots, columns=people)

# Fill the DataFrame
for person, meetings in all_people_meetings.items():  # Replace 'all_people_meetings' with your actual data
    for meeting in meetings:
        start_time = meeting['start_time']
        end_time = start_time + meeting['duration']
        for time in range(start_time, end_time, 15):
            if time in schedule_spreadsheet.index:
                schedule_spreadsheet.at[time, person] = meeting['summary']  # Include 'summary' in the cell

# Replace NaN with empty strings for better readability
schedule_spreadsheet.fillna('', inplace=True)

# Save DataFrame to a CSV file
csv_file = 'best_schedule.csv'
schedule_spreadsheet.to_csv(csv_file, index_label='Time')

# Print a message indicating the CSV file has been saved
print(f'CSV file "{csv_file}" has been saved in your local directory.')




   
