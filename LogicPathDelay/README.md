Jordan Paul:
Logic Path Delay: Created for homework 5 problem 2 to display logic expression

create and get the path delay from input H
Note: this version onlys works for balanced non branching circuits as B is expected to be 1

Nand, Nor and inverters.

create a logic cirucit by Logic() with any number of series input gates

Ex. 4 input AND gate, is a 4 Input NAND with a Inverter on its output, the logic setup is as follows
logic = Logic(Nand(4), Inverter()) 

- calling logic.delay(1) or any number H will return total path delay D
- logic.pathEffort(H) will return the path effort usally noted as F multiplied by H
- logic.pathDelay() will return the path delay usally noted as P is the sum of the gates parasitic delay
- logic.stages() will return number of stages, Noted as N or can use len(Logic)
- print(Logic) will print out Logic Path expression: 
-  Ex.
-  Name (if given):  Stages- (N)   Delay = N * (H * pathEffort()) ^ (1 / N) + pathDelay()

Gates:
![image](https://github.com/jordanpaul98/homeworkProblems/assets/147276895/ca5d6750-bcc1-403f-a0a3-f5fdc09680fa)


output:

![image](https://github.com/jordanpaul98/homeworkProblems/assets/147276895/848034c4-ff66-444a-ab96-7a166580504a)
