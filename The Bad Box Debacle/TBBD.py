import random
import sys
import time

def generate_boxes(player_count):
    boxes = [0 if i<player_count else 1 for i in range(player_count*20)]
    random.shuffle(boxes)
    return boxes

def print_scoreboard():
    print(f"Remaining boxes {len(boxes)}")
    print("Scoreboard")
    for i, x in enumerate(players):
        print(f"Player {i+1}{'' if x.alive else ' (dead)'}: {x.score}")

class Player:
    score: int = 0
    alive: bool = True

if __name__=="__main__":
    players = [Player() for x in range(2)]
    boxes = generate_boxes(len(players))
    current_player = 0
    
    playing=True
    while playing:
        player = players[current_player]
        while True:
            try:
                val = int(input(f"Player {current_player+1}, enter boxes to draw: "))
                if (val>0 and val<=len(boxes) and val<=10):
                    break
                print("Naughty naughty")
            except KeyboardInterrupt:
                print("\nNo more little Yama")
                exit()
            except:
                print("Naughty naughty")

        for x in range(val):
            box=boxes.pop(0)
            sys.stdout.write(f"Box #{x+1} is a ")
            sys.stdout.flush()
            for i in range(5):
                time.sleep(random.uniform(0.05,0.3))
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(random.uniform(0.05,0.3))
            sys.stdout.write(f" {box} ")
            sys.stdout.flush()
            time.sleep(0.3)

            match box:
                case 0:
                    print("you fucked up")
                    player.alive = False
                    break
                case 1:
                    print("you aight")
                    player.score += 1
                case _:
                    raise("What did you pick up?")
        
        print()
        if len(boxes)<=0:
            print("No more boxes")
            playing=False
        
        print_scoreboard()
        print()
        
        loopty=current_player
        while True:
            current_player = (current_player+1) % len(players)
            if players[current_player].alive:
                break

            if current_player==loopty:
                print("No more living players")
                playing=False
                break
    
    print_scoreboard()