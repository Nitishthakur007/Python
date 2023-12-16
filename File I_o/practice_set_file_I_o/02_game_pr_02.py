def game():                      # score of a game
    return 75                    # return score


new_score = game()                     # storing the score in a variable
with open('hiscore.txt') as f:         # opening file
    hiscore = f.read()                 # read

if hiscore == "":
    with open("hiscore.txt", "w") as f:
        f.write(str(new_score))


elif new_score > int(hiscore):               # if score is greater than prev
    with open("hiscore.txt", "w") as f:    # write method
        f.write(str(new_score))            # if greater than previous
