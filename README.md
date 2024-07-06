# Batch_Image_Processors
藉由雙擊點選欲辨識範圍的左上角與右下角，即可判斷框選範圍內的文字


將需批量裁切的照片放入同一個資料夾後，將檔案名稱統一改為數字編號，藉由雙擊點選欲裁切範圍的左上角與右下角，即可完成批量改名與裁切。

```bash
請輸入要截圖的資料夾名稱：
xkllkx_repo
8051.png >>> xkllkx_repo_1.png
xkllkx_repo_1.png B2W完成
------------------------     
DMA.png >>> xkllkx_repo_2.png
xkllkx_repo_2.png B2W完成
------------------------    
PD.png >>> xkllkx_repo_3.png
xkllkx_repo_3.png B2W完成
------------------------
pokemon.png >>> xkllkx_repo_4.png
xkllkx_repo_4.png B2W完成
------------------------
pyqtgraph.png >>> xkllkx_repo_5.png
xkllkx_repo_5.png B2W完成
------------------------
```

This repository demonstrates using PIL and OpenCV to create a Pokémon game scenario generator.
The application is divided into two main parts:

### Character Info Edit
Allows users to edit the character's name and HP.

<img src="https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/character_info_edit/f_w_model.jpg" width="45%" height="45%"><img src="https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/character_info_edit/f_w.png" width="45%" height="45%">

### Animation Generate
Continues from the first part to progressively generate multiple game scenes and create a game animation.

<img src="https://github.com/xkllkx/Pokemon_Scenario_Generator/blob/main/animation_generate/test.gif" width="90%" height="90%">
# Installation
```bash
pip install pillow opencv-python
```

# How to use this repo
## Character Info Edit
### User define variable
- Font
```python
font = ImageFont.truetype("Silver.ttf", 60)
```

- Character model pick
```python
im = Image.open("f_w_model.jpg")
```

- Character HP
```python
player1_start_XY = [976,268] # XY # main character HP left-coor
player1_end_XY = [751,268] # left

player2_start_XY = [403,63] # XY # opponent character HP left-coor
player2_end_XY = [180,63] # left

# only player1 need HP num
num_start_XY = [868,279] # left top

player1_full_blood = 20
player1_current_blood = 10

player2_full_blood = 20
player2_current_blood = 15
```

- Output Scenario (png)
```python
im.save("f_w.png","png")
```

### Run T2P_PIL_finish.py to generate single Pokémon game scenario.
```bash
python T2P_PIL_finish.py
```

## Animation Generate
### User define variable
- As mentioned above

- animation_fps
```python
picture_num = 50
twinkle_num = 4 # slash on/off * 2

picture_name = 0
```

- output folder
```python
filename = "w_g_bb_2"
```

- slash twice
```python
black = Image.open("black.jpg")
twinkle = 0
```

- animation
```python
size = (1009,348) # image size
print(size)
```

###  Run picture_2_movie_final.py to generate scenarios and Pokémon game Animation.
```bash
python picture_2_movie_final.py
```
