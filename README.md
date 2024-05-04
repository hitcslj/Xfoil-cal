# Xfoil cal
> use xfoil calculate Cl/Cd performance in Linux


## Installation

```bash
conda create --name airfoil python=3.8
conda activate airfoil
pip install -r requirements.txt
```

## Useage

1. Download the airfoil dataset [here](https://drive.google.com/file/d/14HIHr3YGP4cqa6yw_ursTF6Jj4x7hRSG/view?usp=drive_link) 
2. ln -s /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen cst_gen
3. ```chmod +x xfoil```
4. python calc.py  --s xx --e xx


## Reference

- [xfoil](https://github.com/RobotLocomotion/xfoil)