
log_file = '2ndDec.log'


error_counts = {}
warning_counts = {}

with open(log_file, 'r') as f:
    for line in f:
        line = line.strip()  
        if line.startswith('ERROR:'):
            
            error_message = line.split('ERROR:')[1].strip()
            
            if error_message in error_counts:
                error_counts[error_message] += 1
            else:
                error_counts[error_message] = 1
        
        if line.startswith("WARNING:"):

            warning_message = line.split('WARNING:')[1].strip()

            if warning_message in warning_counts:
                warning_counts[warning_message] +=1
            else:
                warning_counts[warning_message] = 1


print("Error Summary:")
for error, count in error_counts.items():
    print(f"{error}: {count}")

print("\n\nWarning Summary:")
for warning , count in warning_counts.items():
    print(f"{warning}: {count}")
