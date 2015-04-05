


import sys
import gphoto2 as gp

# set target to save to camera
# http://gphoto-software.10949.n7.nabble.com/capture-image-and-save-on-camera-td14075.html
# gphoto2 --get-config capturetarget
# gphoto2 --set-config capturetarget=1

def capture_img():
    context = gp.gp_context_new()
    camera = gp.gp_camera_new()
    gp.gp_camera_init(camera, context)
    print('Capturing image')
    gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE, context)
    # exit camera
    gp.gp_camera_exit(camera, context)
    return 0

if __name__ == "__main__":
    sys.exit(capture_img())