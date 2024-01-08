#!/usr/bin/env python3
from enum import Enum


class LatTunes(Enum):
  LQR_PV = 0


###### LAT ######
def set_lat_tune(tune, name, MAX_LAT_ACCEL=2.5, FRICTION=0.01, steering_angle_deadzone_deg=0.0, use_steering_angle=True):
  if name == LatTunes.LQR_PV:
    tune.init('lqr')
    tune.lqr.scale = 1650.0
    tune.lqr.ki = 0.028
    tune.lqr.a = [0., 1., -0.22619643, 1.21822268]
    tune.lqr.b = [-1.92006585e-04, 3.95603032e-05]
    tune.lqr.c = [1., 0.]
    tune.lqr.k = [-110.73572306, 451.22718255]
    tune.lqr.l = [0.3233671, 0.3185757]
    tune.lqr.dcGain = 0.0028
  else:
    raise NotImplementedError('This lateral tune does not exist')
