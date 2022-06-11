import Landmark

class Map:
  def __init__(self):
    self.landmarks=[]
  def append_landmark(self,landmark):
    landmark.id = len(self.landmarks)
    self.landmarks.append(landmark)

  def draw(self,ax,elems):
    for Im in self.landmarks:
      Im.draw(ax,elems)
