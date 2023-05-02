from thorcam.camera import ThorCam
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

data_list = []

def gaussian(x, a, b, c, D):
    y = D*np.exp((-2)*((x-a)/b)**2)+c
    return y

def fitting_4par(input_fn, x, y, guess):
    xdata = x
    ydata = y
    parameters, covariance = curve_fit(input_fn, xdata, ydata, p0=guess, maxfev=int(1000))
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    SE = np.sqrt(np.diag(covariance))
    SE_A = SE[0]
    SE_B = SE[1]
    SE_C = SE[2]
    SE_D = SE[3]
    return np.array([fit_A, fit_B, fit_C, fit_D]), np.array([SE_A, SE_B, SE_C, SE_D])

class MyThorCam(ThorCam):
    def __init__(self) -> None:
        super().__init__()
        self.figure, self.ax = plt.subplots(figsize=(4,3))
    
    def received_camera_response(self, msg, value):
        super(MyThorCam, self).received_camera_response(msg, value)
        if msg == 'image':
            return
        print('Received "{}" with value "{}"'.format(msg, value))
    
    def got_image(self, image, count, queued_count, t):
        # access image dat
        # call super method to display image in ThorCam window
        super(MyThorCam, self).got_image(image, count, queued_count, t)
        img = image
        size = img.get_size()
        imgBuffer = img.to_bytearray()[0]
        w, h = size[0], size[1]
        nparray1 = np.array(imgBuffer)
        nparray2 = nparray1.reshape((h, w, 2))
        # set numpy arrays form image data, data type : ffpyplayer
        new_array = nparray2[:,:,0]

        global data_list

        data = np.sum(new_array, axis=0)

        Normalized_data = (data - np.min(data)) / (np.max(data)-np.min(data))

        data_list = list(Normalized_data)

        # print('Received "{}" with value "{}"'.format(image, count))

    def play_camera(self):
        super().play_camera()
        

if __name__=="__main__":
    # create camera
    cam = MyThorCam()

    # start the server etc.
    cam.start_cam_process()
    # get list of attached cams
    serial_num = cam.refresh_cameras()


    # open the camera
    cam.open_camera('16470')

    # update the exposure value
    for i in range(0,7):
        setting_list = ["exposure_ms", 'black_level','roi_x', 'roi_y', 'roi_width', 'roi_height', 'frame_queue_size'] # QUE data as large as possible(frame drop)
        setting_value = [1, 0, 0, 0, 1440, 1080, 10000]
        cam.set_setting(setting_list[i], setting_value[i])

    print(
    cam.exposure_ms,
    cam.black_level,
    cam.roi_x,
    cam.roi_y,
    cam.roi_width,
    cam.roi_height,
    )

    cam.timeout = 5

    # initialize
    cam.play_camera()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
    
        super(MainWindow, self).__init__(*args, **kwargs)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.x1 = list(np.linspace(0, 1339, 1440))
        self.y1 = list(np.zeros(1440))
        self.x2 = list(np.linspace(0, 1339, 1440))
        self.y2 = list(np.zeros(1440))
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Intensity fitting", color="b", size="30pt")
        self.center = int(2)


        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        pen1 = pg.mkPen(color=(0, 0, 255))
        pen2 = pg.mkPen(color=(255, 0, 0))

        self.data_line1 =  self.graphWidget.plot(self.x1, self.y1, "Intensity", pen=pen1)
        self.data_line2 =  self.graphWidget.plot(self.x2, self.y2, "Fitting Graph", pen=pen2)

        # ... init continued ...
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        
        self.x1 = list(np.linspace(0, 1339, 1440))
        self.y1 = data_list[1440:]
        self.y1.extend(data_list) # Remove the first
        self.data_line1.setData(self.x1, self.y1)  # Update the data

        guess = [700, 100, 0, 0.8]
        input_fn = gaussian
        
        par, se = fitting_4par(input_fn, self.x1, data_list, guess)

        # Set Center
        # global center
        
        self.center = int(par[0])
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Normalized Intensity", **styles)
        self.graphWidget.setLabel("bottom", "Horizontal Pixel", **styles)
        self.graphWidget.setLabel("right", "center: {}".format(self.center), **styles)

        fit_y = list(input_fn(self.x1, par[0], par[1], par[2], par[3]))

        self.x2 = list(np.linspace(0, 1339, 1440))
        self.y2 = data_list[1440:]

        self.y2.extend(fit_y) # Remove the first
        self.data_line2.setData(self.x2, self.y2)  # Update the data


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QLabel("Beam allignment")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
