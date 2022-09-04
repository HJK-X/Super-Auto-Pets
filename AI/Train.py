import random

from AI import DQNAgent
import sap


EPISODE_NUM = 10

past_teams = [[] for i in range(100)]

def opponent_generator(num_turns):
    # Returns teams to fight against in the gym 
    if past_teams[num_turns]:
        return past_teams[num_turns][random.randint(0, len(past_teams[num_turns])-1)]
    else:
        return []

if __name__ == "__main__":
    env = SuperAutoPetsEnv(opponent_generator, valid_actions_only= False )
    agent = DQNAgent(env.observation_space, env.action_space)
    # agent.load(START_NUM)

    print("starting")

    for e in range(1, EPISODE_NUM):
        last = env.reset()

        end = False

        while not end:
            action = agent.act(last)
            obs, reward, done, info = env.step(action)

            agent.remember(last, action,
                           reward, obs, end)

            last_screen = obs

            if done:
                last = env.reset()

        agent.replay(32)

        print('episode: {}/{}, score: {}'.format(e, EPISODE_NUM))

        if e % 10 == 0:
            agent.save(e)

    env.close()
    agent.save()
