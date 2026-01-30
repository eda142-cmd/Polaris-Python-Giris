from datetime import datetime

def main():
    exam_input = input("Enter exam date/time (DD.MM.YYYY HH:MM): ")
    try:
        exam_date = datetime.strptime(exam_input, "%d.%m.%Y %H:%M")
        now = datetime.now()
        
        time_left = exam_date - now
        
        if time_left.total_seconds() < 0:
            print("The exam has already passed! ")
        else:
            days = time_left.days
            hours = time_left.seconds // 3600
            print(f"Time remaining: {days} days and {hours} hours. Good luck! ")
            
    except ValueError:
        print("Wrong format! Please use: 15.11.2025 09:30")

if __name__ == "__main__":
    main()
