import numpy as np
class IdealCamera:
  def __init__(self,env_map):
    self.map=env_map

  def data(self,cam_pose):
    observed=[]
    for im in self.map.landmarks:
      p=self.observation_function(cam_pose,im_pos)




  @classmethod
  def observation_function(cls,cam_pose,obj_pos):
    diff = obj_pos - cam_pose[0:2]
    phi = math.atan2(diff[1],diff[0])-cam_pose[2]
    while phi >=np.pi:phi 