# Render For CNN For Keypoint Generation


Original paper : https://arxiv.org/abs/1505.05641

This is a modification of the original paper to cater to our needs for our  IROS18 paper : https://arxiv.org/abs/1803.02057

The steps to run are present in https://github.com/sarthaksharma13/RenderForCNN_KeypointGeneration/Readme.txt. Advise is to go through that first. 
However as this is the data annotation pipeline which generates 3 views to be annotated. The sample views are present in data/view_distribution/Auto.txt
## Purpose Of the Pipeline:

This pipeline is a core part of the IROS18 paper. This pipeline is used to generate images of ShapeNet or other CAD Models for 3 specific views, the views depend upon the camera parameters specified by the user. The camera parameters namely are the **Azimuth, Elevation, Tilt and the Distance of the camera**. 

## Dependencies:

1. Blender.
2. MATLAB.
3. Python.
4. ShapeNet CAD Models(by default) or custom CAD Models.

## Steps to run the pipeline :

1. Run **setup.py** after changing the appropriate path variables.

2. In the file **global_varaibles.m**, change the **class** to the class you want to generate the images for.

3. In the file **global_varaibles.py**, change the following:
  - set up the **blender/matlab paths** as necessary.
  - set up the data paths for : **PASCAL,SHAPE NET** as well as the **SUN dataset**.
  - assign the variable ,**'g_shape_synset_name_pairs'**,with **ID** and the **class name**, accrording to the class you want.
  - setup the ID in **'g_shapenet_car_custom_folder'** (it was named as g_shapenet_car_custom_folder as we used it for car).
  - setup the path **'g_syn_images_keypoints_folder'** where the millions of synthesized images will be stored.
  
4. In the file **render_pipeline/run_render_keypoints.py**:
  - no change.

4.1 Run **makemex** file in MATLAB, present in the render_pipeline/kde/matlab_kde_package/mex/. 
  
5. In the file **render_pipeline/render_helper_keypoints.py**:
  - view_num : Ensure the number of images to be generated per model is stated as **3** for the purpose.

6. Go to the **'/data/view_distribution'**, which contains the parameters of the camera as you want while generating the synthetic images. **Please manually specify the parameters you want your images to be synthesized with.** In the current **data/view_distribution/Auto.txt** we have used the following parameters:
  - Azimuth: 65,90,115
  - Elevation: 0, 0, 0
  - Tilt: 0, 0, 0
  - Distance: 1.5, 1.5, 1.5
 
7. Run **python run_render.py** in the **'render_pipeline' directory'**. This would generate synthetic images without any truncation or background overlaying at the address set in the **g_syn_images_folder** variable present in the **global_variables.py**.


For details contact : Sarthak Sharma(sarthak.alexrider@gmail.com), Junaid Ahmed Ansari(ansariahmedjunaid@gmail.com ), Pratyush Kumar Sahoo(pratyushk.sahoo.min16@itbhu.ac.in)
