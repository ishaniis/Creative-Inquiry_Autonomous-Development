import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

#Real Reinforcement learning agent will not have this thing hard coded
#It'll change with the environment 

#What we are doing is 

#Output of env.observation_space.high = [0.6,0.07]
#Output of env.observation_space.low = [-1.2, -0.07]

#Now we need to arrange for 20 buckets : 20 discrete values for 0.6 to -1.2
#Similarly for the 0.07 to -0.07

DISCRETE_Observation_Size = [20] * len(env.observation_space.high)
discrete_os_window_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_Observation_Size


print(discrete_os_window_size)

#Now constructing the Q Table

q_table = np.random.uniform(low=-2, high=0, size = (DISCRETE_Observation_Size + [env.action_space.n])) 
print(q_table.shape)
print(q_table)

'''
done = False

#while not done is equivalent, until the time it is true. 

while not done:
	#To do a step, we need an action
	#There are three actions:
	#0 - Push the Car Left.
	#1 - Do Nothing! 
	#2 - Push the Car Right.
	#We are pushing the car right
	action = 2
	#Things we are sensing from the environment for a given action
	#Values are getting are - Position and Velocity of the Car
	new_state, reward, done, _ = env.step(action)
	#The below command to render the environment for the given action in the gym
	
	#Convert these continous values referred to as discrete values into bucket these values

	print(new_state)
	env.render()

#Given any combination of position and velocity - Q Table 
#We want to pick up the actions which would lead to maxium cumulative reward

#Initially, the agent would do Exploration & then transcending into Exploitation




env.close()
'''
