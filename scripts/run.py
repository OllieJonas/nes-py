from nes_py import NESEnv
import tqdm
env = NESEnv('C:\\Users\\ollie\\PyCharmProjects\\nes-py\\nes_py\\tests\\games\\super-mario-bros-1.nes', render_mode="human")

terminated = True

try:
    for _ in tqdm.tqdm(range(100_000)):
        if terminated:
            print(terminated)
            state, info = env.reset()
            terminated = False
        else:
            state, reward, terminated, truncated, info = env.step(env.action_space.sample())
            # print(state.shape)
            env.render()
except KeyboardInterrupt:
    pass
