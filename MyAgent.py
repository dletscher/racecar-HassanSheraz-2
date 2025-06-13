class Agent:

    def __init__(self):
        self.last_error = 0.0

    def chooseAction(self, observations, possibleActions):
        
        lidar = observations['lidar']
        v = observations['velocity']
        
        front_left = lidar[1]
        front_right = lidar[3]

        error = front_left - front_right
        deriv = error - self.last_error
        self.last_error = error

        steer_value = (4.0 * error) + (4.0 * deriv)

        if steer_value > 1.2:
            s = 'left'
        elif steer_value < -1.2:
            s = 'right'
        else:
            s = 'straight'

        if v < 0.1:
            t = 'accelerate'
        else:
            abs_steer = abs(steer_value)
            
            if abs_steer < 0.4:
                speed_target = 1.0
            else:
                redux = abs_steer - 0.4
                speed_target = 1.0 - redux * 0.3

            if speed_target < 0.4:
                speed_target = 0.4

            if v < speed_target:
                t = 'accelerate'
            else:
                t = 'coast' 

        current_action = (s, t)
        
        if current_action in possibleActions:
            return current_action
        
        return ('straight', 'coast')
