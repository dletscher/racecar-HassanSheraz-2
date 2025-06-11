import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar'] 
        velocity = observations['velocity']

        left, front_left, front, front_right, right = lidar

        obstacle_threshold = 2.0
        slow_velocity = 1.0
        high_velocity = 3.0

        steering = 'straight'
        throttle = 'coast'

        if front < obstacle_threshold:
            # Obstacle ahead — decide to turn
            if front_left > front_right:
                steering = 'left'
            else:
                steering = 'right'

            if velocity > slow_velocity:
                throttle = 'brake'
            else:
                throttle = 'coast'
        else:
            if left > right:
                steering = 'left'
            elif right > left:
                steering = 'right'
            else:
                steering = 'straight'

            if velocity < high_velocity:
                throttle = 'accelerate'
            else:
                throttle = 'coast'

        action = (steering, throttle)
        if action in possibleActions:
            return action
        else:
            return ('straight', 'coast')
