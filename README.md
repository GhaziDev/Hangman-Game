# Hangman-Game
# Definition: 
It is a game that work on guessing letters until you get the correct word, it has various difficulties, some games give you a letter or 2 as a starter, some gives you nothing,But this project make it so difficult for the user and it give no letter.


# How does generating words work ?
It work based on a txt file that has 200 words (might be updated later), the program randomly select a word and store it in ``self.word`` attribute.

#Game Mechanics (Programitaclly):
After storing the random word, another attribute ``self.guess`` which is made of "dashes", each time you guess a letter correctly, the  dash will be replaced with the correct letter in the correct place
and the game keep going on until you win or you lose, the word is revealed in both cases at the end, one last thing is that you have ``8 lives``.

# Why no "Hanging man" drawing?
Because : 1)This is waste of print functions. 
2)waste of lines code. 
3) will probably make my code ugly.

# Lastly....
This is going to be updated using different method of generating words.
