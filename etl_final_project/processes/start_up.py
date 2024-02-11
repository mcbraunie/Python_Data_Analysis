# start_up.py
import traceback
import processes.function_calls as fc

def main():
    '''
    Function presents user with options for
    selection to proceed through processes.
    '''
    print("Choose a function to run:")
    print("S Start")
    print("Q to exit")

    while True:
        try:
            choice = input("Enter your choice (S or Q): ")
            if choice.upper() == "Q":
                print("Quiting program.")
                break
            elif choice.upper() == 'S':
                # function name
                func_name = "Start"
                print(f"You chose the {func_name} function.")
                fc.main()
            else:
                print("Invalid choice. Please enter S or Q.")
        except Exception as e:
            print(f"An error was encountered: {e}")
            traceback.print_exc()
    