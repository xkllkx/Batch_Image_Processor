# Batch_Image_Processors
This repository demonstrates the use of **OpenCV**, **pyautogui** (for capturing mouse actions) to create a Batch Image Processor.
The application is divided into two main parts:
- **Inverse Image**：This function, implemented in **negative_photo.py**, converts images to their negative forms.
- **Chop Images**：This function, implemented in **crop_photo.py**, allows users to crop images based on specified dimensions.

## Ex：xkllkx_repo/8051.png
### Inverse Image
<img src="https://github.com/xkllkx/Batch_Image_Processor/blob/main/xkllkx_repo/8051.png" width="45%" height="45%"><img src="https://github.com/xkllkx/Batch_Image_Processor/blob/main/xkllkx_repo_B2W/xkllkx_repo_1.png" width="45%" height="45%">

### Chop Images
<img src="https://github.com/xkllkx/Batch_Image_Processor/blob/main/cut_window.png" width="45%" height="45%"><img src="https://github.com/xkllkx/Batch_Image_Processor/blob/main/xkllkx_repo_B2W_cut/xkllkx_repo_B2W_1.png" width="45%" height="45%">

# Installation
```bash
pip install pyautogui opencv-python
```

# How to use this repo
## Inverse Image
### Run negative_photo.py.
```bash
python negative_photo.py
```

After placing the images that need to be transformed into the same folder,
then pick the images folder to start transforming.

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

## Chop Images
###  Run crop_photo.py.
```bash
python crop_photo.py
```

After placing the images that need to be batch-chopped into the same folder,
then pick the images folder to start transforming.

Double-click to select the top-left and bottom-right corners of the desired crop area and input **Y** to check it.
then you can complete the batch renaming and cropping.

```bash
請輸入要截圖的資料夾名稱：
xkllkx_repo_B2W 
---選取截圖範圍---
請選取欲截圖範圍的左上角與右下角
1920 1080
(1080, 1842, 3)
1.0
1080.0 1842.0
27,152
已選取1個點,還剩1個點
393,197
已選取2個點,完成選取
---請關閉圖片---
裁切範圍確認(Y/N):
Y
---改名並開始裁切---
檔案標號確認(預設為0)(Y/N):
Y
xkllkx_repo_1.png >>> xkllkx_repo_B2W_1.png
判斷裁切
xkllkx_repo_B2W_1.png裁切完成
------------------------
xkllkx_repo_2.png >>> xkllkx_repo_B2W_2.png
判斷裁切
xkllkx_repo_B2W_2.png裁切完成
------------------------
xkllkx_repo_3.png >>> xkllkx_repo_B2W_3.png
判斷裁切
xkllkx_repo_B2W_3.png裁切完成
------------------------
xkllkx_repo_4.png >>> xkllkx_repo_B2W_4.png
判斷裁切
xkllkx_repo_B2W_4.png裁切完成
------------------------
xkllkx_repo_5.png >>> xkllkx_repo_B2W_5.png
判斷裁切
xkllkx_repo_B2W_5.png裁切完成
------------------------
```
