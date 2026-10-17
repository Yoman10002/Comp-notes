# ==========================================
# PYTHON SCRIPT TEMPLATE WITH STEP-BY-STEP COMMENTS
# ==========================================

# --- SYNTAX STRUCTURE ---
# for variable in sequence:
#     code_block

# --- SIMPLE EXPLANATION ---
# A loop allows you to repeat a block of code multiple times automatically 
# instead of writing the same instruction over and over again.

# --- STEP-BY-STEP PROCESS ---
# Step 1: Define the sequence or range of numbers you want to loop through.
# Step 2: Assign the current value of the sequence to the loop variable.
# Step 3: Execute the indented code block using that current value.
# Step 4: Automatically move to the next value in the sequence and repeat until finished.

# --- REAL-LIFE EXAMPLE ---
# Imagine an automated ticket counter at a movie theater handing out tickets 
# to people standing in a line, one by one, until everyone has been served.

# --- VARIATIONS ---

# Variation A: Standard Forward Loop (Output: 1, 2, 3, 4)
print("Forward Loop (Counting up):")
for i in range(1, 5): # Step 1 & 2: Starts at 1 and stops right before 5
    print(i)          # Step 3: Prints the current number (Step-by-step action)

# Variation B: Reverse Loop (Output: 4, 3, 2, 1)
print("\nReverse Loop (Counting down):")
for i in range(4, 0, -1): # Variation Step: Starts at 4, goes down to 1 (stops at 0), stepping by -1
    print(i)

# --- COMMON MISTAKES ---
# 1. Off-by-one errors: Forgetting that range(1, 5) stops at 4, not 5.
# 2. Indentation Errors: Forgetting to indent the code block inside the loop, 
#    which causes Python to throw an IndentationError.
