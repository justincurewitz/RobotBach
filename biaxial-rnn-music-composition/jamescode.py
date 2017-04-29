import model
import time
m = model.Model([30,30],[10,5],dropout=0.5)

import multi_training
pcs = multi_training.loadPieces("music")

print "Loaded Pieces"

start = time.time();
multi_training.trainPiece(m, pcs, 10000)
end = time.time();

print "Trained"
total = end-start
hours = total/3600
minutes = (total%3600)/60
seconds = (total%60)
print 'Elapsed time: %i:%i:%i' %(hours, minutes, seconds)
