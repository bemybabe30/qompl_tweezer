from thorcam.camera import ThorCam
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import time
from scipy.optimize import curve_fit

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
        
        data = np.sum(new_array, axis=0)
        Normalized_data = (data-np.min(data))/(np.max(data)-np.min(data))

        x = np.linspace(0, 1339, 1440)
        y = Normalized_data
        self.ax.set_ylim(0,1)

        line1, = self.ax.plot(x, y)
        line1.set_color('blue')
        line1.set_xdata(x)
        line1.set_ydata(y)

        
        # set fitting parameters
        '''def gaussian(x, a, b, c):
            y = np.exp((-2)*((x-a)/b)**2)+c
            return y
        
        def fitting_3par(input_fn, x, y, guess):
            xdata = x
            ydata = y
            parameters, covariance = curve_fit(input_fn, xdata, ydata, p0=guess, maxfev = int(1e6))
            fit_A = parameters[0]
            fit_B = parameters[1]
            fit_C = parameters[2]
            SE = np.sqrt(np.diag(covariance))
            SE_A = SE[0]
            SE_B = SE[1]
            SE_C = SE[2]
            return np.array([fit_A, fit_B, fit_C]), np.array([SE_A, SE_B, SE_C])

        guess = [700, 80, 0]
        input_fn = gaussian
        par, se = fitting_3par(input_fn, x, y, guess)
        fit_y = input_fn(x, par[0], par[1], par[2])

        line2, = self.ax.plot(x, fit_y, color = 'red')

        line2.set_xdata(x)
        line2.set_ydata(fit_y)

        center = int(par[0])
        self.ax.text(1000, 0.5, 'center point: {}'.format(center), fontsize=10)'''

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        time.sleep(0.001)

        plt.cla()

    def play_camera(self):
        super().play_camera()
        plt.show()
    
    

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
        setting_list = ["exposure_ms", 'black_level','roi_x', 'roi_y', 'roi_width', 'roi_height', 'frame_queue_size']
        setting_value = [20, 0, 0, 0, 1440, 1080, 100]
        cam.set_setting(setting_list[i], setting_value[i])

    print(
    cam.exposure_ms,
    cam.black_level,
    cam.roi_x,
    cam.roi_y,
    cam.roi_width,
    cam.roi_height,
    )

    # initialize
    data = cam.play_camera()

