import torch
from metrics import Matrix_Loss, mae


if __name__ == "__main__":
    # Example input: [batch_size, 1, height, width]
    pred = torch.rand(2, 1, 480, 800)
    gt = torch.rand(2, 1, 480, 800)

    criterion = Matrix_Loss(kld_parm=1, cc_parm=-0.1, sim_parm=-0.2, nss_parm=-0.005)
    _, kld, cc, sim, nss = criterion(pred, gt)
    mae_sal = mae(pred, gt)

    print("MAE_sal:", mae_sal.item())
    print("KLD:", kld.item())
    print("CC:", cc.item())
    print("SIM:", sim.item())
    print("NSS:", nss.item())
