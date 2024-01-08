# MeetingShuffle


From a List of people and a List of Current Meetings
It should try 10,000 random meeting orders/times
and pick the ones with the best time.

ive got it currently outputting the ones which have less "wasted time" inbetween meetings
it outputs about 5 before it cant find a better order
the best one is where Best time: 0

which is the last output of the "Best time" lot 
I then try to get it to only print the last best time and associated Best Schedule but it picks a random Schedule.
Example below the Proper Best Schedule should be the Best Schedule where Best time is 0:



Best time: 15
Best Schedule: [{'summary': 'Test moveable', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 210}, {'summary': 'Trial test calendar', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 30}, {'summary': '15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 330}, {'summary': 'Another 15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 315}, {'summary': 'First OOO Test', 'participants': ['Odin'], 'type': 'outOfOffice', 'duration': 60, 'start_time': 135}]

Best time: 0
Best Schedule: [{'summary': 'Test moveable', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 45}, {'summary': 'Trial test calendar', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 195}, {'summary': '15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 165}, {'summary': 'Another 15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 180}, {'summary': 'First OOO Test', 'participants': ['Odin'], 'type': 'outOfOffice', 'duration': 60, 'start_time': 105}]

Proper Best time: 0
Proper Best Schedule: [{'summary': 'Test moveable', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 210}, {'summary': 'Trial test calendar', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 60, 'start_time': 30}, {'summary': '15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 330}, {'summary': 'Another 15 mino', 'participants': ['Odin'], 'type': 'Google Meet', 'duration': 15, 'start_time': 315}, {'summary': 'First OOO Test', 'participants': ['Odin'], 'type': 'outOfOffice', 'duration': 60, 'start_time': 135}]
CSV file "best_schedule.csv" has been saved in your local directory.
