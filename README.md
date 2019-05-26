# Render For CNN For Keypoint Generation


Original paper : https://arxiv.org/abs/1505.05641

This is a modification of the original paper to cater to our needs for our  IROS18 paper : https://arxiv.org/abs/1803.02057

The steps to run are present in https://github.com/sarthaksharma13/RenderForCNN_KeypointGeneration/Readme.txt. Advise is to go through that first. 
However as this is the data annotation pipeline which generates 3 views to be annotated. The sample views are present in data/view_distribution/Auto.txt

## Steps to run the pipeline :

1. In the file **setup.py**, change the **class** to the class you want to generate the images for.

2. In the file **global_varaibles.m**, change the **class** to the class you want to generate the images for.

3. In the file **global_varaibles.py**, change the following:
  - set up the **blender/matlab paths** as necessary.
  - set up the data paths for : **PASCAL,SHAPE NET** as well as the **SUN dataset**.
  - assign the variable ,**'g_shape_synset_name_pairs'**,with **ID** and the **class name**, accrording to the class you want.
  - setup the ID in **'g_shapenet_car_custom_folder'** (it was named as g_shapenet_car_custom_folder as we used it for car).
  - setup the path **'g_syn_images_keypoints_folder'** where the millions of synthesized images will be stored.
  
4. In the file **render_pipeline/run_render_keypoints.py**:
  - no change.
  
5. In the file **render_pipeline/render_helper_keypoints.py**:
  - view_num : Ensure the number of images to be generated per model is stated as **3** for the purpose.

6. Go to the **'/data/view_distribution'**, which contains the parameters of the camera as you want while generating the synthetic images. PLease specify the parameters you want your images to be synthesized with.

7. Run **python run_render_keypoints.py** in the **'render_pipeline' directory'**. This would generate synthetic images without any truncation or background overlaying at the address set in the **g_syn_images_folder** variable present in the **global_variables.py**.


For details contact : Sarthak Sharma(sarthak.alexrider@gmail.com), Junaid Ahmed Ansari(ansariahmedjunaid@gmail.com )
