import argparse
from roku import Roku

def play_command(roku):
    roku.play()

def up_command(roku):
    roku.up()

def down_command(roku):
    roku.down()

def left_command(roku):
    roku.left()

def right_command(roku):
    roku.right()

def select_command(roku):
    roku.select()

def back_command(roku):
    roku.back()

def home_command(roku):
    roku.home()


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Control Roku via command-line')
    parser.add_argument('command', choices=['play', 'up', 'down', 'left', 'right', 'select', 'back', 'home'],
                        help='Command to send to Roku')

    # Parse the arguments
    args = parser.parse_args()

    # Initialize Roku instance
    roku = Roku('192.168.1.3')

    # Execute the corresponding command
    if args.command == 'play':
        play_command(roku)
    elif args.command == 'up':
        up_command(roku)
    elif args.command == 'down':
        down_command(roku)
    elif args.command == 'left':
        left_command(roku)
    elif args.command == 'right':
        right_command(roku)
    elif args.command == 'select':
        select_command(roku)
    elif args.command == 'back':
        back_command(roku)
    elif args.command == 'home':
        home_command(roku)


if __name__ == "__main__":
    main()
