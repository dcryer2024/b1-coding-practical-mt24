def compute_action(reference, pos_y, previous_error, Kp= 0.15, Kd = 0.6):
    # Compute the current error
    current_error = reference - pos_y

    # Compute the derivative of the error (change in error)
    error_derivative = current_error - previous_error

    # PD control: Proportional + Derivative
    action = Kp * current_error + Kd * error_derivative

    return action, current_error  # Return action and the current error for next step
