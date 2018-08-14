# Ground Truth Visualization

This kit help interpate the disparity map of KITTI ground truth. Basically I follow the [KITTI Stereo]((http://www.cvlibs.net/datasets/kitti/eval_scene_flow.php?benchmark=stereo
) [devkit](https://s3.eu-central-1.amazonaws.com/avg-kitti/devkit_scene_flow.zip) to process the image. I only add a cv2.MORPH_CLOSE function to make the image more smooth. The kernel is implemented as a pseudo circle, while the rectangle and ellipse are available. 

The colormap is using "plasma" to better visuaize the result. 

## Ground Truth Disparity Map
![alt text](https://github.com/kspeng/Dataset-Preparation/blob/master/KITTI/Ground_Truth_Visualization/image/disp_gt_cmap_plasma.png)

## Interpolated Ground Truth Disparity Map
![alt text](https://github.com/kspeng/Dataset-Preparation/blob/master/KITTI/Ground_Truth_Visualization/image/disp_gt_interp.png)
