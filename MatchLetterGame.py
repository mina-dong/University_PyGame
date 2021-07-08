# 글자맞추기게임(202110710동민아)

#사용모듈
import turtle as t
import random
import time
import winsound

# 기본설정
eng_words = ["cat", "happy","python"]
# eng_words = open('./resource/word.txt','r').read().split('\n')

answer = random. choice(eng_words)
guess_letters = list("_" * len(answer))
life = 5

t.bgcolor("Powderblue")
t.title("MATCH-LETTER GAME")
t.ht()
t.up()
t.write("Hello, This is MATCH-LETTER game.", False, "center", ("Britannic Bold",30))
time.sleep(3)
t.clear()

yoursname = t.textinput("MATCH-LETTER GAME", "What is your name? ")

t.write("Good luck! "+ yoursname , False, "center", ("Britannic Bold",30))
time.sleep(3)
t.clear()


# 본 게임
game_over = False

while not game_over:
    t.write(f"life : {'❤ ' * life} ", False, "center", ("Britannic Bold",30))
    time.sleep(3)
    t.clear()

    user_guess = t.textinput("MATCH-LETTER GAME", "Please enter letter.").lower()

    if len(user_guess) == 1 and user_guess.isalpha():   
        for i in range(len(answer)):
            if answer[i] == user_guess:
                guess_letters[i] = user_guess
        t.write(guess_letters, False, "center", ("Britannic Bold",30))
        time.sleep(2)
        t.clear()

        if "_" not in guess_letters:
            game_over = True
            t.write("YOU WIN! Congratulations! "+yoursname+"!", False, "center", ("Britannic Bold",30))
            winsound.PlaySound('./sound/Congratulations.wav', winsound.SND_FILENAME)
            time.sleep(3)
            t.clear()

        if user_guess not in answer:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            life -= 1
            if life == 0:
                game_over = True
                t.write(yoursname+"!"+f"YOU LOSE!!The answer is {answer}.", False, "center", ("Britannic Bold",30))
                time.sleep(5)
                t.clear()
    else:
        t.write("Please enter only English one letter!", False, "center" , ("Britannic Bold",30))
        time.sleep(3)
        t.clear()   
