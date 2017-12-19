import numpy as np
print(np.__version__)
a = np.arange(9).reshape((3,3))
test = np.arange(5)
print(np.isin(a, test))

#conda create -n ipykernel_py3 python=3 ipykernel
#activate ipykernel_py3    # On Windows, remove the word 'source'
#python -m ipykernel install --user

# https://github.com/jupyter/jupyter/issues/147
# However, I reinstalled ipykernel using python2 -m pip install ipykernel and python2 -m ipykernel install --user and that seems to have solved the problem!
