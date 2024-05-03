# Xfoil cal
> use xfoil calculate Cl/Cd performance in Linux


## Installation

```bash
conda create --name airfoil python=3.8
conda activate airfoil
pip install -r requirements.txt
```

## Useage

1. Download the airfoil dataset [here](https://drive.google.com/file/d/1latg3Oe5YCfzcb7gexu-hpZcFagmm-7E/view?usp=sharing) 
2. ln -s /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen cst_gen
3. ```chmod +x xfoil```
4. python calc.py  --s xx --e xx


## Reference

- [xfoil](https://github.com/RobotLocomotion/xfoil)