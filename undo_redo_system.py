# -------------------------------------------------------------
# Project: Simple Undo-Redo System using Stacks
# Course: Programming Fundamentals (Final Lab Exam)
# Achievement: Highest marks in class (8/10)
# Description: Implements text actions with dynamic undo/redo 
#              capabilities using Stack (LIFO) logic.
# -------------------------------------------------------------

print('------ SIMPLE UNDO REDO SYSTEM ------')
undo_stack = []
redo_stack = []
action_perform = []

print('0 - Exit & Proceed to Functions')
print('1 - Typing text')
print('2 - Deleting text')
print('3 - Formatting text')

# Phase 1: Performing Actions
while True:
    user_action = int(input('Which action do you want to perform? Press respective number: '))
    if user_action == 1:
        action = input('Enter text: ')
        action_perform.append(action)
        undo_stack.append(action)
    elif user_action == 2:
        action = input('Which text do you want to delete: ')
        if action in undo_stack:
            action_perform.remove(action)
            undo_stack.append(action)
        else:
            print('This text is not present!')
    elif user_action == 3:
        action = input('Format text: ')
        action_perform.append(action)
        undo_stack.append(action)
    elif user_action == 0:
        break
    else:
        break

print('\n------ UNDO / REDO FUNCTIONS ------')
print('0 - Exit Application')
print('1 - Undo Function')
print('2 - Redo Function')

# Phase 2: Undo and Redo Execution
while True:
    function = int(input('Which function do you want to perform? Press respective number: '))
    if function == 1:
        if undo_stack:
            popped = undo_stack.pop()
            redo_stack.append(popped)
            print('This is the text after undo function:', undo_stack)
        else:
            print('Undo function cannot perform because stack is empty!')
    elif function == 2:
        if redo_stack:
            popped = redo_stack.pop()
            undo_stack.append(popped)
            print('This is the text after redo function:', undo_stack)
        else:
            print('Redo function cannot perform because nothing was undone!')
    elif function == 0:
        print('Application finished successfully.')
        break
    else:
        break
