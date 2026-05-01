import os
import sys
import re

def segment_homework(filepath):
    """
    Script: python segment.py path/to/directory
    Add cell markers (#%%) before each task in a homework file.
    Tasks are identified by patterns like:
    - # TASK n:
    - # ⭐ BONUS
    - Task-like comments
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    segmented_lines = []
    i = 0
    
    # Pattern to detect task markers
    task_patterns = [
        r'^#\s*TASK\s+\d+',           # # TASK 1:, # TASK 2:, etc.
        r'^#\s*SECTION\s+\d+',        # # SECTION 1:, # SECTION 2:, etc.
        r'^#\s*TOPIC\s+\d+',          # # TOPIC 1:, # TOPIC 2:, etc.
        r'^#\s*⭐\s*',                # # ⭐ BONUS, # ⭐ CHALLENGE
        r'^#\s*BONUS\s*',            # # BONUS CHALLENGE
        r'^#\s*DAY\s+\d+',            # # DAY 1:, # DAY 2:, etc.
    ]
    
    # Check if line is a task marker
    def is_task_marker(line):
        stripped = line.strip()
        for pattern in task_patterns:
            if re.match(pattern, stripped):
                return True
        return False
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a task marker line
        if is_task_marker(line):
            # Check if there's already a #%% on the previous line
            if segmented_lines and segmented_lines[-1].strip() == "#%%":
                # Already has a cell marker, just add the line
                segmented_lines.append(line)
            else:
                # Add cell marker before this line
                segmented_lines.append("#%%\n")
                segmented_lines.append(line)
        else:
            segmented_lines.append(line)
        
        i += 1
    
    # Write back to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(segmented_lines)
    
    print(f"✅ Segmented: {os.path.basename(filepath)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        # Check if it's a directory
        if os.path.isdir(target):
            directory = target
            print(f"📂 Scanning directory: {directory}")
            
            converted_count = 0
            script_name = os.path.basename(__file__)
            for filename in sorted(os.listdir(directory)):
                if filename.endswith(".py") and filename != script_name:
                    filepath = os.path.join(directory, filename)
                    segment_homework(filepath)
                    converted_count += 1
            
            if converted_count == 0:
                print("❌ No .py files found in the directory.")
            else:
                print(f"✅ Successfully segmented {converted_count} file(s)!")
        # Check if it's a file
        elif os.path.isfile(target):
            segment_homework(target)
        else:
            print(f"❌ Path not found: {target}")
    else:
        # Scan current directory for homework files
        directory = os.getcwd()
        print(f"📂 Scanning directory: {directory}")
        
        converted_count = 0
        script_name = os.path.basename(__file__)
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".py") and filename != script_name:
                filepath = os.path.join(directory, filename)
                segment_homework(filepath)
                converted_count += 1
        
        if converted_count == 0:
            print("❌ No .py files found.")
        else:
            print(f"✅ Successfully segmented {converted_count} file(s)!")
