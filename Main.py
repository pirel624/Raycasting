class point:
    def __init__(self, x1, y1, real = True):
        self.X1 = x1
        self.Y1 = y1
        self.imaginary = not real

    def changex(self, x):
        self.X1 = x

    def changey(self, y):
        self.Y1 = y

    def get_data(self):
        return [self.X1, self.Y1, self.imaginary]





class line:
    def __init__(self, Xtitik1, Ytitik1, Xtitik2, Ytitik2):
        self.X1 = Xtitik1
        self.X2 = Xtitik2
        self.Y1 = Ytitik1
        self.Y2 = Ytitik2
        self.Slope = (self.Y2 - self.Y1) / (self.X2 - self.X1)
        self.Constant = self.Y1 - (self.Slope * self.X1)
        self.isParallelX = False
        self.isParallelY = False
        if self.X1 = self.X2:
            self.isParallelY = True
        if self.Y1 = self.Y1:
            self.isParallelX = True

    def change(self, x1, y1, x2, y2, staticx1 = False, staticy1 = False, staticx2 = False, staticy2 = False):
        if not staticx1:
            self.X1 = x1              
        if not staticx2:
            self.X2 = x2
        if not staticy1:
            self.Y1 = y1
        if not staticy2:
            self.Y2 = y2
        else:

        if self.X1 = self.X2:
            self.isParallelY = True
        if self.Y1 = self.Y1:
            self.isParallelX = True

        if not isParallelY and not isParallelX:
            self.Slope = (self.Y2 - self.Y1) / (self.X2 - self.X1)
            self.Constant = self.Y1 - (self.Slope * self.X1)

    def compile_data(self):
        if self.X1 = self.X2:
            self.isParallelY = True
        if self.Y1 = self.Y1:
            self.isParallelX = True

        if not isParallelY and not isParallelX:
            self.Slope = (self.Y2 - self.Y1) / (self.X2 - self.X1)
            self.Constant = self.Y1 - (self.Slope * self.X1)

    def get_coordinate_list(self):
        return [self.X1, self.Y1, self.X2, self.Y2]

    def get_identity(self):
        
        compile_data()

        if isParallelX:
            return "parallel_x"
        elif isParallelY:
            return "parallel_y"
        else:
            return [self.Slope, self.Constant]


class ray:                                       # Ray is created by cutting a line in two, the discarding one of them.
    def __init__(self, StartingX, StartingY, DirectionX, DirectionY, undefine = False):
        self.Sx = StartingX
        self.Sy = StartingY                                    # Hold the data for which part should be kept
        self.Dx = Directionx
        self.Dy = Directiony
        self.isDefined = not undefine                          # The line that is used to define the ray
        self.BaseLine = line(self.Sx, self.Sy, self.Dx, self.Dy)

    def change_starting_x(self, x):
        self.Sx = StartingX
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_starting_y(self, y):
        self.Sy = StartingY
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_direction_x(self, x):
        self.Dx = DirectionX
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_direction_y(self, x):
        self.Dx = DirectionX
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def define(self, StartingX, StartingY, DirectionX, DirectionY):
        self.Sx = StartingX
        self.Sy = StartingY                                    
        self.Dx = Directionx
        self.Dy = Directiony
        self.isDefined = True                          
        self.BaseLine.change(self.Sx, self.Sy, self.Dx, self.Dy)

    def activate(self):
        self.isDefined = True

    def deactivate(self):
        self.isDefined = False

    def compile_data(self):
        self.BaseLine.change(self.Sx, self.Sy, self.Dx, self.Dy)

    def get_coordinate_list(self):
        return [self.Sx, self.Sy, self.Dx, self.Dy]

    def isActive(self):
        return self.isDefined

    def get_identity(self):
        return self.BaseLine.get_identity()


class segment:                                       # Line is created by slicing a segment of line between two line
    def __init__(self, Limit1X, Limit1Y, Limit2X, Limit2Y, undefine = False):
        self.Sx = Limit1X
        self.Sy = Limit1Y                                    # Hold the data for which part should be kept
        self.Dx = Limit2X
        self.Dy = Limit2Y
        self.isDefined = not undefine                          # The line that is used to define the ray
        self.BaseLine = line(self.Sx, self.Sy, self.Dx, self.Dy)

    def change_starting_x(self, x):
        self.Sx = X
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_starting_y(self, y):
        self.Sy = Y
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_direction_x(self, x):
        self.Dx = X
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def change_direction_y(self, x):
        self.Dx = X
        self.BaseLIne.change(self.Sx, self.Sy, self.Dx, self.Dy, False, False, False, False)

    def define(self, Limit1X, Limit1Y, Limit2X, Limit2Y):
        self.Sx = Limit1X
        self.Sy = Limit1Y                                    # Hold the data for which part should be kept
        self.Dx = Limit2X
        self.Dy = Limit2Y
        self.isDefined = True                          # The line that is used to define the ray
        self.BaseLine = line(self.Sx, self.Sy, self.Dx, self.Dy)

    def activate(self):
        self.isDefined = True

    def deactivate(self):
        self.isDefined = False

    def compile_data(self):
        self.BaseLine.change(self.Sx, self.Sy, self.Dx, self.Dy)

    def get_coordinate_list(self):
        return [self.Sx, self.Sy, self.Dx, self.Dy]

    def isActive(self):
        return self.isDefined

    def get_identity(self):
        return self.BaseLine.get_identity()
