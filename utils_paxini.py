import torch
import numpy as np

def cvt_pixels_to_pc(pixels, img_depth_raw, dict_intri):
    depth = img_depth_raw * dict_intri['depth_scale']
    # 1000 mm => 0.001 meters

    z = depth[pixels[:,0], pixels[:,1]]
    x =  z * (pixels[:,1] - dict_intri['ppx']) / dict_intri['fx']
    y =  z * (pixels[:,0] - dict_intri['ppy']) / dict_intri['fy']

    pc = np.dstack((x, y, z))[0]
    pc = torch.tensor(pc).float()

    return pc

def get_camera_intri(id_cam):
    if id_cam > 1:
        pass
    else:
        pass
    color_frame = self.cam_r.get_raw_frame()[0]
    intrinsics = color_frame.profile.as_video_stream_profile().intrinsics
    dict_intri = {'fx':intrinsics.fx, 'fy':intrinsics.fy,'ppx':intrinsics.ppx,'ppy':intrinsics.ppy}

    # torch.save(dict_intri, '/home/a/huo/dataset/7_22/intri/intri_r.pt')
    return dict_intri

