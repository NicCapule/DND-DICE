import random
import datetime

def choice_conversion(choice_str):
    """Converts a dice string like 'D20' to an integer."""
    return int(choice_str.replace("D", ""))

def roll_die(choice_str):
    """Roll the dice and return the result."""
    die = choice_conversion(choice_str)
    result = random.randint(1, die)
    return die, result

def format_log_entry(die, result):
    """Format log entry with timestamp."""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%I:%M:%S %p")
    return f"{formatted_time}: Rolled a D{die}: {result}\n"
