from NIENV import *


# API METHODS

# self.main_widget()        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------
from numpy.linalg import matrix_power


class MatrixPower_Node(Node):
    def __init__(self, params):
        super(MatrixPower_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        matrix = matrix_power(self.input(0), self.input(1))
        self.set_output_val(0, matrix)
        self.main_widget().update_matrix(matrix)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...

    def removing(self):
        pass
