import os
import sys
import json
import re

def convert_to_ipynb(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    cells = []
    
    current_block_type = None
    current_lines = []
    
    def add_cell():
        nonlocal current_block_type, current_lines
        if not current_lines:
            current_block_type = None
            return
            
        if current_block_type == "code":
            while current_lines and current_lines[-1].strip() == "":
                current_lines.pop()
        
        if not current_lines:
            current_block_type = None
            return
            
        if current_block_type == "markdown":
            md_lines = []
            for line in current_lines:
                if line.startswith("# "):
                    md_lines.append(line[2:])
                elif line.startswith("#"):
                    md_lines.append(line[1:])
                else:
                    md_lines.append(line)
            if md_lines:
                md_lines[-1] = md_lines[-1].rstrip('\r\n')
                
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": md_lines
            })
        else:
            if current_lines:
                current_lines[-1] = current_lines[-1].rstrip('\r\n')
                
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": current_lines
            })
        
        current_lines = []
        current_block_type = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped.startswith("#"):
            comment_block = []
            j = i
            is_md_block = False
            while j < len(lines) and lines[j].strip().startswith("#"):
                cmt_line = lines[j].strip()
                comment_block.append(lines[j])
                # Check for patterns that indicate a markdown block (headers, tasks, etc)
                if (re.match(r'^#\s*-{3,}', cmt_line) or 
                    re.match(r'^#\s*\d+\.', cmt_line) or 
                    re.match(r'^#\s*TASK\s*\d+', cmt_line, re.IGNORECASE) or 
                    re.match(r'^#\s*⭐', cmt_line) or
                    re.match(r'^#\s*DAY\s*\d+', cmt_line, re.IGNORECASE) or
                    re.match(r'^#\s*HOMEWORK\s*\d+', cmt_line, re.IGNORECASE)):
                    is_md_block = True
                j += 1
                
            if is_md_block:
                add_cell() # push any pending code cell
                current_block_type = "markdown"
                current_lines.extend(comment_block)
                add_cell() # push this markdown cell
                i = j
                continue
            else:
                # Regular comment logic
                if current_block_type != "code":
                    add_cell()
                    current_block_type = "code"
                current_lines.append(line)
        else:
            if stripped == "":
                if current_block_type is not None:
                    current_lines.append(line)
            else:
                if current_block_type != "code":
                    add_cell()
                    current_block_type = "code"
                current_lines.append(line)
        i += 1

    add_cell()
    
    notebook = {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }
    
    out_filepath = filepath[:-3] + ".ipynb"
    with open(out_filepath, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1)
        
    os.remove(filepath)
    print(f"Converted {os.path.basename(filepath)} -> {os.path.basename(out_filepath)}")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    
    print(f"Scanning directory: {directory}")
    converted_count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename != os.path.basename(__file__):
            filepath = os.path.join(directory, filename)
            convert_to_ipynb(filepath)
            converted_count += 1
            
    if converted_count == 0:
        print("No .py files found to convert.")
    else:
        print(f"Successfully converted {converted_count} files into intelligent notebooks!")
