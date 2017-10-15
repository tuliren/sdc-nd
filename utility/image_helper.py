import matplotlib.pyplot as plt

def remove_frames():
  plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off',
                  labelright='off', labelbottom='off')

def save(filename):
  remove_frames()
  plt.savefig(filename, bbox_inches='tight', pad_inches=0)

def show():
  remove_frames()
  plt.show()
