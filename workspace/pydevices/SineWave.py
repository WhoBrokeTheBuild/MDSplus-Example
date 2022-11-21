
import MDSplus
import time
import math

class SineWave(MDSplus.Device):

    # These are the nodes added to the tree that make up this device
    parts = [
        {
            'path': ':FREQUENCY',
            'type': 'numeric',
            'value': 1,
            'options': ('no_write_shot',)
        },
        {
            'path': ':AMPLITUDE',
            'type': 'numeric',
            'value': 10,
            'options': ('no_write_shot',)
        },
        {
            'path': ':LENGTH',
            'type': 'numeric',
            'value': 10,
            'options': ('no_write_shot',)
        },
        {
            'path': ':SAMPLE_RATE',
            'type': 'numeric',
            'value': 30,
            'options': ('no_write_shot',)
        },
        {
            'path': ':DATA',
            'type': 'signal',
            'options': ('no_write_model',)
        },
    ]

    def init(self):
        
        twopi = math.pi * 2

        start = time.time()
        end = start + float(self.LENGTH.data())
        
        # SAMPLE_RATE is N samples per second
        delta = 1.0 / float(self.SAMPLE_RATE.data())
        
        points = []
        segmentIndex = 0
        
        now = start
        while now < end:
            elapsed = now - start
            
            theta = (elapsed * twopi) * float(self.FREQUENCY.data())
            point = math.sin(theta) * float(self.AMPLITUDE.data())
            
            points.append(point)
            
            if len(points) == self.SAMPLE_RATE.data():
                
                dimBegin = segmentIndex * self.SAMPLE_RATE.data() * delta
                dimEnd = dimBegin + ((self.SAMPLE_RATE.data() - 1) * delta)
                
                self.DATA.makeSegment(
                    dimBegin,
                    dimEnd,
                    MDSplus.Range(dimBegin, dimEnd, delta),
                    MDSplus.Float32Array(points)
                )
                
                points = []
                segmentIndex += 1
            
            time.sleep(delta)
            now = time.time()

    # This is required to make TDI case-insensitive
    INIT = init