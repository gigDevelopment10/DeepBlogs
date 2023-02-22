import streamlit as st 
import time
from PIL import Image

image_1 = Image.open('assets/images/png_1.png')

st.title('Do you know what is an Auto-grad ? and why neural networks are hungry for them ?')
st.caption('February 8, 2023  |  3 min read   | Zoya Jamadar')

st.header('Auto-grad - Introduction')
st.markdown('Auto-grad is an automatic **differentiation library** for gradient computation in Python programming language. It is used in machine learning and deep learning to efficiently calculate the **gradients (derivative)** of functions with respect to their input parameters, which is used in optimization algorithms to update the parameters in the direction that reduces the loss.')

st.markdown('To put this in simple words **Auto-grad influences back-propagation** (You can say a mathematical model that trains the neural parameter) and helps to efficiently evaluate the gradient of some kind of loss function that influences the weight of a neural network to learn a feature.')

st.markdown('It is meant to automatically calculate the **derivatives of a function**, freeing the user from the manual and error-prone calculation of derivatives, making it easier to implement complex models and perform optimization.')



st.image(image_1, caption='Some powerful auto-grad libraries', use_column_width=True)

st.markdown('Here is a list of some powerful auto-grad libraries that will help you get your neural network stronger')

st.markdown('- **PyTorch**: An open-source machine learning library based on the Torch library. It provides a flexible, high-performance platform for building and deploying deep learning models.')

st.markdown('- **TensorFlow**: An open-source software library for dataflow and differentiable programming across a range of tasks. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.')

st.markdown('- **Chainer**: A flexible, intuitive, and high-performance deep learning framework. It provides a straightforward, modular approach to building deep learning models and allows for GPU acceleration.')

st.markdown('- **JAX**: A Python library that makes it easy to combine the NumPy API with automatic differentiation to build and train deep learning models.')

st.markdown("""---""")

st.markdown('Neural networks are hungry for an **autograd engine** because the computation of gradients can be time-consuming and complex, especially for deep neural networks with many layers. An autograd engine takes care of this computation, allowing the user to focus on defining the architecture of the network and the training process. The autograd engine also enables the efficient implementation of different optimization algorithms, making the training process more efficient and easier to implement.')

st.subheader('In summary, an autograd engine is crucial for the successful training of neural networks, and this is why neural networks are hungry for an autograd engine.')

st.markdown('**Well that is all for the day... stay tuned for more upcoming DeepInAI topics !!🚀🚀**')


st.markdown(':blue[#ai hashtag#design hashtag#intelligence hashtag#artificialintelliegence hashtag#deeplearning hashtag#DeepInAI hashtag#computervision hashtag#neuralnetworks hashtag#machinelearning ]')