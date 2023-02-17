#Created by Vanessa Bonner
#Date: Febraury 17, 2023
#open ai gym library this will let us create an interactive environment
import gym
import time
#create an environment for the mountaincar-v0 game problem in the human render mode
env = gym.make("ALE/AirRaid-v5", render_mode='human')

print("Welcome to the AirRaid version 5!")

#Set the intital state of the car and the flag is false
observation = env.reset()
done = False

while not done:
    #Render the environment
    env.render()
    #Wait 1 second before the next step
    time.sleep(1)
    #Choose a random section from the action space
    action = env.action_space.sample()
    #Take the chose action and get the next state, reward, and if the episode is done
    observation, reward, done, info, *_ = env.step(action)

#Check if the flag was reached, and print a message to user
if observation[0] >= 0.5:
    print("You beat the game!")
else:
    print("You did not beat the game!")

#Close the environment
#Wait for user to press enter before closing the window
input("Press enter to close the window!")
env.close
