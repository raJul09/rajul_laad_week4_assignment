import csv

def calculate_average_grades(input_csv, output_csv):
    try:
        with open(input_csv, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            with open(output_csv, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(["Student Name", "Average Grade"])
                
                for row in reader:
                    student_name = row[0]
                    try:
                        grades = list(map(float, row[1:]))
                        average_grade = sum(grades) / len(grades)
                    except ValueError:
                        print(f"Invalid grade found for {student_name}. Skipping.")
                        continue
                    
                    writer.writerow([student_name, round(average_grade, 2)])
        
        print(f"Average grades written to {output_csv}")
    except FileNotFoundError:
        print(f"Error: {input_csv} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage example
calculate_average_grades("grades.csv", "averages.csv")
