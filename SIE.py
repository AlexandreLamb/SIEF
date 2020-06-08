#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time
import csv
from datetime import datetime

def main():

    try:

        client = carla.Client('localhost', 2000)
        client.set_timeout(2.0)

        world = client.get_world()

        actor_list = world.get_actors()
        actor_vehicle = actor_list.filter('vehicle.*')
        my_vehicle = actor_vehicle[0]
        max_steer_angle = my_vehicle.get_physics_control().wheels[0].max_steer_angle

        with open('record.csv', mode = 'w') as record_file :
            record_writer = csv.writer(record_file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            while 1:
                if my_vehicle.get_control().steer != 0 :
                    print(my_vehicle.get_control().steer*max_steer_angle)
                    record_writer.writerow([my_vehicle.get_control().steer*max_steer_angle,datetime.now()])
            #        print(my_vehicle.get_transform().rotation.yaw)
            pass

    finally :
        print("ok")
if __name__ == '__main__':

    main()
