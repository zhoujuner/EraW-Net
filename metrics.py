import torch.nn as nn
import torch
import torch.nn as nn
import cv2



class Matrix_Loss(nn.Module):
    def __init__(self, kld_parm=None, cc_parm=None, sim_parm=None,nss_parm=None):
        super(Matrix_Loss, self).__init__()
        self.kld = 0
        self.cc = 0
        self.sim = 0
        self.nss = 0

        self.kld_parm = 0 if kld_parm is None else kld_parm
        self.cc_parm = 0 if cc_parm is None else cc_parm
        self.sim_parm = 0 if sim_parm is None else sim_parm
        self.nss_parm = 0 if nss_parm is None else nss_parm

    #def forward(self, s_map, gt, fix):
    def forward(self, s_map, gt):
 
        s_map = s_map.squeeze(dim=1)
        gt = gt.squeeze(dim=1)
        #fix = fix.squeeze(dim=1)
        if self.kld_parm != 0:
            self.kld = kldiv(s_map, gt)
        if self.cc_parm != 0:
            self.cc = cc(s_map, gt)

        if self.sim_parm != 0:
            self.sim = similarity(s_map, gt)
        if self.nss_parm != 0:
            #self.nss = nss(s_map,fix)
            self.nss = nss(s_map,gt)
        loss = self.kld_parm * self.kld + self.cc_parm * self.cc + self.sim_parm * self.sim + self.nss_parm * self.nss 

        return [loss, self.kld, self.cc, self.sim, self.nss]




def kldiv(s_map, gt):
    batch_size = s_map.size(0)
    w = s_map.size(1)
    h = s_map.size(2)

    sum_s_map = torch.sum(s_map.view(batch_size, -1), 1)
    expand_s_map = sum_s_map.view(batch_size, 1, 1).expand(batch_size, w, h)

    assert expand_s_map.size() == s_map.size()

    sum_gt = torch.sum(gt.view(batch_size, -1), 1)
    expand_gt = sum_gt.view(batch_size, 1, 1).expand(batch_size, w, h)

    assert expand_gt.size() == gt.size()

    s_map = s_map / (expand_s_map * 1.0)
    gt = gt / (expand_gt * 1.0)

    s_map = s_map.view(batch_size, -1)
    gt = gt.view(batch_size, -1)

    eps = 2.2204e-16
    result = gt * torch.log(eps + gt / (s_map + eps))
    # print(torch.log(eps + gt/(s_map + eps))   )
    return torch.mean(torch.sum(result, 1))


def cc(s_map, gt):
    batch_size = s_map.size(0)
    w = s_map.size(1)
    h = s_map.size(2)

    mean_s_map = torch.mean(s_map.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)
    std_s_map = torch.std(s_map.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)

    mean_gt = torch.mean(gt.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)
    std_gt = torch.std(gt.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)

    s_map = (s_map - mean_s_map) / std_s_map
    gt = (gt - mean_gt) / std_gt

    ab = torch.sum((s_map * gt).view(batch_size, -1), 1)
    aa = torch.sum((s_map * s_map).view(batch_size, -1), 1)
    bb = torch.sum((gt * gt).view(batch_size, -1), 1)
    eps = 2.2204e-16
    return torch.mean(ab / (torch.sqrt(aa * bb + eps)))


def similarity(s_map, gt):
    ''' For single image metric
        Size of Image - WxH or 1xWxH
        gt is ground truth saliency map
    '''

    
    batch_size = s_map.size(0)
    w = s_map.size(1)
    h = s_map.size(2)

    s_map = normalize_map(s_map)
    gt = normalize_map(gt)

    sum_s_map = torch.sum(s_map.view(batch_size, -1), 1)
 
    expand_s_map = sum_s_map.view(batch_size, 1, 1).expand(batch_size, w, h)

    assert expand_s_map.size() == s_map.size()

    sum_gt = torch.sum(gt.view(batch_size, -1), 1)
    expand_gt = sum_gt.view(batch_size, 1, 1).expand(batch_size, w, h)
    
            
    eps = 2.2204e-16

    expand_s_map = expand_s_map.clone()
    expand_s_map[expand_s_map < eps] = eps

    expand_gt = expand_gt.clone()
    expand_gt[expand_gt < eps] = eps

    s_map = s_map / (expand_s_map * 1.0)
    gt = gt / (expand_gt * 1.0)

    s_map = s_map.view(batch_size, -1)
    gt = gt.view(batch_size, -1)
    return torch.mean(torch.sum(torch.min(s_map, gt), 1))




def nss(s_map, gt):
    if s_map.size() != gt.size():
        s_map = s_map.cpu().squeeze(0).numpy()
        s_map = torch.FloatTensor(cv2.resize(s_map, (gt.size(2), gt.size(1)))).unsqueeze(0)
        s_map = s_map.cuda()
        gt = gt.cuda()
    # print(s_map.size(), gt.size())
    assert s_map.size() == gt.size()
    batch_size = s_map.size(0)
    w = s_map.size(1)
    h = s_map.size(2)
    mean_s_map = torch.mean(s_map.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)
    std_s_map = torch.std(s_map.view(batch_size, -1), 1).view(batch_size, 1, 1).expand(batch_size, w, h)

    eps = 2.2204e-16
    s_map = (s_map - mean_s_map) / (std_s_map + eps)

    s_map = torch.sum((s_map * gt).view(batch_size, -1), 1)
    count = torch.sum(gt.view(batch_size, -1), 1)
    return torch.mean(s_map / count)




def normalize_map(s_map):
    # normalize the salience map (as done in MIT code)
    batch_size = s_map.size(0)
    w = s_map.size(1)
    h = s_map.size(2)

    min_s_map = torch.min(s_map.view(batch_size, -1), 1)[0].view(batch_size, 1, 1).expand(batch_size, w, h)
    max_s_map = torch.max(s_map.view(batch_size, -1), 1)[0].view(batch_size, 1, 1).expand(batch_size, w, h)

    eps = 2.2204e-16
    norm_s_map = (s_map - min_s_map) / (max_s_map - min_s_map + eps)
    return norm_s_map
