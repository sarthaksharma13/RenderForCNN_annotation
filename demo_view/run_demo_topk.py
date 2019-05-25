#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(BASE_DIR))
from global_variables import *
sys.path.append(os.path.join(g_render4cnn_root_folder, 'view_estimation'))
from evaluation_helper import viewpoint_topk
files = os.listdir("/home/rishabh/RenderforCNN/RenderForCNN/demo_view/Chair_Cropped/");
if __name__ == '__main__':
    
    for name in files:
        flag = 1;

    #img_filenames = [os.path.join(BASE_DIR, 'aeroplane_image.jpg')]
    #class_idxs = [g_shape_names.index('aeroplane')]
        img_filenames = [os.path.join(BASE_DIR, 'Chair_Cropped',name)]
        class_idxs = [g_shape_names.index('chair')]
        name = [name.strip().split('.')]
        op = name[0][0] + '.txt'
        output_result_file = os.path.join(BASE_DIR,'Chair_NewRun_Out',op)
        topk = 2
        
        if not os.path.exists(output_result_file):
            viewpoint_topk(img_filenames, class_idxs, topk, output_result_file)
     

        # display result by rendering an image of estimated viewpoint
        estimated_viewpoints = [[float(x) for x in line.rstrip().split(' ')] for line in open(output_result_file,'r')]
        v = estimated_viewpoints[0]
        topk = len(v)/4
        print("Estimated views and confidence: ")
        for k in range(topk):
            a,e,t,c = v[4*k : 4*k+4]
            print('rank:%d, confidence:%f, azimuth:%d, elevation:%d, tilt:%d' % (k+1, c, a, e, t))
        