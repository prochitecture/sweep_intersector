import random
import matplotlib.pyplot as plt
from SweepIntersectorLib.SweepIntersector import SweepIntersector

segList = []

# create some random segments
for i in range(50):
    vs = (random.uniform(-1,1),random.uniform(-1,1))
    ve = (random.uniform(-1,1),random.uniform(-1,1))
    segList.append( (vs,ve) )

# add some vertical segments
for i in range(5):
    vs = (random.uniform(-1,1),random.uniform(-1,1))
    ve = (vs[0],random.uniform(-1,1))
    segList.append( (vs,ve) )

# compute intersections
isector = SweepIntersector()
isecDic = isector.findIntersections(segList)

# plot original segments
for seg in segList:
    vs,ve = seg
    plt.plot([vs[0],ve[0]],[vs[1],ve[1]],'k:')

# plot intersection points
for seg,isects in isecDic.items():
    for p in isects[1:-1]:      
        plt.plot(p[0],p[1],'r.')

plt.gca().axis('equal')
plt.show()
