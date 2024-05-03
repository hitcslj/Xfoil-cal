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
2. ```chmod +x xfoil```
3. python calc.py --data_path xx --s xx --e xx


## Reference

- [xfoil](https://github.com/RobotLocomotion/xfoil)