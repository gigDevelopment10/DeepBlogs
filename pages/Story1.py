import streamlit as st

st.title('Let us reinforce learnings with StableBaselines')
st.caption('February 12, 2023  |  5 min read   | Zoya Jamadar')

st.header('Stable Baselines in reinforcement learning')
st.markdown('Stable Baselines is a **high-quality implementation of reinforcement learning** algorithms in Python. It is built on top of the popular deep learning framework TensorFlow and PyTorch and provides a unified interface for various reinforcement learning algorithms. The algorithms included in Stable Baselines are carefully tested, optimized and updated to provide users with a stable and efficient implementation of reinforcement learning techniques.')

st.markdown('The package includes popular algorithms such as Proximal Policy Optimization (PPO), A2C (Advantages Actor-Critic), and A3C (Asynchronous Advantage Actor-Critic), among others. The implementation of these algorithms is designed to be easy to use, while still providing users with access to the underlying algorithms and their parameters so that they can be customized as needed.')

st.markdown('Stable Baselines is particularly useful for those who are new to reinforcement learning, as it provides a convenient and intuitive interface to get started quickly. Additionally, it is also useful for experienced reinforcement learning practitioners who are looking for a fast and efficient implementation of reinforcement learning algorithms for their projects.')

st.markdown("""---""")

st.markdown('Here is an implementation of an Agent playing Lunar Lander using Deep Q-Networks  - (DQN) a Q-learning algorithm')

st.markdown('Lunar Lander is a classical rocket trajectory optimisation problem considered as a challenging problem in Reinforcement learning. The objective of the lunar lander task is to control the thrust of the lander to safely land it on the moon while minimizing fuel consumption and maximizing landing accuracy.')

st.markdown('For a lunar lander problem there are four discrete actions available in the ACTION SPACE:')

st.markdown('- **0**: do nothing')
st.markdown('- **1**: fire left orientation engine')
st.markdown('- **2**: fire main engine')
st.markdown('- **3**: fire right orientation engine')
st.markdown('The reward for each action is based on the proximity of the lander to the landing pad, the orientation of the lander, and the amount of fuel remaining.')

st.markdown('----')

st.markdown('There is another popular algorithms that has been successfully applied to the Lunar Lander problem, called Proximal Policy Optimization (PPO), which have shown promising results in solving the task.In conclusion, Stable Baselines offers a simple and powerful solution for tackling the problems through reinforcement learning. The library contains numerous well-optimized RL algorithms and is built on top of TensorFlow, PyTorch and OpenAI Gym, making it a useful tool for researchers and practitioners alike.')

st.markdown('**Well that is all for the day... stay tuned for more upcoming DeepInAI topics !!🚀🚀**')

st.markdown(':blue[#ai hashtag#design hashtag#intelligence hashtag#artificialintelliegence hashtag#deeplearning hashtag#DeepInAI hashtag#computervision hashtag#neuralnetworks hashtag#machinelearning ]')
